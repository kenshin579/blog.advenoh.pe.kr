---
title: "Kafka CLI 명령어 모음"
description: "Kafka CLI 명령어 모음"
date: 2022-08-14
update: 2022-08-14
tags:
  - kafka
  - script
  - cli
  - ahkq
  - 명령어
  - 카프카
  - 브로커
  - 메시지
  - 아파치
series: "Apache Kafka"
---


Kafka 사용시 [Ahkq](https://github.com/tchiotludo/akhq) UI를 대부분 사용하고 있지만, Trouble-shooting이나 스크립트 작성을 하는 경우에는 Kafka CLI를 사용하는 경우도 종종있다. 자주 사용하는 Kafka CLI 명령어를 정리합니다.

로컬환경에서 Kafka를 실행하는 방법은 그전 [포스팅](https://blog.advenoh.pe.kr/로컬환경에서-kafka-실행하기-with-akhq/)을 참고해주세요.

## 1.Download Kafka

최신 Kafka binary 파일은 아래 링크에서 다운로드한다.

- https://kafka.apache.org/downloads

```bash
$ cd src
$ wget https://downloads.apache.org/kafka/3.2.1/kafka_2.13-3.2.1.tgz
$ tar -jxvf kafka_2.13-3.2.1.tgz
```

## 2.Kafka CLI

Kafka 기본 포트번호는 9092로 시작하지만, [로컬환경에서 Kafka 실행하기](https://blog.advenoh.pe.kr/로컬환경에서-kafka-실행하기-with-akhq/)에서 설정한 포트번호로 실행한다.

> Kafka v2.2이하에서는 Zookeeper URL과 port 번호 (ex. `localhost:2181`)를 사용했지만, Kafka v2.2+ 부터는 `--bootstrap-server` 옵션을 사용을 추천하낟. v3부터는 Zoopkeeper 옵션을 제거될 예정이다.

Kafka CLI를 자주사용하는 경우라면 `PATH` 환경변수에 추가하는 걸 추천한다. 매번 Kafka binary 폴더로 이동해서 명령어를 입력하지 않아도 된다.

```bash
$ vim ~/.zshrc
...생략...

# Kafka cli
export PATH="/Users/user/src/kafka_2.13-3.2.0/bin:$PATH"

$ source ~/.zshrc
```



### 2.1 Topics

#### 2.1.2 Topic 목록 출력

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --list
__connect-config
__connect-offsets
__connect-status
__consumer_offsets
_schemas
frank
test
```

#### 2.1.1 Topic 생성

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --replication-factor 1 --partitions 1 --topic my_topic --create
Created topic my_topic.
```



#### 2.1.3 Topic 정보 보기

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --describe
Topic: my_topic	TopicId: Zlpf9YfsSRO07grMU3MZlA	PartitionCount: 1	ReplicationFactor: 1	Configs: compression.type=gzip
	Topic: my_topic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
```

#### 2.1.4 Topic 삭제하기

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --delete
```



### 2.2  Producer

```bash
$ kafka-console-producer.sh --bootstrap-server localhost:29092 --topic my_topic
```

아래 `> `가 표시되면 topic에 데이터를 보낼 수 있다. (`Enter` 키를 누르면 전송이 된다)

```bash
> 
```

producer console 창에서 나가려면 `Ctrl+C`를 입력하여 종료시킨다.

#### 2.2.1 `kafka-console-producer.sh`에서 키와 같이 메시지를 생성하는 방법은?

기본적으로 Kafka topic에 메시지를 보내면 `null` 키가 있는 메시지가 생성된다. 키와 함께 메시지를 보내려면, `parse.key`와 `key.separator` 속성 값을 사용해야 한다. 예제에서는 `:`를 separator로 사용했다.

```bash
$ kafka-console-producer.sh --bootstrap-server localhost:29092 --topic my_topic --property parse.key=true --property key.separator=:
> key:value
```



### 2.3 Consumer

`kafka-console-consumer.sh` 명령어 사용시 알아야 하는 내용들이다.

- `--from--begining` 옵션을 지정하지 않는 한, 가장 최신 메시지만 출력된다
- Topic이 생성되지 않았을 경우에는 기본적으로 topic을 자동으로 생성한다
- 쉼표로 여러 topic을 지정하면 한 번에 여러 topic을 consume 할 수 있다
- consumer group을 지정하지 않는 경우 `kafka-console-consumer`는 임의 consumer group을 생성한다
- 메서지의 순서는 보장이 안될 수도 있다
    - 메시지의 순서는 topic 레벨이 아니라 partition 레벨에서만 순서를 보장한다

`kafka-console-consumer.sh` 명령어 옵션은 다음과 같다.

- `--from-beginning`
    - 처음부터 메시지를 받을 수 있다
- `--group`
    - Consumer group을 지정하지 않으면 기본적으로 임의의 consumer group ID가 자동으로 생성이 된다
- `--partition`
    - 특전 partition에서만 consumer하려면 이 옵션을 사용한다

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic
```



#### 2.3.2 key, value 값을 출력하려면?

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning
CreateTime:1660481815124	null	hello world
CreateTime:1660481829859	null	asdf
CreateTime:1660481833837	null	hello world
CreateTime:1660481919699	null	sdfj sdf
CreateTime:1660481923366	null	hello
CreateTime:1660481924547	null	asdf
```



### 2.4 Consumer Group

Consumer group 기능에 대해서 알아보기 위해서 topic은 최소 2개 이상의 partition 값으로 생성한다. Consumer group 시 알아야 하는 사항은 다음과 같다.

- Kafka topic의 partition 수는 group에 더 많은 consumer를 가질 수 없다. (# of consumer <= # of partition)
- `--group` 옵션 사용해서 consumer group에서 데이터를 consume하고 나중에 다시 같은 consumer group으로 `--from-begining` 옵션을 사용해보면 무시되는 것을 볼 수 있다. 이런 경우, consumer group을 재설정해야 한다
- `--group` 옵션을 지정하지 않으면 consumer group은 `console-consumer-11984`와 같은 임의의 consumer group이 생성된다
- 하나의 consumer가 모든 메지지를 받는다면, 아마 topic의 partition 수가 1로 만들어졌을 것이다.

Partition 3으로 topic을 생성한다.

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --replication-factor 1 --partitions 3 --topic my_topic --create
```

터미널 창을 2개 띄워서 `--group` 옵션으로 consumer group을 각각 시작한다.

```bash
# console 1
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic --group my-first-application 

# console 2
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic --group my-first-application 
```

Topic에 메시지를 보내보면 번갈라 가면서 consume 을 하는 것을 볼 수 있다.

```bash
$ kafka-console-producer.sh --bootstrap-server localhost:29092 --topic my_topic
> 11
> 22
```

### 2.5. Consumer Group Management

여기서는 Kafka consumer group을 어떻게 재설정 할 수 있는지 다룬다.

- 활성화된 consumer 가 있는 경우에는 consumer group을 재설정 할 수 없다
- 재설정은 consumer group의 데이터를 재처리하는데 사용한다 (ex. 버그 수정이 있는 경우)
- `--reset-offsets` 옵션으로 설정한다
- Offset reset 전략 옵션
    - `--to-datetime`, `--by-period`, `--to-earliest`, `--to-latest`, `--shift-by`, `--from-file`, `--to-current`

`kafka-consumer-groups.sh` 명령어 옵션은 다음과 같다.

- `--dry-run`
    - 실행할 결과만 보여주고 실제로 명령은 수행하지 않는다
- `--all-groups`
    - 모든 group에 reset offset을 적용할 수 있기 때문에 주의해서 사용해야 한다
- `--all-topics`
    - 모든 topic에 reset offset을 적용할 수 있기 때문에 주의해서 사용해야 한다
- `--by-duration`
    - duration으로 offset을 reset한다

#### 2.5.1 `to-earliest` 옵션으로 offset 재설정하기

먼저 활성화된 consumer가 없는지 확인한다.

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --describe --group my-first-application
Consumer group 'my-first-application' has no active members.
GROUP                TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                 HOST            CLIENT-ID
my-first-application my_topic        0          18              18              0               sarama-8e27bd86-2a35-4c2b-b127-24b69923d171 /172.19.0.1     sarama
my-first-application my_topic        1          8               8               0               sarama-8e27bd86-2a35-4c2b-b127-24b69923d171 /172.19.0.1     sarama
my-first-application my_topic        2          9               9               0               sarama-8e27bd86-2a35-4c2b-b127-24b69923d171 /172.19.0.1     sarama
```

Topic 전체를 다시 읽으려면, offset을 최초의 위치(earliest)로 변경한다.

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --group my-first-application --reset-offsets --to-earliest --execute --topic my_topic

GROUP                          TOPIC                          PARTITION  NEW-OFFSET
my-first-application           my_topic                       0          0
my-first-application           my_topic                       1          0
my-first-application           my_topic                       2          0
```

모든 partition에 새로운 offset이 0으로 재설정되었다. 해당 consumer를 다시 시작하면 각 partition의 시작 offset부터 읽어온다.

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic --group my-first-application
hello world
asdf
...생략...
value
```

#### 2.5.2 `--shift-by` 옵션으로 offset 재설정하기

Offset을 2만큼 이동하는 방법도 있다.

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --group my-first-application --reset-offsets --shift-by -2 --execute --topic my_topic

GROUP                          TOPIC                          PARTITION  NEW-OFFSET
my-first-application           my_topic                       0          16
my-first-application           my_topic                       1          6
my-first-application           my_topic                       2          7
```

Consumer를 재시작하면 topic의 각 partition에서 마지막 2개의 메시지만 반환하는 것을 볼 수 있다.

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic --group my-first-application
200
22
180
210
44
value
```

## 3.FAQ

### 3.1 Topic의 Partition 수를 늘리는 방법

현재 partition 수를 확인한다

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --describe
Topic: my_topic	TopicId: ufrRaY-tTyqcHjFAY-q0ew	PartitionCount: 1	ReplicationFactor: 1	Configs: compression.type=gzip
	Topic: my_topic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
```

`my_topic` Topic의 partition 수를 3으로 늘린다

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --alter --topic my_topic --partitions 3
```

잘 반영이 되었는지 확인하다
```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --describe
Topic: my_topic	TopicId: ufrRaY-tTyqcHjFAY-q0ew	PartitionCount: 3	ReplicationFactor: 1	Configs: compression.type=gzip
	Topic: my_topic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_topic	Partition: 1	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_topic	Partition: 2	Leader: 0	Replicas: 0	Isr: 0
```



### 3.2 Kafka에서 Consumer Group을 삭제하는 방법

Consumer group을 삭제하여 완전히 처음부터 데이터를 읽어 올 수 있다.

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --delete --group my-first-application
Deletion of requested consumer groups ('my-first-application') was successful.
```

### 3.3 Consumer Group에서 모든 Consumer를 조회하는 방법

Consumer group에서 모든 consumer를 조회하면, consumer가 네트워크 상으로 어디에 위치해 있고 얼마나 topic을 consume을 하고 있는지 쉽게 알 수 있다.

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --describe --group my-first-application
GROUP                TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                 HOST            CLIENT-ID
my-first-application my_topic        0          18              18              0               sarama-473590a9-11eb-40c2-afa7-70c5ec448edf /172.18.0.1     sarama
my-first-application my_topic        1          8               8               0               sarama-473590a9-11eb-40c2-afa7-70c5ec448edf /172.18.0.1     sarama
my-first-application my_topic        2          9               9               0               sarama-473590a9-11eb-40c2-afa7-70c5ec448edf /172.18.0.1     saram
```

### 3.4 특정 offset과 partition에서 메시지를 조회하는 방법

https://developer.confluent.io/tutorials/kafka-console-consumer-read-specific-offsets-partitions/confluent.html

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic report --partition 5 --offset 373601
```

### 3.5 메시지의 Timestamp도 출력하는 방법

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic report --property print.timestamp=true
```

참고

- https://github.com/confluentinc/schema-registry/issues/947

## 4. 참고

- https://www.conduktor.io/kafka/kafka-cli-tutorial
- https://kafka.apache.org/documentation/#basic_ops
- https://betterprogramming.pub/kafka-cli-commands-1a135a4ae1bd
- https://medium.com/@TimvanBaarsen/apache-kafka-cli-commands-cheat-sheet-a6f06eac01b
- https://akageun.github.io/2020/05/07/kafka-cli.html
- https://hevodata.com/learn/kafka-cli-commands/
- https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/kafka-commands.html

