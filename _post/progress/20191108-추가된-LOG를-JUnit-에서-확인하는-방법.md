---
title: '추가된 LOG를 JUnit에서 확인하는 방법'
date: 2019-10-13 10:23:33
category: 'java'
tags: ["java", "logger", "junit", "unittest", "자바", "유닛테스트", "로거"]
---

# 1. 들어가며

Unit Test를 작성 할 때 메서드의 결과를 기본적으로 확인하여 로직을 검증합니다. void 인 메서드인 경우에는 내부 메서드에서 실행하는 메서드의 실행 여부나 메서드로 넘겨진 인자 값을 가지고 확인하기고 합니다. 

개발 하다보면 로직에 변화는 없지만, 단순히 메서드에서 로그를 추가하는 경우가 생깁니다. 굳이 Unit Test로 확인할 것 까지는 없어보였지만, 혹시 추가한 로그도 Unit Test에서 확인할 수 있는지 알아보았습니다.

# 2. 개발 환경

소스 코드는 아래 링크를 참고해주세요.

* OS : Mac OS

* IDE: Intellij

* Java : JDK 1.8

* Source code : [github](https://github.com/kenshin579/tutorials-java/tree/master/junit-unit-test) 

* Software management tool : Maven

# 3. 로그 찍히는 지 확인하는 방법

개발하는 프로젝트에서 아래와 같이 예외처리가 안된 부분에 로그를 추가하여 원하는 정보를 출력하도록 하였습니다. catch 문구에 추가된 로그를 Unit Test에서 확인해보겠습니다. 

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

로그로 출력하는 메시지를 확인하기 위해서 



```java
@Slf4j
public class LogAssertTest {
	@Test
	public void requestJobId() {
    SomeService someService = new SomeService();
		String jobId = "12342";

		Logger logger = (Logger) LoggerFactory.getLogger(SomeService.class);
		ListAppender<ILoggingEvent> listAppender = new ListAppender<>();
		listAppender.start(); //

		logger.addAppender(listAppender);

		someService.requestJobId(jobId);

		List<ILoggingEvent> logsList = listAppender.list;
		assertThat(logsList.get(0).getMessage()).contains("[servicedebug] error occurred : jobId : ");
	}
}
```



# 4. 참고

* Logger Assert
	* [https://stackoverflow.com/questions/1827677/how-to-do-a-junit-assert-on-a-message-in-a-logger](https://stackoverflow.com/questions/1827677/how-to-do-a-junit-assert-on-a-message-in-a-logger)
	* https://stackoverflow.com/questions/29076981/how-to-intercept-slf4j-with-logback-logging-via-a-junit-test
	* https://www.jvt.me/posts/2019/09/22/testing-slf4j-logs/