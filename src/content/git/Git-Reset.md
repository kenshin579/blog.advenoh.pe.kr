---
title: 'Git Reset으로 커밋된 내용 다시 되돌리기'
layout: post
category: 'git'
author: [Frank Oh]
tags: ["git", "reset", "revert", "깃", "깃허브", "리셋"]
image: ../img/cover-git.png
date: '2020-01-02T22:43:23.000Z'
draft: false
---

Git으로 작업하보면 커밋된 이력을 다시 되돌려야 할 때가 종종 발생한다. Git Reset



# 1.Git Reset

## 1.1 Git Reset 종류
- - soft

  - - 

  - mixed (기본)

  - - 내가 수정한 건 남이 있음
    - staging area를 비우기까지 함
    - giit commit 뒤돌리고
    - git add 명령까지 되돌린다

  - hard

  - - 내가 수정한 데이터도 지워짐
    - mixed + working directory에서 작업한 내용도 다 되돌린다

## 1.2 Git Reset 해보기

HEAD 기준으로 하는 방법, commit 값으로... 

```bash
$ git reset <>
```



### 1.2.1 Soft Reset

### 1.2.2 Mixed Reset (기본)

### 1.2.3 Hard Reset



# 참고

- [https://www.devpools.kr/2017/02/05/%EC%B4%88%EB%B3%B4%EC%9A%A9-git-%EB%90%98%EB%8F%8C%EB%A6%AC%EA%B8%B0-reset-revert](https://www.devpools.kr/2017/02/05/초보용-git-되돌리기-reset-revert)/
- https://backlog.com/git-tutorial/kr/stepup/stepup6_3.html
- [https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Reset-%EB%AA%85%ED%99%95%ED%9E%88-%EC%95%8C%EA%B3%A0-%EA%B0%80%EA%B8%B0](https://git-scm.com/book/ko/v2/Git-도구-Reset-명확히-알고-가기)
- https://opentutorials.org/module/4032/24533
- https://c10106.tistory.com/3930
- https://antilog.tistory.com/33

