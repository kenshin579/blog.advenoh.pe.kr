# 블로그 : RabbitMQ 사용법
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] rabbitmq가 뭔가
- [ ] 현재 프로젝트에서 설정 및 어떻게 사용되는지 알아보기
ㅁ.

- [ ] 어느 application에 사용하는게 좋은가?
ㅁ.채팅?
ㅁ.메시징은 어느 곳에서 사용하는게 좋은 가?

- [ ] rabbitmq을 reboot하면 tomcat도 같이 reboot을 해야 하나?
ㅁ.

1. 들어가며

RabbitMQ는 메시지는 받아 다른 곳으로 보내는 메시지 브로커입니다.
Java와 Erlang 으로 개발됨.

RabbitQM의 특징

먼저 용어 정리하고 들어갈게요.

* (P) Producer: Producer는 메세지를 생성(producing)해서 보내는 프로그램이다
* (C) Consumer: Consumer는 메시지를 수진(consuming)하는 프로그램이다
	* 같은 작업을 처리하는 Consumer는 보통 하나의 Queue를 바라 본다 (중복방지)
		* 자동으로 메시지를 분배하여 전달됨
* Queue : 메시지를 저장하는 버퍼이다
	* Queue는 Exchange에 Bindings된다?
* Publish : Producer가 메시지를 보냄
* Subscribe : Consumer가 메세지를 수진하기 위해 Queue를 실시간으로 리스닝함
* (X) Exchange : Producer가 전달할 메시지를 Queue에 전달하는 역할
	* 메시지는 queue에 직접 전달되지 않고 exchange type이라는 속성에 정의에 따라서 동작한다

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_11.png)

* Exchange Type : 타입에 따라서 전달 하는 방식이 다르다

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_9.png)

* Bindings : Exchange와 Queue를 연결해준다
* Routing : Exchange가 Queue에 메시지를 전달하는 과정을 말한다
* RoutingKey : Exchange와 Queue가 binding 될때 Exchange가 Queue에 메시지를 전달하는 기준?
	* 잘 이해 안됨

- [ ] AMQP 프로토콜을 구현한 메시지 큐임
- [ ] AMQP의 중요 3가지 컴포넌트
1. exchange : 발행자로부터 수신한 메시지를 큐 또는 다른 익스체인지로 보내는 라우터 역할
ㅁ. 익스체인지는 익스체인지 타입과 비인딩이라는 규칙을 따르는 라우터 알고리즘에 의해 움직임
2. queue
3. binding

- [ ] 핵심 : 라우터 키와 함께 메시지를 익스체인지로 보내면 익스체인지 타입별로 메시지를 큐로 보낸다.

1. Default exchange : 생성한 큐에 모두 자동 바인딩
2. Direct exchange : 라우팅 키와 1대1 바인딩
3. Topic exchange : 직접 익스체인지와 비슷하나, 라우팅 키에 와일드 키를 추가해서 비인딩할 수 있음
4. Headers exchange : 메시지 헤더에 따라 바인딩하는 기능
5. Fanout exchange : 메시지를 바인딩한 큐 전체에 복사함 (broadcasting)

2. 개발 환경 및 RabbitMQ 설치

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

**2.1 Rabbitmq 설치하기**
recording asciinema로 저장하기

패키지 설치
># brew install rabbitmq

**Management Plugin 활성화**
># rabbitmq-plugins enable rabbitmq_management

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_26.png)

># rabbitmq-server

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_2.png)

- [ ] 아래 접속
[http://localhost:15672/#/](http://localhost:15672/#/)

계정
guest/guest

계정 생성하기

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_7.png)

RabbitMQ 관리
초기화

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_20.png)

rabbitmqadmin

3. RabbitMQ ??

3.1 간단한 큐로 메시지 ‘Hello world’ 보내기

Producer가 큐에 ‘Hello world’ 메시지를 보내면 Consumer가 보낸 메시지를 받아 출력하는 메시지입니다.

Send.java & Receive.java 참조

queues에 몇개가 들어가 있는지 확인
- [ ] send 하나 하면 queue에 하나 들어감

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_16.png)

3.2 Work Queues (aka. Task Queues)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_15.png)

Producer(ex. NewTask.java)가 메시지를 계속 보내면 메시지를 받는 여러 개의 Consumer(ex. Worker.java)가 메시지를 수신하여 처리하는 예제입니다. 병렬로 처리가 된다.
- [ ] round-robin dispatching…
ㅁ. 기본으로 메시지를 처리하는 방식은 메시지가 온 순서대로 차례대로 다음 consumer에게 감.

- [ ] Message ack
ㅁ. ack를 통해서 메시지가 lost되는 것을 방지함. 한 consumer가 작업중 죽게 되면 RabbitMQ는 메시지를 re-queue해서 다른 consume에게 전달되도록 함.
ㅁ. 메시지 timeout은 존재하지 않고 consumer가 죽게 되면 다시 처리된다.
ㅁ. 기본으로 ack가 작동함

- [ ] debug시… unack된 메시지 개수 확인...

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_5.png)

