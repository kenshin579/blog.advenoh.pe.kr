---
title: "JPA 일대일(1:1) @One-To-One 연관관계"
description: "JPA 일대일(1:1) @One-To-One 연관관계"
date: 2019-12-27
update: 2019-12-27
tags:
  - database
  - jpa
  - spring
  - db
  - OneToOne
  - 데이터베이스
  - 스프링
  - 스프링부트
  - 연관관계
  - 단방향
  - 양방향
  - 일대일
series: "Spring JPA"
---

## 1. 들어가며

이번 포스팅에서는 일대일 (1:1) 매핑에 대해서 알아보겠습니다.


## 2. 개발 환경

포스팅에서 작성한 코드는 깃허브에 올라가 있어요.

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code :
    * 주 테이블에 외래 키
        * [단방향](https://github.com/kenshin579/tutorials-java/tree/master/springboot-jpa-one-to-one-unidirectional)
        * [양반향](https://github.com/kenshin579/tutorials-java/tree/master/springboot-jpa-one-to-one-bidirectional)
    * 대상 테이블에 외래 키
        * [양반향](https://github.com/kenshin579/tutorials-java/tree/master/springboot-jpa-one-to-one-bidirectional-target)
* Software management tool : Maven

## 3. 일대일 (1:1) 연관관계

일대일 관계에서는 반대도 일대일 관계가 됩니다. 다대일 관계에서는 다(N)쪽이 항상 외래 키를 가지고 있지만, 일대일 관계에서는 주 테이블이나 대상 테이블에 외래 키를 둘 수 있어서 개발 시 어느 쪽에 둘지를 선택해야 합니다.

### 3.1 주 테이블에 외래 키가 있는 경우

주 테이블에 외래 키가 있으면 주 객체에도 객체 참조를 두는 구조로 매핑을 하게 됩니다.

- 주 테이블 : `User`
    - 외래 키(phone_id)가 있는 경우
- 대상 테이블 : `CelluarPhone`

<img src="image_1.png" style="zoom:50%;" />

#### 3.1.1 일대일 단방향

일대일 단방향으로 설정해보겠습니다. 주 객체인 `User` 엔티티에 @OneToOne 선언 이후 대상 테이블인 `CellularPhone` 객체를 선언합니다. `User` 객체를 통해서 사용자의 핸드폰 정보를 조회할 수 있는 구조입니다.

<img src="image_2.png" style="zoom:50%;" />

```java
@Table(name = "user")
public class User extends DateAudit {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "user_id", unique = true, nullable = false)
    private Long id;

    private String username;
    ...(생략)...

    @OneToOne
    @JoinColumn(name = "id")
    private CellularPhone cellularPhone;
		...(생략)...
}
```



```java
@Table(name = "cellular_phone")
public class CellularPhone extends DateAudit {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "phone_id")
    private Long id;

    private String phoneNumber;

    private String model;
		...(생략)...
}
```

`User`와 `CellularPhone` 객체를 저장하고 조회해보겠습니다.

```java
@Test
public void save_user_phone() {
  CellularPhone cellularPhone = CellularPhone.builder()
    .model("android")
    .phoneNumber("010-2342-5234")
    .build();
  phoneRepository.save(cellularPhone);

  User user = User.builder()
    .name("Frank")
    .email("sdf@sdf.com")
    .username("id1234")
    .password("1234")
    .build();
  
  user.setCellularPhone(cellularPhone); //연관관계를 맺음

  userRepository.save(user);

  List<User> users = userRepository.findAll();
  assertThat(users.get(0).getName()).isEqualTo("Frank");
  assertThat(users.get(0).getCellularPhone().getPhoneNumber()).isEqualTo("010-2342-5234");
}
```



#### 3.1.2 일대일 양반향

이제 양반향으로 설정해볼까요? `CellularPhone` 객체에도 `User` 객체를 가지도록 합니다.

<img src="image_4.png" style="zoom:50%;" />

`CellularPhone` 엔티티에 추가로 @OneToOne 어노테이션을 선언합니다. 그리고 양방향이므로 `mappedBy` 속성으로 연관 관계의 주인을 지정해줍니다. `user` 테이블에 외래 키를 가지고 있음으로 `User`의 `cellularPhone`을 연관관계 주인으로 설정합니다.

```java
@Table(name = "cellular_phone")
public class CellularPhone extends DateAudit {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "phone_id")
    private Long id;
  	...(생략)...

    @OneToOne(mappedBy = "cellularPhone")
    private User user;
}
```

Unit Test로 엔티티 저장후 조회해보겠습니다.

```java
@Test
public void save_user_phone() {
  CellularPhone cellularPhone = CellularPhone.builder()
    .model("android")
    .phoneNumber("010-2342-5234")
    .build();

  User user = User.builder()
    .name("Frank")
    .email("sdf@sdf.com")
    .username("id1234")
    .password("1234")
    .build();
  user.setCellularPhone(cellularPhone);

  cellularPhone.setUser(user); //CellularPhone에서 User 객체 설정
  userRepository.save(user);
  phoneRepository.save(cellularPhone);

  List<User> users = userRepository.findAll();
  assertThat(users.get(0).getName()).isEqualTo("Frank");
  assertThat(users.get(0).getCellularPhone().getPhoneNumber()).isEqualTo("010-2342-5234");

  assertThat(cellularPhone.getUser().getName()).isEqualTo("Frank"); //CellularPhone 객체에서 User 정보 확인한다
}
```



> **주의사항**
>
> 일대일 관계에서 지연 로딩으로 설정을 해도 즉시 로딩이 되는 경우가 있습니다. 예를 들면,
>
> - `User.cellularPhone` : 지연 로딩이 된다
> - `CellularPhone.user` : 지연 로딩이 안된다
    >   - 프록시의 한계로 인해서 외래 키를 직접 관리하지 않는 일대일 관계에서는 지연 로딩으로 설정을 해도 즉시 로딩이 된다
>
> 참고로 @OneToOne 어노테이션의 기본 fetch 타입은 즉시 로딩(EAGER)입니다.
>
> ```java
> @Test
> public void 일대일관계에서_지연로딩_테스트() {
> saveUserWithPhones(1, 1);
> 
> List<User> users = userRepository.findAll();
> assertThat(users.get(0).getCellularPhone().getModel()).startsWith("android"); //(1).지연로딩으로 동작한다
> 
> List<CellularPhone> phones = phoneRepository.findAll(); //(2).User도 같이 조회된다.
> }
> ```
>
> - (1) `users.get(0).getCelluarPhone().getModel()`을 호출 할때 SQL 구문이 실행되어 지연로딩이 잘 되는 것을 확인할 수 있다
> - (2) `CelluarPhone.user`는 지연로딩으로 설정되어 있지만, `findAll()` 호출시 즉시 로딩되는 것을 확인할 수 있다



### 3.2 대상 테이블에 외래 키가 있는 경우

외래 키가 주 테이블이 아니라 대상 테이블에 존재하는 경우에는 어떻게 달라지는 알아보겠습니다.

- 주 테이블 : `User`
- 대상 테이블 : `CellularPhone`
    - 외래 키(user_id)가 있는 경우

<img src="image_5.png" style="zoom:50%;" />

#### 3.2.1 일대일 단방향

외래 키는 `cellular_phone` 테이블에 있고 아래와 같은 일대일 연관관계는 JPA에서 지원하지 않아 매핑할 수 없습니다.

<img src="image_2.png" style="zoom:50%;" />

#### 3.2.2 일대일 양반향

<img src="image_4.png" style="zoom:50%;" />



대상 테이블인 `celluar_phone`에 외래 키를 두고 싶으면 아래와 같이 설정하면 됩니다. `CellularPhone` 엔티티에 @OneToOne 어노테이션으로 설정하고 `User` 엔티티에서는 @OneToOne 어노테이션과 `mappedBy` 속성으로 외래 키를 소유하고 있는 `CellularPhone`의 `user`를 연관관계 주인으로 지정합니다.

```java
@Table(name = "cellular_phone")
public class CellularPhone extends DateAudit {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "phone_id")
    private Long id;
		...(생략)...

    @OneToOne
    @JoinColumn(name = "id")
    private User user;
		...(생략)...
}
```



```java

@Table(name = "user")
public class User extends DateAudit {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "user_id", unique = true, nullable = false)
    private Long id;
		...(생략)...
          
    @OneToOne(mappedBy = "user")
    private CellularPhone cellularPhone;
		...(생략)...
}
```

## 4. 참고

* 일대일
    * [https://kwonnam.pe.kr/wiki/java/jpa/one-to-one](https://kwonnam.pe.kr/wiki/java/jpa/one-to-one)
    * [https://riptutorial.com/ko/jpa/example/22229/%EC%A7%81%EC%9B%90%EA%B3%BC-%EC%B1%85%EC%83%81-%EA%B0%84%EC%9D%98-%EC%9D%BC%EB%8C%80%EC%9D%BC-%EA%B4%80%EA%B3%84](https://riptutorial.com/ko/jpa/example/22229/직원과-책상-간의-일대일-관계)
    * [https://www.popit.kr/spring-boot-jpa-step-08-onetoone-%EA%B4%80%EA%B3%84-%EC%84%A4%EC%A0%95-%ED%8C%81/](https://www.popit.kr/spring-boot-jpa-step-08-onetoone-관계-설정-팁/)
* 책 : 자바 ORM 표준 JPA 프로그래밍
    * <a href="http://www.yes24.com/Product/Goods/19040233?	scode=032&OzSrank=2">![책: JPA 프로그래밍](jpa_book1.jpg)</a>
