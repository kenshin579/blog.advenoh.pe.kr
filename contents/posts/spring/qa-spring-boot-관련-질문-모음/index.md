---
title: "Q&A Spring Boot 관련 질문 모음"
description: "Q&A Spring Boot 관련 질문 모음"
date: 2019-12-04
update: 2019-12-04
tags:
  - Q&A
  - faq
  - spring
  - springboot
  - batch
  - 스프링
  - 배치
  - 질문
---

개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.


## Q&A 전체 목록

### <span style="color:orange">[답변완료]</span>

### <span style="color:brown">1. application.properties : server.compression.enabled 속성의 의미는?</span>

스프링 부트에서 기본적으로 GZip 압축은 비활성화 되어 있습니다. 하지만, server.compression.enabled=true로 설정하면 웹 자원(ex. html, css)을 압축해서 클라이언트로 보내져서 응답 시간을 줄일 수 있는 장점이 있습니다.

참고
* [https://www.callicoder.com/configuring-spring-boot-application/](https://www.callicoder.com/configuring-spring-boot-application/)


### <span style="color:brown">2. Quartz에서 @PersistJobDataAfterExecution 어노테이션의 의미는 뭔가? </span>

Job 로직에서 JobDataMap 데이터를 수정하면 실행이후에 DB에 저장이 안됩니다. 하지만, @PersistJobDataAfterExecution 어노테이션을 클래스에 추가하면 JobDataMap을 수정한 데이터를 다음 실행 때에도 반영된 데이터를 읽을 수 있습니다.

```java
@PersistJobDataAfterExecution
@DisallowConcurrentExecution
public class StatefulDumbJob implements Job {

    public static final String NUM_EXECUTIONS = "NumExecutions";
    public static final String EXECUTION_DELAY = "ExecutionDelay";

    public StatefulDumbJob() {
    }
    public void execute(JobExecutionContext context)
        throws JobExecutionException {
        System.err.println("---" + context.getJobDetail().getKey()
                + " executing.[" + new Date() + "]");

        JobDataMap map = context.getJobDetail().getJobDataMap();

        int executeCount = 0;
        if (map.containsKey(NUM_EXECUTIONS)) {
            executeCount = map.getInt(NUM_EXECUTIONS);
        }

        executeCount++;
        map.put(NUM_EXECUTIONS, executeCount); //다시 JobDataMap에 저장을 함

        long delay = 5000l;
        if (map.containsKey(EXECUTION_DELAY)) {
            delay = map.getLong(EXECUTION_DELAY);
        }

        try {
            Thread.sleep(delay);
        } catch (Exception ignore) {
        }

        System.err.println("  -" + context.getJobDetail().getKey()
                + " complete (" + executeCount + ").");
    }
}
```


* [https://www.concretepage.com/scheduler/quartz/quartz-2-scheduler-pass-parameters-to-job-with-jobdatamap-using-persistjobdataafterexecution-and-disallowconcurrentexecution-example](https://www.concretepage.com/scheduler/quartz/quartz-2-scheduler-pass-parameters-to-job-with-jobdatamap-using-persistjobdataafterexecution-and-disallowconcurrentexecution-example)
* [http://www.quartz-scheduler.org/documentation/quartz-2.1.7/examples/Example5.html](http://www.quartz-scheduler.org/documentation/quartz-2.1.7/examples/Example5.html)


### <span style="color:brown"> 3. @SpringBootTest와 @DataJpaTest의 차이점은 뭔가?</span>

- @SpringBootTest

    - 모든 빈을 읽어서 테스트할 수 있다
    - 실행이 느리다
- @DataJpaTest
    - @Entity, @Repository만 스캔해서 빈으로 설정된다
    - @Configuration, @Component, @Service를 스캔하지 않는다.
    - DB는 인메모리 데이터 베이스를 사용하여 테스트를 수행한다
    - @Transactional이 이미 포함되어 있다


**@SpringBootTest**

```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@BootstrapWith(SpringBootTestContextBootstrapper.class)
@ExtendWith({SpringExtension.class})
public @interface SpringBootTest {
```

**@DataJpaTest**

```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@BootstrapWith(DataJpaTestContextBootstrapper.class)
@ExtendWith({SpringExtension.class})
@OverrideAutoConfiguration(
    enabled = false
)
@TypeExcludeFilters({DataJpaTypeExcludeFilter.class})
@Transactional
@AutoConfigureCache
@AutoConfigureDataJpa
@AutoConfigureTestDatabase
@AutoConfigureTestEntityManager
@ImportAutoConfiguration
public @interface DataJpaTest {
```

참고

* [https://lalwr.blogspot.com/2018/05/spring-boot-springboottest-datajpatest.html](https://lalwr.blogspot.com/2018/05/spring-boot-springboottest-datajpatest.html)
* https://kok202.tistory.com/116

- - - -

### <span style="color:orange">[미 답변 질문]</span>



