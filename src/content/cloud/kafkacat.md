---
title: 'kafkacat 사용방법 (메시지 보내고 받기 테스트)'
layout: post
category: 'cloud'
author: [Frank Oh]
tags: ["kafka", "kafkacat", "broker", "message", "producer", "consumer", "apache", 카프카", "브로커", "메시지", "아파치""]
image: ../img/cover-kafka-helm.jpg
date: '2021-07-20T11:11:20.000Z'
draft: false
---

`kafkacat`은 아파치 카프카를 쉽게 테스트하고 디버깅하는데 유용하게 사용할 수 있는 도구이다. `kafkacat` 명령어를 통해서 메시지를 보내고 받거나 메타데이터 목록을 확인할 수 있다. 기본적으로 동적에 대해서 알아보자. Kafka 설치는 [헬름으로 Kafka 설치](https://blog.advenoh.pe.kr/cloud/%ED%97%AC%EB%A6%84%EC%9C%BC%EB%A1%9C-Kafka-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0/)를 참고해주세요. 

## kafkacat 설치

여러 방법으로 설치 가능하지만, 본 포스팅에서는 맥기준으로 설명합니다. `brew`로 `kafkacat`을 설치한다. 


```bash
$ brew install kafkacat
```



## kafkacat 기본 사용방법

### 기본 Synatx

`kafkacat` 의 기본 명령어 포맷은 아래와 같다. 기본적인 

```bash
$ kafkacat <mode> -b <brokers> -t new_topic
```

- `-C | -P | -L | -Q  Mode` 
  - Consume, Produce, Metadata List, Query 모드를 지정한다
- `-t <topic>`
  - 토픽을 지정한다
- `-b <brokers, ...>`
  -  브로커 목록을 지정한다

## 메시지 보내기 (-P)

메시지는 Produce (`-P`) 모드를 지정해서 메시지를 보낼 수 있다. 필수로 Kafka 브로커 (`-b`)와 토픽 옵션 (`-t`)을 지정해줘야 한다. kafkacat을 사용하여 특정 토픽에 쉽게 메시지를 보낼 수 있다. -P 명령으로 실행하고 원하는 데이터를 입력한 다음 Ctrl-D를 눌러 완료한다. 

```bash
$ kafkacat -b my-kafka.default.svc.cluster.local:9092 -t test -P
11
22
```

잘 보내줬는지 확인하려면 -C consume 모드로 확인한다. 

```bash
$ kafkacat -b my-kafka.default.svc.cluster.local:9092 -t test -C
11
22
```

메시지를 키와 함께 생성하고 싶은 경우에는 키 구분자 (key delimiter) -K 옵션으로 원하는 구분자를 같이 지정해서 사용하면 된다. 

```bash
$ kafkacat -b my-kafka.default.svc.cluster.local:9092 -t test -P -K :
key1:msg1
key2:msg2
```

메시지를 파일에서 읽어올 수도 있다. 

```bash
$ cat msg.txt
key1:msg1
key2:msg2
key3:msg3

$ kafkacat -b my-kafka.default.svc.cluster.local:9092 -t test -P -K: msg.txt
```

파티션 (Partition)은 각 토픽 당 데이터를 분산 처리하는 단위로 카프카에서는 토픽을 여러 파티션에 나눠서 저장하고 카프카 옵션에서 지정한 replica의 수만큼 파티션이 각 브로커에 복제가 된다. 

토픽을 여러 파티션으로 설정해두었다면 아래와 같이 파티션 1에 메시지를 보내고 받을 수 있다. 

```bash
$ kafkacat -b my-kafka.default.svc.cluster.local:9092 -t test -P -p 1 
hello world

$ kafkacat -b my-kafka.default.svc.cluster.local:9092 -t test -C -p 1
hello world
```

토픽의 파티션의 수를 늘려주려면 아래와 같이 kafka script를 통해서 늘려주면 된다. 

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
$ kafka-topics.sh --zookeeper my-kafka-zookeeper:2181 --alter --topic test --partitions 3WARNING: If partitions are increased for a topic that has a key, the partition logic or ordering of the messages will be affected
Adding partitions succeeded!

# 수정된 파티션의 수를 확인한다
$ kafka-topics.sh --describe --zookeeper my-kafka-zookeeper:2181 --topic test
Topic: test	TopicId: sLitGkHfRSyg261FxMoGCA	PartitionCount: 3	ReplicationFactor: 1	Configs:
	Topic: test	Partition: 0	Leader: 1	Replicas: 1	Isr: 1
	Topic: test	Partition: 1	Leader: 2	Replicas: 2	Isr: 2
	Topic: test	Partition: 2	Leader: 0	Replicas: 0	Isr: 0
```

> 카프카에서는 파티션을 한번 늘리면 줄일 수 있는 방법은 없어서 실제 production 환경에서는 더 많은 고려이후 파티션을 늘려줘야 한다. 
>

## 메시지 받기 (-D)

- consumer
  - - 
  - 
  - 특정 오프셋부터 가져오기
  - 특정 파티션에서 마지막 데이터 가져오기
  - timestamp 기반으로 메시지 가져오기
    - 시작 ~ 끝으로 지정해서 메디지를 가져올 수 있음
- - 
  
- 

모든 메시지 가져오기

- 기본적으로 kafkacat는 처음부터 메시지를 가져온다

```bash
$ kafkacat -b my-kafka.default.svc.cluster.local:9092 -t test -C
```



X 만개의 메시지만 가져오기

```bash
$ kafkacat -b my-kafka.default.svc.cluster.local:9092 -t test -C -c10
```



Formatting output

- 기본적으로 message payload를 출력한다 (record의 값만)

```bash
$ kafkacat -b my-kafka.default.svc.cluster.local:9092 -t test -C  -f '\nKey (%K bytes): %k\t\nValue (%S bytes): %s\n\tPartition: %p\tOffset: %o\n--\n'


```



## 메타데이터 조회하기 (-L)

- 특정 topic metadata 조회하기

-L 옵션으로 



```bash
$ kafkacat -L -b my-kafka.default.svc.cluster.local
Metadata for all topics (from broker -1: my-kafka.default.svc.cluster.local:9092/bootstrap):
 3 brokers:
  broker 0 at my-kafka-0.my-kafka-headless.default.svc.cluster.local:9092
  broker 2 at my-kafka-2.my-kafka-headless.default.svc.cluster.local:9092 (controller)
  broker 1 at my-kafka-1.my-kafka-headless.default.svc.cluster.local:9092
 2 topics:
  topic "test" with 1 partitions:
    partition 0, leader 1, replicas: 1, isrs: 1
  topic "__consumer_offsets" with 50 partitions:
    partition 0, leader 2, replicas: 2, isrs: 2
    partition 1, leader 1, replicas: 1, isrs: 1
    partition 2, leader 0, replicas: 0, isrs: 0
    partition 3, leader 2, replicas: 2, isrs: 2
    partition 4, leader 1, replicas: 1, isrs: 1
    partition 5, leader 0, replicas: 0, isrs: 0
    partition 6, leader 2, replicas: 2, isrs: 2
```



# 참고

- https://docs.confluent.io/platform/current/app-development/kafkacat-usage.html
- https://github.com/edenhill/kafkacat
- https://dev.to/de_maric/learn-how-to-use-kafkacat-the-most-versatile-kafka-cli-client-1kb4
- https://codingharbour.com/kafkacat-cheatsheet/
- https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/kafkacat.html#client-examples-kafkacat
- https://wonyong-jang.github.io/kafka/2021/02/10/Kafka-message-order.html
- https://redhat-developer-demos.github.io/kafka-tutorial/kafka-tutorial/1.0.x/03-consumers-producers.html

