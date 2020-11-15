---
title: '자바 Exception 종류'
date: 2020-10-15 19:56:00
category: 'java'
tags: ["java", "exception", "checked", "unchecked", "자바", "예외"]
---

- Exception 종류
- 

# Exception 종류

- Checked exception (강제성이 높음)

- - 예외처리가 필수이고 처리 하지 않으면 컴파일이 안됨

  - 실행하기전에 예측 가능한 오류

  - - IOException
    - FileNotFoundException

  - rollback을 하지 않음

- Unchecked exception

- - 컴파일 때 체크되지 않고 runtime에 발생하는 exception

  - - ex. NullPointerException, ArrayIndexOutOfBoundException

  - rollback을 함

# 참고

- https://sjh836.tistory.com/122
- http://www.nextree.co.kr/p3239/

