---
title: 'Logback filter 기능으로 원하는 log 제외시키기'
date: 2019-10-13 10:23:33
category: 'java'
tags: ["java", "logback", "log", "logger", "filter", "로그", "자바", "로그백", "필더"]
---

# 1. 들어가며

내용입니다. 


# 2. 개발 환경

포스팅에서 작성한 코드는 아래 github 링크를 참조해주세요.

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : [github](https://github.com/kenshin579/tutorials-java/tree/master/springboot-quartz-cluster)
* Software management tool : Maven

# 3. Logback filter 기능 알아보기

```xml
<appender name="console" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
        <pattern>[%d{yyyy-MM-dd HH:mm:ss}] [%-5p] %C{1}.%M[%L] %m%n</pattern>
    </encoder>
    <filter class="com.tmoncorp.media.api.config.logback.MessageIgnoreFilter" />
</appender>
```


```java
/**
 * tmon-core 쪽의 불필요한 log 출력을 제외시키기 위하여 등록.\
 * logback.xml 에 filter 등록.
 */
public class MessageIgnoreFilter extends Filter<ILoggingEvent> {
	@Override
	public FilterReply decide(ILoggingEvent event) {
		if (event.getMessage().contains("## domain =")) {
			return FilterReply.DENY;
		}else{
			return FilterReply.ACCEPT;
		}
	}
}
```


# 4. 정리

정리 내용입니다.

# 5. 참고

* Logback
  * [https://jeong-pro.tistory.com/154](https://jeong-pro.tistory.com/154)
