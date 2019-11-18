---
title: '추가된 LOG를 JUnit에서 확인하는 방법'
date: 2019-10-18 18:53:33
category: 'java'
tags: ["java", "logger", "junit", "unittest", "자바", "유닛테스트", "로거"]
---

# 1. 들어가며

Unit Test를 작성할 때 메서드의 결과를 기본적으로 확인하여 로직을 검증합니다. void인 메서드인 경우에는 내부 메서드에서 실행하는 메서드의 실행 여부나 메서드로 넘겨진 인자 값을 가지고 확인하기도 합니다. 

개발 하다 보면 로직에 변화는 없지만, 단순히 메서드에서 로그를 추가하는 경우가 생깁니다. 개인적으로는 추가한 로그를 Unit Test로 확인해야 하나 쉽지만, 확인이 가능한지 궁금증이 생겨서 알아보았습니다. 

StackOverflow에는 없는 게 없네요. 저만 궁금한 게 아니었나 봐요.

# 2. 개발 환경

소스 코드는 아래 링크를 참고해주세요.

* OS : Mac OS

* IDE: Intellij

* Java : JDK 1.8

* Source code : [github](https://github.com/kenshin579/tutorials-java/tree/master/junit-unit-test) 

* Software management tool : Maven

# 3. 로그 찍히는 지 확인하는 방법

개발하는 프로젝트에서 아래와 같이 예외처리가 안 된 부분에 로그를 추가하여 원하는 정보를 출력하도록 하였습니다. catch 문구에 추가된 로그를 Unit Test에서 확인해보겠습니다. 

```java
@Slf4j
public class SomeService {
	public void requestJobId(String jobId) {
		try {
			throwMethodTest("throwing test");
		} catch (Exception e) {
			log.error("[servicedebug] error occurred : jobId : {}", jobId); //추가된 로그
		}
	}

	private void throwMethodTest(String msg) throws Exception {
		throw new Exception(msg);
	}
}
```

ListAppender 클래스는 발생하는 Log 이벤트를 List에 저장하여 나중에 조회 가능하도록 해주는 클래스입니다. 


```java
public class LoggerTestUtil {
	public static ListAppender<ILoggingEvent> getListAppenderForClass(Class clazz) {
		Logger logger = (Logger) LoggerFactory.getLogger(clazz);

		ListAppender<ILoggingEvent> listAppender = new ListAppender<>();
		listAppender.start(); //기록을 시작한다

		logger.addAppender(listAppender); //로거에 ListAppender를 추가하여 발생하는 로그를 List에 저장하도록 한다

		return listAppender;
	}
}
```

someService.requestJobId() 메서드에서 로그를 찍게 되고 로그로 출력한 내용은 listAppender에 저장됩니다. 저장한 로그의 메시지를 확인하기 위해 listAppender.list에서 List를 가져옵니다. 

```java
 @Test
    public void requestJobId() throws JsonProcessingException {
        String jobId = "12342";

        ListAppender<ILoggingEvent> listAppender = LoggerTestUtil.getListAppenderForClass(SomeService.class);

        someService.requestJobId(jobId); //메서드 실행

        List<ILoggingEvent> logsList = listAppender.list; //저장한 데이터를 가져온다
        log.info("전체 logsList : {}", new ObjectMapper().writerWithDefaultPrettyPrinter() //JSON 포멧을 pretty하게 정렬한다
		        .writeValueAsString(logsList));
        assertThat(logsList.get(0).getMessage()).contains("[servicedebug] error occurred : jobId : ");
    }
```

# 4. 참고

* Logger Assert
	* [https://stackoverflow.com/questions/1827677/how-to-do-a-junit-assert-on-a-message-in-a-logger](https://stackoverflow.com/questions/1827677/how-to-do-a-junit-assert-on-a-message-in-a-logger)
	* [https://stackoverflow.com/questions/29076981/how-to-intercept-slf4j-with-logback-logging-via-a-junit-test](https://stackoverflow.com/questions/29076981/how-to-intercept-slf4j-with-logback-logging-via-a-junit-test)
	* [https://www.jvt.me/posts/2019/09/22/testing-slf4j-logs/](https://www.jvt.me/posts/2019/09/22/testing-slf4j-logs/)
* ListAppender
    * [http://people.apache.org/~carnold/log4j/docs/jdiff_report/Version%201.3/org/apache/log4j/varia/ListAppender.html](http://people.apache.org/~carnold/log4j/docs/jdiff_report/Version%201.3/org/apache/log4j/varia/ListAppender.html)