- [ ] Message durablity
ㅁ. rabbitmq가 죽게 되면 메시지를 날라감
ㅁ. queue와 messages가 durable로 지정해야 함
ㅁ. RabbitMQ는 이미 생성한 큐를 재 설정하지 않는다.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_22.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/A2436A6D-6960-4E61-A377-C35D6F99F6C8.png)

ㅁ.RabbitMQ는 완벽하게 persistency를 보장하지 않음. (ex. 받은 메시지를 바로 flush하지 않음)

- [ ] Fair dispatch
ㅁ. RabbitMQ는 기본적으로 evenly하게 dispatch를 함 (10개의 메시지가 있으면 2개의 consume에 5개씩 부조건 할당됨)
ㅁ. 한쪽만 busy 한 형상이 발샣알 수 있음
ㅁ. 해결 : 메세지를 하나 이상주지 않도록 설정함. (새로운 메시지를 주지 않은 busy하면… 다음 consumer에게 전달함)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_23.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_12.png)

- [ ] queue size
ㅁ. 큐에 많이 쌓이면 문제가 생길 수 있음.. consumer을 더 늘리던지 해야 함.
ㅁ. 큐에 넣지 못하면 날라가나?

- [ ] NewTask는 3개의 스트링 값을 …에 대한 설명…
- [ ] Worker.java에 대한 설명 넣기

- [ ] 실행에 대한 설명…
ㅁ. mux에서 실행해서 보여주면 좋을 것 같다.

># cd rabbitmq-amqp-client/

># mvn clean package
># mvn exec:java -Dexec.mainClass=“com.rabbitmq.queue.task.Worker"
># mvn exec:java -Dexec.mainClass=“com.rabbitmq.queue.task.Worker”

Intellij에서 바로 실행하던지 아니면 아래 명령어로 터미널에서 실행하면 됩니다.

># mvn exec:java -Dexec.mainClass="com.rabbitmq.queue.task.NewTask"

3.3 Publish / Subscribe에 대한 예제

Producer(EmitLog)가 메시지를 보내면 여러 Consumer(ReceiveLogs)가 한번에 메시지를 받아 처리하는 Pub/Sub 패턴 예제입니다.

- [ ] RabbitMQ에서 producer가 직접 consumer에게 보내지는 않습니다. Producer는 단지 exchange에게 메시지를 보낼 뿐입니다. Exchange가 하는 역할은 메시지를 받아서 Queue에 넣습니다. 하지만, Exchange가 구체적으로 한 큐에 넣을 지 여러 큐에 넣을 등의 규칙을 알아야 합니다. 이런 규칙을 Exchange Type이라고 합니다.

- [ ] 4개자 타입이 존해함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_1.png)

현재 exchanges 목록을 볼 수 있음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_24.png)

- [ ] nameless exchange
ㅁ. empty string””으로 지정하면 default exchange로 지정됨.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_8.png)

- [ ] Temporary queues
ㅁ. 임시 큐도 생성할 수 있음
#. rabbit에 접속하면 empty queue
#. random queue name

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_28.png)

#. consumer가 없으면 자동 큐삭제

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_25.png)

- [ ] Bindings
ㅁ. Exchange와 queue의 관계를 binding이라고 하며 exchange가 메시지를 큐로 보내기 위해 binding 설정이 필요하다
ㅁ. 현재 binding된 목록
># rabbitmqctl list_bindings

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_3.png)

># mvn exec:java -Dexec.mainClass=“com.rabbitmq.queue.task.ReceiveLogs"
># mvn exec:java -Dexec.mainClass=“com.rabbitmq.queue.task.ReceiveLogs"

logs exchange는 random queue 2개와 연결됨

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_13.png)

3.5 Routing

모든 메시지를 받는 것 대신 특정 메시지만 받을 수 있는 예제입니다.

Binding시 routingKey를 추가하여

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_17.png)

- [ ] direct exchange
ㅁ. 메시지는 큐와 바인딩 binding_key가 정확하게 메시지의 routing_key와 매칭되는 것들만 보낸다.
* Q1은 orange binding_key와 바인딩되어 있고 Q2는 black, green binding_key와 바인딩 됨
* 메시지가 routing key orange와 함께 exchange로 publish하면, Q1으로 보내진다.
* 다른 메시지들은 그냥 무시된다.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_6.png)

- [ ] Multiple bindings
ㅁ. 같은 binding key를 여러 큐에 바인딩 시킬 수 있음 (fanout처럼 동작함 - broadcasting)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_19.png)

- [ ] Emitting logs
ㅁ. severity : info, warning, error

- [ ] Subscribing

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_27.png)

># mvn clean package

Consumer
># mvn exec:java -Dexec.mainClass="com.rabbitmq.exchange.routing.ReceiveLogsDirect" -Dexec.args=“warning error"

Producer
># mvn exec:java -Dexec.mainClass="com.rabbitmq.exchange.routing.EmitLogDirect" -Dexec.args="error 'hello world’"

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_4.png)

3.6 Topic

Direct exchange의 경우에는 선택적으로 원하는 로그만 받도록 했다면, Topics exchange는 pattern(topics)에 따라서 메시지를 받을 수 있습니다.

