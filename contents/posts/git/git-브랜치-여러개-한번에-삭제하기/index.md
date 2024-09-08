---
title: "Git 브랜치 여러 개 한번에 삭제하기"
description: "Git 브랜치 여러 개 한번에 삭제하기"
date: 2020-07-11
update: 2020-07-11
tags:
  - git
  - github
  - branch
  - multiple
  - delete
  - 깃
  - 깃허브
  - 다중
  - 삭제
  - 브랜치
---

Git local, remote 브랜치를 한번에 삭제하는 방법에 대해서 알아보자.

## 1. 다중 Local 브랜치 삭제하기

### 1.1 삭제하려는 브랜치 목록보기

`grep` 명령어로 삭제하려는 브랜치 목록을 확인한다.

```bash
$ git branch | grep "MEDIA-1"
  deploy/MEDIA-1078
  deploy/MEDIA-1210
  feature/MEDIA-1068
```

### 1.2 검색 패턴으로 한번에 브랜치를 삭제하기

`grep`으로 찾은 브랜치를 `xargs` 명령에 pipeline으로 넘겨줘서 삭제한다.

> `xargs` 명령어는 앞 명령어의 출력 결과를 다음 명령어의 인자로 넘겨주는 명령이다.

```bash
$ git branch | grep "MEDIA-1" | xargs git branch -D
Deleted branch deploy/MEDIA-1078 (was f21fb73ce).
Deleted branch deploy/MEDIA-1210 (was d8918276b).
Deleted branch feature/MEDIA-1068 (was e5c3e4d6b).
```

## 2. 다중 Remote 브랜치 삭제하기

### 2.1 Remote 브랜치 목록 확인하기

Remote 브랜치도 같은 원리로 삭제할 수 있다. git의 `-r` (`--remotes`) 옵션으로 Remote 브랜치의 목록을 확인할 수 있다.

```bash
$ git branch -r | grep -Eo 'greenkeeper/.*'
greenkeeper/monorepo.gatsby-20190320034241
greenkeeper/monorepo.gatsby-20190322142727
greenkeeper/monorepo.gatsby-20190322145441
```

### 2.2 Remote 브랜치 다중 삭제하기

검색 패턴으로 찾은 브랜치를 xargs로 하나씩 삭제한다.

`git push origin :branch-to-delete` 명령어는 local 브랜치가 삭제되고 remote 브랜치도 삭제할 때 사용한다.

```bash
$ git branch -r | grep -Eo 'greenkeeper/.*' | xargs -I {} git push origin :{} 
To https://github.com/kenshin579/advenoh.pe.kr.git
 - [deleted]         greenkeeper/monorepo.gatsby-20190320034241
To https://github.com/kenshin579/advenoh.pe.kr.git
 - [deleted]         greenkeeper/monorepo.gatsby-20190322142727
To https://github.com/kenshin579/advenoh.pe.kr.git
 - [deleted]         greenkeeper/monorepo.gatsby-20190322145441
```

## 3. 참고

* git branch
    * https://medium.com/@rajsek/deleting-multiple-branches-in-git-e07be9f5073c
    * https://stackoverflow.com/questions/10555136/delete-multiple-remote-branches-in-git
    * https://www.educative.io/edpresso/how-to-delete-remote-branches-in-git
    * https://trustyoo86.github.io/git/2017/11/28/git-remote-branch-create.html
* xargs
    * https://rsec.kr/?p=91
