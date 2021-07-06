---
title: '더 읽기 쉽게 kubenetes 설정 파일 cleanup 해주는 쿠버네티스 플러그인 (neat)'
layout: post
category: 'cloud'
author: [Frank Oh]
tags: ["kubernetes", "docker", "plugin", "neat", "cleanup", "yaml", "쿠버네티스", "플러그인", "설정"]
image: ../img/cover-kubernetes.png
date: '2021-07-10T10:23:33.000Z'
draft: false
---

- krew 설치
- plugin 설치
- 실행해보기
  - hello world 실행
  - neat로 비교해보기

Kubernetes 리소스, 즉 Pod를 만들 때 Kubernetes는 원래 작성한 yaml 또는 json에 전체 내부 시스템 정보를 추가합니다. 여기에는 다음이 포함됩니다.

상태, 메타 데이터 및 빈 필드에 대한 일반적인 정리 외에도 kubectl-neat은 주로 Kubernetes의 개체 모델에 의해 삽입 된 기본값과 공통 변경 컨트롤러의 두 가지 유형을 찾습니다.



뭔지를 간단하게 설명하기

# 쿠버네티스 플러그인 설치하기

## krew 설치

Krew는 kubectl 플러그인을 쉽게 사용할 수있는 도구입니다. Krew는 플러그인을 검색하고 컴퓨터에 설치 및 관리 할 수 있도록 도와줍니다. apt, dnf 또는 brew와 같은 도구와 유사합니다. 현재 Krew에서 130 개 이상의 kubectl 플러그인을 사용할 수 있습니다.

```bash
$ brew install krew
```

## neat 플러그인 설치

```bash
$ kubectl krew install neat
```



## neat 사용법

```bash
# yaml 포멧으로 출력된다
$ kubectl get deployments hello-world -o yaml | kubectl neat 

# json 포멧으로 출력하기
$ kc get deployments hello-world -o yaml | kc neat -o json
```



애플리케이션 서비스 생성하기

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world
spec:
  selector:
    matchLabels:
      run: load-balancer-example
  replicas: 2
  template:
    metadata:
      labels:
        run: load-balancer-example
    spec:
      containers:
        - name: hello-world
          image: gcr.io/google-samples/node-hello:1.0
          ports:
            - containerPort: 8080
              protocol: TCP

```



```bash
$ kubectl apply -f https://k8s.io/examples/service/access/hello-application.yaml
```



# 참고



- https://github.com/kubernetes-sigs/krew
- https://github.com/itaysk/kubectl-neat
- https://kubernetes.io/ko/docs/tasks/access-application-cluster/service-access-application-cluster/
- https://github.com/ishantanu/awesome-kubectl-plugins
- https://krew.sigs.k8s.io/plugins/

