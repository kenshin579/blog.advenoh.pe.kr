---
title: 'Kafka Connect에 대한 소개'
tags: [kafka, broker, message, connect, kafkaconnect, producer, consumer, apache, 카프카, 브로커, 메시지, 아파치, 카프카커넥트, 커넥트]
social_image: /media/cover/cover-kafka-helm.jpg
date: 2022-05-10
---

# 1. Kafka Connect란?

Kafka Connect에 대해서 언급 하기전에 간단하게 Kafka에 대해서 설명하고 

## 1.1 Kafka?



- pub-sub 모델을 지원하는 분산 메시지 큐 시스템
- Kafka Usage (todo : 이거 수정이 필요함)
  - arcbrain component 간에 데이터를 주고 받을 때
  - arcbrain <-> robot간에 데이터를 주고 받을 때



## 1.2 Kafka Connect?

Kafka Connect는 Kafka를 사용하여 다른 시스템과 데이터를 주고 받기 위한 오픈소스 프레임워크이다. Kafka Connect에는 기존 시스템에 연결하여 Kafka와 데이터를 주고 받는 데 도움이 되는 다양한 내장 커넥터를 제공해주고 있다.

- 반복적인 파이프라인 생성 작업시 매번 프로듀서 컨슈머 어플리케이션을 개발하고 배포, 운영 하는것은 비효율적이다
- 커넥트를 이용하면 특정한 작업 형태를 템플릿으로 만들어 놓은 커넥터를 실행함으로써 반복작업을 줄일 수 있다
  - Business 로직에만 집중할 수 있고, 내부 시스템 코드도 더욱 단순화되는 장점이 있음
- 커넥터는 2가지 타입이 있다
  - Source Connector (External System -> Kafka)
  - Sink Connector (Kafka -> External System)
- 다양한 Connector를 제공하고 있다 (오픈소스, 유료)
  - MongoDB, JDBC, Redis, HTTP, S3, Elasticsearch, AWS Lambda, etc
  - [Connector 목록](https://www.confluent.io/product/connectors/?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.nonbrand_tp.prs_tgt.kafka-connectors_mt.mbm_rgn.apac_lng.eng_dv.all_con.kafka-connectors&utm_term=%2Bkafka+%2Bconnector&placement=&device=c&creative=&gclid=CjwKCAjwopWSBhB6EiwAjxmqDQK_IP1BwHGk2QuxnbEMBpLSzpELe-SxeCH5U_kd8VdmaM22beSGTBoC4yEQAvD_BwE)
  - [Confluent Hub](https://www.confluent.io/hub/?_ga=2.105942858.818878415.1648561146-1727219079.1644563166&_gac=1.183425876.1648562015.Cj0KCQjw3IqSBhCoARIsAMBkTb3IVhJSR686GZrLNaiMPSNYbde-qKWCTOL8TR0_Hdew4qqm6MDPY4saAv1kEALw_wcB) - Connector App Store



![Debezium architecture](/media/go/kafka-connect에-대한-소개/84282307-8a1e0280-ab74-11ea-9fb8-689a05741d33.png)

## 1.3 Kafka Connect Usecase

1.writing databases from kafka (Arcbrain에서 사용하려고 고려중) <-- 수정이 필요함

- application -> kafka -> (kafka connect) -> db

2.building stream pipelines

- kafka -> (kafka connect) -> **multiple targets** (s3, hdfs)
- 비지니스 요구에 따라서 다양한 외부 데이터 시스템을 도입해서 빠르게 개발할 수 있음
  - LINE 쇼핑 : https://engineering.linecorp.com/ko/blog/line-shopping-platform-kafka-mongodb-kubernetes

3.migrating old application to new application (새로운 application으로 replace 하는 경우)

![Evolve Processing From Old systems to new](/media/go/kafka-connect에-대한-소개/evolve-processing-from-old-systems-to-new-kafka-connect.png)



# 2.내부 구성요서 및 동작 원리

- 커넥터 (Connector) : 파이프라인에 대한 추상 객체. task들을 관리
- 테스크 (Task) : 카프카와의 메시지 복제에 대한 구현체. 실제 파이프라인 동작 요소
  - Task Rebalancing 기능 제공
- 워커 (Worker) : 커넥터와 테스크를 실행하는 프로세스
- 컨버터 (Converter) : 커넥트와 외부 시스템 간 메시지를 변환하는 객체
- 트랜스폼 (Transform) : 커넥터를 통해 흘러가는 각 메시지에 대해 간단한 처리
- 데드 레터 큐 (Dead Letter Queue) : 커넥트가 커넥터의 에러를 처리하는 방식



![image-20220510155538827](/media/go/kafka-connect에-대한-소개/image-20220510155538827.png)




1. Plugin은 Sink Connector에 대한 구현 아티팩트를 제공한다
2. Single worker sink connector 인스턴스를 시작시킨다
3. Sink connector 데이터 처리를 위해 task를 생성한다
4. Task는 Kafka를 polling 하기 위해 병렬로 실행되고 record를 반환한다
5. Converter는 외부 데이트 시스템에 적합한 형식으로 레코드를 저장한다
6. Transform은 record를 여러 방식(ex. renaming, filtering)으로 변환한다



## 2.1 Task Rebalancing

Task Rebalancing이 일어나는 경우는 다음과 같다

1. 클러스터에 새로운 Connector가 등록이 되는 경우
   - 전체 connector와 task를 각 worker 에서 같은 양의 작업을 가지도록 재조정을 한다
2. Tasks의 rebalancing은 tasks의 수 설정을 변경하거나 connector 설정 값?을 변경하는 경우
3. 하나의 Worker 가 Failure 되는 경우
   - Fail Task는 Active한 Worker에 다시 할당되지만, 실패된 task는 자동으로 재시작되지 않고 수동으로 API로 restart 시켜야 함

![img](/media/go/kafka-connect에-대한-소개/image-20220510160001.png)

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

![image-20220510160002391](/media/go/kafka-connect에-대한-소개/image-20220510160002391.png)



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

![Create a second sink](/media/go/kafka-connect에-대한-소개/Create_Second_Sink-e1552340041115.png)



# 3. 정리



# 참고

- https://www.confluent.io/ko-kr/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/

- https://www.kai-waehner.de/blog/2020/10/20/apache-kafka-event-streaming-use-cases-architectures-examples-real-world-across-industries/

- https://www.baeldung.com/kafka-connectors-guide

- https://docs.confluent.io/platform/current/connect/index.html

- https://strimzi.io/docs/operators/latest/overview.html

- https://www.confluent.io/blog/kafka-connect-tutorial/

- 

  
