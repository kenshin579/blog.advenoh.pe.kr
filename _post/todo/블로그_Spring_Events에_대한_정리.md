# 블로그 : Spring Events에 대한 정리
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] 스프링에서 ApplicationListener가 하는 일이 뭔가?

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Spring%20Events%EC%97%90%20%EB%8C%80%ED%95%9C%20%EC%A0%95%EB%A6%AC/image_2.png)

ㅁ. 스프링에서 event을 발생(publish)시키고 listener에 등록된 메서드를 실행하도록 해주는 기능임
ㅁ. 자주 사용되는 부분은 컨텍스트(ex. tomcat)가 refresh될떄 MyListener가 통보되고 init하는 코드가 실행되게...
- [ ] @EventListener
ㅁ. 스프링 4.2부터 추가됨
ㅁ. 이 어노테이션을 선언하면 자동으로 해당 메서드가 ApplicationListener로 등록됨
#. …implements 하지 않아도 됨

-- 이벤트 처리는 sync (기본), async를 지원함-

-- ApplicationEventPublisher란?-
ㅁ. Spring 4.2이후부터 어노테이션으로 코딩가능해짐

-- 비동기인 경우에는 listener는 별도의 쓰레드에서 처리된다-

[https://galid1.tistory.com/517](https://galid1.tistory.com/517)

- [ ] custom event도 생성할 수 있지만, 스프링에서 기본적으로 제공하는 이벤트들이 있다.
ㅁ. 어플레케이션, context레벨에서의 lifecyle에 필요한 hook 제공

* ContextRefreshedEvent
* ContextStartedEvent
* RequestHandledEvent

-- event listener에서 조건을 SpEL 표현식으로 정의하여 해당 값이 true인 경우에 실행하게 할 수 있음-

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Spring%20Events%EC%97%90%20%EB%8C%80%ED%95%9C%20%EC%A0%95%EB%A6%AC/image_3.png)

-- @TransactionalEventListener 어노테이션으로 transaction의 단계에 이벤트 리스너를 등록할 수 있음-

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Spring%20Events%EC%97%90%20%EB%8C%80%ED%95%9C%20%EC%A0%95%EB%A6%AC/image_1.png)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* ApplicationListner
	* [https://www.baeldung.com/spring-events](https://www.baeldung.com/spring-events)
	* [https://infoscis.github.io/2017/06/07/better-application-events-in-spring-framework-4-2/](https://infoscis.github.io/2017/06/07/better-application-events-in-spring-framework-4-2/)
	* [https://docs.spring.io/spring-framework/docs/5.0.0.M1/spring-framework-reference/html/websocket.html](https://docs.spring.io/spring-framework/docs/5.0.0.M1/spring-framework-reference/html/websocket.html)
	* [https://renjitthnarayanan.wordpress.com/2015/02/20/spring-websocket-sample/](https://renjitthnarayanan.wordpress.com/2015/02/20/spring-websocket-sample/)
* 좋은 예?
	* [https://javacan.tistory.com/entry/Handle-DomainEvent-with-Spring-ApplicationEventPublisher-EventListener-TransactionalEventListener](https://javacan.tistory.com/entry/Handle-DomainEvent-with-Spring-ApplicationEventPublisher-EventListener-TransactionalEventListener)
* 스프링 pre defined Events
	* [https://www.baeldung.com/spring-context-events](https://www.baeldung.com/spring-context-events)