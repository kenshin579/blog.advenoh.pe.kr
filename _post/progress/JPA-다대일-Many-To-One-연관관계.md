---
title: '[JPA-2] JPA 다대일(N:1)+일대다(1:N) @Many-To-One, @One-To-Many 연관관계'
date: 2019-12-6 10:23:33
category: 'database'
tags: ["jpa", "database", "db", spring", "springboot", "persistence", "ManyToOne", "OneToMany", mapping", "데이터베이스", "스프링", "스프링부트", 연관관계", "단방향", "양방향", "다대일", "일대다"]
---

# 1. 들어가며

JPA 연관관계 매핑에 대한 내용은 [JPA 연관관계 매핑 정리](https://blog.advenoh.pe.kr/database/JPA-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84-%EB%A7%A4%ED%95%91-%EC%A0%95%EB%A6%AC/) 포스팅을 참고해주세요. 이번 포스팅에서는 JPA에서 가장 자주 사용하는 다대일(N:1)과 그 반대방향인 일대다(1:N) 연관관계에 대해서 알아보겠습니다. 

> - Post (일)
> - Comment (다)
>   - 테이블에서는 다쪽에 외래 키가 존재한다
>   - 양방향 관계에서는 다쪽이 연관관계의 주인이 된다
>

객체 관련 그림 넣기


<img src="images/JPA-다대일-Many-To-One-연관관계/image-20191206140042471.png" alt="image-20191206140042471" style="zoom:50%;" />

# 2. 개발 환경

작성한 샘플 코드는 아래 깃허브 링크를 참고해주세요. 

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
  * [단방향](https://github.com/kenshin579/tutorials-java/tree/master/springboot-jpa-many-to-one-undirectional)
  * [양방향](https://github.com/kenshin579/tutorials-java/tree/master/springboot-jpa-many-to-one-undirectional)
* Software management tool : Maven

# 3. 다대일 (N:1) 연관관계

## 3.1 다대일 연관관계



### 3.1.1 다대일 단방향

### 3.1.2 다대일 양방향

양방향, 단방향

연관관계의 주인이라...

연관관계 편의 메서드란...

@ManyToOne 속성

@JoinColumn의 속성

## 3.2 일대다 연관관계

일대다관계는 엔티티를 하나 이상 참조할 수 있으므로 자바 Collection, List, Set, Map중에 하나를 사용해야 합니다. 

- 실제 query가 어떻게 시작되는지도 적어두자
- 

### 3.2.1 일대다 단방향

### 3.2.2 일대다 양방향



## 3.3 주의사항

### 3.3.1 무한 루프에 빠지는 경우

영방향 매핑때에는 무한 루프에 빠질 수 있어서 주의가 필요합니다. 예를 들어 Comment.toString()에서 getPost()를 호출하게 되면 

- 엔티티를 JSON으로 변환하는 경우
  - [Jackson에서 Infinite Recursion에 해결하는 방법](https://blog.advenoh.pe.kr/java/Jackson%EC%97%90%EC%84%9C-Infinite-Recursion-%EC%9D%B4%EC%8A%88-%ED%95%B4%EA%B2%B0%EB%B0%A9%EB%B2%95/)을 참고해주세요
- toString() 사용시
  - Lombok 라이브러리 사용시에도 발생할 수 있어 toString(exclude={##, ##})으로 제외시킨다

# 4. FAQ

## 4.1 언제 양반향, 단방향을 사용해야 하나?

ㄴㅇㄴㅇㄹ

## 4.2 ??

# 5. 참고

- JPA - one-to-many mapping
  - [https://www.callicoder.com/hibernate-spring-boot-jpa-one-to-many-mapping-example/](https://www.callicoder.com/hibernate-spring-boot-jpa-one-to-many-mapping-example/)
  - [https://www.baeldung.com/hibernate-one-to-many](https://www.baeldung.com/hibernate-one-to-many)
  - [https://jdm.kr/blog/141](https://jdm.kr/blog/141)
- H2 옵션
  - [https://www.h2database.com/javadoc/org/h2/engine/DbSettings.html](https://www.h2database.com/javadoc/org/h2/engine/DbSettings.html)
