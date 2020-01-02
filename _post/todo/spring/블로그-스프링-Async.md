# 블로그 : 스프링 @Async
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] @Async을 메서드에 선언하면 별도의 쓰레드에서 실행됨
- [ ] AsyncResult
- [ ] ListenableFutureCallback?

[https://yakolla.tistory.com/172](https://yakolla.tistory.com/172)
[https://nickebbitt.github.io/blog/2017/03/22/async-web-service-using-completable-future](https://nickebbitt.github.io/blog/2017/03/22/async-web-service-using-completable-future)

- [ ] Executor를 직접생성하고 등록해야 하는 이유
ㅁ. 스프링에서 기본으로 사용하는 심플 익스큐터는 스레드를 쓰고 버리는 특징이 있음.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20@Async/image_2.png)

[https://awayday.github.io/2018-07-22/spring-4-async/](https://awayday.github.io/2018-07-22/spring-4-async/)

1. 들어가며

- [ ] post를 날리고 나서 응답을 기다렸다가 처리하는 건가?

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20@Async/3198CBBD-B7BC-4D2D-BA27-DF60388C4709.png)

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* @Async
	* [https://www.baeldung.com/spring-async](https://www.baeldung.com/spring-async)
	* [https://frontdev.tistory.com/entry/Asynchronous-Multi-thread-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0](https://frontdev.tistory.com/entry/Asynchronous-Multi-thread-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0)
	* [https://howtodoinjava.com/spring-boot2/enableasync-async-controller/](https://howtodoinjava.com/spring-boot2/enableasync-async-controller/)
	* [https://www.javacodegeeks.com/2017/10/call-asynchronous-rest.html](https://www.javacodegeeks.com/2017/10/call-asynchronous-rest.html)
	* [https://www.baeldung.com/spring-async](https://www.baeldung.com/spring-async)
	* [https://github.com/google/guava/wiki/ListenableFutureExplained](https://github.com/google/guava/wiki/ListenableFutureExplained)
	* [https://blog.jayway.com/2014/09/09/asynchronous-spring-service/](https://blog.jayway.com/2014/09/09/asynchronous-spring-service/)
	* [https://dzone.com/articles/non-blocking-rest-services-with-spring](https://dzone.com/articles/non-blocking-rest-services-with-spring)
	* [http://airanluis.com/async-request-with-configured-timeout-spring-asyncresttemplate](http://airanluis.com/async-request-with-configured-timeout-spring-asyncresttemplate)
	* [https://www.concretepage.com/spring-4/spring-4-asyncresttemplate-listenablefuture-example](https://www.concretepage.com/spring-4/spring-4-asyncresttemplate-listenablefuture-example)
* Mode
	* [http://dveamer.github.io/java/SpringAsync.html](http://dveamer.github.io/java/SpringAsync.html)
	* [http://dveamer.github.io/java/SpringAsyncAspectJ.html](http://dveamer.github.io/java/SpringAsyncAspectJ.html)

#tistory #blog #스터디중