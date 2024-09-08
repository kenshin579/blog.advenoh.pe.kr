---
title: "Quartz에서 실행중인 Job을 Interrupt하여 Job Scheduler를 정상종료 시키는 방법"
description: "Quartz에서 실행중인 Job을 Interrupt하여 Job Scheduler를 정상종료 시키는 방법"
date: 2019-10-12
update: 2019-10-12
tags:
  - quartz
  - spring
  - job
  - interrupt
  - hook
  - 인터럽트
  - 셧다운훅
  - 스케줄러
  - 스케줄
  - 스프링
  - 스프링부트
series: "Spring Quartz"
---

## 1. 들어가며

본 포스팅은 Quartz 튜터리얼에서 4번째 시리즈로 Quartz 서버를 셧다운 시킬 때 gradefully하게 처리하는 방법에 대해서 다룹니다. 셧다운 이벤트가 발생하면 실행 중인 Quartz Job에 내부 interrupt() 함수가 호출이 되고 interrupt로 노티를 받으면 개발자가 알아서 close 로직을 짜면 됩니다. 실행 쓰레드를 kill 할 수도 있고 (비추천) 실행 중인 Job을 기다리고 다음 스케줄에서 제외시킬 수도 있습니다.

## 2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : [github](https://github.com/kenshin579/tutorials-java/tree/master/springboot-quartz-cluster-reactjs)
* Software management tool : Maven

# 3. Quartz에서 ShutdownHook 등록하고 기존 Job을 Interruptable Job으로 구현하기

실행 중인 Job을 gracefully하게 셧다운 하려면 2가지만 설정해주면 됩니다.

## 3.1 Quartz 설정에 SchedulerFactoryBean에 대한 ShutdownHook 등록하기

Quartz에서 사용하는 SchedulerFactoryBean은 SmartLifeCycle 인터페이스를 구현하고 있습니다.

```java
public class SchedulerFactoryBean extends SchedulerAccessor implements FactoryBean<Scheduler>,
BeanNameAware, ApplicationContextAware, InitializingBean, DisposableBean, SmartLifecycle
```

스프링의 SmartLifeCycle은 콜백 인터페이스로 여러 LifeCycle에 대한 메서드를 가지고 있고 어플리케이션이 종료되거나 시작될 때 정의된 메서드가 호출됩니다.

QuartzConfiguration 파일에 gracefulShutdownHookForQuartz 메서드를 빈으로 정의하여 Shutdown Hook을 등록합니다.

```java
@Bean
public SmartLifecycle gracefulShutdownHookForQuartz(@Qualifier("schedulerFactoryBean") SchedulerFactoryBean schedulerFactoryBean) {
   return new SmartLifecycle() {
      private boolean isRunning = false;
 
      @Override
      public boolean isAutoStartup() {
         return true;
      }
 
      @Override
      public void stop(Runnable callback) {
         stop();
         log.info("Spring container is shutting down.");
         callback.run();
      }
 
      @Override
      public void start() {
         log.info("Quartz Graceful Shutdown Hook started.");
         isRunning = true;
      }
 
      @Override
      public void stop() {
         isRunning = false;
 
         try {
            log.info("Quartz Graceful Shutdown...");
            interruptJobs(schedulerFactoryBean);
            schedulerFactoryBean.destroy();
         } catch (SchedulerException e) {
            try {
               log.info("Error shutting down Quartz: ", e);
               schedulerFactoryBean.getScheduler().shutdown(false);
            } catch (SchedulerException ex) {
               log.error("Unable to shutdown the Quartz scheduler.", ex);
            }
         }
      }
 
      @Override
      public boolean isRunning() {
         return isRunning;
      }
 
      @Override
      public int getPhase() {
         return Integer.MAX_VALUE;
      }
   };
}
```

Gracefully 하게 셧다운 해야 하기 때문에 저희가 관심 있는 메서드는 stop() 메서드입니다. 이 메서드가 호출되면 Quartz 스케줄러에서 현재 실행 중인 모든 Job을 조회하여 실행 중인 Job의 interrupt() 메서드를 호출합니다. Job에서는 어떻게 처리할 수 있는지 다음 장에서 설명할게요.

