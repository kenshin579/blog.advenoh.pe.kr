---
title: "Spring Boot + Quartz을 이용한 Job Scheduler 구현 (In-memory)"
description: "Spring Boot + Quartz을 이용한 Job Scheduler 구현 (In-memory)"
date: 2019-09-09
update: 2019-09-09
tags:
  - quartz
  - spring
  - job
  - scheduler
  - memory
  - 메모리기반
  - 스케줄러
  - 스케줄
  - 스프링
  - 스프링부트
  - 분산환경
  - 다중서버
  - multiple server
  - distributed environment
series: "Spring Quartz"
---

## 1. 들어가며

이 포스팅은 Quartz 튜터리얼 시리즈에 한 부분으로 첫 번째의 포스팅 [Quartz Job Scheduler란?](https://blog.advenoh.pe.kr/quartz-job-scheduler란/) 에 이어 2부 내용으로 Spring Boot 기반의 RAMJobStore을 이용한 Quartz 스케줄러 구현을 다룹니다. 기본 개념은 이미 1부에서 다루었기 때문에 여기에서는 작성한 코드 기반으로 어떻게 스프링에서 Quartz를 설정하여 사용할 수 있는지에 대해서 알아보겠습니다.

## 2. 개발 환경

스프링 부트에서는 Quartz을 사용하려면 spring-boot-starter-quartz 라이브러리를 추가해줘야 합니다. pom.xml 메이븐 파일에 아래 내용을 추가합니다.

```xml

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-quartz</artifactId>
</dependency>
```

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : [github](https://github.com/kenshin579/tutorials-java/tree/master/springboot-quartz-in-memory)
* Software management tool : Maven

## 3. 스프링 부트 기반의 Quartz 스케줄러 구축

### 3.1 Quartz를 위한 관련 설정

#### 3.1.1 스프링 JavaConfig

스프링의 SchedulerFactoryBean은 Bean으로 선언하여 다른 클래스에서 DI (dependency injection)해서 사용할 수 있습니다.

```java
@Component
public class ScheduleServiceImpl implements ScheduleService {
 
    @Autowired
    private SchedulerFactoryBean schedulerFactoryBean;
```

그리고 [첫번째 포스팅](https://blog.advenoh.pe.kr/spring/quartz-job-scheduler%EB%9E%80/) 에서 언급했던 것처럼 SchedulerFactoryBean 은 ApplicationContext에서 LifeCycle 형식으로 Scheduler을 관리하고 있습니다.

Listener와 Quartz 관련된 설정도 여기서 지정합니다.

```java
@Bean
public SchedulerFactoryBean schedulerFactoryBean(ApplicationContext applicationContext) {
   SchedulerFactoryBean schedulerFactoryBean = new SchedulerFactoryBean();
 
   AutowiringSpringBeanJobFactory jobFactory = new AutowiringSpringBeanJobFactory();
   jobFactory.setApplicationContext(applicationContext);
   schedulerFactoryBean.setJobFactory(jobFactory);
 
   schedulerFactoryBean.setApplicationContext(applicationContext);
   
   Properties properties = new Properties();
   properties.putAll(quartzProperties.getProperties());
 
   schedulerFactoryBean.setGlobalTriggerListeners(triggersListener);
   schedulerFactoryBean.setGlobalJobListeners(jobsListener);
   schedulerFactoryBean.setOverwriteExistingJobs(true);
   schedulerFactoryBean.setQuartzProperties(properties);
   schedulerFactoryBean.setWaitForJobsToCompleteOnShutdown(true);
   return schedulerFactoryBean;
}
```

#### 3.1.2 Quartz 관련 설정

스프링 부트에서는 Quartz 관련 설정을 application.properties에서 합니다. 관련 설정이 없으면 기본 값으로 구동됩니다. ThreadPool, Scheduler Setting, JobStore 등에 관련된 많은 설정이 존재하기 때문에 [Quartz Configuration](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/configuration/ConfigMain.html) 문서를 참고해주세요. 예제에서는 threadCount를 5개만 생성하고 스케줄러 쓰레드 이름의 prefix를 QuartzScheduler로 지정하였습니다.

```
#Quartz
spring.quartz.scheduler-name=QuartzScheduler
spring.quartz.properties.org.quartz.threadPool.threadCount = 5
```

### 3.2 Scheduler Controller과 ScheduleService 구현

샘플 프로젝트에서는 사용자가 정의한 Job을 쉽게 등록하고 삭제, 조회 등을 할 수 있도록 아래와 같은 API를 제공합니다.

* 제공할 Scheduler API
    * Job 추가 : POST _scheduler_job
    * 모든 등록된 Job 조회 : GET _scheduler_jobs
    * Job 삭제 : DELETE _scheduler_job
    * Job 멈춤 : PUT _scheduler_job/pause
    * Job 재시작 : PUT _scheduler_job/resume

컨트롤러와 서비스단의 로직을 보면 기본 로직은 간단하기 때문에 몇개의 API만 설명하겠습니다. 실행할 Job을 먼저 보도록 하겠습니다.

#### 3.2.1 사용자 Job 구현

Job 작업 내용은 지정한 sleep 타임에 따라서 화면에 숫자를 출력하는 것입니다.

##### **3.2.1.1 SimpleJob**

loop을 돌면서 화면에 숫자를 출력하고 지정한 sleep 타임동안 쉬고 다시 반복하는 로직입니다.

```java
public class SimpleJob extends QuartzJobBean {
   private int MAX_SLEEP_IN_SECONDS = 5;
   private volatile Thread currThread;
 
   @Override
   protected void executeInternal(JobExecutionContext context) throws JobExecutionException {
      JobKey jobKey = context.getJobDetail().getKey();
      currThread = Thread.currentThread();
 
      IntStream.range(0, 5).forEach(i -> {
         log.info("SimpleJob Counting - {}", i);
         try {
            TimeUnit.SECONDS.sleep(MAX_SLEEP_IN_SECONDS);
         } catch (InterruptedException e) {
            log.error(e.getMessage(), e);
         }
      });
   }
}
```

##### **3.2.1.2 CronJob**

CronJob 구현도 SimpleJob과 동일하고 추가로 jobId를 JobDataMap으로 받아서 화면에 출력하고 있습니다.

```java
public class CronJob extends QuartzJobBean {
   private int MAX_SLEEP_IN_SECONDS = 5;
   private volatile Thread currThread;
 
   @Override
   protected void executeInternal(JobExecutionContext context) throws JobExecutionException {
      JobDataMap jobDataMap = context.getJobDetail().getJobDataMap();
      int jobId = jobDataMap.getInt("jobId");
      JobKey jobKey = context.getJobDetail().getKey();
 
      currThread = Thread.currentThread();
 
     … (생략) ...
      log.info("CronJob ended :: jobKey : {} - {}", jobKey, currThread.getName());
   }
}
```

#### 3.2.2 Job 추가 API

##### **3.2.2.1 Controller Job 추가**

Quartz 스케줄러에서는 SimpleJob과 CronJob 형식으로 추가할 수 있어서 cron 표현식이 있는 경우에는 CronJob으로 등록하도록 조건문을 추가했습니다.

```java
@RequestMapping(value = "/job", method = RequestMethod.POST)
public ResponseEntity<?> addScheduleJob(@ModelAttribute JobRequest jobRequest) {
… (생략) … 
 
   JobKey jobKey = new JobKey(jobRequest.getJobName(), jobRequest.getJobGroup());
   if (!scheduleService.isJobExists(jobKey)) {
      if (jobRequest.getCronExpression() == null) {
         scheduleService.addJob(jobRequest, SimpleJob.class);
      } else {
         scheduleService.addJob(jobRequest, CronJob.class);
      }
   } else {
      return new ResponseEntity<>(new ApiResponse(false, "Job already exits"),
            HttpStatus.BAD_REQUEST);
   }
   return new ResponseEntity<>(new ApiResponse(true, "Job created successfully"), HttpStatus.CREATED);
}
```

##### **3.2.2.2 ScheduleService Job 추가**

사용자가 제공한 Job 이름, 그룹, Cron 표현 등으로 Trigger와 JobDetail을 생성하고 schedulerJob() 메서드로 job을 Quartz에 등록할 수 있습니다.

```java
@Override
public boolean addJob(JobRequest jobRequest, Class<? extends Job> jobClass) {
    JobKey jobKey = null;
    JobDetail jobDetail;
    Trigger trigger;
 
    try {
        trigger = JobUtils.createTrigger(jobRequest);
        jobDetail = JobUtils.createJob(jobRequest, jobClass, context);
        jobKey = JobKey.jobKey(jobRequest.getJobName(), jobRequest.getJobGroup());
 
        Date dt = schedulerFactoryBean.getScheduler().scheduleJob(jobDetail, trigger);
        log.debug("Job with jobKey : {} scheduled successfully at date : {}", jobDetail.getKey(), dt);
        return true;
    } catch (SchedulerException e) {
        log.error("error occurred while scheduling with jobKey : {}", jobKey, e);
    }
    return false;
}
```

서비스단의 로직도 Unit Test로 쉽게 체크할 수 있습니다. Quartz 소스 코드를 참조해서 작성했습니다.

```java
@Test
public void addJob() {
    JobRequest jobRequest = new JobRequest();
    jobRequest.setCronExpression("0/10 * * ? * *");
    jobRequest.setJobName(jobName);
    jobRequest.setJobGroup(groupName);
 
    when(schedulerFactoryBean.getScheduler()).thenReturn(scheduler);
 
    boolean result = scheduleService.addJob(jobRequest, CronJob.class);
    assertThat(result).isTrue();
 
    verify(schedulerFactoryBean).getScheduler();
}
```

#### 3.2.3 등록된 모든 Job 조회 API

Scheduler에서 현재 등록된 Job 정보도 scheduler에서 제공하는 여러 메서드을 통해서 쉽게 얻어 올 수 있습니다. 개별 Job 정보외에도 간단한 통계 수치도 같이 count해서 응답 값으로 내려주고 있습니다.

```java
@Override
public JobStatusResponse getAllJobs() {
    JobResponse jobResponse;
    JobStatusResponse jobStatusResponse = new JobStatusResponse();
    List<JobResponse> jobs = new ArrayList<>();
    int numOfRunningJobs = 0;
    int numOfGroups = 0;
    int numOfAllJobs = 0;
 
    try {
        Scheduler scheduler = schedulerFactoryBean.getScheduler();
        for (String groupName : scheduler.getJobGroupNames()) {
            numOfGroups++;
            for (JobKey jobKey : scheduler.getJobKeys(GroupMatcher.jobGroupEquals(groupName))) {
                List<Trigger> triggers = (List<Trigger>) scheduler.getTriggersOfJob(jobKey);
 
                jobResponse = JobResponse.builder()
                        .jobName(jobKey.getName())
                        .groupName(jobKey.getGroup())
                        .scheduleTime(DateTimeUtils.toString(triggers.get(0).getStartTime()))
                        .lastFiredTime(DateTimeUtils.toString(triggers.get(0).getPreviousFireTime()))
                        .nextFireTime(DateTimeUtils.toString(triggers.get(0).getNextFireTime()))
                        .build();
 
                if (isJobRunning(jobKey)) {
                    jobResponse.setJobStatus("RUNNING");
                    numOfRunningJobs++;
                } else {
                    String jobState = getJobState(jobKey);
                    jobResponse.setJobStatus(jobState);
                }
                numOfAllJobs++;
                jobs.add(jobResponse);
            }
        }
    } catch (SchedulerException e) {
        log.error("[schedulerdebug] error while fetching all job info", e);
    }
 
    jobStatusResponse.setNumOfAllJobs(numOfAllJobs);
    jobStatusResponse.setNumOfRunningJobs(numOfRunningJobs);
    jobStatusResponse.setNumOfGroups(numOfGroups);
    jobStatusResponse.setJobs(jobs);
    return jobStatusResponse;
}
```

아래와 같이 응답 값을 내려주고 있습니다.

```json
{
  "numOfAllJobs": 3,
  "numOfGroups": 1,
  "numOfRunningJobs": 2,
  "jobs": [
    {
      "jobName": "cronJob1",
      "groupName": "DEFAULT",
      "jobStatus": "RUNNING",
      "scheduleTime": "2019-09-09 22:08:16",
      "lastFiredTime": "2019-09-09 22:10:00",
      "nextFireTime": "2019-09-09 22:11:00"
    },
    …(생략)...
  ]
}
```

#### 3.2.4 Listeners

##### **3.2.4.1 TriggerListener**

메서드 이름으로 쉽게 알 수 있듯이 이벤트(ex. triggerFire, triggerMisfired) 발생시 호출되는 메서드들입니다.

vetoJobExecution 메서드는 해당 Trigger를 veto(거부, 금지) 시킬지 결정할 수 있는 메서드로 true이면 veto를 시켜서 Job이 실행되지 않고 false이면 veto를 시키지 않아 Job을 실행시킬 수 있어서 특정 조건을 넣어서 실행 여부를 결정 짓을 수 있는 메서드입니다.

```java
@Component
public class TriggersListener implements TriggerListener {
    …(생략)…
 
    @Override
    public void triggerFired(Trigger trigger, JobExecutionContext context) {
        JobKey jobKey = trigger.getJobKey();
        log.info("triggerFired at {} :: jobKey : {}", trigger.getStartTime(), jobKey);
    }
 
    @Override
    public boolean vetoJobExecution(Trigger trigger, JobExecutionContext context) {
        return false;
    }
 
    @Override
    public void triggerMisfired(Trigger trigger) {
        JobKey jobKey = trigger.getJobKey();
        log.info("triggerMisfired at {} :: jobKey : {}", trigger.getStartTime(), jobKey);
    }
 
    @Override
    public void triggerComplete(Trigger trigger, JobExecutionContext context,
                        Trigger.CompletedExecutionInstruction triggerInstructionCode) {
        JobKey jobKey = trigger.getJobKey();
        log.info("triggerComplete at {} :: jobKey : {}", trigger.getStartTime(), jobKey);
    }
}
```

##### **3.2.4.2 JobListener**

JobListener도 메서드 이름만으로 발생 이벤트시 호출 되는 메서드를 쉽게 알 수 있습니다. jobExecutionVetoed는 TriggersListener.vetoJobExecution() 메서드에서 veto를 시킨 경우 호출됩니다.

```java
@Component
public class JobsListener implements JobListener {
…(생략)…
 
   @Override
   public void jobToBeExecuted(JobExecutionContext context) {
      JobKey jobKey = context.getJobDetail().getKey();
      log.info("jobToBeExecuted :: jobKey : {}", jobKey);
   }
 
   @Override
   public void jobExecutionVetoed(JobExecutionContext context) {
      JobKey jobKey = context.getJobDetail().getKey();
      log.info("jobExecutionVetoed :: jobKey : {}", jobKey);
   }
 
   @Override
   public void jobWasExecuted(JobExecutionContext context, JobExecutionException jobException) {
      JobKey jobKey = context.getJobDetail().getKey();
      log.info("jobWasExecuted :: jobKey : {}", jobKey);
   }
}
```

## 4. 정리

Quartz에서는 Scheduler의 여러 기능을 (scheduler, unschedule, pause, resume, stop) 제공하고 있어서 애플리케이션 내에 스케줄링 기능을 잘 구현할 수 있습니다. 이 포스팅에서는 스프링에서 Quartz를 어떻게 설정해서 사용할 수 있는지 알아보았습니다. RAMJobStore를 기본으로 사용해서 스케줄링 정보가 메모리에 저장되기 때문에 다중 서버 환경에서는 적합하지 않습니다. 서버 이중화를 Quartz를 어떻게 설정해야 하는지 다음 포스팅에서 알아보겠습니다.

## 5. 참고

* Quartz 공식 사이트
    * [http://www.quartz-scheduler.org](http://www.quartz-scheduler.org/)
* Spring Boot Quartz Scheduler
    * [https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-quartz.html](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-quartz.html)
    * [https://www.baeldung.com/spring-quartz-schedule](https://www.baeldung.com/spring-quartz-schedule)
    * [https://gs.saro.me/dev?tn=549](https://gs.saro.me/dev?tn=549)
