---
title: "(Docker-1) Docker 도커 명령어 모음"
description: "(Docker-1) Docker 도커 명령어 모음"
date: 2019-12-08
update: 
tags:
  - 도커
  - 컨테이너
  - 가상화
  - 명령어
  - docker
  - container
  - vm
  - cli
---

## 1. 들어가며

도커를 다루는 데 있어서 크게 2가지 종류로 나뉠 수 있습니다.

- 도커 이미지 다루기
- 도커 컨테이너 다루기

도커 관련된 여러 명령어들이 많아서 자주 사용되는 명령어 위주로 정리를 해봤습니다. 전체 도커 명령어에 대한 내용은 [도커 문서](https://docs.docker.com/engine/reference/commandline/docker/) 사이트를 참고해주세요.


## 2. 도커 명령어
### 2.1 도커 도움말

도커 도움말은 명령어 창에서 help로 확인할 수 있습니다.
```bash
$ docker help
Usage:  docker [OPTIONS] COMMAND
...(생략)...

Management Commands:
  builder     Manage builds
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
 ...(생략)...

Run 'docker COMMAND --help' for more information on a command.

```

도커를 다루는 데 있어서 여러 관리 명령어(서브 명령어)가 존재를 하고 해당 도움말도 아래 명령어로 자세하게 확인할 수 있습니다.

```bash
$ docker COMMAND
$ docker COMMAND --help
```

도커 볼륨 명령어 도움말은 다음과 같습니다.

```bash
$ docker volume
Usage:  docker volume COMMAND

Manage volumes

Commands:
  create      Create a volume
  inspect     Display detailed information on one or more volumes
  ls          List volumes
  prune       Remove all unused local volumes
  rm          Remove one or more volumes

Run 'docker volume COMMAND --help' for more information on a command.
```



### 2.2 도커 이미지 다루기

도커 컨테이너를 실행하기 전에 원하는 이미지를 검색하거나 새로운 이미지를 생성할 필요가 있습니다. 도커 이미지를 어떻게 다룰 수 있는지 알아보겠습니다.

#### 2.2.1 도커 이미지 검색하기

Docker Hub 레지스트리에서 도커 이미지를 검색합니다.

```bash
$ docker search redis
```

Redis 관련 이미지를 목록으로 보여줍니다. 검색된 결과는 깃허브의 스타 순으로 정렬해서 출력됩니다. 목록을 보면 대부분 ####/redis 앞에 네임스페이스가 붙지만, 첫 번째 아이템은 네임스페이스 없이 redis으로만 되어 있습니다. 공식 리포지토리의 네임스페이스는 library이고 이 네임스페이스는 생략될 수 있습니다.

```bash
$ docker search redis
NAME   DESCRIPTION   STARS   OFFICIAL   AUTOMATED
redis Redis is an open source key-value store that…         7557   [OK]                
bitnami/redis   Bitnami Redis Docker Image                  132   [OK]
sameersbn/redis                                             78   [OK]
grokzen/redis-cluster   Redis cluster 3.0, 3.2, 4.0 & 5.0   62                                      

```

search 명령어로는 여러 버전의 redis를 검색할 수 없기 때문에 다음과 같은 API를 통해서 조회하면 됩니다.

> jq 명령어는 JSON 포멧을 다룰 수 있는 명령어이고 맥에 설치되어 있지 않다면 brew install jq로 설치하면 된다

```bash
$ curl -s 'https://hub.docker.com/v2/repositories/library/redis/tags/?page_size=10'  | jq -r '.results[].name'                                                                              !10013
alpine3.10
alpine
5.0.6-alpine3.10
5.0.6-alpine
5.0-alpine3.10
5.0-alpine
5-alpine3.10
5-alpine
4.0.14-alpine3.10
4.0.14-alpine
```



#### 2.2.2 이미지 다운로드하기

도커 이미지를 도커 registry에서 내려받으려면 docker image pull 명령을 사용합니다.

```bash
$ docker image pull [옵션] 리포지토리명[:태그명]
```

redis 이미지를 다운로드받으려면 다음과 같이 하면 됩니다. 태그 명을 생략하면 기본적으로 latest 태그가 적용됩니다.

```bash
$ docker image pull redis
Using default tag: latest
latest: Pulling from library/redis
8d691f585fa8: Pull complete 
8ccd02d17190: Pull complete 
4719eb1815f2: Pull complete 
200531706a7d: Pull complete 
eed7c26916cf: Pull complete 
e1285fcc6a46: Pull complete 
Digest: sha256:fe80393a67c7058590ca6b6903f64e35b50fa411b0496f604a85c526fb5bd2d2
Status: Downloaded newer image for redis:latest
docker.io/library/redis:latest
```

#### 2.2.3 이미지  빌드하기

docker image built 명령어로 도커 이미지를 생성하고 Dockerfile 파일에 정의된 내용에 따라서 이미지가 생성됩니다.

- -t 옵션은 이미지명과 태그명을 같이 붙이는 옵션이다. 거의 필수 옵션으로 쓰인다

```bash
$ docker image build -t 이미지명[:태그명] Dockerfile 파일의 경로
```
Dockerfile 파일을 보면 이미지 생성하는 인스트럭션이 나열되어 있습니다.

| 인스트럭션 | 설명                                                         |
| ---------- | ------------------------------------------------------------ |
| FROM       | 지정한 이미지를 레지스트리에서 다운로드 한다 (ex. ubuntu:16.04 이미지 다운로드) |
| COPY       | 호스트에 있는 파일을 도커 이미지로 복사한다                  |
| RUN        | FROM 에서 다운로드 받은 이미지를 기반으로 RUN에 정의된 명령어를 실행하여 새로운 이미지가 생성이 된다 |
| CMD        | 컨테이너가 시작되었을 때 실행되는 명령어를 정의한다          |

```bash
$ cat Dockerfile
FROM ubuntu:16.04

COPY helloworld.sh /usr/local/bin
RUN chmod +x /usr/local/bin/helloworld.sh

CMD ["helloworld.sh"]
```
> 참고로 이미지가 한번 다운로드되어 있으면 로컬에 저장된 이미지를 사용한다. --pull =true 옵션을 추가하면 매번 베이스 이미지를 강제로 새로 다운로드받는다.

```bash
$ docker image build -t helloworld:latest .
Sending build context to Docker daemon  3.072kB
Step 1/4 : FROM ubuntu:16.04
16.04: Pulling from library/ubuntu
e80174c8b43b: Pull complete 
d1072db285cc: Pull complete 
858453671e67: Pull complete 
3d07b1124f98: Pull complete 
Digest: sha256:bb5b48c7750a6a8775c74bcb601f7e5399135d0a06de004d000e05fd25c1a71c
Status: Downloaded newer image for ubuntu:16.04
 ---> 5f2bf26e3524
Step 2/4 : COPY helloworld.sh /usr/local/bin
 ---> b948d39a6b4f
Step 3/4 : RUN chmod +x /usr/local/bin/helloworld.sh
 ---> Running in 669a25a95285
Removing intermediate container 669a25a95285
 ---> a2ffdb53aaeb
Step 4/4 : CMD ["helloworld.sh"]
 ---> Running in 83864f5c36f6
Removing intermediate container 83864f5c36f6
 ---> b06d1d769f4f
Successfully built b06d1d769f4f
Successfully tagged helloworld:latest
```

#### 2.2.4 이미지 목록 보기

docker image ls 명령어로 현재 보유하고 있는 이미지의 목록을 볼 수 있습니다. Docker Hub에서 내려받은 이미지나 이미지를 빌드한 것들이 목록으로 보여집니다.

```bash
$ docker image ls
REPOSITORY   TAG   IMAGE   ID   CREATED   SIZE
example/mysql-data   latest   d4f1510aa2be        2 days ago          1.22MB
jenkins/jenkins      latest   55614b251a46        3 days ago          552MB
example/echo         latest   4a3aa6cc6b21        4 days ago          750MB

```

#### 2.2.5 이미지에 태그 붙이기

docker image tag 명령어로 이미지에 태그를 달 수 있습니다.

```bash
$ docker image tag 기반이미지[:태그] 새이미지명[:태그]
```
예를 들어 helloworld의 이미지에 0.1.0 태그를 추가하려면 다음과 같이 실행하면 됩니다.

```bash
$ docker image tag helloworld:latest helloworld/test:0.1.0
$ docker image ls
REPOSITORY        TAG      IMAGE ID       CREATED      SIZE
helloworld/test   0.1.0    b06d1d769f4f   6 days ago   123MB
helloworld        latest   b06d1d769f4f   6 days ago   123MB

```

이미지를 다음과 같은 상황에서 빌드를 하면 매번 새로운 이미지가 생성이 됩니다.

- 이미지를 빌드하는 경우
- Dockerfile을 편집하는 경우
- COPY 대상이 되는 파일의 내용이 변경이 된 경우

COPY 대상이 되는 helloworld 파일을 수정하고 빌드를 해보겠습니다.

```bash
$ cat helloworld
#!/bin/sh
echo "Hello, World!"

$ vim helloworld
#!/bin/sh
echo "Hello, World!"
echo "Hi!!"
```

이미지를 빌드하고 조회를 하면 <none>가 새로 추가되었습니다. 새로운 이미지는 helloworld:latest로 새로운 생성이 되었고 그전 오래된 이미지들은 <none>으로 표시가 됩니다.

```bash
$ docker image build -t helloworld:latest . 
$ docker image ls
REPOSITORY   TAG      IMAGE ID       CREATED              SIZE
helloworld   latest   4427b4290f55   3 seconds ago        123MB
<none>       <none>   411cc8adaba2   About a minute ago   123MB


```

#### 2.2.6 이미지 공유하기

docker image push 명령어로 도커 허브 등의 레지스트리에 등록할 수 있습니다.

```bash
$ docker image push [옵션] 이미지명:[:태그]
```

helloworld 이미지를 도커 허브에 올려보겠습니다. helloworld:latest 이미지는 도커 허브에 이미 등록되어 있어서 이미지의 네임스페이스를 먼저 바꾸고 push를 하면 됩니다.

```bash
$ docker image tag helloworld:latest kenshin579/helloworld:latest
$ docker image ls
REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
kenshin579/helloworld    latest               4427b4290f55        5 days ago          123MB
helloworld               latest              4427b4290f55        5 days ago          123MB
```

도커에 로그인이 안 되어 있으면 로그인을 먼저하고 이미지를 push 하면 도커 허브에 공유가 됩니다.

```bash
$ docker login
$ docker image push kenshin579/helloworld:latest
The push refers to repository [docker.io/kenshin579/helloworld]
cde5c9054b7e: Pushed 
bc72fb2e7b74: Pushed 
903669ee7207: Pushed 
a5a5f8c62487: Pushed 
788b17b748c2: Pushed 
latest: digest: sha256:7906b00f23cc5eb44dcedcc2d0fe39e2a7253c3f2373b88f661cb7aa2bda4470 size: 1564

```

![Docker Repository List](image1.png)

### 2.3 도커 컨테이너 다루기

#### 2.3.1 컨테이너 실행하기

docker container run 명령어는 컨테이너를 생성하고 실행하는 명령어입니다.

```bash
$ docker container run [옵션] 이미지명[:태그] [명령] [명령인자...]
```

redis 이미지를 백그라운드에서 실행하려면 -d 옵션을 주고 다음과 같이 실행하면 됩니다.

```bash
$ docker container run --name redis_test -d -p 7000:6379 redis
```

-p 옵션으로 호스트 포트 7000 -> 컨테이너 포트 6379으로 포트 포워딩했으므로 다음과 같이 redis에 접속할  때 포트 번호를 7000으로 해서 접속해야 합니다.

```bash
$ redis-cli -p 7000
127.0.0.1:7000> set hello world
OK
127.0.0.1:7000> get hello
"world"
127.0.0.1:7000> 
```

**컨테이너 옵션**

| 옵션   | 설명                                                         |
| ------ | ------------------------------------------------------------ |
| -d     | 백그라운드로 실행한다                                        |
| -p     | 외부포트:컨테이터포트 (ex. 9000:8080)<br />포트를 지정하지 않는 경우 임의의 포트가 자동으로 할당된다 |
| -t     | 유닉스 터미널 연결 활성화를 시킨다<br />-i 옵션과 같이 많이 사용되어 -it 옵션으로 합쳐서 실행한다 |
| -i     | 컨테이너 쪽 표준 입력(stdout)과 연결을 유지한다. 컨테이너 쪽 셀에 들어가려면 이 옵션을 추가해야 한다. |
| -rm    | 컨테이터가 종료시 컨테이너를 파기한다.                       |
| --name | 컨테이너에 원하는 이름을 붙일 수 있다. 이름으로 조회하거나 삭제할 수 있다. |

##### 2.3.1.1 명령 인자로 실행하기

docker container run 명령어에 명령 인자를 추가해서 실행하면 Dockerfile에 정의된 CMD 인스트럭션은 무시되고 명령 인자로 넘어온 값으로 실행됩니다.

```bash
$ docker container run -it redis
1:C 07 Dec 2019 01:16:39.642 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
1:C 07 Dec 2019 01:16:39.642 # Redis version=5.0.6, bits=64, commit=00000000, modified=0, pid=1, just started
1:C 07 Dec 2019 01:16:39.642 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf

```

위 명령어는 redis 디몬이 실행되는 반면에 'uname -a' 인자를 추가한 명령어는 인자 명령어를 실행한 값이 출력됩니다.

```bash
$ docker container run -it redis uname -a 
Linux 36e0253d1a29 4.9.184-linuxkit #1 SMP Tue Jul 2 22:58:16 UTC 2019 x86_64 GNU/Linux
```



#### 2.3.2 실행 중인 컨테이너 조회하기

docker container ls 명령어로 현재 실행 중인 컨테이너를 확인할 수 있습니다. 20e9f060fc15 ID를 가진 컨테이너는 redis_test 이름을 가진 컨테이너로 --name 옵션으로 실행된 컨테이너입니다. --name 옵션 없이 실행되면 랜덤 값의 이름이 부여됩니다.

```bash
$ docker container ls
CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES
20e9f060fc15  redis  "docker-entrypoint.s…"  25 hours ago  Up 25 hours  0.0.0.0:7000->6379/tcp   redis_test

```

##### 2.3.2.1 컨테이너 목록 필터링해서 보기

--filter 옵션으로 필터링 조건을 추가하여 컨테이너 목록을 필터링해서 조회할 수 있습니다.

```bash
$ docker container ls --filter "필터명=값"
```

필터 조건으로 name을 추가하면 컨테이너 이름에 redis가 포함된 컨테이너를 조회합니다.

```bash
$ docker container ls --filter "name=redis"
```

##### 2.3.2.2 종료된 컨테이너 목록 보기

종료된 컨테이너는 목록에서 보여지지 않지만, -a 옵션을 추가하여 종료된 컨테이너를 확인할 수 있습니다.

```bash
$ docker container ls -a
```

#### 2.3.3 실행중인 컨테이너 정지하기

docker container stop 명령어로 실행 중인 컨테이너를 컨테이너 ID나 컨테이너 이름으로 정지 시킬 수 있습니다.

```bash
$ docker container stop 컨테이너ID_OR_컨테이너명
```

#### 2.3.4 정지된 컨테이너 재시작하기

정지된 컨테이너를 다시 시작하려면 docker container restart를 사용하면 됩니다.

```bash
$ docker container restart 컨테이너ID_OR_컨테이너명
```

#### 2.3.5 실행중인 컨테이너 삭제하기

컨테이너를 정지시키면 정시된 시점의 상태를 계속 유지한 체 디스크에 남아 있습니다. 완전히 파기하려면 rm 명령어를 추가하여 삭제합니다.

```bash
$ docker container rm 컨테이너ID_OR_컨테이너명
```

컨테이너 실행하고 종료한 이후에 자동으로 파기하려면 다음 명령어와 같이 컨네이터 실행시 --rm 옵션을 추가합니다.

```bash
$ docker container run --rm -d -p 7000:6379 redis
```

#### 2.3.6 컨테이너의 stdout(표준 출력)를 호스트 stdout으로 출력하기

docker container logs 명령어로 도커 컨테이너의 표준 출력을 호스트 화면으로 볼 수 있습니다.

```bash
$ docker container logs [옵션] 컨테이너ID_OR_컨테이너명
```

jenkins 도커를 실행한 후 jenkins 서버에서 출력하는 내용을 보기 위해서는 다음과 명령어를 입력하면 됩니다.

| 명령어 | 옵션 | 설명                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| logs   | -f   | 출력하는 로그를 계속 화면에 출력한다. (ex. tail -f와 같은 옵션) |
| ls     | -q   | docker container ls에서 -q 옵션은 컨테이너의 ID를 얻어온다   |

```bash
$ docker container run --rm -d jenkins
$ docker container logs -f $(docker container ls --filter "ancestor=jenkins" -q)
```

#### 2.3.7 실행중인 컨테이너에서 명령 실행하기

docker container exec 명령어로 현재 실행 중인 컨테이너에 명령을 수행할 수 있습니다.


```bash
$ docker container exec [옵션] 컨테이너ID_OR_컨테이너명 실행할_명령
```

셀을 오픈해서 내부 파일을 확인하고 싶으면 다음 명령어로 확인하면 됩니다.

```bash
$ docker container exec -it 5bb352057045 bash
$ jenkins@5bb352057045:/$ ls
bin  boot  dev  docker-java-home  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

#### 2.3.8 파일 복사하기

컨테이너<-> 호스트 간에 파일을 복사하기 위한 명령어입니다.

```bash
$ docker container cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH # 컨테이너 -> 호스트
$ docker container cp [OPTIONS] SRC_PATH CONTAINER:DEST_PATH # 호스트 -> 컨테이너
```

호스트 파일을 컨테이너에 복사하고 복사한 텍스트를 보려면 다음과 같이 하면 됩니다.

```bash
$ echo "hello world" > /tmp/test.txt
$ docker container cp /tmp/test.txt echo:/tmp
$ docker container exec cat echo:/tmp/test.txt
hello world
```


## 3. 부록(기타사항)

### 3.1 도커 축약 명령어

docker container run 명령어가 길기 때문에 축약 명령어도 제공합니다. 하지만, 축약 명령어보다는 full 명령어를 사용하는 걸 추천하는 분위기입니다.

| 도커 full 명령어     | 축약 명령어  |
| -------------------- | ------------ |
| docker container run | docker run   |
| docker image pull    | docker pull  |
| docker image build   | docker build |

### 3.2 도커 운용관련 명령어

#### 3.2.1 컨테이너 및 이미지 파기하기

컨테이너나 이미지를 파기할 때 사용하는 명령어입니다. docker container prune은 현재 실행 중이 아닌 모든 컨테이너를 삭제하는 명령어입니다.

```bash
$ docker container ls -a
$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
5bd169e3043f51d33347a165e483a03ea142442cb9ef83b5faf13440d0ca329b
350b12c364310514b7f2024ebbf8f19bdb9e5a2331337d143ef3329f90bfb089
460912b768d82b58d7158e32d55da684d449d7b69fa144e0bff556c038d2396f
dd91039088a7109cbcf8e365624671701c1751ea16324c1f45af3528c9bc5baa
...(생략)...

Total reclaimed space: 28.49MB
```

이미지도 사용하지 않는 것은 점차 누적되어 디스크 용량을 차지 하기 때문에 정기적으로 삭제해주면 좋습니다.

docker image prune은 태그가 붙지 않는 모든 이미지를 삭제합니다.

```bash
$ docker image ls
$ docker image prune 
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Deleted Images:
deleted: sha256:411cc8adaba2c3fc9d2070aca8b8a4d58041f1cfb63aebfe617991115821ff9f
deleted: sha256:3f72f3ef13a37d85b13901e8cc89d3499beb7e452cab1d38e53041949502396f
...(생략)...

Total reclaimed space: 84B
```

docker system prune은 이미지, 컨테이너, 볼륨, 네트워크 등 모든 리소스를 일괄적으로 삭제하는 명령어입니다.

```bash
$ docker system prune
```

#### 3.2.2 컨테이너 시스템 리소스 사용 현황 확인하기

현재 실행 중인 컨테이너 시스템 리소스 사용 현황을 확인할 수 있습니다. Linux의 top 명령어처럼 실시간으로 현환을 업데이트해서 보여줍니다.

```bash
$ docker container stats [옵션] [컨테이너ID ...]
```

```bash
$ docker container stats
CONTAINER ID        NAME                CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
5b3e2e966799        boring_sutherland   0.19%               1.68MiB / 1.952GiB    0.08%               648B / 0B           8.43MB / 0B         4
5bb352057045        vigorous_meninsky   0.17%               349.5MiB / 1.952GiB   17.48%              4.18MB / 91.5kB     124MB / 24.3MB      34

```

## 4. 참고

- 도커 명령어 참조
    - [https://docs.docker.com/engine/reference/commandline/docker/](https://docs.docker.com/engine/reference/commandline/docker/)
- 축약 명령어
    - https://www.slipp.net/wiki/pages/viewpage.action?pageId=41583363
- 책 : 도커, 쿠버네티스를 활용한 컨테이너 개발 실전 입문
    - ![도커 책](image2.jpg)
