---
title: "Travis CI에서 Slack 연동해서 빌드 notification 받기"
description: "Travis CI에서 Slack 연동해서 빌드 notification 받기"
date: 2020-10-22
update: 2020-10-22
tags:
  - travis
  - ci
  - slack
  - notification
  - build
  - 빌드
  - 슬랙
  - 자동화
---

## 들어가며

Travis CI로 빌드 이후 notification을 Slack으로 받는 방법에 대해서 알아보자. Git*hub* 소스를 Travis CI로 배포하는 방법에 대한 설명은 다른 곳에 이미 많이 있기 때문에 부여 설명은 생략한다.

사전에 필요한 작업들이다. 간단하게 언급만 하고 넘어간다.

- Slack 워크스페이스 생성 및 채널 생성
- Github 소스 코드
- Travis CI로 Github 소스 빌드 및 배포하기

빌드하려는 소스는 [app-quotes](https://github.com/kenshin579/app-quotes) 이고 이 포스팅에 작성되는 파일도 여기 소스에 포함되어 있다.

## Travis CI에 Slack 연동하기

### 1. Slack App Directory에서 Travis CI 추가

slack app directory에서 Travis CI App을 찾아 추가한다.

![Travis CI App](image-202010243533216.png)

Slack에 추가 > 채널 선택 > Travis CI 통합 앱 추가 버튼 클릭하여 Slack와 Travis CI를 연동한다.

![](image-20201024185548896.png)

Travis CI 통합 앱 추가 이후에는 앱 토큰 정보를 알려준다. 이 정보를 기반으로 추후 작업을 하면 된다. 여기서도 언급되어 있는 것처럼 소스 코드가 public으로 되어 있어 앱 토큰이 노출되면 누구나 메시지를 보낼 수 있기 때문에 해당 토큰을 암호화하도록 하자.

![](image-20201024190107595.png)

연동이 잘 되면 Slack 채널에 메시지를 받게 된다.

![](205B5442-FCB2-4013-AA4D-1FEC7AB6CA46.png)

### 2. travis.yml 설정에 slack 정보 추가하기

#### 2.1 앱 토큰 암호화 하기

암호화에 필요한 travis 명령어를 설치한다.

```bash
$ ruby -v 
$ sudo gem install travis
$ travis —-version
```

--com은 travis-ci.com을 사용하는 경우에 추가하여 로그인을 하면 된다.

```bash
$ travis login
$ travis login --com
```

travis.yml 파일이 있는 곳에서 실행하면 기존 설정 + slack 정보가 추가되어 전체 설정을 출력해준다.

```bash
$ travis encrypt "<슬랙도메인명>:<travis APP의 token>#<채널명>" --add notifications.slack
```

#### 2.2 travis.yml 설정에 Slack 설정 추가

빌드 성공 + 실패시에도 메시지를 항상 받도록 설정해 두었다. Travis 빌드 설정에 대한 부여 설명은 [Travis 문서](https://docs.travis-ci.com/user/notifications/)를 참고하세요.

```yaml
notifications:
  slack:
    on_success: always
    on_failure: always
    secure: pnEZaS1REkNU5VWKLK+JE2tbA7n18vfE8Cikk9RCO5rkGeubTDG/Pgicc=
```

#### 2.3 Travis CI에서 빌드하기

Travis CI에서 빌드를 직접해보면 Slack에 빌드 메시지를 잘 받는 것을 확인할 수 있다.

![](BE2B65F9-8EFE-4991-9118-849627BE8F8B.png)

## 마무리

Travis CI 빌드시 Slack으로 빌드 메시지를 받을 수 있도록 연동 작업을 했다. 다음 포스팅에서는 Github Action과 Slack 연동 작업에 대해서 작업할 예정이다.

## 참고


* Slack 연동하기

    * https://berndrabe.de/enabling-travis-ci-with-slack-integration/
    * https://www.edmondscommerce.co.uk/handbook/Development-Tools/Testing/Travis-CI/
    * [https://riverandeye.tistory.com/entry/Travis-Travis-Ci-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-%EB%8F%84%EC%A0%84%EA%B8%B0-2-%EC%8A%AC%EB%9E%99-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0](https://riverandeye.tistory.com/entry/Travis-Travis-Ci-튜토리얼-도전기-2-슬랙-연동하기)
    * https://docs.travis-ci.com/user/notifications/
* Travis CI로 배포하기

    * https://teichae.tistory.com/entry/Travis-CI%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%B0%B0%ED%8F%AC-1