```java
private void interruptJobs(SchedulerFactoryBean schedulerFactoryBean) throws SchedulerException {
   Scheduler scheduler = schedulerFactoryBean.getScheduler();
   for (JobExecutionContext jobExecutionContext : scheduler.getCurrentlyExecutingJobs()) {
      final JobDetail jobDetail = jobExecutionContext.getJobDetail();
      log.info("interrupting job :: jobKey : {}", jobDetail.getKey());
      scheduler.interrupt(jobDetail.getKey());
   }
}
```

3.2 Quartz Job에 InterruptableJob 인터페이스를 implements하여 구현하기

Interrupt 가능한 Job을 구현하려면 InterrutableJob 인터페이스를 구현하고 interrupt() 메서드를 구현해주면 됩니다. 이미 짐작 하셨겠지만, 셧다운시 3.1에서 정의한 SmartLifeCycle의 stop() 메서드에 의해 호출이 되고 현재 실행 중인 Job의 쓰레드를 interrupt 시킵니다.

```java
public class CronJob2 extends QuartzJobBean implements InterruptableJob {
    private volatile boolean isJobInterrupted = false;
    …(생략)…
 
    @Override
    public void executeInternal(JobExecutionContext context) throws JobExecutionException {
        JobKey jobKey = context.getJobDetail().getKey();
        if (!isJobInterrupted) { //flag 값을 이용해서 다음에 스케줄에서 제외되도록 한다
            …(생략)...
        }
    }
 
    @Override
    public void interrupt() {
        isJobInterrupted = true; //interrupt 되었다고 flag를 둔다
        if (currThread != null) {
            log.info("interrupting - {}", currThread.getName());
            currThread.interrupt(); //쓰레드가 일시 정지 상태이면 바로 깨워서 실행시킨다
        }
    }
}
```

## 4. 정리

실행 중인 Job을 Gracefully 하게 셧다운 시키는 방법에 대해서 알아보았습니다. 다음 포스팅은 Quartz 튜터리얼 시리지로의 마지막으로 Quartz 어드민 UI 구현에 대해서 알아보겠습니다.

## 5. 참고

* Servlet 시작시
    * [https://karismamun.tistory.com/46](https://karismamun.tistory.com/46)
* Spring SmartLifeCyle
    * [https://jjhwqqq.tistory.com/155](https://jjhwqqq.tistory.com/155)
    * [https://krksap.tistory.com/1240](https://krksap.tistory.com/1240)
* Interrupt
    * [https://m.blog.naver.com/PostView.nhn?blogId=qbxlvnf11&logNo=221106055566&proxyReferer=https%3A%2F%2Fwww.google.com%2F](https://m.blog.naver.com/PostView.nhn?blogId=qbxlvnf11&amp;logNo=221106055566&amp;proxyReferer=https%3A%2F%2Fwww.google.com%2F)
    * [https://blog.naver.com/qbxlvnf11/220921178603?proxyReferer=http%3A%2F%2Fblog.naver.com%2FPostView.nhn%3FblogId%3Dqbxlvnf11%26logNo%3D220945432938%26parentCategoryNo%3D%26categoryNo%3D12%26viewDate%3D%26isShowPopularPosts%3Dtrue%26from%3Dsearch](https://blog.naver.com/qbxlvnf11/220921178603?proxyReferer=http%3A%2F%2Fblog.naver.com%2FPostView.nhn%3FblogId%3Dqbxlvnf11%26logNo%3D220945432938%26parentCategoryNo%3D%26categoryNo%3D12%26viewDate%3D%26isShowPopularPosts%3Dtrue%26from%3Dsearch)
    * [http://blog.naver.com/PostView.nhn?blogId=qbxlvnf11&logNo=220945432938&parentCategoryNo=&categoryNo=12&viewDate=&isShowPopularPosts=true&from=search](http://blog.naver.com/PostView.nhn?blogId=qbxlvnf11&amp;logNo=220945432938&amp;parentCategoryNo=&amp;categoryNo=12&amp;viewDate=&amp;isShowPopularPosts=true&amp;from=search)

