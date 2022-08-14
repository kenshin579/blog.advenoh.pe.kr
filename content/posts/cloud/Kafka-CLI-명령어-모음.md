---
title: 'Kafka CLI 명령어 모음'
tags: [kafka, script, cli, ahkq, 명령어, 카프카, 브로커, 메시지, 아파치]
image: '/media/cover/cover-kafka-helm.jpg'
date: 2022-08-14
---

Kafka 사용시 [Ahkq](https://github.com/tchiotludo/akhq) UI를 대부분 사용하고 있지만, Trouble-shooting이나 스크립트 작성을 하는 경우에는 Kafka CLI를 사용하는 경우도 종종있다. 자주 사용하는 Kafka CLI 명령어를 정리합니다. 

로컬환경에서 Kafka를 실행하는 방법은 그전 [포스팅](https://blog.advenoh.pe.kr/cloud/%EB%A1%9C%EC%BB%AC%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-Kafka-%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0-with-AKHQ/)을 참고해주세요. 

# 1.Download Kafka 

최신 Kafka binary 파일은 아래 링크에서 다운로드한다. 

- https://kafka.apache.org/downloads

```bash
$ cd src
$ wget https://downloads.apache.org/kafka/3.2.1/kafka_2.13-3.2.1.tgz
$ tar -jxvf kafka_2.13-3.2.1.tgz
```

# 2.Kafka CLI

Kafka 기본 포트번호는 9092로 시작하지만, [로컬환경에서 Kafka 실행하기](https://blog.advenoh.pe.kr/cloud/%EB%A1%9C%EC%BB%AC%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-Kafka-%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0-with-AKHQ/)에서 설정한 포트번호로 실행한다. 

> Kafka v2.2이하에서는 Zookeeper URL과 port 번호 (ex. `localhost:2181`)를 사용했지만, Kafka v2.2+ 부터는 `--bootstrap-server` 옵션을 사용을 추천하낟. v3부터는 Zoopkeeper 옵션을 제거될 예정이다. 

## 2.1 Topics

### 2.1.2 Topic 목록 출력

```bash
$ ./kafka-topics.sh --bootstrap-server localhost:29092 --list
__connect-config
__connect-offsets
__connect-status
__consumer_offsets
_schemas
frank
test
```

### 2.1.1 Topic 생성

```bash
$ ./kafka-topics.sh --bootstrap-server localhost:29092 --replication-factor 1 --partitions 1 --topic my_topic --create
Created topic my_topic.
```



### 2.1.3 Topic 정보 보기

```bash
$ ./kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --describe
Topic: my_topic	TopicId: Zlpf9YfsSRO07grMU3MZlA	PartitionCount: 1	ReplicationFactor: 1	Configs: compression.type=gzip
	Topic: my_topic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
```

### 2.1.4 Topic 삭제하기

```bash
$ ./kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --delete
```



## 2.2  Producer

```bash
$ ./kafka-console-producer.sh --bootstrap-server localhost:29092 --topic my_topic
```

아래 `> `가 표시되면 topic에 데이터를 보낼 수 있다. (`Enter` 키를 누르면 전송이 된다)

```bash
> 
```

producer console 창에서 나가려면 `Ctrl+C`를 누르면 된다. 

## 2.3 Consumer

Consumer에 

- `--from--begining` 옵션을 지정하지 않는 한, 가장 최신 메시지만 출력된다
- topic이 생성되지 않았을 경우에는 기본적으로 topic을 자동으로 생성한다
- 쉼표로 여러 topic을 지정하면 한 번에 여러 topic을 consume 할 수 있다
- consumer group을 지정하지 않는 경우 kafka-console-consumer는 임의 consumer group을 생성한다
- 메서지의 순서는 보장이 안될 수도 있다
  - 메시지의 순서는 topic 레벨이 아니라 partition 레벨에서만 순서를 보장한다

```bash
$ ./kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic
```



> **메시지에 대한 순서** (이건 다시 작성하기  - 책에서는 어떻게 설명이 되어 있는지 확인하기)
>
> The order of messages is not total, it is per partition. As a topic may be created with more than one partition, the order is only guaranteed at the partition level. If you try with only one partition, you will see total ordering.



- `--from-beginning`
  - 
- `--group`
  - 
- `--partition`
  - 

### 



### 2.3.2 key, value 값을 출력하려면?

```bash
$ ./kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning
CreateTime:1660481815124	null	hello world
CreateTime:1660481829859	null	asdf
CreateTime:1660481833837	null	hello world
CreateTime:1660481919699	null	sdfj sdf
CreateTime:1660481923366	null	hello
CreateTime:1660481924547	null	asdf
```



## 2.4 Consumer Group
```bash

```

## 2.5. Consumer Group Management
```bash

```





# 3. 참고

- https://www.conduktor.io/kafka/kafka-cli-tutorial
- https://kafka.apache.org/documentation/#basic_ops
- https://betterprogramming.pub/kafka-cli-commands-1a135a4ae1bd
- https://medium.com/@TimvanBaarsen/apache-kafka-cli-commands-cheat-sheet-a6f06eac01b
- https://akageun.github.io/2020/05/07/kafka-cli.html
- https://hevodata.com/learn/kafka-cli-commands/
- https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/kafka-commands.html
- 
