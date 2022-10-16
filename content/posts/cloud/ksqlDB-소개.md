---
title: 'ksqlDB 소개'
tags: [kafka, ksql, ksqldb, event, connect, confluent, stream]
image: '/media/cover/cover-kafka-helm.jpg'
date: 2022-10-16
---

# 1.What

ksqlDB (예전 이름: Kafka SQL, KSQL)는 

 is an event streaming database for Apache Kafka



- KSQL is the streaming SQL engine for Apache Kafka. It provides an easy and completely interactive SQL interface for stream processing on Kafka—no need to write any code in a programming language such as Java or Python. KSQL supports a wide range of powerful stream processing operations including filtering, transformations, aggregations, joins, windowing, sessionization, and much more
- KSQL is open source (Apache 2.0 licensed), distributed, scalable, fault-tolerant, and real-time.

## 1.1 Feature

- It is distributed, scalable, reliable, and real-time

- ksqlDB combines the power of real-time stream processing with the approachable feel of a relational database through a familiar, lightweight SQL syntax. ksqlDB offers these core primitives:

- - Streams and tables 
    - Create relations with schemas over your Apache Kafka topic data
  
  - Materialized views ??
    - Define real-time, incrementally updated materialized views over streams using SQL
    - java library나 rest api로 query를 날릴 수 있음
  
  - Push queries
    - Continuous queries that push incremental results to clients in real time
  
  - Pull queries
    - Query materialized views on demand, much like with a traditional database

  - Connect 
    - Integrate with any Kafka Connect data source or sink, entirely from within ksqlDB
  
- 여러 함수들을 제공해준다
  - STRINGTOTIMESTAMP(Created_At, 'EEE MMM dd HH:mm:ss ZZZZZ yyyy') AS Created_At
  - EXTRACTJSONFIELD(User, '$.name') as User_name
  - kafka connect에서도 simple transform을 지원함
  - 별도 topics 간의 joining도 가능하다
  - windows 함수도 지원함

- 아주복잡한 건 streams api를 사용해서 직접 구현하거나 아니면 ksql으로 충분하다면 괜찮을 듯함
  - kafka stream api를 사용해서 개발을 했음




## 1.2 Architecture

![../../_images/ksql-architecture-and-components.png](images/ksqlDB-소개/ksql-architecture-and-components.png)

- KSQL Server
- KSQL CLI
- KSQL UI
- KSQL 클라이언트는 사용자의 요청을 KSQL 엔진에 전달할 수 있게 CLI 방식과 REST API 방식을 제공합니다

참고

- https://docs.confluent.io/5.4.3/ksql/docs/index.html
- https://www.confluent.io/blog/ksql-streaming-sql-for-apache-kafka/
- https://docs.ksqldb.io/en/latest/tutorials/event-driven-microservice/
- https://github.com/confluentinc/ksql
- https://docs.ksqldb.io/en/latest/operate-and-deploy/how-it-works/
- 

# 2.Who

- ksqlDB는 Confluent 회사에 의해서 2017년부터 개발되었다

## 2.1 History

- Kafka
  - 2010년 LinkedIn에서 내부 회사에서 발생하고 있는 이슈들을 해결하기 위해 만들어짐
  - 2011년 Apache Kafka 오픈소스로 세상에 처음 공개
  - 2014년 Confluent 회사 설립
    - Kafka 공동 창시자가 LinkedIn을 나와서 새로운 회사를 설립

- Kafka Connect
  - 2015년 Kafka 0.9.0.0 relealse 버전에 포함

- Kafka Stream
  - 2016년 Kafka 0.10.0.0 release 버전에 포함
- ksqlDB
  - 2017년부터 개발 시작
  - 2019년 KSQL (Kafka SQL) -> kdqlDB 재브랜딩을 위해 새로운 이름올 변경


참고

