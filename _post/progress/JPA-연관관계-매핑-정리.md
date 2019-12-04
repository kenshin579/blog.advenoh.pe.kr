---
title: '[JPA-1] JPA 연관관계 매핑 정리'
date: 2019-12-3 10:10:23
category: 'database'
tags: ["jpa", "database", "db", spring", "springboot", "persistence", "ManyToMany", "ManyToOne", "OneToMany", "OneToOne", "mapping", "데이터베이스", "스프링", "스프링부트", 연관관계", "단방향", "양방향", "다대다", "다대일", "일대다", "일대일"]
---

# 1. 들어가며



엔티티는 다른 엔티티의 참조(변수)를 가지면서 관계를 서로 맺게 됩니다. 학생 엔티티가 어떤 과목을 선택했는지 과목 엔티티와 연관 관계가 존재한다면 관련 정보를 얻어 올 수 있습니다. 테이블에서는 이런 관계를 외래 키를 사용해서 관계를 맺습니다. 

JPA에서 테이블간의 관계를 엔티티의 연관관계로 매핑하는 작업이 가장 먼저하게 되고 핵심이 되는 작업입니다. JPA에서 엔티티 매핑 작업시 자주 접하는 핵심 용어에 대해서 알아보고 각 시리즈 포스팅에서 구체적으로 예제 코드를 통해서 각 연관관계에 대해서 알아보겠습니다. 

# 2. 방향성 (Directional)

> - 학생 엔티티
> - 



- 단방향
  - 객체 관계에서 한 쪽만 참조하는 경우
  - 학생 -> 과목
- 양방향
  - 
  - 객체 관계에서 양 쪽다 참조하는 경우
  - 테이블은 항상 양방향이다

# 3. 연관관계 (Associations/Relationships)

객체 연관관계 : 객체는 참조(주소)로 연관관계를 맺는다

테이블 연관관계 : 테이블은 외래 키로 연관관계를 맺는다.

엔티티 관계의 종류


* 다대일 (N:1)
* 일대다 (1:N)
* 일대일 (1:1)
* 다대다 (N:N)

# 4. 연관관계의 주인 (Owner)



# 5. 참고

- JPA 관계
  - [[https://minwan1.github.io/2018/12/21/2018-12-26-jpa-%EA%B4%80%EA%B3%84%EC%84%A4%EC%A0%95/](https://minwan1.github.io/2018/12/21/2018-12-26-jpa-관계설정/)](https://minwan1.github.io/2018/12/21/2018-12-26-jpa-%EA%B4%80%EA%B3%84%EC%84%A4%EC%A0%95/)
  - [https://siyoon210.tistory.com/27](https://siyoon210.tistory.com/27)
  - [https://howtodoinjava.com/hibernate/how-to-define-association-mappings-between-hibernate-entities/](https://howtodoinjava.com/hibernate/how-to-define-association-mappings-between-hibernate-entities/)
- 책 : 자바 ORM 표준 JPA 프로그래밍
  - <a href="http://www.yes24.com/Product/Goods/19040233?scode=032&OzSrank=1"><img src="images/JPA-연관관계-매핑-정리/JPA_book.jpeg" align="left" alt="자바 ORM 표준 JPA 프로그래밍" style="zoom:33%;" /></a>
