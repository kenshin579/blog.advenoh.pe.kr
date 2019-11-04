---
title: 'JUnit에서 Logger의 메시지를 확인하는 방법'
date: 2019-10-13 10:23:33
category: 'java'
tags: ["java", "logger", "junit", "unittest", "자바", "유닛테스트", "로거"]
---

# 1. 들어가며

기본적으로 Unit Test를 작성할 때 로직을 확인하기 위해서 output 결과를 주로 확인합니다. Unit Test를 작성을 하다보면 내가 변경한 부분에 대해서 체크해보고 싶어서 

개발하다보니, 네가 변경한 부분에 대해서 제대로 확인하기

catch 구문이 없는 부분에 추가하게 되면서 변경한 로직을 Unit Test로 작성하기 위해서 



Unit Test 에서 catch 구문에 throw하는 로직 대신 로그를 찍는 부분에 



 찍는 로그를 확인하는 경우가 생겨서 작성하게 되었습니다. 



이런 경우는 매우 드믈 것으로 catch 구문을 추가해서 로그까 찍히는지 

# 2. 개발 환경

* OS : Mac OS

* IDE: Intellij

* Java : JDK 1.8

* Source code : [github](https://github.com/kenshin579/tutorials-java/tree/master/junit-unit-test) 

* Software management tool : Maven

# 3. Unit Test에서 로그 찍히는 지 확인하는 방법

```java
@Slf4j
public class LogAssertTest {
	SomeService someService;

	@Before
	public void setUp() throws Exception {
		someService = new SomeService();
	}

	@Test
	public void requestJobId() {
		String jobId = "12342";

		Logger logger = (Logger) LoggerFactory.getLogger(SomeService.class);
		ListAppender<ILoggingEvent> listAppender = new ListAppender<>();
		listAppender.start();

		logger.addAppender(listAppender);

		someService.requestJobId(jobId);

		List<ILoggingEvent> logsList = listAppender.list;
		assertThat(logsList.get(0).getMessage()).contains("[servicedebug] error occurred : jobId : ");
	}
}
```



```java
@Slf4j
public class SomeService {
	public String someMethod(SomeEntity someEntity) {
		return someEntity.getSomeProperty();
	}

	public void requestJobId(String jobId) {
		try {
			throwMethodTest("throwing test");
		} catch (Exception e) {
			log.error("[servicedebug] error occurred : jobId : {}", jobId);
		}
	}

	private void throwMethodTest(String msg) throws Exception {
		throw new Exception(msg);
	}
}
```



# 4. 참고

* Logger Assert
	* [https://stackoverflow.com/questions/1827677/how-to-do-a-junit-assert-on-a-message-in-a-logger](https://stackoverflow.com/questions/1827677/how-to-do-a-junit-assert-on-a-message-in-a-logger)