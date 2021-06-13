---
title: 'Helm으로 Mysql 설치하기'
layout : post
category: 'cloud'
author: [Frank Oh]
image: ../img/cover-helm2.png
date: '2021-05-28T18:18:23.000Z'
draft: false
tags: ["kubernetes", "k8s", "helm", "mysql", "db", cloud", "docker", "쿠버네티스", "도커", "헬룸"]
---

- helm 설치는 아미 되었다고 가정함
- values.yaml 

# 1.들어가며

헬름 (Helm)으로 

쿠버네티스로 mysql 구동시키



# 2.헬름으로 Mysql 설치하기

## 2.1 Mysql 설치하기

```bash
$ helm install my-mysql bitnami/mysql -f values.yaml
```



## 2.2 구동후 Mysql Pod로 접근하기

### 2.2.1 Pod에서 접근하기

직접 pod로 접근하거나 다른 pod에서 접근할 수 있다

```bash
$ kc run my-mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.23-debian-10-r57 --namespace default --command -- bash
```

```bash
$ kc 
```

> 제 블로그에서는 kubectl 대신  kc 를 사용한다. 

```bash
$ alias | grep kc                                                           
kc=kubectl
```



### 2.2.2 telepresence로 접근하기

```bash
$ telepresence --run-shell 
$ mysql -h my-mysql.default.svc.cluster.local -uroot -p my_database
```






# 참고

- https://www.howtodo.cloud/kubernetes/2019/04/15/kubernetes-helm.html
- https://artifacthub.io/packages/helm/bitnami/mysql
- https://github.com/bitnami/charts/tree/master/bitnami/mysql
- https://helm.sh/







