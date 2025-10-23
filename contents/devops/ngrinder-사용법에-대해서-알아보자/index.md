---
title: "nGrinder 사용법에 대해서 알아보자"
description: "nGrinder 사용법에 대해서 알아보자"
date: 2020-03-22
update: 2020-03-22
tags:
  - ngrinder
  - test
  - performance
  - api
  - 테스트
  - 성능테스트
---

## 1. 들어가며

nGrinder는 스트레스 테스트 도구로 [Grinder](http://grinder.sourceforge.net/) 오픈소스 기반으로 작성되었고 네이버에 의해서 개발되었다. nGrinder 설치에서부터 API 테스트까지 알아보자.

### 1.1 nGrinder 구성요소


| 구성       | 설명                                                         |
| ---------- | ------------------------------------------------------------ |
| controller | 웹 기반의 GUI 시스템으로 테스트 전반적인 작업이 이 컨트롤러에 의해서 작동된다 |
| agent      | 컨트롤러 명령어를 받아서 target 머신에 프로세스와 스레드를 실행시켜 부하를 발생시킨다. 테스트하려는 머신에 agent를 설치하면 된다 |
| target     | 테스트하려는 target 머신이다                                 |



### 1.2 환경

- 테스트환경
    - 추가 장비가 없기 때문에 1대에서 테스트 환경을 구축하고 테스트한다
- 테스트할 API
    - [springboot-quartz-in-memory](https://github.com/kenshin579/tutorials-java/tree/master/springboot-quartz-in-memory) 이 quartz 프로젝트의 API를 테스트한다

## 2. nGrinder 사용법

### 2.1 nGrinder 설치

[nGrinder 릴리스](https://github.com/naver/ngrinder/releases) 페이지에서 최신 WAR 버전을 다운로드한다.

```bash
$ mkdir ngrinder
$ cd ngrinder
$ wget https://github.com/naver/ngrinder/releases/download/ngrinder-3.5.2-20200929/ngrinder-controller-3.5.2.war
```

다운로드이후  -jar 옵션을 두고 실행한다. 구동하려는 애플리케이션도 8080 포트를 사용할 예정이라 컨트롤러는 7070 포트로 띄운다.

```bash
$ java -jar ngrinder-controller-3.5.2.war --port 7070
```

이상없이 구동이 되면 http://localhost:7070/login 사이트 주소로 접속할 수 있다.

![image-20201025215243779](image-20201025215243779.png)

초기 어드민 id/password는 admin/admin이다.

### 2.2 Agent 설치

다음은 테스트하려는 target 머신에 agent를 설치해보자. agent는 사이트에 로그인한 이후 메뉴에서 admin > Download Agent를 클릭하면 agent가 다운로드된다. 다운로드한 파일을 아래 명령어로 압축을 푼다.

```bash
$ tar -xvf ngrinder-agent-3.5.2-localhost.tar
```

agent 설정파일에 컨트롤러 IP 주소를 수정한다. 이 테스트에서는 로컬에 컨트롤러가 있어서 여기서는 수정없이 그냥 둔다.

```bash
$ cd ngrinder-agent
$ vim __agent.conf
common.start_mode=agent
agent.controller_host=localhost
agent.controller_port=16001
agent.region=NONE
```

agent을 아래 shell script로 실행한다. 이상없으면 컨트롤러에 등록이 된다.

```bash
$ ./run_agent.sh
```

![](image-20201025212130395.png)

컨트롤러에서 잘 등록되었는지 admin > Agent Management 클릭하여 확인할 수 있다.

![](image-20201025215330969.png)

### 2.3 API 테스트

#### 2.3.1 Script 작성하기

![](image-20201025215610234.png)

스크립트 생성후 Validate 버튼을 클릭해서 실제 API 호출에 이상이 없는지 확인후 저장을 한다.

![](image-20201025215639641.png)

#### 2.3.2 Performance Test 생성하기

Performanc Test > Create Test 클릭후 원하는 테스트 설정을 한다.

![](image-20201025215810490.png)

#### 2.3.3 테스트 실행 후 결과

테스트 실행시에도 라이브로 테스트 진행되는 것을 볼 수 있고 테스트 종료 이후에는 전체 테스트 Summary와 Detailed Report를 통해서 더 자세하게 결과를 확인할 수 있다.

![](image-20201025220008476.png)

## 3. 정리

여기서는 간단하게 nGrinder 테스트 도구의 사용법에 대해서 알아보았다. 실제 개발하는 웹 애플리케이션의 성능을 개선하려고 한다면, 구체적인 테스트 시나리오와 코드 개선 전후로 테스트 결과를 확인하면서 점진적으로 코드를 개선해 나가야 한다. 기회 되면 API 성능 개선한 사례에 대해서 포스팅할 예정이다.


## 4. 참고

- nGrinder
    - http://naver.github.io/ngrinder/
    - https://heedipro.tistory.com/279
    - https://brownbears.tistory.com/26
    - https://nesoy.github.io/articles/2018-10/nGrinder-Start
- 설정
    - https://programmer.help/blogs/ngrinder-2-stress-test-script-groovy.html
