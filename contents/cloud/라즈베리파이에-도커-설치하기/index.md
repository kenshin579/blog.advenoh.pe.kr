---
title: "라즈베리파이에 도커 설치하기"
description: "라즈베리파이에 도커 설치하기"
date: 2021-07-18
update: 2021-07-18
tags:
  - raspberry
  - docker
  - install
  - 도커
  - 라즈베리파이
  - 설치
---

라즈베리파이에 도커 설치하는 방법에 대해서 알아보겠습니다.

### 사전 조건

- 라즈베리파이에 Raspbian OS 설치
    - 참고 : [모니터없이 Raspberry Pi 4 OS 설치](https://blog.advenoh.pe.kr/raspberry-pi4-os-설치/)
- SSH 연결 활성화

## 라즈베리파이에 도커 설치하기

### 스크립트로 도커 설치

도커에서 제공하는 설치 스크립트를 다운로드해서 바로 실행시킨다.

```bash
$ curl -sSL https://get.docker.com | sh
Executing docker install script, commit: 7cae5f8b0decc17d6571f9f52eb840fbc13b2737
+ sudo -E sh -c apt-get update -qq >/dev/null
+ sudo -E sh -c DEBIAN_FRONTEND=noninteractive apt-get install -y -qq apt-transport-https ca-certificates curl >/dev/null
+ sudo -E sh -c curl -fsSL "https://download.docker.com/linux/raspbian/gpg" | apt-key add -qq - >/dev/null
Warning: apt-key output should not be parsed (stdout is not a terminal)
...생략...
```



### 도커 그룹에 non-root 사용자 추가하기

기본적으로 도커 컨테이너를 실행시키려면 root 권한이 필요하다. sudo로 실행할 수 있지만, root 권한이 없는 사용자도 실행하고 싶은 경우 docker 그룹에 사용자를 추가하면 된다. 로그아웃하고 다시 로그인해야 실행이 가능하다.

```bash
$ sudo usermod -aG docker pi
```

지금까지 도커 설치가 잘 되었는지 도커 명령어를 실행해보자. 잘 설치가 되었으면 도커 버전과 추가 정보를 확인할 수 있다.

```bash
$ docker verion
```



### Hello World 컨테이너 실행해서 테스트해보기

도커 설치가 잘 되었는지 테스트하는 가장 좋은 방법은 마지막으로 Hello World 컨테이너를 실행하는 것이다. 아래 명령어로 컨테이너를 실행시킨다.

```bash
$ docker run hello-world
```

## 참고

- https://dev.to/elalemanyo/how-to-install-docker-and-docker-compose-on-raspberry-pi-1mo
- https://www.boolsee.pe.kr/installation-and-running-of-docker-in-raspberry-pi-buster/
- https://phoenixnap.com/kb/docker-on-raspberry-pi

