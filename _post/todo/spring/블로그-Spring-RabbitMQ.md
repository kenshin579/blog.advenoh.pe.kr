# 블로그 : Spring RabbitMQ
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] 코드상에서 rabbitmq가 어떻게 사용되나?
ㅁ.

- [ ] rabbitmq관련 코드에서 unit test는 어떻게 작성하나?
ㅁ.

- [ ] 우리 코드에서는 어떻게 사용되나?
ㅁ.

- [ ] RabbitTemplate vs AmqpTemplate의 차이점은?
ㅁ.

- [ ] virtualHost는 뭔가?

-- @RabbitListener를 사용하려면, @EnableRabbit을 @Configuration 어노테이션을 붙인 클래스에 선언해줘야함-

-

1. 들어가며

2. 개발 환경 및 RabbitMQ 설치

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

<dependency>
<groupId>org.springframework.amqp</groupId>
<artifactId>spring-rabbit</artifactId>
<version>2.1.4.RELEASE</version>
</dependency>

3. 사용법

4. 참고

* in Java
	* [https://www.rabbitmq.com/tutorials/tutorial-one-java.html](https://www.rabbitmq.com/tutorials/tutorial-one-java.html)
* RabbitMq in 스프링
	* [https://heowc.tistory.com/36](https://heowc.tistory.com/36)
	* [http://blog.naver.com/PostView.nhn?blogId=tmondev&logNo=220419853534&parentCategoryNo=&categoryNo=6&viewDate=&isShowPopularPosts=false&from=postView](http://blog.naver.com/PostView.nhn?blogId=tmondev&amp;logNo=220419853534&amp;parentCategoryNo=&amp;categoryNo=6&amp;viewDate=&amp;isShowPopularPosts=false&amp;from=postView)
	* [https://www.rabbitmq.com/tutorials/tutorial-four-spring-amqp.html](https://www.rabbitmq.com/tutorials/tutorial-four-spring-amqp.html)
	* [https://www.baeldung.com/rabbitmq-spring-amqp](https://www.baeldung.com/rabbitmq-spring-amqp)
	* [https://spring.io/guides/gs/messaging-rabbitmq/](https://spring.io/guides/gs/messaging-rabbitmq/)
	* [https://github.com/rabbitmq/rabbitmq-tutorials/tree/master/spring-amqp/src/main/java/org/springframework/amqp/tutorials](https://github.com/rabbitmq/rabbitmq-tutorials/tree/master/spring-amqp/src/main/java/org/springframework/amqp/tutorials)
	* [https://heowc.tistory.com/36](https://heowc.tistory.com/36)
	* [https://examples.javacodegeeks.com/enterprise-java/spring/integration/spring-integration-custom-transformer-with-rabbitmq-example/](https://examples.javacodegeeks.com/enterprise-java/spring/integration/spring-integration-custom-transformer-with-rabbitmq-example/)
* Unit Test
	* [https://github.com/spring-projects/spring-amqp-samples](https://github.com/spring-projects/spring-amqp-samples)
	* [https://github.com/rabbitmq/rabbitmq-website.git](https://github.com/rabbitmq/rabbitmq-website.git)
	* [https://github.com/cristianprofile/spring-boot-rabbitmq-integration-test](https://github.com/cristianprofile/spring-boot-rabbitmq-integration-test)
	* [https://tamasgyorfi.net/2016/04/21/writing-integration-tests-for-rabbitmq-based-components/](https://tamasgyorfi.net/2016/04/21/writing-integration-tests-for-rabbitmq-based-components/)
	* [https://dzone.com/articles/mocking-rabbitmq-for-integration-tests](https://dzone.com/articles/mocking-rabbitmq-for-integration-tests)
	* [https://piotrminkowski.wordpress.com/2018/06/15/building-and-testing-message-driven-microservices-using-spring-cloud-stream/](https://piotrminkowski.wordpress.com/2018/06/15/building-and-testing-message-driven-microservices-using-spring-cloud-stream/)
	* [https://dzone.com/articles/building-and-testing-message-driven-microservices](https://dzone.com/articles/building-and-testing-message-driven-microservices)