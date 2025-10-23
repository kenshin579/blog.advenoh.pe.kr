---
title: "새로운 기능 및 개선 사항 목록 - 자바11에서의 변화"
description: "새로운 기능 및 개선 사항 목록 - 자바11에서의 변화"
date: 2018-09-09
update: 2018-09-09
tags:
  - java
  - java11
  - upgrade
  - JEP
  - 자바
  - 자바11
  - 개선사항
---

## 자바11

- JEP 181: Nest-Based Access Control
- JEP 309: Dynamic Class-File Constants
- JEP 315: Improve Aarch64 Intrinsics
- JEP 318: Epsilon: A No-Op Garbage Collector
- JEP 320: Remove the Java EE and CORBA Modules
- **JEP 321: HTTP Client (Standard)**
- **JEP 323: Local-Variable Syntax for Lambda Parameters**
- JEP 324: Key Agreement with Curve25519 and Curve448
- JEP 327: Unicode 10
- JEP 328: Flight Recorder
- JEP 329: ChaCha20 and Poly1305 Cryptographic Algorithms
- JEP 330: Launch Single-File Source-Code Programs
- JEP 331: Low-Overhead Heap Profiling
- JEP 332: Transport Layer Security (TLS) 1.3
- JEP 333: ZGC: A Scalable Low-Latency Garbage Collector (Experimental)
- JEP 335: Deprecate the Nashorn JavaScript Engine
- JEP 336: Deprecate the Pack200 Tools and API

자바11에 추가된 여러 기능 및 개선 사항은 다음 링크를 참조해주세요.

- [http://openjdk.java.net/projects/jdk/11/](http://openjdk.java.net/projects/jdk/11/)

## JEP 321: HTTP Client (Standard)

자바 9 & 10에서 incubated된 HTTP client는 자바11에서는 표준화된 버전으로 릴리스 되었습니다.
패키지 : java.net.http

HTTP2에 대한 더 자세한 사항은 [나만 모르고 있던 - HTTP/2](https://www.popit.kr/%EB%82%98%EB%A7%8C-%EB%AA%A8%EB%A5%B4%EA%B3%A0-%EC%9E%88%EB%8D%98-http2/) 를 참조하세요.

## JEP 323: Local-Variable Syntax for Lambda Parameters

JDK 10에서 var가 도입되었지만, 암묵적 타입의 람다 표현식에는 사용할 수 없었습니다. 자바11부터는 람다 표현식에서도 var 키워드를 사용할 수 있게 되었습니다.

```java
@Test
public void test_JEP323() {
    var xs = new in[]{3, 2, 6, 4, 8, 9};
    int x = Arrays
            .stream(xs)
            .filter((var a) -> a < 5)
            .sum();
    System.out.println(x);
}
```
### 참고

- 자바11
    - [https://blog.takipi.com/java-11-will-include-more-than-just-features/?utm_source=10countdown&utm_medium=readmore](https://blog.takipi.com/java-11-will-include-more-than-just-features/?utm_source=10countdown&utm_medium=readmore)
    - [https://medium.com/antelabs/what-is-new-in-java-11-442af9315f07](https://medium.com/antelabs/what-is-new-in-java-11-442af9315f07)

