---
title: "자바 자료구조 - Priority Queue (우선순위 큐)"
description: "자바 자료구조 - Priority Queue (우선순위 큐)"
date: 2020-09-20
update: 2020-09-20
tags:
  - java
  - queue
  - priority
  - priority queue
  - heap
  - 자바
  - 자료구조
  - 우선순위 큐
  - 큐
  - 힙
---

## 1.Priority Queue (우선순위 큐)란?

자바에서 제공하는 여러 자료구조 중에 `Priority Queue`에 대해서 알아보자. 우리가 잘 알고 있는 `Queue` 자료구조와 같이 `FIFO` (First-In-First-Out) 알고리즘으로 동작하지만, 추가로 우선순위가 있는 `BIFO` (Best-In-First-Out) 알고리즘으로 동작한다고 보면 된다. 기본 자료구조에서는 Heap (Min, Max) 자료구조로 보면 이해가 쉽다.

PriorityQueue 클래스는 큐 인터페이스를 구현한 구현체이고 이제 어떻게 사용하는지 예제를 통해서 알아보자.

![Queue-Deque-PriorityQueue-In-Java](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200903183026/Queue-Deque-PriorityQueue-In-Java.png)

> 클래스 다이어그램은 GeeksforGeeks에서 발취함



### 1.1 기본 메서드 및 복잡도

`PriorityQueue` 클래스에서 제공하는 기본 메서드와 복잡도에 대한 설명이다.

| 메서드 이름              | 복잡도     | 설명                                             |
| ------------------------ | ---------- | ------------------------------------------------ |
| `boolean add(E element)` | O(N log N) | 우선순위에 따라서 큐에 삽입한다.                 |
| `public peek()`          | O(1)       | 큐의 first 아이템을 제거하지 않고 확인할 수 있다 |
| `public poll()`          | O(1)       | 큐의 first 아티엠을 제거하고 데이터를 반환한다   |

메서드에 대한 더 자세한 내용은 [Oracle Java API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/PriorityQueue.html)를 참고해주세요.

# 2. Priority Queue 사용법

## 2.1 Min Heap

`PriorityQueue` 객체를 추가 인자 없이 생성하면 Min Heap으로 동작한다. 예제에서 보면 데이터 추가 이후 데이터를 추출하면 값이 가장 낮은 값이 반환된다.

```java
 @Test
 public void test_minHeap() {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.add(3);
        minHeap.add(1);
        minHeap.add(10);
        minHeap.add(5);

        assertThat(minHeap.poll()).isEqualTo(1);
        assertThat(minHeap.poll()).isEqualTo(3);
}
```



### 2.2 Max Heap

`PriorityQueue` 객체 생성시 생성자에 Comparator 를 넘겨주어 데이터에 대한 우선순위를 지정할 수 있다. 값 추출시 Integer의 Max 값이 반환되도록 하기 위해 Collections 에서 기본적으로 제공하는 `reverseOrder()` 메서드로 지정해준다.

```java
 @Test
 public void test_maxHeap() {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(Collections.reverseOrder());
        minHeap.add(3);
        minHeap.add(1);
        minHeap.add(10);
        minHeap.add(5);

        assertThat(minHeap.poll()).isEqualTo(10);
        assertThat(minHeap.poll()).isEqualTo(5);
}
```



### 2.3 Min Heap - Student 객체

기본 Integer 값 외에도 객체에서 특정 값이 우선순위를 가지도록 설정할 수 있다. 예제에서는 Student 객체 Age의 가장 낮은 값이 먼저 추출되도록 설정하였다. Comparator를 인자로 넘겨주기 위해 `Comparator.comparing()` 메서드를 사용하였다. `comparing()` 메서*드는* 인자로 필드 값 기준으로 Comparator 메서드 함수를 반환해주어 쉽게 Comparator를 생성할 수 있다.

```java
@Test
public void test_student_age() {
        int capacity = 4;
        PriorityQueue<Student> studentAgeHeap = new PriorityQueue<>(capacity, Comparator.comparing((Student student) -> student.getAge()));

        studentAgeHeap.add(new Student("Frank", 23));
        studentAgeHeap.add(new Student("Angela", 10));
        studentAgeHeap.add(new Student("David", 30));
        studentAgeHeap.add(new Student("Joe", 15));

        assertThat(studentAgeHeap.poll().getName()).isEqualTo("Angela");
        assertThat(studentAgeHeap.poll().getName()).isEqualTo("Joe");

}
```

## 3. 마무리

`PriorityQueue`은 우선순위를 가지는 Queue 자료구조이다. 개발 시 `PriorityQueue`를 사용하면 쉽게 Min+Max Heap 자료구조로 사용할 수 있다.

예제 코드는 [github](https://github.com/kenshin579/tutorials-java/blob/master/java8/src/test/java/com/advenoh/structure/PriorityQueueTest.java)를 참고해주세요.

## 4. 참고

- Priority Queue
    - http://asuraiv.blogspot.com/2015/11/java-priorityqueue.html
    - https://coding-factory.tistory.com/603
    - https://woovictory.github.io/2020/05/13/PriorityQueue/
    - https://lottogame.tistory.com/996
    - https://www.webucator.com/how-to/how-use-the-comparatorcomparing-method-java-8.cfm
    - https://medium.com/@logishudson0218/java-collection-framework-896a6496b14a
- Heap
    - https://ko.wikipedia.org/wiki/%ED%9E%99_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0)
- Comparator.comparing
    - https://www.webucator.com/how-to/how-use-the-comparatorcomparing-method-java-8.cfm

