---
title: 'ksqlDB 소개'
tags: [kafka, ksql, ksqldb, sql, event, connect, confluent, stream, kstream, ksetl, etl]
image: '/media/cover/cover-kafka-helm.jpg'
date: 2022-10-16
---

# 1.What

ksqlDB (formerly Kafka SQL, KSQL)는 Kafka를 위한 스트리밍 SQL 엔진이다. SQL 인터페이스를 제공하고 있어 익숙한 SQL 구분으로 개발자들이 쉽게 Kafka에서 스트리밍 처리를 할 수 있게 도와준다. ksqlDB에서 제공하는 기능은 다음과 같다. 

합니다.

## 1.1 Feature

- It is distributed, scalable, reliable, and real-time
- ksqlDB combines the power of real-time stream processing with the approachable feel of a relational database through a familiar, lightweight SQL syntax
- Streams and tables 

  - Create relations with schemas over your Apache Kafka topic data
  - Materialized views ??
    - Define real-time, incrementally updated materialized views over streams using SQL
    - java library나 rest api로 query를 날릴 수 있음
  - Push queries
    - Continuous queries that push incremental results to clients in real time
  - Pull queries
    - Query materialized views on demand, much like with a traditional database
- SQL 문
- ksqlDB 내에서 Kafka Connect를 관리할 수 있도록 Connector 생성, 조회 기능을 제공
- 데이터 필터링, 변환, 집계, 조인, 윈도우 및 세션화를 포함하여 광범위한 스트리밍 작업을 지원
- 많은 내장 함수 (ex. SUM, COUNT)를 제공
  - 함수는 KSQL 쿼리 내에서 데이터를 필터링, 변환, 또는 집계하는데 사용된다
- KSQL 사용자 정의 함수도 구현 가능하도록 지원

참고

- https://docs.ksqldb.io/en/latest/developer-guide/ksqldb-reference/functions
- https://docs.confluent.io/5.4.0/ksql/docs/developer-guide/udf.html



## 1.2 ksqlDB Architecture

![Diagram showing architecture of ksqlDB](images/ksqlDB-소개/ksqldb-architecture-and-components.png)



- KSQL Server
  - KSQL 서버는 Kafka 클러스트와 통신을 하게 된다

  - Engine
    - KSQL엔진은 KSQL쿼리를 실행시킨다. KSQL 쿼리를 작성하고 실행하면 KSQL서버안에서 application을 build하고 실행시킨다. 각 KSQL서버들은 KSQL 엔진을 인스턴스로 실행시킨다. 

  - REST API
    - Rest서버는 KSQL엔진과 통신하면서 CLI나 Confluent Control Center 혹은 기타 application과 rest통신을 할 때 사용된다.

- KSQL CLI
  - KSQL CLI는 console화면에서 KSQL 엔진에 접근할 수 있도록 도와준다. KSQL CLI는 KSQL 서버인스턴스와 연동되며 streaming application을 개발하는데 사용할 수 있다. KSQL CLI는 Mysql이나 Postgre와 같은 cli와 유사한 모습으로 사용가능하다.

- KSQL UI
  - - 

- KSQL 클라이언트는 사용자의 요청을 KSQL 엔진에 전달할 수 있게 CLI 방식과 REST API 방식을 제공합니다

참고

- https://docs.confluent.io/5.4.3/ksql/docs/index.html
- https://docs.ksqldb.io/en/latest/operate-and-deploy/how-it-works/
- https://www.confluent.io/blog/ksql-streaming-sql-for-apache-kafka/
- https://docs.ksqldb.io/en/latest/tutorials/event-driven-microservice/
- https://github.com/confluentinc/ksql
- https://docs.ksqldb.io/en/latest/operate-and-deploy/how-it-works/



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
  - 2017년 KSQL Developer Preview로 공개
  - 2018년? Confluent Platform 공식 컨포넌트로 포함됨 <-- 이거 확인해보기
  - 2019년 KSQL (Kafka SQL) -> kdqlDB 재브랜딩을 위해 새로운 이름올 변경


참고

- https://docs.ksqldb.io/en/latest/operate-and-deploy/changelog/?_ga=2.211885267.679177078.1665747634-256754440.1665501546&_gac=1.60161119.1665905457.Cj0KCQjw166aBhDEARIsAMEyZh6DZ-g9fEdHzNf4ywXk1Oj2Q93_PLdfgAe_phLu9UaUpztGK_aOoFYaAsqyEALw_wcB
- https://docs.confluent.io/platform/current/installation/versions-interoperability.html#ksqldb
- https://dbdb.io/db/ksqldb
- https://www.buesing.dev/post/kafka-versions/
- https://www.linkedin.com/pulse/kafkas-origin-story-linkedin-tanvir-ahmed/


