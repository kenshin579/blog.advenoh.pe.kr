---
title: "데이터베이스의 키 종류"
description: "데이터베이스의 키 종류"
date: 2018-11-25
update: 2018-11-25
tags:
  - database
  - key
  - super key
  - primary key
  - foreign key
  - 키
  - 후보키
  - 대체키
  - 수퍼키
  - 기본키
  - 외래키
---


## 1. 데이터베이스의 키 종류

이번 포스팅에서는 데이터베이스의 여러 키 종류를 정리해보겠습니다.

![키 종류](key.png)

키 종류에 대한 설명을 위해 아래 샘플 데이터를 사용하겠습니다. 샘플 데이터는 자동으로 생성해주는 [dummy data](http://filldb.info/) 사이트에서 얻어왔습니다.

![샘플 데이터](5D16F149-4334-4C3A-9E39-CA985AC78B3C.png)

### 1.1 수퍼키 (super key)

- **유일성의 특성을 만족하는 속성들의 집합으로 이루어진 키** 를 수퍼키라 한다
    - 유일성이란? - **하나의 키로 어떠한 행을 바로 찾아낼 수 있는 성질** 을 의미한다
- 예. authors 테이블
    - id, (id, first_name), (first_name, last_name), email 등이 수퍼키가 된다

### 1.2 후보키 (candidate key)

- **유일성과 최소성을 만족하는 속성** 또는 속성들의 집합이다. 즉, 수퍼키중에서 최소성을 만족하는 것이 후보키가 된다
    - 최소성이란? - **레코드를 식별하는데 꼭 필요한 속성** 들로만 구성한다
- 예. authors 테이블
    - id와 email이 후보키가 된다

### 1.3 기본키 (primary key)

- **후보키중에 특별히 선택된 키** 이다
- 키본키는 **NULL 값이나 중복된 값** 을 가질 수 없다
- 예. authors 테이블 \* 후보키중에 id를 기본키로 선정할 수 있다. (중복값이나 NULL 값이 없다)

### 1.4 대체키 (alternate key)

- 대체키란 **기본키로 선택되지 못한 후보키** 를 의미하고 **보조키** 라고도 한다
- 예. authors 테이블
    - email가 대체키가 된다.

### 1.5 외래키 (foreign key)

- **어떤 릴레이션에 있는 속성이 다른 릴레이션의 기본키가 되는 키** 를 의미한다
- 외래키 속성의 도메인과 참조되는 기본키 속성의 도메인은 같아야 한다
- 외래키는 같은 릴레이션을 참조할 수도 있다
- 외래키는 NULL 값을 가질 수 있다
- 예. posts 테이블
    - authors_id가 외래키가 된다

## 2. 참고

- 책
    - ![책: 데이터베이스 개론](image_4.jpeg)
- 키 종류
    - [https://m.blog.naver.com/dlwjddns5/220620195019](https://m.blog.naver.com/dlwjddns5/220620195019)
    - [http://limkydev.tistory.com/108](http://limkydev.tistory.com/108) \* [https://m.blog.naver.com/PostView.nhn?blogId=slrkanjsepdi&logNo=90118418840&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F](https://m.blog.naver.com/PostView.nhn?blogId=slrkanjsepdi&logNo=90118418840&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)
