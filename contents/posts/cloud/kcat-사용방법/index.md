---
title: "kcat 사용방법"
description: "kcat 사용방법"
date: 2021-07-20
update: 2021-07-20
tags:
  - kcat
  - kafka
  - kafkacat 
  - 카프카
  - 브로커
  - 메시지
  - 아파치
series: "Apache Kafka"
---


`kcat`은 아파치 카프카를 쉽게 테스트하고 디버깅하는데 유용하게 사용할 수 있는 도구이다. `kcat` 명령어를 통해서 메시지를 보내고 받거나 메타데이터 목록을 확인할 수 있다. 기본적인 사용방법에 대해서 알아보자. 카프카 설치는 [로컬환경에서 Kafka 실행하기](https://blog.advenoh.pe.kr/로컬환경에서-kafka-실행하기-with-akhq/)를 참고해주세요.

## kcat 설치

여러 방법으로 설치 가능하지만, 본 포스팅에서는 맥기준으로 설명합니다. `brew`로 `kcat`을 설치한다.


```bash
$ brew install kcat
```


## kcat 기본 사용방법

### 기본 Synatx

`kcat` 의 기본 명령어 포맷은 아래와 같다.

```bash
$ kcat <mode> -b <brokers> -t new_topic
```

- `-C | -P | -L | -Q  Mode`
    - Consume, Produce, Metadata List, Query 모드를 지정한다
- `-t <topic>`
    - 토픽을 지정한다
- `-b <brokers, ...>`
    -  브로커 목록을 지정한다

## 메시지 보내기 (-P)

메시지는 Produce (`-P`) 모드를 지정해서 메시지를 보낼 수 있다. 필수로 카프카 브로커 (`-b`)와 토픽 옵션 (`-t`)을 지정해줘야 한다. `kcat`을 사용하여 특정 토픽에 쉽게 메시지를 보낼 수 있다. `-P` 명령으로 실행하고 원하는 데이터를 입력한 다음 `Ctrl-D`를 눌러 완료한다.

### 메시지 값 생성하기

```bash
$ kcat -b localhost:29092 -t test -P
11
22
```

잘 보내줬는지 확인하려면 `-C` consume 모드로 확인한다.

```bash
$ kcat -b localhost:29092 -t test -C
11
22
```

### 키와 값을 가진 메시지를 생성하기

메시지를 키와 함께 생성하고 싶은 경우에는 키 구분자 (key delimiter) `-K` 옵션으로 원하는 구분자를 같이 지정해서 사용한다.

```bash
$ kcat -b localhost:29092 -t test -P -K :
key1:msg1
key2:msg2
```

### 파일로 메시지 생성하기

메시지를 파일에서도 읽어 드려 메시지를 생성할 수 있다.

```bash
$ cat msg.txt
key1:msg1
key2:msg2
key3:msg3

$ kcat -b localhost:29092 -t test -P -K: msg.txt
```

파티션 (Partition)은 각 토픽 당 데이터를 분산 처리하는 단위로 카프카에서는 토픽을 여러 파티션에 나눠서 저장하고 카프카 옵션에서 지정한 replica의 수만큼 파티션이 각 브로커에 복제가 된다.

토픽을 여러 파티션으로 설정해두었다면 아래와 같이 파티션 1에 메시지를 보내고 받을 수 있다.

```bash
$ kcat -b localhost:29092 -t test -P -p 1 
hello world

$ kcat -b localhost:29092 -t test -C -p 1
hello world
```

### 토픽의 파티션의 수 늘리기

토픽의 파티션의 수를 늘려주려면 아래와 같이 카프카에서 제공하는 스트립트를 통해서 파티션을 추가할 수 있다.

```bash
# kafka script를 사용을 위해 my-kafka-client POD를 띄워준다
$ kubectl run my-kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.0-debian-10-r30 --namespace default --command -- sleep infinity
$ kubectl exec -it my-kafka-client -- /bin/bash

# 현재 파티션 수를 확인한다
$ kafka-topics.sh --describe --zookeeper my-kafka-zookeeper:2181 --topic test
\Topic: test	TopicId: sLitGkHfRSyg261FxMoGCA	PartitionCount: 1	ReplicationFactor: 1	Configs:
	Topic: test	Partition: 0	Leader: 1	Replicas: 1	Isr: 1
```

```bash
# test 토픽의 파티션 수를 3으로 늘려준다
$ kafka-topics.sh --zookeeper my-kafka-zookeeper:2181 --alter --topic test --partitions 3
WARNING: If partitions are increased for a topic that has a key, the partition logic or ordering of the messages will be affected
Adding partitions succeeded!

# 수정된 파티션의 수를 확인한다
$ kafka-topics.sh --describe --zookeeper my-kafka-zookeeper:2181 --topic test
Topic: test	TopicId: sLitGkHfRSyg261FxMoGCA	PartitionCount: 3	ReplicationFactor: 1	Configs:
	Topic: test	Partition: 0	Leader: 1	Replicas: 1	Isr: 1
	Topic: test	Partition: 1	Leader: 2	Replicas: 2	Isr: 2
	Topic: test	Partition: 2	Leader: 0	Replicas: 0	Isr: 0
```

> 카프카에서는 파티션을 한번 늘리면 줄일 수 있는 방법은 없기 때문에 Real 환경에서는 늘려주기 전에 꼭 필요한 상황인지 판단할 필요가 있다.

## 메시지 받기 (-D)

### 토픽에서 모든 메시지 받기

`kcat`은 기본적으로 추가 옵선 지정없이 토픽에서 처음부터 모든 메시지를 가져온다.

```bash
$ kcat -b localhost:29092 -t test -P
11
22
33
44

$ kcat -b localhost:29092 -t test -C
11
22
33
44
```

### N 개만 메시지 받기

모든 메시지를 가져오는 대신 몇개만 메시지를 가져오려면 `-c` 옵션으로 개수를 지정하면 된다.

```bash
$ kcat -b localhost:29092 -t test -C -c 2
11
22
```

### 특정 오프셋에서 메시지 가져오기

`-o` 옵션으로 특정 오프셋이후부터 데이터를 가져온다.

```bash
$ kcat -b localhost:29092 -t test -C -o 1
22
33
44
```

> 오프셋을 절대 값으로 지정할 수도 있지만, 처음과 끝은 `begining`이나 `end`  로 지정할 수 있다.
>
> `$ kcat -b my-kafka.default.svc.cluster.local:9092 -t test -C -o begining`

오프셋 값을 음수로 지정하면 끝에서부터 메시지를 가져온다.

```bash
$ kcat -b localhost:29092 -t test -C -o -2
33
44
```

### 출력 포멧 변경하기

기본적으로 `kcat`은 메시지 값(카프카 레코드의 값)만 출력한다. 출력의 포멧을 변경하려면 `-f` 옵션으로 아래와 같이 여러 값을 사용해서 정의할 수 있다.

```bash
Format string tokens:
  %s                 Message payload
  %S                 Message payload length (or -1 for NULL)
  %k                 Message key
  %K                 Message key length (or -1 for NULL)
  %t                 Topic
  %p                 Partition
  %o                 Message offset
  \n \r \t           Newlines, tab
  \xXX \xNNN         Any ASCII character
```

Key와 Value, 그리고 Partition, Offset의 값을 읽게 편하게 출력할 수 있다.

```bash
$ kcat -b localhost:29092 -t test -C  -f '\nKey (%K bytes): %k\t\nValue (%S bytes): %s\n\tPartition: %p\tOffset: %o\n--\n'

Key (-1 bytes):
Value (2 bytes): 11
	Partition: 0	Offset: 0
--

Key (-1 bytes):
Value (2 bytes): 22
	Partition: 0	Offset: 1
--

Key (-1 bytes):
Value (2 bytes): 33
	Partition: 0	Offset: 2
--

Key (-1 bytes):
Value (2 bytes): 44
	Partition: 0	Offset: 3
--

```



## 메타데이터 조회하기 (-L)

브로커나 현재 토픽에 대한 정보를 확인하려면 `-L` 옵션으로 확인할 수 있다. 브로커는 총 3대로 구성되어 있고 토픽당 몇개의 파티션으로 구성되어 있는지도 확인할 수 있다.

```bash
$ kcat -L -b localhost:29092
Metadata for all topics (from broker -1: my-kafka.default.svc.cluster.local:9092/bootstrap):
 3 brokers:
  broker 0 at my-kafka-0.my-kafka-headless.default.svc.cluster.local:9092
  broker 2 at my-kafka-2.my-kafka-headless.default.svc.cluster.local:9092
  broker 1 at my-kafka-1.my-kafka-headless.default.svc.cluster.local:9092
 3 topics:
  topic "test" with 3 partitions:
    partition 0, leader 1, replicas: 1, isrs: 1
    partition 2, leader 0, replicas: 0, isrs: 0
    partition 1, leader 2, replicas: 2, isrs: 2
  topic "test1" with 1 partitions:
    partition 0, leader 0, replicas: 0, isrs: 0
  topic "__consumer_offsets" with 50 partitions:
    partition 0, leader 2, replicas: 2, isrs: 2
    partition 10, leader 1, replicas: 1, isrs: 1
    partition 20, leader 0, replicas: 0, isrs: 0
    partition 40, leader 1, replicas: 1, isrs: 1
    ...생략...
```



## 참고

- https://docs.confluent.io/platform/current/app-development/kafkacat-usage.html
- https://github.com/edenhill/kafkacat
- https://dev.to/de_maric/learn-how-to-use-kafkacat-the-most-versatile-kafka-cli-client-1kb4
- https://codingharbour.com/kafkacat-cheatsheet/
- https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/kafkacat.html#client-examples-kafkacat
- https://wonyong-jang.github.io/kafka/2021/02/10/Kafka-message-order.html
- https://redhat-developer-demos.github.io/kafka-tutorial/kafka-tutorial/1.0.x/03-consumers-producers.html

