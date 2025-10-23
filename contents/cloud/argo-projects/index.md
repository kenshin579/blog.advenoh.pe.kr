---
title: "Argo Projects"
description: "Argo Projects"
date: 2022-03-04
update: 2022-03-04
tags:
  - argo
  - argocd
  - events
  - workflow
  - cloud
series: "ArgoCD"
---


## Argo Projects?

Argo Project란 쿠버네티스 환경에서 application이나 job을 실행하거나 배포를 도와주는 일련의 쿠버네티스 도구 집합이다. 모든 Argo 프로그램은 `CRD (Custom Resource Definition)`와 사용자 쿠버네티스 클러스터로 구현되어 있다. 현재 4가지 대표 서브 프로젝트가 존재하고 각 프로그램은 독립적으로 사용할 수도 있지만, 함께 사용하면 더욱 강력한 도구가 되기도 한다.

### What?

- `Argo Workflows`
    - 컨테이너 기반의 워크플로우 엔진

        - Job 단위가 프로세스가 아닌 컨테이너 단위로 실행된다

        - 다양한 실행 방식을 지원한다

            - ex. sequence, parallel, with dependency w/ DAG, etc

- `Argo Events`
    - 쿠버네티스를 위한 이벤트 기반 워크로플로우 자동화 프레임워크 도구

        - 아래와 같은 다양한 Event와 Trigger를 제공하고 Event 발생시 Trigger하는 역할을 수행한다

        - Events Source (20+):

            - Github, NATS, File, NATS, MQTT, Slack, Webhooks, HDFS, K8s Resources, Kafka, Redis, etc

        - Triggers (10+)

            - Argo Workflow, Argo Rollouts, k8s Object, AWS Lambda, AWS Lamda, NATS message, Kafka message, Log, Slack Notification, etc

- [`Argo CD`](https://blog.advenoh.pe.kr/argo-cd/)
    - 선언적인 GitOps 기반의 CD (Continuous Deployment) 도구

- `Argo Rollouts`
    - Progress Delivery 를 지원하는 도구

    - 여러 배포 방식을 지원한다

    - ex. canary, blue/green, rolling updates, etc


#### 참고

- https://github.com/terrytangyuan/awesome-argo

### Who?

- Applatix 회사에서 Argo 를 만들고 cloud-native 개발자 커뮤니티에 오픈소스로 제공을 함
- 2018년에 Intuit라는 회사가 Applatix를 인수를 함
- 2020년 Argo 프로젝트가 CNCF 프로젝트 Incubator 프로젝트로 승인됨
- 현재 여러 회사에 의해서 유지되고 있음

#### 참고

- https://argoproj.github.io/
- https://www.intuit.com/blog/innovation/cloud-native-computing-foundation-accepts-argo-as-an-incubator-project/
- https://www.intuit.com/blog/innovation/welcome-applatix-to-the-intuit-team/
- https://blog.argoproj.io/argo-goes-to-cncf-incubator-f0e9dfb40597


### Where?

- 180개 이상의 여러 회사에서 프로덕션에 적극적으로 사용하고 있음

- ex. Adobe, Alibaba Cloud, Data Dog, Datastax, Google, GitHub, IBM, MLB, NVIDIA, Red Hat, SAP, Tesla, Ticketmaster, 당근마켓, LINE

### Reference

- https://argoproj.github.io/

### Note

> 본 내용은 저희 Platform Engineering 팀내 CNCF 스터디를 위해 준비한 자료입니다. 저희가 하는 로봇 플랫폼 개발에 관심이 있는 분들은 아래 링크를 참고해주시고 도전적이고 열정적으로 같이 일하실 분은 많이 지원해주세요.
>
> - 네이버는 왜 제2사옥 1784를 지었을 까요?  https://www.youtube.com/watch?v=WG7JHLfClEo
> - 네이버 랩스 - https://www.naverlabs.com/


