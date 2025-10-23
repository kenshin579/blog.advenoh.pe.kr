---
title: "AWS에서 EC2로 API 서버 구축하기"
description: "AWS에서 EC2로 API 서버 구축하기"
date: 2023-03-18
update: 2023-03-18
tags:
  - aws
  - ec2
  - api
  - server
  - 구축
  - 가상머신
  - api
  - heroku
  - gcp
  - amazon
  - vm
  - virtual
  - rest
---

API 서버를 구축하기 위해 사용할 수 있는 서비스는 아래와 같이 여러 서비스가 존재한다.

- [Heroku](https://dashboard.heroku.com/)
- [GCP](https://cloud.google.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)
- [AWS](https://aws.amazon.com/) (Amazon Web Service)

위 서비스들은 대부분 무료 플랜을 제공하고 있고 제한된 리소스와 기능을 제공한다. 개인적으로 여러 서비스 중에서 그래도 장기간 12개월간 무료로 사용할 수 있는 AWS를 선호한다. 자주 EC2를 구축하지는 않지만, EC2로 API를 구축하면 매번 구글링해서 세팅하는 과정이 시간이 걸린다. 이번에 [stock-api](https://rapidapi.com/kenshin579-dCJkBINoF/api/stock-api7/) 구축하면서 나중에 바로 참고할 수 있도록 블로그에 정리해둡니다.

## 1.서버 구축 사전작업

### AWS 계정 생성하기

AWS 계정은 12개월 무료로 사용할 수 있지만, 이메일 주소로 계정을 생성해야 한다. 매번 새로운 이메일 주소를 생성하기보다는 구글의 [별칙 기능](https://blog.advenoh.pe.kr/하나의-구글-계정으로-여러-이메일-주소-사용하기/)을 사용하기를 추천한다.

AWS 계정을 생성하고 콘솔에 로그인한다.

## 2. AWS에서 EC2 서버 구축하기

### 2.1 EC2 인스턴스 생성하기

AWS 서비스 중에 인스턴스를 찾아들어가 EC2 AWS에서 가상머신을 생성한다. 왼쪽 메뉴에서 인스턴스 > 인스턴스 시작 버튼을 클릭한다.

기본적으로 EC2 인스턴스 생성 시 기본값은 설정되어 있다. 사용자가 채워 넣어야 하는 값은 다음과 같다.

- 이름: 원하는 이름을 넣는다 (ex. `echo-server`)

- 애플리케이션 및 OS 이미지

    - 이미지: `Amazon Linux 2 AMI`
    - 아키텍처: `64비트`

- 인스턴스 유형: t2 micro

- 키 페어 (로그인): `echo-server`

    - 키 페어는 나중에 EC2 인스턴스 생성후 ssh로 로그인하기 위해 필요한다
    - 일단 새 키 페어 생성 클릭해서 생성하고

- 네트워크 설정

    - `에서 SSH 트래픽 허용` 체크박스 클릭하고 `내 IP`를 선택하다
    - `0.0.0.0/0`이 선택되어 있으면 누구나 로그인 시도를 할 수 있어 특정 네트워크나 네트워크 주소에서만 접근하도록 하는게 좋다


- 스토리지 구성 : `30`
    - 프리 티어는 최대 30GB까지 사용할 수 있어 `30`으로 변경한다

![EC2 인스턴스](image-20230306213316281.png)

![EC2 인스턴스 설정](image-20230306213304863.png)

#### 2.1.1 키 페어 생성

생성하면 `PEM` 파일이 자동으로 다운로드된다. 키 페어는 인스턴스 생성 이후 접근할 때 사용하는 파일이다.

![키 페어 생성](image-20230306212515060.png)



### 2.2 Elastic IP 설정하기

EC2 인스턴스를 재시작하게 되면 매번 새 IP가 할당된다. IP가 변경되면 PC에서 접근할 때마다 IP 주소를 확인해야 하는 번거로운지 존재한다. 매번 IP가 변경되지 않고 고정 IP를 할당받으려면 Elastic IP를 설정해야 한다.

`EC2 메뉴` > `네트워크 및 보안` > `탄력적 IP` > `탄력적 IP 주소 할당` 버튼을 클릭한다. 아래와 같은 설정으로 할당한다.

![Elastic IP 설정 - 주소 할당](image-20230306214219371.png)

`EC2 메뉴` > `네트워크 및 보안` > `탄력적 IP` > `작업 Pull Down 메뉴` > `탄력적 IP 주소 연결` 선택한다. 생성한 EC2 인스턴스와 프라이빗 IP 주소를 입력한다.

![Elastic IP 설정 - 주소 연결](image-20230306214114369.png)

### 2.3 EC2 서버에 ssh로 접속하기

위에서 다운로드한 `PEM` 파일을 가지고 ssh로 접근하려면 아래 명령어를 입력하면 된다.

#### 2.3.1 ssh 옵션에서 PEM 파일 지정하기

```bash
$ ssh -i echo-server.pem xxx.xxxx.xxx.xxx # EC2의 탄력적 IP 주소
```

IP 주소로 기억하기 쉽지 않고 매번 긴 명령어 입력을 해야 해서 ssh 설정 파일을 다음과 같이 설정하면 간단한 명령어로 접근이 가능하다.

#### 2.3.1 ssh 설정에 미리 PEM 파일 및 서버 IP 주소 설정하기

`PEM` 파일을`.ssh` 폴더로 복사하고 권한을 변경한다.

```bash
$ cp echo-server.pem ~/.ssh
$ chmod 0600 ~/.ssh/echo-server.pem
```

`config` 파일을 생성해서 다음 정보를 입력한다.

```bash
$ vim ~/.ssh/config
# echo-server
Host echo-server #원하는 서비스명을 입력한다
HostName xxx.xxxx.xxx.xxx #탄력적 IP 주소 입력
User ec2-user
IdentityFile ~/.ssh/echo-server.pem

$ chmod 0700 ~/.ssh/config
```

이제 아래 명령을 입력하면 EC2 인스턴스에 로그인할 수 있다.

```bash
$ ssh echo-server
Last login: Tue Mar  7 20:08:03 2023 from 59.10.139.253

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
19 package(s) needed for security, out of 22 available
Run "sudo yum update" to apply all updates.
[ec2-user@xxx.xxx.xxx.xxx ~]$
```

### 2.4. EC2 생성 후 EC2 인스턴스 추가 설정

#### 2.4.1 타임존 변경

EC2 서버의 기본 타입 존은 UTC이다. 한국시간에 맞게 타임존을 변경한다.

```bash
$ sudo rm /etc/localtime
$ sudo ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```



#### 2.4.2 Hostname 변경

여러 서버를 관리하고 있다면 IP 주소만으로는 어떤 서비스의 서버인지 확인이 어렵기 때문에 `Hostname` 이름을 변경해준다.

Amazon Linux AMI 2 이미지 기존으로 hostname을 변경하는 방법이다.

```bash
$ sudo hostnamectl set-hostname echo-server
```

추가로 /etc/hosts에 hostname을 등록하면 등록한 hostname으로 접근하기 편한 부분이 있어 같이 수정을 해준다.

```bash
$ vim /etc/hosts
127.0.0.1 echo-server

$ reboot
```

IP 주소 대신 등록한 hostname을 사용해서 접근할 수 있다.

```bash
$ curl echo-server
curl: (7) Failed to connect to echo-server port 80: Connection refused
```

아직 서버에 서버를 띄우지 않아서 위 오류 메시지가 뜨지만, curl 호스트 이름으로 실행은 잘 된 것을 확인할 수 있다.

참고

- https://bbeomgeun.tistory.com/157

### 2.5 (옵션) EC2 보안 그룹에 추가 설정

EC2 인스턴스 생성 시 ssh 트래픽 허용하지 않았다면 보안 그룹에 추가로 설정을 해줘야 한다.

`네트워크 및 보안` > `보안 그룹` > `EC2 인스턴스에 적용된 보안 그룹` 선택 > `작업 pull down 메뉴` > `인바운드 규칙 편집` 선택 한다

맨 아래 `규칙 추가` 버튼을 클릭해서 소스 유형 > 내 IP를 선택해서 내 컴퓨터에서만 접근되도록 한다.

![EC2 보안 그룹](image-20230318173043607.png)

## 3. EC2에 API 배포하기



### 3.1 Github 소스 코드 다운로드

ssh로 EC2 인스턴스에 접근하고 github 에서 소스 코드를 다운로드한다.

```bash
$ ssh echo-server
$ git clone https://github.com/kenshin579/echo-server
```

### 3.1 golang 설치

Echo server는 golang으로 작성이 되어 있어서 golang을 설치한다.

```bash
$ sudo yum install -y golang
```

### 3.2 소스 코드 빌드

Makefile에 빌드 명령이 지정되어 있어 쉽게 make로 빌드한다.

```bash
$ make build
go mod tidy
go build -v -o bin/go-echo-server cmd/server/main.go
go.uber.org/dig/internal/graph
go.uber.org/fx/internal/fxclock
go.uber.org/dig/internal/digerror
go.uber.org/dig/internal/digreflect
go.uber.org/dig/internal/dot
golang.org/x/tools/go/internal/cgo
go.uber.org/fx/internal/fxreflect
go.uber.org/fx/fxevent
go.uber.org/dig
github.com/labstack/echo/v4
golang.org/x/tools/go/loader
go.uber.org/fx/internal/lifecycle
go.uber.org/fx/internal/fxlog
github.com/swaggo/swag
go.uber.org/fx
github.com/kenshin579/echo-server/ping/route/http
github.com/kenshin579/echo-server/echo/route/http
github.com/labstack/echo/v4/middleware
github.com/kenshin579/echo-server/docs
github.com/swaggo/echo-swagger
github.com/kenshin579/echo-server/cmd/bootstrap
command-line-arguments
```

### 3.3 Echo 실행하고 외부에서 테스트해보기

#### 3.3.1 API 실행

```bash
$ go run cmd/server/main.go
[Fx] PROVIDE    *echo.Echo <= github.com/kenshin579/echo-server/cmd/bootstrap.newEcho()
[Fx] PROVIDE    fx.Lifecycle <= go.uber.org/fx.New.func1()
[Fx] PROVIDE    fx.Shutdowner <= go.uber.org/fx.(*App).shutdowner-fm()
[Fx] PROVIDE    fx.DotGraph <= go.uber.org/fx.(*App).dotGraph-fm()
[Fx] INVOKE             github.com/kenshin579/echo-server/echo/route/http.NewEchoHandler()
[Fx] INVOKE             github.com/kenshin579/echo-server/ping/route/http.NewPingHandler()
[Fx] INVOKE             github.com/kenshin579/echo-server/cmd/bootstrap.serve()
[Fx] HOOK OnStart               github.com/kenshin579/echo-server/cmd/bootstrap.serve.func1() executing (caller: github.com/kenshin579/echo-server/cmd/bootstrap.serve)
{"time":"2023-03-18T17:41:47.605105+09:00","level":"INFO","prefix":"-","file":"app.go","line":"46","message":"Starting echo api server."}
[Fx] HOOK OnStart               github.com/kenshin579/echo-server/cmd/bootstrap.serve.func1() called by github.com/kenshin579/echo-server/cmd/bootstrap.serve ran successfully in 179.625µs

   ____    __
  / __/___/ /  ___
 / _// __/ _ \/ _ \
/___/\__/_//_/\___/ v4.10.2
High performance, minimalist Go web framework
https://echo.labstack.com
____________________________________O/_______
                                    O\
[Fx] RUNNING
⇨ http server started on [::]:80

```

#### 3.3.2 외부에서 API 접근하기

먼저 EC2 공개 주소를 알아야 접근할 수 있기 때문에 EC2 인스턴스 세부 정보에서 확인한다.

`인스턴스` > `인스턴스` > `인스턴스 목록에서 인스턴스 ID 를 선택하면 IP 주소나 DNS 주소를 확인할 수 있다.

![외부로 접근할 수 있는 DNS 확인](image-20230318174426135.png)



`curl` 명령어로 API을 호출해보면 잘 되는 걸 확인할 수 있다. 끝!!

```bash
$ curl --location 'https://ec1-3-30-20-2342.ap-northeast-2.compute.amazonaws.com/ping'
Pong
```

## 참고

- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/go-devenv.html
- https://ryanwoo.tistory.com/8
- https://technoracle.com/how-to-install-git-on-amazon-linux-2/
- https://chat.openai.com/chat
- http://www.yes24.com/Product/Goods/83849117