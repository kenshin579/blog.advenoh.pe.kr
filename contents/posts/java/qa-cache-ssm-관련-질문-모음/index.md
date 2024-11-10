---
title: "Q&A Cache-SSM 관련 질문 모음"
description: "Q&A Cache-SSM 관련 질문 모음"
date: 2018-07-29
update: 2018-07-29
tags:
  - Q&A
  - faq
  - ssm
  - cache-ssm
  - cache
  - 캐쉬
---


개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.

## Q&A 전체 목록

### <span style="color:orange">[답변완료]</span>

### <span style="color:brown">1. @CacheKeyMethod 란?</span>

SSM관련 어노테이션으로 key 값 제공 메서드이고 없는 경우에는 toString()을 호출하게 됩니다. 추가로 캐쉬내 namespace에 toString()로 해서 같은 key 있으면 충돌이 발생합니다.

![](image_1.png)

참고
* [https://m.blog.naver.com/PostView.nhn?blogId=kbh3983&logNo=220934569378&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F](https://m.blog.naver.com/PostView.nhn?blogId=kbh3983&logNo=220934569378&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)

### <span style="color:brown">2. 왜 DB 데이터를 캐싱을 해야 하나?</span>

매번 DB에서 데이터를 가져오면 많이 느린 이슈가 있습니다.

참고
* [https://charsyam.wordpress.com/2016/07/27/입-개발-왜-cache를-사용하는가/](https://charsyam.wordpress.com/2016/07/27/%EC%9E%85-%EA%B0%9C%EB%B0%9C-%EC%99%9C-cache%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%EA%B0%80/)

- - - -
- 
### <span style="color:orange">[미 답변 질문]</span>

#### -

