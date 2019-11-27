---
title: '[JPA-1] JPA 다대일(N:1) @Many-To-One 연관관계'
date: 2019-11-1 10:23:33
category: 'database'
tags: ["jpa", "database", "db", spring", "springboot", "persistence", "ManyToOne", "mapping", "데이터베이스", "스프링", "스프링부트", 연관관계", "단방향", "양방향", "다대일]
---

# 1. 들어가며

sdfsf



양방향, 단방향에 대한 설명... 

연관관계에 대한 설명... 가장 많이 사용되는 다대일에 대해서 알아보겠습니다. 

- 다대일
- 일대다
- 일대일
- 다대다

# 2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

# 3. 다대일 (N:1) 연관관계

## 3.1 다대일 연관관계.. 

양방향, 단방향

연관관계의 주인이라...

연관관계 편의 메서드란...

@ManyToOne 속성

@JoinColumn의 속성



## 3.3 주의사항

무한 루프에 빠지는 경우

- Member.toString()에서 getTeam()을 호출하고 Team.toString()에서 getMember(0 호출 하면 무한루프 빠짐 
  - 엔티티를 JSON으로 변환할 떄 
- Lombok 사용시에도 무한루프 

# 4. 정리

# 5. 참고

* JPA - one-to-many mapping
	* [https://www.callicoder.com/hibernate-spring-boot-jpa-one-to-many-mapping-example/](https://www.callicoder.com/hibernate-spring-boot-jpa-one-to-many-mapping-example/)
	* [https://www.baeldung.com/hibernate-one-to-many](https://www.baeldung.com/hibernate-one-to-many)