- https://docs.ksqldb.io/en/latest/operate-and-deploy/changelog/?_ga=2.211885267.679177078.1665747634-256754440.1665501546&_gac=1.60161119.1665905457.Cj0KCQjw166aBhDEARIsAMEyZh6DZ-g9fEdHzNf4ywXk1Oj2Q93_PLdfgAe_phLu9UaUpztGK_aOoFYaAsqyEALw_wcB
- https://docs.confluent.io/platform/current/installation/versions-interoperability.html#ksqldb
- https://dbdb.io/db/ksqldb
- https://www.buesing.dev/post/kafka-versions/
- https://www.linkedin.com/pulse/kafkas-origin-story-linkedin-tanvir-ahmed/


# 3. Where

- ksql 어느회사에서 사용?
- https://www.confluent.io/ko-kr/product/ksqldb/
- https://ksqldb.io/?_ga=2.225034205.679177078.1665747634-256754440.1665501546&_gac=1.28168270.1665905457.Cj0KCQjw166aBhDEARIsAMEyZh6DZ-g9fEdHzNf4ywXk1Oj2Q93_PLdfgAe_phLu9UaUpztGK_aOoFYaAsqyEALw_wcB
- 

![image-20221016163306547](images/ksqlDB-소개/image-20221016163306547.png)

- LINE

# 4.Why?

- 왜 ksqldb를 사용하나?
- 개발자가 직접 코딩하기 보다
- 개발자는 sql에 대부분 익숙해져 있음

# 5.When

- 언제 사용하면 좋은가?

- 카프카는 내부 토픽을 Sub하여 분석하거나, Sub 한 토픽을 정제하여 다시 토픽으로 Pub 할 수 있습니다

- 구현할 수 있는 3가지 방법
  - Kafka Client를 이용한 Consumer/Producer 직접 구현 배포
  - Kafka Streams API 라이브러리를 이용한 어플리케이션 구현 배포
  - KSQL 문으로 로직 구현하고 KSQL 서버에 배포
  - https://developer.confluent.io/tutorials/transform-a-stream-of-events/kafka.html#create-the-code-that-does-the-transformation
  - https://laredoute.io/blog/why-how-and-when-to-use-ksql/
  - 

- 기존 database와 다른 점은?
  - continuous queries
  - 주요 차이점은 연속 쿼리의 개념입니다. KSQL을 사용하면 Kafka 주제에 새 데이터가 도착할 때마다 변환이 지속적으로 수행됩니다.


## 5.1 usecase

일반적인 관점에서 KSQL은 데이터 스트림 동안 변환, 통합 및 분석이 즉시 발생할 때 사용해야하는 것입니다.

- real time analytics
- security and anomaly detection
- oneline

참고

- https://github.com/confluentinc/ksql/tree/0.1.x/docs#ksql-documentation
- https://developer.confluent.io/tutorials/

# 6.How

## 6.1 로컬 설치 및  ksql 사용법

- query

  - transient
  - persistent
  - push
  - pull

- windows 

  - windowing is an useful option, especially when combined with HAVING clauses since it gives the option to define metrics for real time analysis.

    - I may be interested only items that have been ordered more than 100 times in the last hour, or, in my twitter example in user_locations having a nr_of_tweets greater than 5 in the last 30 minutes.

  - tumbling
    - Fixed size, non overlapping
    - size
  
  - hopping
    - Fixed size, possibly overlapping
    - size, advance
  
  - sessions
    - Fixed size, starting from the first entry for a particular Key, it remains active until a new message with the same key happens within the INACTIVITY_GAP which is the parameter to be specified
  

![image-20221016162716549](images/ksqlDB-소개/image-20221016162716549.png)

참고

- https://www.rittmanmead.com/blog/2017/10/ksql-streaming-sql-for-apache-kafka/
- https://docs.ksqldb.io/en/latest/concepts/time-and-windows-in-ksqldb-queries/
- 




- table과 stream간의 관계?

- table

- - 스트림의 상태 정보의 축적

- stream

- - stream은 table 변경 로그임?

![image-20221016162313016](images/ksqlDB-소개/image-20221016162313016.png)



## 6.2 datagen & confluent control center UI 소개

