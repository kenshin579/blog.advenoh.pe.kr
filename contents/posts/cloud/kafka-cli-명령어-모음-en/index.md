---
title: "Kafka CLI Collection"
description: "Kafka CLI Collection"
date: 2023-03-06
update: 2023-03-06
tags:
  - kafka
  - mq
  - script
  - cli
  - ahkq
  - broker
  - mq
  - en
---

When using Kafka, it is much nicer to have some kind of UI interface and I believe many people use [Ahkq](https://github.com/tchiotludo/akhq) UI including myself. But sometimes using Kafka CLI is necessary for troubleshooting and it can be used for scripting. This article summarizes frequently used Kafka CLI commands.

To learn how to run Kafka on your local environment, see our previous [article](https://blog.advenoh.pe.kr/로컬환경에서-kafka-실행하기-with-akhq/).

## 1.Download Kafka

The Kafka binary file has CLI so let's download the latest binary file from the link below.

- https://kafka.apache.org/downloads

```bash
$ cd src
$ wget https://downloads.apache.org/kafka/3.2.1/kafka_2.13-3.2.1.tgz
$ tar -jxvf kafka_2.13-3.2.1.tgz
```

## 2.Kafka CLI

The default port number for Kafka is 9092. If you running the Kafka in different port,  make sure to use the number instead.

> In Kafka v2.2 and earlier version uses the Zookeeper URL and port number (e.g. `localhost:2181`), but since  the Kafka v2.2 higher version, `--bootstrap-server` the option should be used. After v3, the Zoopkeeper option will be removed.

If you use the Kafka CLI frequently, I recommend adding it to your `PATH` environment variable. This way you won't have to navigate to the Kafka binary folder and type the command every time.

```bash
$ vim ~/.zshrc
...skip...

# Kafka cli
export PATH="/Users/user/src/kafka_2.13-3.2.0/bin:$PATH"

$ source ~/.zshrc
```



### 2.1 Topics

#### 2.1.2 A List of Topics

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

### 2.1.1 Creating a Topic

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --replication-factor 1 --partitions 1 --topic my_topic --create
Created topic my_topic.
```



#### 2.1.3 View Topic Information

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --describe
Topic: my_topic	TopicId: Zlpf9YfsSRO07grMU3MZlA	PartitionCount: 1	ReplicationFactor: 1	Configs: compression.type=gzip
	Topic: my_topic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
```

#### 2.1.4 Deleting a Topic

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --delete
```

### 2.2  Producer

```bash
$ kafka-console-producer.sh --bootstrap-server localhost:29092 --topic my_topic
> 
```

When the `> `prompt is displayed, you can send data to the topic (press `Enter` to send). To exit the producer console window, enter `Ctrl+C`.

#### 2.2.1 How to send a message with a key?

By default, sending a message to a Kafka topic generates a message with a `null` key. To send a message with a key, you need to use the values of the `parse.key` and `key.separator` properties. In the example, `:` is used as the separator.

```bash
$ kafka-console-producer.sh --bootstrap-server localhost:29092 --topic my_topic --property parse.key=true --property key.separator=:
> key:value
```



### 2.3 Consumer

Here are the things to know when using the `kafka-console-consumer.sh` command:

- Unless the `--from-beginning` option is specified, only the latest message is shown.
- If the topic does not exist, it is automatically created by default.
- Multiple topics can be consumed at once by specifying them separated by commas.
- If the consumer group is not specified, `kafka-console-consumer` creates an arbitrary consumer group.
- The order of messages is not guaranteed.
    - The message order is only guaranteed at the partition level, not at the topic level.

The options for the `kafka-console-consumer.sh` command are as follows:

- `--from-beginning`
    - Start consuming messages from the beginning.
- `--group`
    - If no consumer group is specified, an arbitrary consumer group ID is automatically generated.
- `--partition`
    - Use this option to consume only from a specific partition.

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic
```



#### 2.3.2 How to print out the consumed message with key?

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

To learn about the Consumer group feature, a topic is created with at least two partition values. Here's what you need to know about consumer groups:

- The number of consumers in a group cannot exceed the number of partitions in a Kafka topic. (# of consumer <= # of partition)
- If you consume data from a consumer group using the `--group` option and later try to consume from the beginning using the same consumer group with the `--from-beginning` option, the messages are ignored. In this case, you need to reset the consumer group.
- If you do not specify the `--group` option, a random consumer group such as `console-consumer-11984` will be created.
- If one consumer receives all the messages, the topic was probably created with a partition count of 1.

To play around with the consumer group, let's create a topic with partition 3.

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --replication-factor 1 --partitions 3 --topic my_topic --create
```

Open two terminal windows and start the consumer group with the `--group` option in each.

```bash
# console 1
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic --group my-first-application 

# console 2
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic --group my-first-application 
```

If you send a message to the topic, you'll see that it takes turns to consume.

```bash
$ kafka-console-producer.sh --bootstrap-server localhost:29092 --topic my_topic
> 11
> 22
```

### 2.5. Consumer Group Management

This section covers how you can reset a Kafka consumer group.

- You cannot reset a consumer group if there are active consumers
- Resetting a consumer group is used to reprocess data in the group (e.g., to fix bugs).
- Use the `--reset-offsets` option to reset a consumer group.
- Offset reset strategy options include:
    - `--to-datetime`, `--by-period`, `--to-earliest`, `--to-latest`, `--shift-by`, `--from-file`, `--to-current`

The following are options for the `kafka-consumer-groups.sh` command:

- `--dry-run`: Only shows what the result of the command would be without actually executing it.
- `--all-groups`: Be careful using this option, as it applies the offset reset to all consumer groups.
- `--all-topics`: Be careful using this option, as it applies the offset reset to all topics.
- `--by-duration`: Resets the offset by duration.

#### 2.5.1 Reset offset with `to-earliest` option

Make sure to check to see if there is any active consumers.

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --describe --group my-first-application
Consumer group 'my-first-application' has no active members.
GROUP                TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                 HOST            CLIENT-ID
my-first-application my_topic        0          18              18              0               sarama-8e27bd86-2a35-4c2b-b127-24b69923d171 /172.19.0.1     sarama
my-first-application my_topic        1          8               8               0               sarama-8e27bd86-2a35-4c2b-b127-24b69923d171 /172.19.0.1     sarama
my-first-application my_topic        2          9               9               0               sarama-8e27bd86-2a35-4c2b-b127-24b69923d171 /172.19.0.1     sarama
```

To read the entire topic again, change the offset to the initial position (earliest).

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --group my-first-application --reset-offsets --to-earliest --execute --topic my_topic

GROUP                          TOPIC                          PARTITION  NEW-OFFSET
my-first-application           my_topic                       0          0
my-first-application           my_topic                       1          0
my-first-application           my_topic                       2          0
```

The new offset is reset to 0 for all partitions. When you restart the consumer, it will read from the start offset of each partition.

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic my_topic --group my-first-application
hello world
asdf
...생략...
value
```

#### 2.5.2 Reset the offset with `--shift-by`

You can also move the offset by 2.

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --group my-first-application --reset-offsets --shift-by -2 --execute --topic my_topic

GROUP                          TOPIC                          PARTITION  NEW-OFFSET
my-first-application           my_topic                       0          16
my-first-application           my_topic                       1          6
my-first-application           my_topic                       2          7
```

When you restart the consumer, you will see that only the last 2 messages are returned from each partition of the topic.

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

### 3.1 How to increase the number of partition for a topic?

First, you can check the current number of partition by the following command.

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --describe
Topic: my_topic	TopicId: ufrRaY-tTyqcHjFAY-q0ew	PartitionCount: 1	ReplicationFactor: 1	Configs: compression.type=gzip
	Topic: my_topic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
```

Let's increase the number of partitions for the `my_topic` topic by 3.

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --alter --topic my_topic --partitions 3
```

Let's verify the updated number of partition.

```bash
$ kafka-topics.sh --bootstrap-server localhost:29092 --topic my_topic --describe
Topic: my_topic	TopicId: ufrRaY-tTyqcHjFAY-q0ew	PartitionCount: 3	ReplicationFactor: 1	Configs: compression.type=gzip
	Topic: my_topic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_topic	Partition: 1	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_topic	Partition: 2	Leader: 0	Replicas: 0	Isr: 0
```



### 3.2 How to delete a consumer group?

You can read the entire message from the beginning if you delete the consumer group.

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --delete --group my-first-application
Deletion of requested consumer groups ('my-first-application') was successful.
```

### 3.3 How to list all consumers in the consumer group?

By querying all consumers in the consumer group, you can easily see where the consumers are located on the network and figure out how many offset each consumer received from the topic.

```bash
$ kafka-consumer-groups.sh --bootstrap-server localhost:29092 --describe --group my-first-application
GROUP                TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                 HOST            CLIENT-ID
my-first-application my_topic        0          18              18              0               sarama-473590a9-11eb-40c2-afa7-70c5ec448edf /172.18.0.1     sarama
my-first-application my_topic        1          8               8               0               sarama-473590a9-11eb-40c2-afa7-70c5ec448edf /172.18.0.1     sarama
my-first-application my_topic        2          9               9               0               sarama-473590a9-11eb-40c2-afa7-70c5ec448edf /172.18.0.1     saram
```

### 3.4 To view message at the specific offset and partition

https://developer.confluent.io/tutorials/kafka-console-consumer-read-specific-offsets-partitions/confluent.html

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic report --partition 5 --offset 373601
```

### 3.5 To print out the timestamp in the message

https://github.com/confluentinc/schema-registry/issues/947

```bash
$ kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic report --property print.timestamp=true
```

## 4. Reference

- https://www.conduktor.io/kafka/kafka-cli-tutorial
- https://kafka.apache.org/documentation/#basic_ops
- https://betterprogramming.pub/kafka-cli-commands-1a135a4ae1bd
- https://medium.com/@TimvanBaarsen/apache-kafka-cli-commands-cheat-sheet-a6f06eac01b
- https://akageun.github.io/2020/05/07/kafka-cli.html
- https://hevodata.com/learn/kafka-cli-commands/
- https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/kafka-commands.html