# 3. Where

다음과 같이 여러 회사에서 공식적으로 ksqlDB를 사용하고 있다고 하고 국내에서는 LINE에서 ksqlDB를 이용해서 AB Test Report 시스템을 개선했다고 한다. 

- Naver LINE
  - [AB Test Report](https://velog.io/@anjinwoong/Line-Developer-Day-2021-KSETL%EB%A1%9C-Kafka-%EC%8A%A4%ED%8A%B8%EB%A6%BC-ETL-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%84-%EB%B9%A0%EB%A5%B4%EA%B2%8C-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0) 
  - 기준 시스템 구조에서는 Redis에 저장된 event log를 가져와 join window를 구현함
  - ksqlDB를 사용해서 아키텍쳐가 단순화됨 (join two streams without redis)
- [ticketmaster](https://www.ticketmaster.com/) - 티켓 판매 회사
- [Nuuly](https://www.nuuly.com/) - 옷 렌탈 및 재판재 서비스
- [ACERTUS](https://acertusdelivers.com/) - 자동차 픽업/배달 서비스
- [optimove](https://www.optimove.com/) - CRM 마케팅 소프트웨어 (w/ AI)를 서비스로 개발 및 판매하는 비상장 회사
- [Bosch](https://www.bosch.com/): 자동차 및 산업 기술, 소비재 및 빌딩 기술 분야의 선도적 기업
- [Voicebridge](https://voicebridge.io/): voice-based systems for rural populations in developing countries that lack internet access

![image-20221016163306547](images/ksqlDB-소개/image-20221016163306547.png)

![image-20221017235058316](images/ksqlDB-소개/image-20221017235058316.png)

![image-20221017221925139](images/ksqlDB-소개/image-20221017221925139.png)



참고

- https://stackshare.io/ksql
- https://ksqldb.io/
- https://www.confluent.io/ko-kr/product/ksqldb/

# 4.Why?

- 왜 ksqldb를 사용하나?
- 개발자가 직접 코딩하기 보다
- 개발자는 sql에 대부분 익숙해져 있음

구현할 수 있는 3가지 방법

- Kafka Client를 이용한 Consumer/Producer 직접 구현 배포
- Kafka Streams API 라이브러리를 이용한 어플리케이션 구현 배포
- KSQL 문으로 로직 구현하고 KSQL 서버에 배포
- https://developer.confluent.io/tutorials/transform-a-stream-of-events/kafka.html#create-the-code-that-does-the-transformation
- https://laredoute.io/blog/why-how-and-when-to-use-ksql/
- 

## 1.3 ksqlDB vs Kafka Streams



![The Confluent Platform stack, with ksqlDB built on Kafka Streams](images/ksqlDB-소개/ksqldb-kafka-streams-core-kafka-stack.png)

https://yooloo.tistory.com/m/115

# 5.When

- 언제 사용하면 좋은가?
- 카프카는 내부 토픽을 Sub하여 분석하거나, Sub 한 토픽을 정제하여 다시 토픽으로 Pub 할 수 있습니다
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
  

참고

- https://www.rittmanmead.com/blog/2017/10/ksql-streaming-sql-for-apache-kafka/

- https://docs.ksqldb.io/en/latest/concepts/time-and-windows-in-ksqldb-queries/

  


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
- datagen source connector

## 6.3 rest api

- https://rmoff.net/2019/01/17/ksql-rest-api-cheatsheet/
- https://docs.ksqldb.io/en/latest/developer-guide/api/

## 6.4 Connector management

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
- https://www.confluent.io/ko-kr/blog/license-changes-confluent-platform/

![Apache 2.0 License | Confluent Community License | Confluent Enterprise License](images/ksqlDB-소개/relicensing-blog_faq-1920x1080px-2-1024x576.png)

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
  - https://docs.ksqldb.io/en/latest/developer-guide/ksqldb-reference/show-streams/

- ksql
  - \https://ksqldb.io/quickstart.html?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform
  - https://always-kimkim.tistory.com/entry/kafka101-ksql
  - https://www.rittmanmead.com/blog/2017/10/ksql-streaming-sql-for-apache-kafka/
  - https://www.confluent.io/blog/intro-to-ksqldb-sql-database-streaming/
  - https://docs.confluent.io/platform/current/platform-quickstart.html#ce-quickstart?utm_source=github&utm_medium=demo&utm_campaign=ch.examples_type.community_content.cp-quickstart
  - https://github.com/confluentinc/demo-scene/blob/master/introduction-to-ksqldb/demo_introduction_to_ksqldb_01.adoc
