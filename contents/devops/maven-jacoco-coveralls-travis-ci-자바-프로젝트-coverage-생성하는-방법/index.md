---
title: "Maven + JaCoCo + Coveralls + Travis CI : 자바 프로젝트 Coverage 생성하는 방법"
description: "Maven + JaCoCo + Coveralls + Travis CI : 자바 프로젝트 Coverage 생성하는 방법"
date: 2020-12-12
update: 2020-12-12
tags:
  - jacoco
  - coveralls
  - travis
  - coverage
  - junit
  - maven
  - 메이븐
  - 커버리지
  - 테스트
---


## 1. 들어가며

Maven + Java 프로젝트의 코드 커버리지를 확인할 수 있는 방법에 대해서 알아보자. 전체적인 작업 흐름은 JaCoCo로 자바 커버리지를 생성하고 Coveralls 사이트로 업로드하여 결과를 확인할 것이다.

- JaCoCo
    - 코드 커버리지를 체크하는 라이브러리이다
    - Unit Test 실행 후 커버리지 결과를 여러 형태(ex. HTML)의 파일로 생성해준다
- Coveralls
    - 웹 기반의 코드 커버리지 관리 사이트이다
    - 저장소(ex. Github)와 연동하여 커버리지를 관리한다
- Travis CI
    - Github 에서 진행하는 프로젝트를 위한 CI 서비스이다.

이 포스팅에서 적용한 내용은 현재 개발 중인 개인 프로젝트 [app-quotes](https://github.com/kenshin579/app-quotes) 에서 확인할 수 있다.

## 2. Maven 설정

### 2.1 JaCoCo dependency

프로젝트에 Querydsl 파일이 있는 경우 configuration에서 exclude 태그로 제외한다.

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.3</version>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
    </executions>
    <configuration>
        <excludes>
            <exclude>**/Q*.class</exclude>
        </excludes>
    </configuration>
</plugin>
```



### 2.2 Coveralls dependency

Coveralls dependency 추가 시 Repo Token을 Coveralls 사이트에 확인하여 repoToken 태그에 넣어줘야 한다. 이 토큰 값으로 해당 프로젝트로 커버리지 결과가 업로드된다.

<img src="image-20201212162832132.png" alt="image-20201212162832132" style="zoom:50%;" />

```xml
<plugin>
    <groupId>org.eluder.coveralls</groupId>
    <artifactId>coveralls-maven-plugin</artifactId>
    <version>4.3.0</version>
    <configuration>
        <repoToken>gpJoZREE123412341234bMmUsdfRQ</repoToken>
    </configuration>
    <dependencies>
        <dependency>
            <groupId>javax.xml.bind</groupId>
            <artifactId>jaxb-api</artifactId>
            <version>2.3.1</version>
        </dependency>
    </dependencies>
</plugin>
```

JDK 높은 버전(ex. 14)으로 실행하는 경우 javax/xml/bind/Datatype*Converter* 클래스를 찾지 못하는 오류가 발생할 수 있다. 클래스를 못 찾는 오류이어서 jaxb-api dependency를 추가하면 된다.

![](image-20201212112943558.png)

## 3. 실행

### 3.1 JaCoCo 보고서 생성

JaCoCo dependency를 추가 이후 아래 명령을 실행하면 target/site/jacoco 폴더에 HTML 파일이 생성된다.

- skipTests=false
    - Unit Test가 실행되어야 커버리지를 확인할 수 있다
- maven.test.failure.ignore=true
    - 실패 떨어지는 Unit Test가 있더라도 커버리지를 생성할 수 있도록 ignore 옵션을 준다

```bash
$ mvn clean test jacoco:report -DskipTests=false -Dmaven.test.failure.ignore=true
```

패키지별로 커버리지를 확인할 수 있다.

![](image-20201212163844309.png)

### 3.2 Coveralls 에 커버리지 결과 업로드

JaCoCo 실행 결과를 Coveralls로 업로드하려면 coveralls:report를 추가해서 실행한다.

```bash
$ mvn clean test jacoco:report coveralls:report -DskipTests=false -Dmaven.test.failure.ignore=true
```

성공적으로 업로드하면 완료된 job 링크로 확인할 수 있다.

![](image-20201212164531772.png)

app-quotes는 67%의 커버리지 가지고 있다. 프로젝트 개발할 때 생각보다 Unit Test에 많은 신경을 쓰지 못했던 것 같은데, 나쁘지 않은 듯하다.

![](image-20201212164630635.png)

### 3.3 Travis 빌드로 코드 커버리지 Coveralls로 업로드하기

app-quotes는 이미 Travis CI에 연동되어 있다. Github + Travis CI 연동에 대한 내용은 다음에 다룰 예정이다. `.travis.yml` 파일에 지금까지 실행해본 명령어를 추가하면 된다.

```yml
after_success:
  - CI=false ./mvnw test jacoco:report coveralls:report -DskipTests=false -Dmaven.test.failure.ignore=true
```

## 4. 정리

이번 시간에는 Maven 프로젝트에서 JaCoCo와 Coveralls로 코드 커버리지를 확인하는 방법에 대해서 알아보았다. 다음 시간에는 여러 모듈로 구성된 한 프로젝트의 코드 커버리지를 확인하는 방법에 대해서도 알아볼 예정이다.

## 5. 참고

- https://woowabros.github.io/experience/2020/02/02/jacoco-config-on-gradle-project.html
- https://github.com/trautonen/coveralls-maven-plugin
- https://jojoldu.tistory.com/275
