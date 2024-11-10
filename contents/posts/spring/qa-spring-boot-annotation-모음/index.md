---
title: "Q&A Spring Boot Annotation 모음"
description: "Q&A Spring Boot Annotation 모음"
date: 2019-07-03
update: 2019-07-03
tags:
  - Q&A
  - faq
  - spring
  - annotation
  - 스프링
  - 어노테이션
---

개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.

## Q&A 전체 목록

### <span style="color:orange">[답변완료]</span>

쉽게 찾기 위해서 알파벳 순으로 정리합니다.

### <span style="color:brown">@SpringBootApplication</span>

@SpringBootApplication 어노테이션은 @Configuration, @EnableAutoConfiguration, @ComponentScan 어노테이션이 뭉쳐진 어노테이션입니다.

* @EnableAutoConfiguration
    * 이 어노테이션은 스프링 부트에서 자동 구성(Auto-Configuration)을 활성화 시키는 어노테이션이다.
    * 스프링 부트는 클래스패스, 어노테이션, 구성 파일을 보고 가장 적절한 앱에 맞는 기술을 넣어 구성을 해준다.

참고
* [http://partnerjun.tistory.com/54](http://partnerjun.tistory.com/54)

- - - -

### <span style="color:orange">[미 답변 질문]</span>

#### - @SpringBootTest와 @DataJpaTest의 차이점은 뭔가?
* [https://lalwr.blogspot.com/2018/05/spring-boot-springboottest-datajpatest.html](https://lalwr.blogspot.com/2018/05/spring-boot-springboottest-datajpatest.html)

