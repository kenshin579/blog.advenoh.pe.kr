---
title: '자주 접하는 게 되는 Http Status Code 목록'
date: 2020-11-12 15:11:13
category: 'spring'
tags: ["http", "status", "code", "statuscode", "상태값", "응답값", "상태코드"]
---

API 개발 시 접하게 되는 HTTP 상태 코드를 정리해보았다. 이외에도 더 많겠지만, 한 번쯤 들어보고 접한 응답 코드들이다. 

HTTP 상태 값에 따라 고양이 이미지를 보여주는 사이트도 존재한다. 이 개발자는 고양이를 무척 좋아하나보다. 

- [HTTP Cats API](https://http.cat/)



<img src="images/Http-Status-Code/image-20201112182603389.png" alt="image-20201112182603389" style="zoom: 25%;" />


# Http Status Code

- 1xx 

- 2xx (성공) : 요청에 대한 성공
  
  - 200 OK : 성공
- 201 Created : resource 생성 성공
  
- 3xx (리다이렉션) : 

  - 301 Mo
  - 302(임시 이동): 현재 서버가 다른 위치의 페이지로 요청에 응답하고 있지만 요청자는 향후 요청 시 원래 위치를 계속 사용해야 한다.

- 4xx (클라이언트 오류) : 요청시 오류 발생

  - 400 (bad request)

  - 401 Unauthorized
  - 403 (Forbidden, 금지됨): 서버가 요청을 거부하고 있다. 예를 들자면, 사용자가 리소스에 대한 필요 권한을 갖고 있지 않다. (401은 인증 실패, 403은 인가 실패라고 볼 수 있음)
  - 404 : not found
  - 409 : conflicts

- 5xx (서버 오류) : 

  - 500 (내부 서버 오류)
  - 501 (구현되지 않음)
  - 502 (Bad Gateway)
  - 503 (서비스를 사용할 수 없음)
  - 504 (게이트웨이 시간초과)



# FAQ

## 1. 서버에서 오류 발생시 500, 503 어느 응답이 맞나?

- 500
  - 서버 일반 적인 오류에도 사용한다 (ex. Facebook, twitter API)

- 503
  - 서버는 실행중이지만, 많은 requests로 인해서 overloaded된 경우

# 참고

- Http Status Code
  - https://http.cat/
  - https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C
- Error 발생시
  - https://www.baeldung.com/rest-api-error-handling-best-practices
  - https://developer.twitter.com/en/docs/basics/response-codes