- [ ] Topic exchange
ㅁ. 메시지와 함께 보내지는 routing key값은 하나의 값이 아닌 점으로 구분된 여러 값목록이어야 한다.
ㅁ. binding key 또한 같은 형식어어야 한고 다음과 같은 의미를 가기게 됨
* * : exactly one word와 substitute
* # : zero or more words와 substitute

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_18.png)

routing_key : <speed>.<colour>.<species>

* **.orange.**
	* Q1 : 오랜지 색의 동물들
* **.**.rabbit : 토끼들만
* lazy.# : 색깔 동물 상관없이 lazy한 것들 모두
* # : 모든 메시지를 받음
* 아무것도 사용하지 않으면 : direct과 같음 (왜?)

**Consumer**
># mvn clean compile
># mvn exec:java -Dexec.mainClass="com.rabbitmq.exchange.topics.ReceiveLogsTopic" -Dexec.args=“#”
># mvn exec:java -Dexec.mainClass="com.rabbitmq.exchange.topics.ReceiveLogsTopic" -Dexec.args="*.critical"
># mvn exec:java -Dexec.mainClass="com.rabbitmq.exchange.topics.ReceiveLogsTopic" -Dexec.args="kern.*"

**Producer**
># mvn exec:java -Dexec.mainClass="com.rabbitmq.exchange.topics.EmitLogTopic" -Dexec.args="cron.critical 'hello world’"

3.7 RPC

Request/reply pattern으로 remote에서 함수를 실행하고 그 결과는 받을 수 있는 패턴입니다.

- [ ] callback queue
ㅁ. 응답을 받으려면 callback queue 주소(ex. reply_to)를 request와 같이 보냄

- [ ] correlation id
ㅁ. 추천 : single callback queue per client (대신 : callback queue per rpc request)
#. response을 받을 때 어떤 request에 대한 응답인지 구분하기 위해서 correlation id가 필요함
ㅁ. callback queue에 있는 unknown 메시지는 무시해야 하나 (왜)?
#. RPC 서버가 죽고 다시 시작할 때, 다시 같은 request을 다시 보내기 때문에,

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_14.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20RabbitMQ%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_21.png)

4. 결론

다음 포스팅에서는 스프링에서 RabbitMQ을 사용하는 방법에 대해서 알아보겠습니다.

4. 참고

* RabbitMQ
	* [http://gjchoi.github.io/rabbit/](http://gjchoi.github.io/rabbit/)
	* [https://www.cloudamqp.com/blog/2015-09-03-part4-rabbitmq-for-beginners-exchanges-routing-keys-bindings.html](https://www.cloudamqp.com/blog/2015-09-03-part4-rabbitmq-for-beginners-exchanges-routing-keys-bindings.html)
* RabbitMq 설치 및 관리
	* [https://dzone.com/articles/understanding-when-to-use-rabbitmq-or-apache-kafka](https://dzone.com/articles/understanding-when-to-use-rabbitmq-or-apache-kafka)
	* [https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html)
	* [https://www.rabbitmq.com/getstarted.html](https://www.rabbitmq.com/getstarted.html)
	* [http://hyeonjae-blog.logdown.com/posts/306170-rabbitmq](http://hyeonjae-blog.logdown.com/posts/306170-rabbitmq)
	* [https://jdm.kr/blog/138](https://jdm.kr/blog/138)
	* [http://corecode.pe.kr/2018/02/04/RabbitMQ_usage/](http://corecode.pe.kr/2018/02/04/RabbitMQ_usage/)
* RabbitMQ는 언제 사용하나?
	* [https://stackoverflow.com/questions/5132648/why-do-we-need-to-use-rabbitmq](https://stackoverflow.com/questions/5132648/why-do-we-need-to-use-rabbitmq)
	* [https://stackoverflow.com/questions/29539443/redis-vs-rabbitmq-as-a-data-broker-messaging-system-in-between-logstash-and-elas](https://stackoverflow.com/questions/29539443/redis-vs-rabbitmq-as-a-data-broker-messaging-system-in-between-logstash-and-elas)
* Use Cases
	* [https://donchev.is/post/redis-kafka-ra](https://donchev.is/post/redis-kafka-ra)
* Redis vs RabbitMQ
	* [https://www.quora.com/Which-is-better-to-use-as-a-message-broker-for-concurrency-RabbitMQ-or-Redis](https://www.quora.com/Which-is-better-to-use-as-a-message-broker-for-concurrency-RabbitMQ-or-Redis)
* Spring
	* [https://github.com/spring-projects/spring-amqp-samples](https://github.com/spring-projects/spring-amqp-samples)
	* [https://docs.spring.io/spring-amqp/reference/](https://docs.spring.io/spring-amqp/reference/)
	* [https://github.com/muiruri/SpringRabbitMQSample](https://github.com/muiruri/SpringRabbitMQSample)
	* [http://blog.naver.com/PostView.nhn?blogId=tmondev&logNo=220419853534](http://blog.naver.com/PostView.nhn?blogId=tmondev&amp;logNo=220419853534)
* AMQP
	* [https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)