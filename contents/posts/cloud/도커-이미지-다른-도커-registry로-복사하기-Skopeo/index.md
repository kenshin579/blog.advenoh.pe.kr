---
title: "도커 이미지 다른 도커 registry로 복사하기 - Skopeo"
description: "도커 이미지 다른 도커 registry로 복사하기 - Skopeo"
date: 2024-08-26
update: 2024-08-26
tags:
  - skopeo
  - 쿠버네티스
  - Kubernetes
  - docker
  - 도커
  - 도커 이미지
  - 도커 레지스트리
  - 레지스트리
  - registry
  - docker registry
  - mirror docker registry
  - 도커 이미지 복사
---

## 1. 개요

최근 들어 우리 회사는 다양한 쿠버네티스 클러스터 환경에 제품을 배포해야 하는 상황이 많아졌다. 동일한 도커 이미지를 여러 쿠버네티스의 도커 레지스트리에 복사해야 했다.

기본 도커 명령어를 사용하여 이미지를 로컬에 다운로드한 후, 다른 도커 레지스트리로 푸시하는 방식으로 작업을 진행했다.

```bash
DOCKER_REGISTRY_SRC_ADDR="docker.io"
DOCKER_REGISTRY_DST_ADDR="demo.goharbor.io"

# download dockker image
docker pull --platform=linux $DOCKER_REGISTRY_SRC_ADDR/library/mariadb:latest

# tag docker image
docker tag $DOCKER_REGISTRY_SRC_ADDR/library/mariadb:latest $DOCKER_REGISTRY_DST_ADDR/library/mariadb:latest

# login to docker registry
docker login $DOCKER_REGISTRY_DST_ADDR

# push docker image
docker push $DOCKER_REGISTRY_DST_ADDR/library/mariadb:latest
```

여러 도커 명령어를 실행해야 하지만, shell 스크립트로 작성하면 다소 번거로움은 줄일 수 있어서 그냥 사용했었다. 근데, 직장 동료의 추천으로 Skopeo 라는 CLI를 알게 되었고 기존 도커 명령어로 실행하는 것보다 더 쉽게 도커 이미지를 다른 레지스트리로 복사할 수 있어서 Skopeo는 뭔가 어떻게 사용하는지 공유 차원에서 정리를 해둔다.

## 2. Skopeo란

Skopeo는 컨테이너 이미지를 다루기 위한 명령줄 도구로, 이미지의 복사, 검사, 서명, 삭제 등 다양한 작업을 지원한다. Skopeo는 Docker 엔진 없이도 이미지 레지스트리 간의 작업을 수행할 수 있어, 클라우드 네이티브 환경에서 특히 유용하다.

> M1에서는 harbor registry 서버 설치가 잘 안되어서 Harbor 사이트에서 제공하는 데모 서버를 이용한다. New Project를 생성해서 사용하면 된다. 
> 참고: [Test Harbor with the Demo Server](https://goharbor.io/docs/2.11.0/install-config/demo-server/)

### 2.1 Skopeo 설치

맥에서는 Homebrew 명령어를 통해서 아래와 같이 설치한다.

```bash
> brew install skopeo
```

### 2.2 Skopeo 사용방법

#### 2.2.1 이미지 검사하기

이미지를 로컬에 다운로드하지 않고도 원격 레지스트리의 이미지를 검사할 수 있다. 이미지의 메타데이터를 아래와 같이 확인할 수 있다.

```bash
❯ skopeo inspect docker://docker.io/library/mariadb
FATA[0001] Error parsing manifest for image: choosing image instance: no image found in image index for architecture "arm64", variant "v8", OS "darwin"
```

M1 맥북에서 실행하면 위와 같이 오류가 발생하는데, 아래 옵션으로 OS와 Arch를 지정해서 실행해야 한다.

```bash
> skopeo inspect docker://docker.io/library/mariadb --override-os linux --override-arch amd64
{
    "Name": "docker.io/library/mariadb",
    "Digest": "sha256:4b812bbd9a025569fbe5a7a70e4a3cd3af53aa36621fecb1c2e108af2113450a",
    "RepoTags": [
        "10",
        "10-bionic",
        "10-focal",
        "10-jammy",
        "10-jessie",
        "10-ubi",
(...생략...)
```

#### 2.2.2 다른 도커 레지스트리로 이미지 복사하기

Skopeo의 강력한 기능 중 하나는 이미지를 한 레지스트리에서 다른 레지스트리로 복사하는 것이다. 예를 들어, Docker Hub에서 내부 프라이빗 레지스트리로 이미지를 복사하려면 다음 명령어를 사용하면 된다.

```bash
> skopeo copy docker://docker.io/library/mariadb:latest docker://demo.goharbor.io/frank-test/mariadb:latest --override-os linux --override-arch amd64
Getting image source signatures
Copying blob bc75b4546118 skipped: already exists
Copying blob ad9066662cff skipped: already exists
Copying blob 8687fa065e6d skipped: already exists
Copying blob 31e907dcc94a skipped: already exists
Copying blob c13aedba8d5d skipped: already exists
Copying blob 90824338d93e skipped: already exists
Copying blob a5e6bca88fae skipped: already exists
Copying blob 537f82e52967 skipped: already exists
Copying config 92520f8661 done   |
Writing manifest to image destination
```

#### 2.2.3 이미지 삭제하기

레지스트리에서 더 이상 필요하지 않은 이미지를 아래 명령어로 삭제할 수 있다.

```bash
> skopeo delete docker://demo.goharbor.io/frank-test/mariadb:latest
```

#### 2.2.4 태그 목록 조회

도커 레지스트리에서 제공하는 이미지 목록을 확인하려면 `list-tags` 옵션을 사용하면 된다. 

```bash
> skopeo list-tags docker://docker.io/library/mariadb
{
    "Repository": "docker.io/library/mariadb",
    "Tags": [
        "10",
        "10-bionic",
        "10-focal",
        "10-jammy",
        "10-jessie",
...생략...
```

#### 2.2.5 로그인 인증

`skopeo login` 명령어는 특정 레지스트리에 로그인하고 인증 토큰을 `authfile`에 저장을 해서 자격 증명을 반복해서 입력할 필요가 없다. authfile 기본 파일 위치는 `.config/containers/auth.json`에 저장이 된다.

> 레지스트리에 로그인하기

```bash
# 이번 한번만 로그인을 하면 된다
> skopeo login docker.io
> skopeo login demo.goharbor.io
```

> `—creds` 명령어 옵션 사용하기

```bash
$ skopeo inspect --creds=testuser:testpassword docker://demo.goharbor.io/frank-test/mariadb:latest
{
  "Tag": "latest",
  "Digest": "sha256:473bb2189d7b913ed7187a33d11e743fdc2f88931122a44d91a301b64419f092",
  "RepoTags": [
    "latest"
  ],
  "Comment": "",
  "Created": "2016-01-15T18:06:41.282540103Z",
  "ContainerConfig": {
    "Hostname": "aded96b43f48",
...생략...
```

## 3. 참고

본 포스팅에서 설명한 예제 파일은 [여기](https://github.com/kenshin579/tutorials-go/tree/master/cloud/skopeo)에서 찾아볼 수 있다.

- [skopeo github](https://github.com/containers/skopeo)

