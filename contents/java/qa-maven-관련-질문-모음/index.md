---
title: "Q&A Maven 관련 질문 모음"
description: "Q&A Maven 관련 질문 모음"
date: 2018-07-29
update: 2018-07-29
tags:
  - Q&A
  - faq
  - maven
  - java
  - 메이븐
  - 자바
---

개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.

## Q&A 전체 목록


### <span style="color:orange">[답변완료]</span>

### <span style="color:brown">1. maven으로 특정 클래스의 메서드 unit test 실행은 어떻게 하나?</span>
-DTest= 옵션에 **패키지 이름.파일명#메서드이름** 형식으로 지정하면 원하는 메서드를 실행시킬 수 있습니다. 메이븐에서 -D 옵션은 system property를 지정하는 옵션입니다.

```bash
$ mvn -h #See 메이븐 옵션
$ mvn clean test -Dtest=com.tmoncorp.media.common.util.FileUtilTest#getFileNameBaseCurrentTimestamp -Dmaven.test.skip=true
```

![](image1.png)

### <span style="color:brown">2. Maven 실행시 webxml attribute is required... ?</span>

```java
$ mvn clean package
```
maven 컴파일시 webxml attribute is required...이라는 오류가 발생하는 경우에 대한 해결책은 다음과 같습니다.

![](image2.png)

1. 서블릿 컨테이너 3이하인 경우, WEB-INF/web.xml을 생성해줘야 한다
2. 서블릿 컨테이너 3이상인 경우, web.xml은 없는 경우에는 failOnMissingWebXml=false로 지정하여 무시하도록 설정한다

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-war-plugin</artifactId>
            <configuration>
                <failOnMissingWebXml>false</failOnMissingWebXml>
            </configuration>
        </plugin>
    </plugins>
</build>
```



### 참고

-  https://www.mkyong.com/maven/maven-webxml-attribute-is-required/

---

## <span style="color:orange">[미 답변 질문]</span>

