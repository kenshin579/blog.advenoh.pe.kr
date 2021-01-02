---
title: 'Git 브랜치 여러 개 한번에 삭제하기'
layout: post
category: 'git'
author: [Frank Oh]
tags: ["git", "branch", "multiple", "delete"]
image: ../img/cover-git.png
date: '2020-07-11T23:05:23.000Z'
draft: false
---

Git 브랜치를 한번에 정리하는 방법입니다. 

1. 삭제하려는 브랜치 목록 검색해보기

```bash
$ git branch | grep "MEDIA-1"
  deploy/MEDIA-1078
  deploy/MEDIA-1210
  feature/MEDIA-1068
  feature/MEDIA-1077
  feature/MEDIA-1080
  feature/MEDIA-1108
  feature/MEDIA-1302
  feature/MEDIA-1570
  feature/MEDIA-1603
  feature/MEDIA-1604
  feature/MEDIA-1607
  feature/MEDIA-1609
  feature/MEDIA-1920
```

2. 검색 패턴으로 한번에 브랜치를 삭제하기

`xargs` 명령어는 앞 명령어의 출력 결과를 다음 명령어의 인자로 넘겨주는 명령어 입니다. 

```bash
$ git branch | grep "MEDIA-1" | xargs git branch -D
Deleted branch deploy/MEDIA-1078 (was f21fb73ce).
Deleted branch deploy/MEDIA-1210 (was d8918276b).
Deleted branch feature/MEDIA-1068 (was e5c3e4d6b).
Deleted branch feature/MEDIA-1077 (was f0d955e01).
Deleted branch feature/MEDIA-1080 (was bd67c3303).
Deleted branch feature/MEDIA-1108 (was 7195cace2).
Deleted branch feature/MEDIA-1302 (was e692c3c2e).
Deleted branch feature/MEDIA-1570 (was 91feff2cb).
Deleted branch feature/MEDIA-1603 (was 0c7e10bb3).
Deleted branch feature/MEDIA-1604 (was de8314a18).
Deleted branch feature/MEDIA-1607 (was b5c256f0b).
Deleted branch feature/MEDIA-1609 (was 47fab1d1f).
Deleted branch feature/MEDIA-1920 (was 6de1e07e7).
```

# 참고

* git branch 
  * https://medium.com/@rajsek/deleting-multiple-branches-in-git-e07be9f5073c
* xargs
  * https://rsec.kr/?p=91