- kafka 관련 component 한곳에서 볼 수 있다
  - Kafka connect, ksqlDB, kafka
- 유료임
- 
- datagen source connector
- []



- 

## 6.3 rest api

- https://rmoff.net/2019/01/17/ksql-rest-api-cheatsheet/
- https://docs.ksqldb.io/en/latest/developer-guide/api/

## 6.4 connector management

- source connector
- sink connector

```sql
CREATE SOURCE CONNECTOR rider_profiles WITH (
  'connector.class'          = 'io.confluent.connect.jdbc.JdbcSourceConnector',
  'connection.url'           = 'jdbc:postgresql://postgres:5432/postgres',
  'key'                      = 'profile_id',
  ...
 );
```



## 6.5 ksql library

- golang

- - https://github.com/VinGarcia/ksql
  - https://github.com/rmoff/ksqldb-go
  - https://github.com/VinGarcia/ksql

- java

- - https://www.baeldung.com/ksqldb
  - https://docs.ksqldb.io/en/latest/developer-guide/ksqldb-clients/java-client/

# 7. FAQ

ksqlDB 다양한 FAQ는 아래를 참고해주세요. 

- https://docs.ksqldb.io/en/latest/faq/

## 7.1 ksqlDB의 license는 Apache License 2.0인가?

- Apache License는 아니다. 
- This is a community component of Confluent Platform. ksqlDB is owned and maintained by Confluent Inc. as part of its Confluent Platform product. However, ksqlDB is licensed under the .
- ksqlDB는 Confluent Community License가 부여되었고 Confluent 회사 제품으로 관리되고 있다



## 7.2 Confluent Community License는 어떤 제약이 있나?

> “Excluded Purpose” is making available any software-as a-service, platform-as-a-service, infrastructure-as-a-service or other similar online service that competes with Confluent products or services that provide the Software.

- ksqlDB을 사용해서 Confluent에서 제공하는 형태의 서비스만 제공하지 않으면 사용할 수 있는 것 같다
- 회사 내부 프로젝트에 사용하려면, 사용전에 라이센스 검토가 필요할 것으로 판단된다
- https://www.confluent.io/confluent-community-license-faq/

# 8. Terms

# 9. Summary

- usecase
  - real time analytics
  - security and anomaly detection
  - oneline



- https://www.confluent.io/product/stream-designer/
- https://www.confluent.io/blog/building-streaming-data-pipelines-visually/?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.brand_tp.prs_tgt.confluent-brand_mt.mbm_rgn.apac_lng.kor_dv.all_con.confluent-version&utm_term=confluent+version&placement=&device=c&creative=&gclid=Cj0KCQjw166aBhDEARIsAMEyZh6DZ-g9fEdHzNf4ywXk1Oj2Q93_PLdfgAe_phLu9UaUpztGK_aOoFYaAsqyEALw_wcB&_ga=2.253349966.679177078.1665747634-256754440.1665501546&_gac=1.90700264.1665905457.Cj0KCQjw166aBhDEARIsAMEyZh6DZ-g9fEdHzNf4ywXk1Oj2Q93_PLdfgAe_phLu9UaUpztGK_aOoFYaAsqyEALw_wcB
- 

# 10. Reference

- ksql syntax

- - https://docs.ksqldb.io/en/latest/developer-guide/ksqldb-reference/show-streams/

- ksql

- - https://ksqldb.io/quickstart.html?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform
  - https://always-kimkim.tistory.com/entry/kafka101-ksql
  - https://www.rittmanmead.com/blog/2017/10/ksql-streaming-sql-for-apache-kafka/
  - https://www.confluent.io/blog/intro-to-ksqldb-sql-database-streaming/
  - https://docs.confluent.io/platform/current/platform-quickstart.html#ce-quickstart?utm_source=github&utm_medium=demo&utm_campaign=ch.examples_type.community_content.cp-quickstart
  - https://github.com/confluentinc/demo-scene/blob/master/introduction-to-ksqldb/demo_introduction_to_ksqldb_01.adoc
