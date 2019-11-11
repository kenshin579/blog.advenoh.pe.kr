# 블로그 : WebSocket in 스프링
* 들어가며
* 개발 환경
* 웹 쇼켓 구현 - 채팅 창 구현을 하는게 좋아보임
	* 예제
		* 특정 사용자에게 chat
		* broadcasting 하는 방법
		* [https://www.baeldung.com/spring-websockets-send-message-to-user](https://www.baeldung.com/spring-websockets-send-message-to-user)
		* [https://www.callicoder.com/spring-boot-websocket-chat-example/](https://www.callicoder.com/spring-boot-websocket-chat-example/)
	* NON-STOMP
		* ??
	* STOMP
		* rabbitmq를 사용하는 방법도 알아보자
* 참고

**코멘트**
- [ ] 구혀
- [ ] @Payload
ㅁ.
[https://www.devglan.com/spring-boot/spring-boot-websocket-integration-example](https://www.devglan.com/spring-boot/spring-boot-websocket-integration-example)

- [ ] @SubscribeMapping
ㅁ.
[https://stackoverflow.com/questions/29085791/does-spring-subscribemapping-really-subscribe-the-client-to-some-topic](https://stackoverflow.com/questions/29085791/does-spring-subscribemapping-really-subscribe-the-client-to-some-topic)
[http://clearpal7.blogspot.com/2016/07/18-websocekt-stomp_25.html](http://clearpal7.blogspot.com/2016/07/18-websocekt-stomp_25.html)

- [ ] config.setUserDestinationPrefix("/user");
ㅁ. 잘 이해 안됨

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_8.png)

ㅁ. [https://books.google.co.kr/books?id=GqDcDgAAQBAJ&pg=PA148&lpg=PA148&dq=setUserDestinationPrefix&source=bl&ots=4ywgi2hhPY&sig=ACfU3U1EQaTT44xGIQrCK5y8MIUCy8blEQ&hl=ko&sa=X&ved=2ahUKEwjY6ZyQ27LgAhWEV7wKHfC9BmEQ6AEwCHoECAAQAQ#v=onepage&q=setUserDestinationPrefix&f=false](https://books.google.co.kr/books?id=GqDcDgAAQBAJ&amp;pg=PA148&amp;lpg=PA148&amp;dq=setUserDestinationPrefix&amp;source=bl&amp;ots=4ywgi2hhPY&amp;sig=ACfU3U1EQaTT44xGIQrCK5y8MIUCy8blEQ&amp;hl=ko&amp;sa=X&amp;ved=2ahUKEwjY6ZyQ27LgAhWEV7wKHfC9BmEQ6AEwCHoECAAQAQ#v=onepage&amp;q=setUserDestinationPrefix&amp;f=false)

TODO: 여기서부터 다시 보기
- [ ] 다시 코드를 이해하면 될 것 같다.
[https://supawer0728.github.io/2018/03/30/spring-websocket/](https://supawer0728.github.io/2018/03/30/spring-websocket/)
ㅁ. [https://github.com/badalb/spring-websocket-portfolio](https://github.com/badalb/spring-websocket-portfolio)

- [ ] @MessageMapping("/groupChat") 어노테이션은 클라이언트에서 받아올 때 주소
- [ ] @SendTo("_groupChat_all") 어노테이션은 클라이언트로 보내는 주소
- [ ] @EnableWebSocketMessageBroker vs. @EnableWebSocket의 차이점?
ㅁ. @EnableWebSocket은 (onMessage…)이런 방식으로 설정하는 듯함
[https://hskimsky.tistory.com/36](https://hskimsky.tistory.com/36)
#. OT에서 설정은 어떻게 되나?
- [ ] Fully featured STOMP message broker (ex. RabbitMQ)로 설정해서 사용할 수 있음
- [ ] @MessageExceptionHandler
ㅁ. STOMP에 의해서 발생한 모든 예외는 end 사용자에게 보내짐
[https://www.devglan.com/spring-boot/spring-boot-websocket-integration-example](https://www.devglan.com/spring-boot/spring-boot-websocket-integration-example)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_3.png)

- [ ] sessionId 얻는 방법
ㅁ. interceptor로
[https://www.baeldung.com/spring-websockets-sendtouser](https://www.baeldung.com/spring-websockets-sendtouser)

- [ ] websocket endpoint
ㅁ. 스프링 5.0.5부터는 customization없이 @SendToUser(“_user_{sessionId}” (instead of “_user{_user}/“)로 메시지 보낼 수 있음

- [ ] @SendToUser 로그인 없이 보내는 방법
ㅁ. SimpleMessagingTemplate으로 보내는 방법이 있는 듯함
[https://stackoverflow.com/questions/25082148/spring-websockets-sendtouser-without-login](https://stackoverflow.com/questions/25082148/spring-websockets-sendtouser-without-login)

1. 들어가며

- [ ] 웹소켓에 대한 정의

client에서는 websocket을 사용하거나 sockjs을 사용하 수 있음.
- [ ] 각각의 장단점이 있음.

- [ ] STOMP는 text 지향의 message protocol로 websocket을 이용한 message handling을 보다 더 쉽게 만들어줌
ㅁ. 기존 websocket이나 sockjs의 경우 onmessage 함소에서 받는 메서지를 모두 handling해야 하는 단점이 있었음
#. 기존 websocket에서는 여러 topoic에 대해서 onmessage에서 분기처리 해야 하는 단점이 있었음

ㅁ. STOMP에서는 subscribe & publish로 바뀜
#.stomp에서는 subscribe(’_topic1’) or stomp에서는 subscribe(’_topic2’) : 나눠져 있음

socketjs
stomp

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_4.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_1.png)

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-websocket</artifactId>
<version>${org.springframework-version}</version>
</dependency>
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-messaging</artifactId>
<version>${org.springframework-version}</version>
</dependency>

3. 웹쇼켓 구현 in 스프링

SockJS기반 서버...

스프링 WebSocket 설정
- [ ] withSockJS()를 추가하면 client에서 GET /hello를 호출하여 서버로 부터 받은 정보를 기반으로 클라이언트가 지원여부에 따라 long poll이나 polling으로 통신한다.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_2.png)

SockJS
* javascript library로 웹쇼켓을 지원함
* Cross browser 호환
* STOMP protocal 지원
* Stomp Client과 Message Broker간의 통신 설정을 함

STOMP

설정
- [ ] @EnableWebSocketMessageBroker
ㅁ. 스프링4에 추가된 기능이고 이 어노테이션 선언으로 웹쇼켓을 지원하는 클래스 설정 파일을 활성화한다
ㅁ. message broker를 지원한다?
#. 여기서 message broker란?
- [ ] MessageBrokerRegistry
ㅁ. 이 클래스는 message broker를 동록하는데 쓰인다.
#. “/topic”이라는 broker를 simplebroker로 활성하시키고 browser와 서버가 웹쇼켓을 통해 통신할 수 있도록 destination prefix이름을 지정함
#. stompclient는 “_app_chat”으로 메시지를 보내야 함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_10.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_9.png)

- [ ] StompEndPoint를 설정한다.
ㅁ. stompclient는 _app_chat으로 메시지를 보낼 수 있다

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_5.png)

- [ ] @MessageMapping(“/chat”)
ㅁ. 웹쇼켓을 위한 URL mapping을 정의함.

- [ ] @SendTo(“_topic_messages”)
ㅁ. 1:N으로 메시지를 뿌림
ㅁ. “_topic_messages”을 subscribe하고 있는 모든 stomp client에게 메세지를 보낸다.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_7.png)

- [ ] @SendToUser(“_queue_reply”)
ㅁ. 차이점은 뭔가?
ㅁ. 1:1으로 메시지를 보낼 때 사용하는 구조이면 보통 경로가 /queue로 시작함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20WebSocket%20in%20%EC%8A%A4%ED%94%84%EB%A7%81/image_6.png)

4. 참고

* Websocket이란
	* [https://en.wikipedia.org/wiki/WebSocket](https://en.wikipedia.org/wiki/WebSocket)
* 소스 예제
	* [https://github.com/OKCoin/websocket](https://github.com/OKCoin/websocket)
	* [https://github.com/rstoyanchev/spring-websocket-portfolio](https://github.com/rstoyanchev/spring-websocket-portfolio)
	* [https://o7planning.org/en/10719/create-a-simple-chat-application-with-spring-boot-and-websocket](https://o7planning.org/en/10719/create-a-simple-chat-application-with-spring-boot-and-websocket)
	* [https://thysmichels.com/2014/08/26/metrics-dashboard-using-stomp-websockets/](https://thysmichels.com/2014/08/26/metrics-dashboard-using-stomp-websockets/)
	* [https://medium.com/@yairharel/websockets-spring-boot-application-cd33c8e90c0a](https://medium.com/@yairharel/websockets-spring-boot-application-cd33c8e90c0a)
* STOMP
	* [https://stomp.github.io/](https://stomp.github.io/)
	* [http://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3.5:ptl:stomp](http://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3.5:ptl:stomp)
	* [https://github.com/BijanVan/Spring-Boot-Websocket-Sample](https://github.com/BijanVan/Spring-Boot-Websocket-Sample)
	* [https://techblog.bozho.net/websocket-and-java/](https://techblog.bozho.net/websocket-and-java/)
* Spring Websocket Unit Test
	* [https://rafaelhz.github.io/testing-websockets/](https://rafaelhz.github.io/testing-websockets/)
	* [https://medium.com/@MelvinBlokhuijzen/spring-websocket-endpoints-integration-testing-180357b4f24c](https://medium.com/@MelvinBlokhuijzen/spring-websocket-endpoints-integration-testing-180357b4f24c)
* STMOP에 연결된 사용자
	* [https://stackoverflow.com/questions/32211170/spring-4-2-0-how-to-use-simpuserregistry](https://stackoverflow.com/questions/32211170/spring-4-2-0-how-to-use-simpuserregistry)
* Spring Websocket
	* [https://www.pixelstech.net/article/1473756404-Spring-%E2%80%93-Web-sockets-in-Java-Development](https://www.pixelstech.net/article/1473756404-Spring-%E2%80%93-Web-sockets-in-Java-Development)
	* [https://content.pivotal.io/blog/have-you-seen-spring-lately](https://content.pivotal.io/blog/have-you-seen-spring-lately)
	* [http://badalb.blogspot.com/2014/10/websockets-with-spring-4-sockjs-and.html](http://badalb.blogspot.com/2014/10/websockets-with-spring-4-sockjs-and.html)
	* [https://www.concretepage.com/spring-4/spring-4-websocket-sockjs-stomp-tomcat-example](https://www.concretepage.com/spring-4/spring-4-websocket-sockjs-stomp-tomcat-example)
	* [https://www.baeldung.com/websockets-api-java-spring-client](https://www.baeldung.com/websockets-api-java-spring-client)
	* [https://supawer0728.github.io/2018/03/30/spring-websocket/](https://supawer0728.github.io/2018/03/30/spring-websocket/)
	* [https://spring.io/guides/gs/messaging-stomp-websocket/](https://spring.io/guides/gs/messaging-stomp-websocket/)
	* [https://m.blog.naver.com/scw0531/221052774287](https://m.blog.naver.com/scw0531/221052774287)
	* [https://sjh836.tistory.com/166](https://sjh836.tistory.com/166)
	* [https://www.baeldung.com/spring-websockets-send-message-to-user](https://www.baeldung.com/spring-websockets-send-message-to-user)
	* [https://m.blog.naver.com/PostView.nhn?blogId=scw0531&logNo=221097188275&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F](https://m.blog.naver.com/PostView.nhn?blogId=scw0531&amp;logNo=221097188275&amp;proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)
	* [https://netframework.tistory.com/entry/Spring-4x%EC%97%90%EC%84%9C%EC%9D%98-WebSocket-SockJS-STOMP](https://netframework.tistory.com/entry/Spring-4x%EC%97%90%EC%84%9C%EC%9D%98-WebSocket-SockJS-STOMP)
	* [https://docs.spring.io/spring/docs/current/spring-framework-reference/web.html#websocket](https://docs.spring.io/spring/docs/current/spring-framework-reference/web.html#websocket)
	* [https://postitforhooney.tistory.com/entry/SpringStomp-Spring-stomp%EC%99%80-Socjks%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%9B%B9%EC%86%8C%EC%BC%93-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EC%9E%A5%EB%8B%A8%EC%A0%90](https://postitforhooney.tistory.com/entry/SpringStomp-Spring-stomp%EC%99%80-Socjks%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%9B%B9%EC%86%8C%EC%BC%93-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EC%9E%A5%EB%8B%A8%EC%A0%90)
	* [https://netframework.tistory.com/entry/Spring-4x%EC%97%90%EC%84%9C%EC%9D%98-WebSocket-SockJS-STOMP](https://netframework.tistory.com/entry/Spring-4x%EC%97%90%EC%84%9C%EC%9D%98-WebSocket-SockJS-STOMP)
	* [https://github.com/sungjukk/record/blob/master/websocket/stomp%20%EC%82%AC%EC%9A%A9%20%EB%B0%A9%EB%B2%95.md](https://github.com/sungjukk/record/blob/master/websocket/stomp%20%EC%82%AC%EC%9A%A9%20%EB%B0%A9%EB%B2%95.md)

#스프링 #스터디중 #blog #websocket #Spring #stomp #tistory #웹쇼켓