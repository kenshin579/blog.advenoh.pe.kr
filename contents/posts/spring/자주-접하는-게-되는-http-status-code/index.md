---
title: "자주 접하는 게 되는 Http Status Code"
description: "자주 접하는 게 되는 Http Status Code"
date: 2020-09-12
update: 2024-12-27
tags:
  - http
  - status
  - code
  - statuscode
  - 상태값
  - 응답값
  - 상태코드
---


API 개발 시 접하게 되는 HTTP 상태 코드를 정리해보았다. 이외에도 더 많겠지만, 한 번쯤 들어보고 접한 응답 코드들이다.

HTTP 상태 값에 따라 고양이 이미지를 보여주는 사이트도 존재한다. 이 개발자는 고양이를 무척 좋아하나보다.

- [HTTP Cats API](https://http.cat/)

![](image-20201115171009139.png)


## Http Status Code

### **1xx** (조건부 응답)
- 개인적으로 아직까지는 접해보지 못한 응답 값이다

### **2xx** (성공) : 이 상태 코드 값들은 요청 처리가 성공적인 경우에 응답 값을 내려준다.
- **200** (`OK` 성공)
- **201** (`Created` 생성됨)
  - 요청이 처리되어 새로운 자원을 잘 생성한 경우에 내려준다


### **3xx** (리다이렉션) : 이 상태 코드 값은 클라이언트가 요청을 완료하기 위해 추가 조치를 취해야 함을 나타낸다. 그리고 대부분의 3xx 상태 코드들은 URL 리다이렉션에 사용된다.
- **301** (`Moved Permanently` 영구 이동)
   - 요청한 페이지를 새 위치로 영구적으로 이동시킬 때 사용한다
   - GET 또는 HEAD 요청에 대한 응답에 이 응답 값이면 클라이언트가 자동으로 새 위치로 이동시킨다
   

### **4xx** (클라이언트 오류) : 이 상태 코드 값은 클라이언트측 오류에 의해서 발생한 경우에 내려준다
- **400** (`Bad Request` 잘못된 요청)
- **401** (`Unauthorized` 권한 없음)
  - 요청시 인증이 필요한 경우에 발생하고 인증이 안된 경우에 내려준다

- **403** (`Forbidden` 금지됨)
  - 해당 요청이 서버에 의해서 거부된 경우이다. 요청하는 사용자에게 권한이 없어서 발생할 수 있다.

- **404** (`Not Found` 찾을 수 없음)
- **409** (`Conflicts`)
  - 충돌이 발생하여 요청을 처리할 수 없는 경우에 응답 값으로 내려준다


### **5xx** (서버 오류) : 이 응답 코드 값은 서버에서 요청을 처리할 수 없는 경우에 내려준다
- **500** (`Internal Server Error` 내부 서버 오류)
  - 일반적인 서버 오류에 사용한다

- **501** (`Not Implemented` 구현되지 않음)
- **502** (`Bad Gateway` 불량 게이트웨이)
- **503** (`Service Unavailable` 서비스를 사용할 수 없음) 
  - 서버는 실행중이지만, 많은 requests로 인해서 overloaded된 경우에 사용한다
- **504** (`Gateway Timeout` 게이트웨이 시간초과)

## 참고

- Http Status Code
    - https://http.cat/
    - https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C
- Error 발생시
    - https://www.baeldung.com/rest-api-error-handling-best-practices
    - https://developer.twitter.com/en/docs/basics/response-codes
