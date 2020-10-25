---
title: 'ngrinder 설치 및 기본 설정 방법'
date: 2020-10-22 10:23:33
category: 'devops'
tags: ["ngrinder", "test", "performance", "api", "테스트", "성능테스트"]
---
- 들어가며
  - 용어 정리
- nGrinder 사용법
  - nGrinder 설치
  - Agent 설치
- API 테스트
- 기타사항

#1. 들어가며



## 1.1 용어


- | 용어       | 설명                                                         |
  | ---------- | ------------------------------------------------------------ |
  | controller |                                                              |
  | agent      | controller 명령어를 받아서 target 머신에 프로세스와 스레드를 실행시켜 부하를 발생시킴 |
  | target     |                                                              |



## 1.2 환경



# 2. nGrinder 사용법

## 2.1 nGrinder 설치

```bash
$ mkdir ngrinder
$ cd ngrinder
$ wget https://github.com/naver/ngrinder/releases/download/ngrinder-3.5.2-20200929/ngrinder-controller-3.5.2.war
```



```java
$ java -XX:MaxPermSize=200m -jar ngrinder-controller-3.5.2.war
```

http://127.0.0.1:8080/login

admin/admin

## 2.2 Agent 설치

- 로그인후 menu > admin > download agent
- untar
- 필요시 __agent.conf 파일 수정
- run_agent.sh 실행



# 3. API 테스트

테스트 실행

- script > create > create a script
- - 생성이후 validate 을 해서 제대로 API가 호출이 되는지 확인하기
- Performance Test > 

# 4. 정리




#5. 참고

- nGrinder
	- https://heedipro.tistory.com/279
  - https://brownbears.tistory.com/26
  - https://nesoy.github.io/articles/2018-10/nGrinder-Start
- 설정
	- https://programmer.help/blogs/ngrinder-2-stress-test-script-groovy.html
