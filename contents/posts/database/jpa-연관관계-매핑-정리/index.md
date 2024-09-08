---
title: "JPA 연관관계 매핑 정리"
description: "JPA 연관관계 매핑 정리"
date: 2019-12-04
update: 2019-12-04
tags:
  - jpa
  - database
  - spring
  - OneToMany
  - OneToOne
  - 연관관계
  - 단방향
  - 양방향
  - 다대다
  - 다대일
  - 일대다
  - 일대일
series: "Spring JPA"
---


## 1. 들어가며

엔티티는 다른 엔티티의 참조(변수)를 가지면서 관계를 서로 맺게 됩니다. 블로그에서 해당 포스트에 댓글을 다는 경우를 예를 들면, 댓글(Comment) 엔티티는 포스트 (Post) 엔티티 필드를 가지면서 서로 연관관계를 맺어 해당 댓글을 단 포스트 정보를 조회할 수 있습니다. 테이블에서는 이런 관계를 외래 키를 사용해서 관계를 맺습니다.

JPA에서 테이블 간의 관계를 엔티티의 연관관계로 매핑하는 작업이 가장 먼저 하게 되고 핵심이 되는 작업입니다. 이번 포스팅에서는 JPA에서 엔티티 매핑 작업 시 자주 접하는 핵심 용어에 대해서 알아보겠습니다. 이후 시리즈로 포스팅될 블로그에서는 구체적으로 예제 코드를 통해서 각각의 연관관계에 대해서 알아보겠습니다.

## 2. 방향성 (Directional)

> 시나리오
>
> - 포스트 (Post) -> 댓글 (Comment)
> - 댓글 (Comment) -> 포스트 (Post)

테이블은 외래 키 하나로 테이블을 조인해서 양쪽으로 쿼리가 가능합니다.

```sql
SELECT * FROM post AS p INNER JOIN comment AS c ON p.id = c.post_id
# or
SELECT * FROM comment AS c INNER JOIN post AS P ON p.id = c.post_id

```

하지만, 객체의 경우에는 객체에 참조하는 필드가 존재하면 그 필드를 통해서 연관된 객체를 한쪽으로만 조회가 가능하여 단방향이 되고 서로 각각의 객체를 필드로 가지고 있으면 양방향이 됩니다.

- 단방향 (Unidirectional)
    - 객체 관계에서 한 쪽만 참조하는 경우
    - 포스트 -> 댓글
- 양방향 (Bidirectional)
    - 객체 관계에서 양 쪽 다 참조하는 경우
    - 포스트 -> 댓글, 댓글 -> 포스트

## 3. 연관관계 (Associations/Relationships)

위 예제에서 포스트와 댓글의 관계를 보면, 하나의 포스트(일)에 여러 댓글(다)을 달 수 있고 여러 댓글(다)은 하나의 포스트(일)에 포함되는 관계로 다대일, 일대다 관계를 맺을 수 있습니다. 이 외에도 엔티티 간의 관계에서는 아래와 같이 다양한 관계가 존재합니다.


* 다대일 (N:1)
    * 일대다와 같이 가장 많이 사용되는 연관관계이다
* 일대다 (1:N)
* 일대일 (1:1)
* 다대다 (N:N)
    * 실무에서는 거의 사용하지 않는다

## 4. 연관관계의 주인 (Owner)

테이블은 외래 키가 한쪽에 하나만 존재하여 외래 키 하나로 연관관계를 맺습니다. 하지만, 양방향으로 맺어진 엔티티의 경우에는 양쪽에 서로 참조하는 필드가 존재하게 됩니다.

두 엔티티 중에 하나만 외래 키를 관리하는 곳을 연관관계의 주인이라고 합니다. 추후 업로드할 시리즈 포스팅에서 더 자세히 다루겠지만, 연관*관계의* 주인의 특징은 다음과 같습니다.

- mappedBy 속성을 사용하는 엔티티는 연관관계의 주인이 아니다
    - mappedBy 속성으로 연관관계의 주인이 필드 이름을 지정한다
- 보통 외래 키를 가진 테이블과 매핑한 언티티(ex. Comment)가 외래 키ㅐ를 관리하는 주인으로 선택한다
    - 다대일 양방향에서는 다(N)이 연관관계의 주인이 된다

## 5. 참고

- JPA 관계
    - [[https://minwan1.github.io/2018/12/21/2018-12-26-jpa-%EA%B4%80%EA%B3%84%EC%84%A4%EC%A0%95/](https://minwan1.github.io/2018/12/21/2018-12-26-jpa-관계설정/)](https://minwan1.github.io/2018/12/21/2018-12-26-jpa-%EA%B4%80%EA%B3%84%EC%84%A4%EC%A0%95/)
    - [https://siyoon210.tistory.com/27](https://siyoon210.tistory.com/27)
    - [https://howtodoinjava.com/hibernate/how-to-define-association-mappings-between-hibernate-entities/](https://howtodoinjava.com/hibernate/how-to-define-association-mappings-between-hibernate-entities/)
- 책 : 자바 ORM 표준 JPA 프로그래밍
    - <a href="http://www.yes24.com/Product/Goods/19040233?scode=032&OzSrank=1"><img src="images/JPA-연관관계-매핑-정리/JPA_book.jpeg" align="left" alt="자바 ORM 표준 JPA 프로그래밍" style="zoom:33%;" /></a>
