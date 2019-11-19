---
title: 'H2 데이터베이스 사용법 및 Intellij에서 Database 연동'
date: 2019-11-20 10:23:33
category: 'database'
tags: ["h2", "database", "spring", "springboot", "intellij", "DB", "데이터베이스", "인텔리제이"]

---
# 1. 들어가며

H2는 자바로 구현된 오픈소스 데이터베이스입니다. 인 메모리와 파일 기반의 데이터베이스 설정이 가능합니다. 자바 애플리케이션에 임베디드해서 사용하거나 서버 모드로 구동할 수 있습니다. 별도의 설치과정 없이 임베디드로 바로 사용할 수 있는 장점으로 많이 사용되는 DB입니다. 

이 포스팅에서는 H2에서 제공하는 여러 모드 외에도 웹 콘솔과 Intelij에서 H2에 연동하는 방법도 같이 알아보겠습니다. 

- 임베디드 모드
  - 메모리
  - 파일
- 서버 모드 - 여러 도구에서 같은 DB에 연동이 가능함

# 2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven


# 3. Spring Boot에서 H2 DB 사용해보기

## 3.1 JPA 샘플 코드 작성

스프링 부트와 H2 DB간의 연동를 위해 pom.xml 파일에 H2 라이브러리를 추가해야 합니다. 

```xml
<dependency>
  <groupId>com.h2database</groupId>
  <artifactId>h2</artifactId>
  <scope>runtime</scope>
</dependency>
```

H2의 여러 환경 테스트를 위해서 간단한 JPA 샘플 코드를 작성해두겠습니다. JPA에서 제공하는 DDL 자동 생성 옵션(jpa.hiberate.ddl-auto)과 초기 데이터 로딩이 되도록 세팅하면 쉽게 테스팅이 쉬울 거예요. 

JPA에서 사용할 Book 엔티티를 생성합니다. 

```java
@Getter
@Setter
@Entity
@NoArgsConstructor
@Table(name = "book")
public class Book {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    private String author;

    private int price;
}
```

src/main/resources/data.sql 파일을 생성하여 아래 초기 데이터를 추가해줍니다. 

```sql
INSERT INTO book (`title`, `author`, `price`) VALUES ('지금 이대로 좋다', '법류 저', 9330);
INSERT INTO book (`title`, `author`, `price`) VALUES ('여행할 땐 책', '채김남', 12150);
INSERT INTO book (`title`, `author`, `price`) VALUES ('기차 타고 부산에서 런던까지', '정은주', 12150);
```

API로 호출 하기 위해서 BookController과 BookRepository 파일도 같이 생성해줍니다. 소스코드를 github 링크를 참고해주세요. 

## 3.2 H2 데이터베이스 설정

### 3.2.1 Memory 

인 메모리

- url : 
- DB_CLOSE_DELAY=-1
  - sdf
- DB_CLOSE_ON_EXIT=FALSE
  - sdf

```yml
# Database Settings
spring:
  datasource:
    url: jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE;
    platform: h2
    username: sa
    password:
    driverClassName: org.h2.Driver
jpa:
  database-platform: org.hibernate.dialect.H2Dialect
  hibernate:
    ddl-auto: update # 테이블 스키마 자동 생성 옵션
```

### 3.2.2 File로 설정



3.3 스프링 부트 구동

# 4. H2 Console

spring-boot-devtools 적용
application.properties 에 spring.h2.console.enabled=true 명시

# 5. 정리

# 6. 참고

* H2 설치 및 사용법
	* [https://en.wikipedia.org/wiki/H2_(DBMS](https://en.wikipedia.org/wiki/H2_%28DBMS) )
	* [https://jojoldu.tistory.com/234](https://jojoldu.tistory.com/234)
	* [https://www.tutorialspoint.com/h2_database/](https://www.tutorialspoint.com/h2_database/)
	* [http://www.h2database.com/html/cheatSheet.html](http://www.h2database.com/html/cheatSheet.html)
* Spring Boot
  * https://engkimbs.tistory.com/794
