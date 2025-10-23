---
title: "맥 환경에서 여러 JDK 버전 설치하고 변경하기"
description: "맥 환경에서 여러 JDK 버전 설치하고 변경하기"
date: 2018-11-11
update: 2018-11-11
tags:
  - java
  - mac
  - jdk
  - version
  - 자바
  - 버전
  - 맥
---

자바 개발을 하다 보면 하나의 JDK 버전이 아니라 여러 버전을 설치해야 할 때가 종종 있습니다. 진행하는 프로젝트마다 개발하는 JDK 버전이 조금씩 다를 수 있고 새로 릴리스한 버전을 설치해서 스터디하고 싶을 때 여러 버전이 존재하게 됩니다. 한 시스템에 여러 버전이 존재하지만, 쉽게 한 버전에서 다른 버전으로 변경할 수 있는 명령어를 JDK에서는 제공하지는 않습니다. 개발자가 알아서 수동으로 변경해야 합니다.

본 포스팅에서는 맥 환경을 대상으로 어떻게 여러 버전의 JDK로 쉽게 변경할 수 있는지 알아보겠습니다.

## 1. 여러 JDK 버전 설치하기

일단, 먼저 여러 JDK 버전을 설치해 볼까요? brew 명령어로 3가지 JDK 버전을 설치하도록 하겠습니다.

```bash
$ brew cask install java java8 zulu8
```

- java : OpenJDK 11
- java8 : Oracle JDK 8
- zulu8 : Azul Zulu Java JDK

## 2. 여러 버전으로 변경해보기

현재 설치된 모든 JDK를 확인하려면, java_home -V 명령어로 확인할 수 있습니다. 제 맥에서는 총 4가지 JDK가 설치되어 있습니다.

```bash
$ /usr/libexec/java_home -V
```

![](image_1.png)

원하는 버전의 JDK로 자바 프로그램을 컴파일하고 실행하려면 기본적으로 아래 2가지를 기본적으로 해줘야 합니다.

- JAVA_HOME 환경 변수를 수정한다
    - JAVA_HOME=“/Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home"
- PATH에도 JDK/bin 폴더를 추가한다
    - PATH=$PATH:$JAVA_HOME/bin

환경변수는 대부분 사용하는 shell의 환경 파일을 손 보면 됩니다. 저는 zsh shell을 사용해서 .zshrc를 아래처럼 수정했습니다.

```bash
$ code ~/.zshrc
```

소스 코드 넣기

실행 화면입니다. 도움말로 더 쉽게 이해할 수 있는 부분이라 별도의 설명은 생략하겠습니다.

![](image_2.png)

## 3. 참고

- OS X에서 기본 자바 JDK 변경하기
    - [https://stackoverflow.com/questions/21964709/how-to-set-or-change-the-default-java-jdk-version-on-os-x](https://stackoverflow.com/questions/21964709/how-to-set-or-change-the-default-java-jdk-version-on-os-x)

