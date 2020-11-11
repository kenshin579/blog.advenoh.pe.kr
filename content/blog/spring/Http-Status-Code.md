---
title: 'Http Status Code'
date: 2020-11-12 15:11:13
category: 'spring'
tags: ["http", "status", "code", "상태값", "응답값"]
---




# Http Status Code

- 1xx

- 2xx (성공) : 요청에 대한 성공
  - 200 : 성공
  - 201 : resource 생성 성공

- 3xx (리다이렉션) : 

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

# 참고

- https://http.cat/
