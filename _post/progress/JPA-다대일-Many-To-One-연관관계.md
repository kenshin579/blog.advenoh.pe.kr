---
title: '[JPA-2] JPA 다대일(N:1) @Many-To-One 연관관계'
date: 2019-11-25 10:23:33
category: 'database'
tags: ["jpa", "database", "db", spring", "springboot", "persistence", "ManyToOne", "mapping", "데이터베이스", "스프링", "스프링부트", 연관관계", "단방향", "양방향", "다대일]
---

# 1. 들어가며

이 포스팅에서는 JPA에서 자주 사용하는 다대일 Many-To-One 연관관계에 대해서 알아보겠습니다. 



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

## 3.1 다대일 연관관계.. 

양방향, 단방향

연관관계의 주인이라...

연관관계 편의 메서드란...

@ManyToOne 속성

@JoinColumn의 속성

## 3.2 일대다 연관관계

일대다관계는 엔티티를 하나 이상 참조할 수 있으므로 자바 Collection, List, Set, Map중에 하나를 사용해야 합니다. 

- 실제 query가 어떻게 시작되는지도 적어두자
- 

## 3.3 주의사항

무한 루프에 빠지는 경우

- Member.toString()에서 getTeam()을 호출하고 Team.toString()에서 getMember(0 호출 하면 무한루프 빠짐 
  - 엔티티를 JSON으로 변환할 떄 
- Lombok 사용시에도 무한루프 

# 4. FAQ

## 4.1 언제 양반향, 단방향을 사용해야 하나?

ㄴㅇㄴㅇㄹ

## 4.2 ??

# 5. 참고

- JPA - one-to-many mapping
- - [https://www.callicoder.com/hibernate-spring-boot-jpa-one-to-many-mapping-example/](https://www.callicoder.com/hibernate-spring-boot-jpa-one-to-many-mapping-example/)
  - [https://www.baeldung.com/hibernate-one-to-many](https://www.baeldung.com/hibernate-one-to-many)
  - [https://jdm.kr/blog/141](https://jdm.kr/blog/141)
- H2 옵션
- - [https://www.h2database.com/javadoc/org/h2/engine/DbSettings.html](https://www.h2database.com/javadoc/org/h2/engine/DbSettings.html)