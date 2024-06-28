---
title: "로컬환경에서 Kafka 실행하기 (with AKHQ)"
description: "로컬환경에서 Kafka 실행하기 (with AKHQ)"
date: 2022-08-07
update: 2022-08-07
tags:
  - kafka
  - docker
  - local
  - akhq
  - 로컬환경
  - 카프카
---

로컬환경에서 Kafka를 실행하는 방법에 대해서 알아보자. 개인 맥북이 M1이라서 M1 기준으로 실행방법에 대해서 기술합니다.

## 1.실행 조건

`docker-compose` 명령어를 이용해서 Kafka를 실행하기 위해서 아래 조건이 만족되어야 실행 가능하다. 아래 조건은 기본이라서 본 포스팅에서 추가로 설명하지 않습니다.

- Docker 실행중이어야 한다
- `docker-compose`가 설치되어 있어야 한다

## 2.Kafka 실행하기

사용자가 쉽게 Kafka를 실행할 수 있도록 여러 오픈소스 프로젝트에서 `docker-compose`나 `helm` 설정 파일을 제공하고 있다. 공개된 프로젝트의 파일을 이용해서 Kafka를 실행해보자

## 2.1 Kafka 컨포넌트만 실행하기

[wurstmeister](https://github.com/wurstmeister/kafka-docker)에서 제공하는 `docker-compose.yml` 파일을 이용해서 도커를 실행한다.

```bash
$ git clone https://github.com/wurstmeister/kafka-docker
$ cd kafka-docker
$ docker-compose up
```

`telnet` 명령어로 `9092` 포트가 접속이 되는지 확인한다. `Connected to localhost`가 출력되는 것을 볼 수 있어서 Kafka 서버가 잘 구동되었음을 확인할 수 있다.

```bash
$ telnet localhost 9092
Trying ::1...
Connected to localhost.
Escape character is '^]'.
```

### 2.2 Kafka + Akhq (UI)도 같이 실행하기

Kafka 서버만 구동하면 topic을 생성하고 조회하려면, kafka binary를 다운로드 받아서 kafka 명령어로 실행해야 하고 여러 옵션을 잘 알고 있어야 한다. 보다 손쉽게 Kafka를 이용하고 관리할 수 있도록 여러 Kafka Manager UI를 제공하는데, 그중에 대표적으로 많이 사용하는 AKHQ도 같이 구동해보자.

AKHQ에서 이미 `docker-compose` 설정 파일을 제공하고 있어서 이 파일을 사용하면 된다.

```bash
$ git clone https://github.com/tchiotludo/akhq
$ cd akhq
```

기본 설정으로 실행도 잘 되지만, 아래 설정도 같이 해주자.

- M1에서도 실행 가능하도록 `platform` 옵션 추가
- 로컬환경에서도 Kafka 서버 접속되도록 `ports` 설정 추가

```bash
$ vim docker-compose.yml
```



```yaml
...생략...
services:
  akhq:
    platform: linux/x86_64
    image: tchiotludo/akhq
...생략...

  zookeeper:
    platform: linux/x86_64
...생략...

  kafka:
    platform: linux/x86_64
    image: confluentinc/cp-kafka
    KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,PLAINTEXT_HOST://localhost:29092
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
...생략...
    ports:
      - "29092:29092"
    links:
      - zookeeper

  schema-registry:
    platform: linux/x86_64
    image: confluentinc/cp-schema-registry
...생략...

  connect:
    platform: linux/x86_64
    image: confluentinc/cp-kafka-connect
...생략...

  test-data:
    platform: linux/x86_64
...생략...

  kafkacat:
    platform: linux/x86_64
...생략...
```

AKHQ에서 제공하는 `docker-compose.yml`를 실행하면 아래 컴포넌트도 같이 실행된다. 사용하지 않는 컴포넌트를 comment out 시켜도 무방하다. 개발 시 여러 컴포넌트를 사용할 수도 있어서 일단 그대로 둔다. 이제 Kafka + AKHQ 구동시켜보자.

- Kafka
- AKHQ
- Kafka Connect
- Schema Registry

```bash
$ docker-compose up
```

Kafka 서버도 로컬환경에서 접속 가능한지 `telnet` 명령어로 확인하다.

```bash
$ telnet localhost 29092
Trying ::1...
Connected to localhost.
Escape character is '^]'.
```

AKHQ UI로 접속하려면, http://localhost:8080로 접속하면 된다.

![AKHQ Web](image-20220807203854874.png)

## 참고

- https://akhq.io/docs/#installation

- https://github.com/wurstmeister/kafka-docker

- https://towardsdatascience.com/overview-of-ui-tools-for-monitoring-and-management-of-apache-kafka-clusters-8c383f897e80

  

