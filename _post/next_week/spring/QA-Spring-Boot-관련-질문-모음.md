---
title: 'Q&A : Spring Boot 관련 질문 모음'
date: 2019-7-3 20:41:23
category: 'spring'
tags: ["Q&A", "faq", "spring", "springboot", "batch", "스프링", "배치", "질문"]
---

개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.


### [Q&A 전체 목록](https://blog.advenoh.pe.kr/java/20190320_Q&A_%EA%B0%9C%EB%B0%9C%EA%B4%80%EB%A0%A8_%EC%A7%88%EB%AC%B8_%EB%AA%A8%EC%9D%8C/)

### <span style="color:orange">[미 답변 질문]</span>
-

- - - -


### <span style="color:orange">[답변완료]</span>

### <span style="color:brown">1. application.properties : server.compression.enabled 속성의 의미는?</span>

스프링 부트에서 기본적으로 GZip 압축은 비활성화 되어 있습니다. 하지만, server.compression.enabled=true로 설정하면 웹 자원(ex. html, css)을 압축해서 클라이언트로 보내져서 응답 시간을 줄일 수 있는 장점이 있습니다.

참고
* [https://www.callicoder.com/configuring-spring-boot-application/](https://www.callicoder.com/configuring-spring-boot-application/)


#### - @SpringBootTest와 @DataJpaTest의 차이점은 뭔가?
* [https://lalwr.blogspot.com/2018/05/spring-boot-springboottest-datajpatest.html](https://lalwr.blogspot.com/2018/05/spring-boot-springboottest-datajpatest.html)
