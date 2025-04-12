---
title: "Git 서브모듈이란? 실전 예제로 배우는 서브모듈 활용법"
description: "Git 서브모듈이란? 실전 예제로 배우는 서브모듈 활용법"
date: 2025-04-03
update: 2025-04-03
tags:
  - git
  - git submodule
  - 깃 서브모듈
  - 서브모듈
---

## 1. 개요

### Git 서브모듈이란?

`Git` 서브모듈(Git Submodule)은 하나의 `Git` 저장소 내에 다른 `Git` 저장소를 포함할 수 있도록 해주는 기능이다. 이를 통해 별도의 저장소를 독립적으로 관리하면서도, 특정 프로젝트 내에서 재사용할 수 있다.

### 왜, 언제 사용하나?

- **코드 재사용**: 여러 프로젝트에서 동일한 라이브러리나 공통 코드베이스를 유지해야 할 때 유용하다
- **독립적인 버전 관리**: 서브모듈은 독립적으로 관리되므로, 메인 프로젝트와 별개로 버전 컨트롤을 할 수 있다
- **공유 및 협업**: 팀 내에서 공통 모듈을 여러 프로젝트에 걸쳐 사용해야 할 경우 편리하다

### 어떻게 사용하나?

`Git` 서브모듈을 사용하면, 하나의 Git 저장소 내에서 별도의 저장소를 포함하고 관리할 수 있다. 기본적으로 다음과 같은 과정을 거친다:

1. 서브모듈 추가
2. 서브모듈을 포함한 저장소 사용
3. 서브모듈 업데이트 및 유지 관리
4. 서브모듈 삭제

------

## 2. 서브모듈 사용해보기

### 2.1 메인 Repo에 서브모듈 Repo 포함시키기

`Git` 서브모듈을 추가하려면 다음 명령어를 실행한다.

```bash
> cd main-repo

# 서브모듈 추가
> git submodule add <https://github.com/kenshin579/submodule-repo.git> submodule
Cloning into '/Users/user/GolandProjects/main-repo/submodule'...
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 11 (delta 0), reused 6 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (11/11), done.
```

위 명령어를 실행하면, 서뷰모듈이 현재 디렉토리에 포함이 된다. 서브모듈을 추가하면 `.gitmodules` 파일이 생성된다. 이 파일에는 서브모듈에 대한 정보가 포함되어 있다.

```
[submodule "submodule"]
	path = submodule
	url = <https://github.com/kenshin579/submodule-repo.git>
```

이 파일은 메인 저장소가 서브모듈을 어떻게 참조해야 하는지 정의한다.

### 2.2 서브모듈을 포함한 Repo 사용해보기

기본적으로 `Git` 저장소를 클론하면 서브모듈은 자동으로 클론되지 않는다. 서브모듈까지 함께 가져오려면 다음과 같이 실행한다.

```bash
> git clone --recursive <https://github.com/kenshin579/main-repo.git>
Cloning into 'main-repo'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 10 (delta 0), reused 6 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (10/10), done.
Submodule 'submodule' (<https://github.com/kenshin579/submodule-repo.git>) registered for path 'submodule'
Cloning into '/Users/user/src/main-repo/submodule'...
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 11 (delta 0), reused 6 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (11/11), done.
Submodule path 'submodule': checked out '988b35283f2d7b7ed93c552e7ae50f4fdd5adb7d'

> cd main-repo
> tree
.
├── README.md
└── submodule
    ├── README.md
    └── submodule-file.txt

2 directories, 3 files
```

만약 `--recursive` 옵션 없이 클론했다면, 서브모듈을 수동으로 초기화하고 업데이트해야 한다.

```bash
> git submodule update --init --recursive
```

### 2.3 서브모듈 최신 코드 다운로드 받아보기

서브모듈에서 새로운 파일을 추가하고 커밋한 후 푸시한다.

```bash
> cd submodule
> echo "New content" > new-file.txt
> git add new-file.txt
> git commit -m "Add new file"
> git push origin main
```

서브모듈이 업데이트되었으므로, 메인 저장소에서도 최신 코드를 받아야 한다.

```bash
> cd main-repo
> git submodule update --remote
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 1), reused 3 (delta 1), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 1.18 KiB | 402.00 KiB/s, done.
From <https://github.com/kenshin579/submodule-repo>
   48e49d4..5419b0a  chores     -> origin/chores
   988b352..d5f4a06  main       -> origin/main
Submodule path 'submodule': checked out 'd5f4a065378f733945944cca2815116c1cece8e9'
```

서브모듈이 최신 상태로 업데이트된 것을 확인할 수 있다.

### 2.4 메인 Repo에서 서브모듈 제거하기

서브모듈을 제거하려면 다음 단계를 수행하면 된다.

```bash
# .gitmodule에서 참고하는 sumobule 제거
> git submodule deinit -f path/to/submodule

# submoudle 폴더 삭제
> git rm --cached path/to/submodule
> rm -rf .git/modules/path/to/submodule

# commit changes
> git commit -m "Removed submodule"
> git push origin main
```

## 3. 마무리

`Git` 서브모듈은 하나의 프로젝트에서 별도의 `Git` 저장소를 효과적으로 관리할 수 있는 강력한 기능이다. 하지만 서브모듈을 사용할 때는 다음과 같은 점을 유의해야 한다.

- 서브모듈은 독립적인 저장소이므로, 별도로 업데이트해야 한다
- `--recursive` 옵션 없이 클론하면 서브모듈이 포함되지 않으므로 초기화 과정이 필요하다
- 서브모듈을 제거할 때는 `.gitmodules` 파일과 `.git/modules` 디렉토리를 정리해야 한다

이 가이드를 참고하여 `Git` 서브모듈을 효과적으로 활용해보세요!

> 참고로 예제로 작성한 건 아래 github에서 확인할 수 있습니다
> - [main-repo](https://github.com/kenshin579/main-repo)
> - [submodule-repo](https://www.notion.so/Git-1ca46a2166e380068207d9c29824569a?pvs=21)

## 4. 참고

- [Git 도구  - 서브모듈](https://git-scm.com/book/ko/v2/Git-도구-서브모듈)
- [Git submodules](https://www.atlassian.com/ko/git/tutorials/git-submodule)
- [Git Submodule 사용하기](https://devocean.sk.com/blog/techBoardDetail.do?ID=165172&boardType=techBlog)

