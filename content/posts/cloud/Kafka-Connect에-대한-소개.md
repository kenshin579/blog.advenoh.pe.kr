---
title: 'Kafka Connect에 대한 소개'
tags: [kafka, connect, producer, connector, consumer, 카프카, 브로커, 커넥트, 커넥터]
date: 2022-05-10
---

# 1. Kafka Connect 소개

Kafka Connect를 사용하려고 고려하고 있다면 Kafka에 대해서는 이미 잘 알고 찾아봤을 거라고 생각해서 Kafka는 간단하게 언급만 하고 바로 Kafka Connect에 대해서 소개한다. 

> 아파치 카프카(Apache Kafka)는 아파치 소프트웨어 재단이 스칼라로 개발한 **오픈 소스 메시지 브로커** 프로젝트이다. ... 
> 요컨대 분산 트랜잭션 로그로 구성된, 상당히 확장 가능한 **pub/sub 메시지 큐로 정의할 수 있으며, 스트리밍 데이터를 처리하기 위한 기업 인프라를 위한 고부가 가치 기능**이다.
>
> From [Wikipedia](https://ko.wikipedia.org/wiki/%EC%95%84%ED%8C%8C%EC%B9%98_%EC%B9%B4%ED%94%84%EC%B9%B4)

Kafka는 메시지 브로커 프로젝트 중에 하나이고 다른 프로젝트와 같이 pub-sub 모델을 지원하는 분산 메시지 큐 시스템이다. 처음 [LinkedIn](https://www.linkedin.com/feed/)에서 개발되어 2011년 초에 오픈소스화 되어 공개되고 2014년 말에는 Kafka를 개발하던 개발자들이 Confluent라는 새로운 회사를 창립하여 Kafka 개발에 집중하고 있다.

Kafka Connect는 Kafka 생태계에서 어떤 역할을 하고 있는지 알아보자. 

## 1.1 Kafka Connect

Kafka Connect는 Kafka를 사용하여 다른 시스템과 데이터를 주고 받기 위한 오픈소스 프레임워크이다. Kafka Connect에는 기존 시스템에 연결하여 Kafka와 데이터를 주고 받는 데 도움이 되는 다양한 내장 Connector(ex. mongo)를 제공해주고 있다. Kafka Connect의 특징과 장점은 다음과 같다. 

- 반복적인 파이프라인 생성 작업시 매번 프로듀서 컨슈머 어플리케이션을 개발하고 배포, 운영 하는것은 비효율적이다
- Connector를 이용하면 특정한 작업 형태를 템플릿으로 만들어 놓은 Connector를 실행함으로써 반복작업을 줄일 수 있다
  - Business 로직에만 집중할 수 있고, 내부 시스템 코드도 더욱 단순화되는 장점이 있다
- Connector는 2가지 타입이 존재한다
  - Source Connector는 외부 시스템에서 Kafka로 데이터를 넣어주는 Connector이다 (External System -> Kafka)
  
  - Sink Connector는 Kafka에서 데이터를 꺼내 외부 시스템에 데이터를 넣어주는 Connector이다. (Kafka -> External System)
- 다양한 Connector들이 존재 (ex. 오픈소스, 유료)하고 개발자들도 직접 원하는 Connector를 개발할 수 있다
  - MongoDB, JDBC, Redis, HTTP, S3, Elasticsearch, AWS Lambda, etc
  - [Connector 목록](https://www.confluent.io/product/connectors/?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.nonbrand_tp.prs_tgt.kafka-connectors_mt.mbm_rgn.apac_lng.eng_dv.all_con.kafka-connectors&utm_term=%2Bkafka+%2Bconnector&placement=&device=c&creative=&gclid=CjwKCAjwopWSBhB6EiwAjxmqDQK_IP1BwHGk2QuxnbEMBpLSzpELe-SxeCH5U_kd8VdmaM22beSGTBoC4yEQAvD_BwE)
  - [Confluent Hub](https://www.confluent.io/hub/?_ga=2.105942858.818878415.1648561146-1727219079.1644563166&_gac=1.183425876.1648562015.Cj0KCQjw3IqSBhCoARIsAMBkTb3IVhJSR686GZrLNaiMPSNYbde-qKWCTOL8TR0_Hdew4qqm6MDPY4saAv1kEALw_wcB) - Connector App Store



![Debezium architecture](Kafka-Connect에-대한-소개/1656195160.png)



## 1.2 Kafka Connect Usecase

다른 시스템에서 Kafka로 Kafka에서 다른 시스템으로 데이터를 스트리밍할 방법은 여러 가지가 있겠지만, 직접 개발하기보다는 Kafka Connect로 쉽게 해결될 수 있는지 첫 번째로 고려해보면 좋을 것이다. 몇 가지 사례를 통해서 어떻게 다양하게 사용될 수 있는지 알아보자. 

### 1.2.1 멀티 타겟 시스템에 스트리밍하기

![streaming-data-pipelines-kafka-connect](images/Kafka-Connect에-대한-소개/streaming-data-pipelines-kafka-connect.png)

Kafka Connect를 사용하면 이미 여러 타겟 시스템 대상으로 connector가 제공되어 있어서 Kafka에 저장된 데이터를 쉽게 스트리밍이 가능하다. 비즈니스 요구에 맞게 새로운 타겟 시스템이 필요할 수 있고 Kafka Connect로 인해서 빠르게 개발 단계로 이어질 수가 있다. 

- kafka -> (kafka connect) -> multiple targets (s3, hdfs)

### 1.2.2 다양한 외부 시스템에서 다른 곳으로 데이터 전달이 필요한 경우

한 component에서 다른 component로 전달할 수 있는 방법은 여러 가지가 있다. 

- A component -> db (ex. mysql) -> (mysql sink connect) -> kafka -> B component (consume)

  - 어드민 성격의 component에서 설정 값을 mysql에 저장한다. 
  - 이 값을 다른 component에서 사용할 필요가 있는 경우에는 mysql source connector를 등록해서 사용하면 쉽게 다른 component로 전달할 수 있다

- A component (http API 노출) -> (http source connect) -> kafka -> (mongo sink connector) -> db (ex.mongo) -> B component

  - B component는 mongodb로 read/write 할 수 있는 application이지만, A component의 역할과 domain에 따라서 직접 db에 접근하는 건 부절적한 경우가 있어 kafka를 이용해서 event 기반으로 개발한다

  - A component에서 직접 kafka로 write 할 수도 있지만, http API로 노출해서 http source connector를 이용해서 kafka로 전달하고 mongo sink connector를 이용해서 db에 넣으면 각 component에서 추가 개발 없이도 B component로 데이터를 전달할 수 있다

    

### 1.2.3 새로운 어플리케이션으로 마이그레이션 작업

![Evolve Processing From Old systems to new](Kafka-Connect에-대한-소개/evolve-processing-from-old-systems-to-new-kafka-connect.png)

- db(ex. mysql) -> (mysql sink connect) -> kafka -> new application (consume)

새로운 어플리케이션 개발할 때 기존의 어플리케이션에는 영향을 주지 않기 위해 Kafka Connect를 사용하면 더 쉽게 마이그레이션이 가능할 수 있다. Mysql이나 MongoDB는 Change Data Cpature (CDC) 기능을 지원하고 있어서 해당 Sink connector를 사용하면 스키마 변경, INSERT, UPDATE, DELETE 모두에 대한 변경은 포착을 해서 Kafka로 데이터를 스트리밍할 수 있다. 이렇게 되면 기존 어플리케이션에는 전혀 수정하지 않고 새로운 어플리케이션을 개발할 수 있다. 

# 2.내부 구성요서 및 동작 원리

Kafka Connect가 동작하기 위해 내부적으로 구성된 여러 요소들에 대해서 알아봅니다. 

Sink Connector가 

기준으로 Kafka로부터 데이터를 가져와서 외부 시스템에 저장하는 

다이어그림이다. 

![image-20220510155538827](Kafka-Connect에-대한-소개/image-20220510155538827.png)

> Plugin은 connectors 와 task의 컬렉션이고 
>


1. Plugin은 Sink Connector에 대한 구현 아티팩트를 제공한다
2. Single worker sink connector 인스턴스를 시작시킨다
3. Sink connector 데이터 처리를 위해 task를 생성한다
4. Task는 Kafka를 polling 하기 위해 병렬로 실행되고 record를 반환한다
5. Converter는 외부 데이트 시스템에 적합한 형식으로 레코드를 저장한다
6. Transform은 record를 여러 방식(ex. renaming, filtering)으로 변환한다



- 커넥터 (Connector) : 파이프라인에 대한 추상 객체이고 Task들을 관리한다
  - task 간의 작업을 나누는 일
  - worker로부터 task를 위한 설정 값을 가져오고 task에게 전달해줌
    - sink 작업을 위해 몇개의 task를 실행할지
- 테스크 (Task) : Kafka의 메시지 복제에 대한 구현체이고 실제 파이프라인 동작 요소이다
  - Kafka로부터 데이터를 가져오고나 넣는 작업을 한다
  - Source Task는 source system으로 부터 데이터를 poll하고 worker를 그 데이터를 Kafka Topic로 보낸다
  - Sink Task는 Kafka로부터 Worker를 통해서 record를 가져오고 SInk system에 record를 쓴다
  - Task Rebalancing 기능을 제공한다
  - 
- 워커 (Worker) : Connector와 Task를 실행하는 프로세스이다
  - Worker가 Task를 시작시킨다
- 컨버터 (Converter) : Connector와 외부 시스템 간의 메시지를 변환하는 객체이다
- 트랜스폼 (Transform) : Connector를 통해 흘러가는 각 메시지에 대해 간단한 변환처리를 한다
- 데드 레터 큐 (Dead Letter Queue) : Connect가 Connector의 에러를 처리하는 방식중에 하나이다

![Kafka Connect Cluster](images/Kafka-Connect에-대한-소개/Kafka-Connect-Architecture-diagram-2.png)



## 2.1 Task Rebalancing

Task Rebalancing이 일어나는 경우는 다음과 같다

1. 클러스터에 새로운 Connector가 등록이 되는 경우
   - 전체 connector와 task를 각 worker 에서 같은 양의 작업을 가지도록 재조정을 한다
2. Tasks의 rebalancing은 tasks의 수 설정을 변경하거나 connector 설정 값?을 변경하는 경우
3. 하나의 Worker 가 Failure 되는 경우
   - Fail Task는 Active한 Worker에 다시 할당되지만, 실패된 task는 자동으로 재시작되지 않고 수동으로 API로 restart 시켜야 함

![img](Kafka-Connect에-대한-소개/image-20220510160001.png)

## 2.2 Workers

Worker는 Connector와 Task를 실행하는 프로세스이고 Worker를 실행하는 모드를 2가지를 제공한다.

- Standalone Mode
  - 모든 connector와 task에 대한 실행을 하나의 process가 담당을 함
  - 로컬머신에서 개발이나 테스트시 사용됨
  - fault tolerance은 지원하지 않음
- Distributed Mode
  - Worker는 여러 머신(node)에서 실행됨
  - 분산 모드에서는 scalability and 자동 fault tolerance를 지원함
  - production에서 사용

![image-20220510160002391](Kafka-Connect에-대한-소개/image-20220510160002391.png)



## 2.3 Converters

Kafka에서 write, read할 때 특정 데이터 형식을 지원하기 위해서 여러 Converter를 제공한다. Task는 Converter를 사용해서 bytes 데이터 형식을 Connect 내부 데이터 형식으로 변경해서 사용한다

- AvroConverter
  - `io.confluent.connect.avro.AvroConverter`: use with Schema Registry
- ProtobufConverter
  - `io.confluent.connect.protobuf.ProtobufConverter`: use with Schema Registry
- JsonSchemaConverter
  - `io.confluent.connect.json.JsonSchemaConverter`: use with Schema Registry
- JsonConverter
  - `org.apache.kafka.connect.json.JsonConverter` (without Schema Registry): use with structured data
- StringConverter
  - `org.apache.kafka.connect.storage.StringConverter`: simple string format
- ByteArrayConverter
  - `org.apache.kafka.connect.converters.ByteArrayConverter`: provides a “pass-through” option that does no conversion
  - 

## 2.4 Transforms

Kafka Connect는 데이터를 변환해주시는 기능을 제공한다.

- 필드를 추가하거나 filtering, renaming 기능도 기본적으로 제공함

- Custom transform도 개발이 가능함

- chain 방식으로 여러 transform을 적용할 수 있음

  

## 2.5 Error Handling



- 오류 발생시 멈춤 (기본 설정)
- 모든 오류 허용 (invalid message 그냥 무시)
- Dead Letter Queue에 저장

![Create a second sink](Kafka-Connect에-대한-소개/Create_Second_Sink-e1552340041115.png)



# 3. 정리

Kafka Connect를 사용하면 어플리케이션에서 반복적으로 개발해야 하는 부분들을 많이 제거할 수 있고 이로 인해서 자연스럽게 비지니스 로직에 집중할 수 있는 장점이 생긴다. 

application 단에서 

Kafka Connect 소개 자료로 커넥트에 있는 여러 기능에 대해서 간단하게 언급만 했다. 각 기능에 대해서는 세부적으로 다루도록 한다. 

# 4. 참고

- https://en.wikipedia.org/wiki/Apache_Kafka

- https://www.confluent.io/ko-kr/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/

- https://www.kai-waehner.de/blog/2020/10/20/apache-kafka-event-streaming-use-cases-architectures-examples-real-world-across-industries/

- https://www.baeldung.com/kafka-connectors-guide

- https://docs.confluent.io/platform/current/connect/index.html

- https://strimzi.io/docs/operators/latest/overview.html

- https://www.confluent.io/blog/kafka-connect-tutorial/

- https://www.instaclustr.com/blog/apache-kafka-connect-architecture-overview/

- 

  
