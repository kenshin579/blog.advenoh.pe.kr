---
title: "새로운 기능 및 개선 사항 목록 - 자바9에서의 변화"
description: "새로운 기능 및 개선 사항 목록 - 자바9에서의 변화"
date: 2018-09-03
update: 2018-09-03
tags:
  - java
  - java8
  - jdk8
  - jdk1.8
  - openjdk
  - JEP
  - 자바
  - 자바8
---

## 자바9

- Java Platform Module System
- JEP 222: Jshell - REPL
- JEP 158: Unified VM logging
    * JVM component에 대한 공통 로깅 시스템 제공 (-Xlog)

- HTML5 Javadoc
    * HTML5 형식의 API를 생성할 수 있는 도구

- Language Update
    * try-with-resources 개선
    * private interface method
        * interface에서는 항상 public로 정의해야 했는데, private도 가능하도록 함
    * diamond operator
        * 익명 내부 클래스에서도 diamond operator가 가능하도록 함

- New Core Libraries
  * Process API
  * JEP264: Platform Logging API and Service
  * [http://openjdk.java.net/jeps/264](http://openjdk.java.net/jeps/264)
  * CompletableFuture API 강화
  * Reactive Streams - Flow API
  * [https://thepracticaldeveloper.com/2018/01/31/reactive-programming-java-9-flow/](https://thepracticaldeveloper.com/2018/01/31/reactive-programming-java-9-flow/)
  * Collections(List, Set, Map)를 위한 팩토리 메소드 (Factory Method for Collections: List, Set, Map)
  * 정적 팩토리 메소드로 작성된 콜렉션은 불변임
  * Enhanced Deprecation
  * Stack-Walking API
  * Other Improvements
  * Stream 개선
  * iterate(), takeWhile()/dropWhile(), ofNullable()
  * Optional 개선

- JEP 11 : HTTP 2.0 (Incubator Modules)
  * [http://openjdk.java.net/jeps/110](http://openjdk.java.net/jeps/110)
- Client Technologies
  * Multi-Resolution Images
  * TIFF Image I/O Plugins
- Internationalization
  * Unicode 8.0
  * Java 8은 Unicode 6.2을 지원
  * UTF-8 Properties files
  * Default Localte Data Change

자바9에 추가된 여러 기능 및 개선 사항은 다음 링크를 참조해주세요.

- [https://docs.oracle.com/javase/9/whatsnew/toc.htm#JSNEW-GUID-C23AFD78-C777-460B-8ACE-58BE5EA681F6](https://docs.oracle.com/javase/9/whatsnew/toc.htm#JSNEW-GUID-C23AFD78-C777-460B-8ACE-58BE5EA681F6)

자바9에서의 큰 변화중에 하나는 모듈 시스템의 도입입니다. 이 부분도 큰 변화이고 스터디할 부분이 많아서 정리되는 대로 포스팅할 계획입니다.
