---
title: "Gitbook으로 전자책 만들어보기"
description: "Gitbook으로 전자책 만들어보기"
date: 2018-07-29
update: 2018-07-29
tags:
  - gitbook
  - pdf
  - epub
  - kindle
  - git
  - github
  - 전자책
---

## 1. 개요

요즘은 콘텐츠 시대라고 해도 과언이 아닙니다. 특정 방송 회사가 콘텐츠를 만들기보다 개인이 직접 좋은 콘텐츠를 만들어 유튜브와 같은 플랫폼에서 퍼블리쉬하는 시대로 바뀌었습니다. [리디북스](https://ridibooks.com/?genre=general) 와 같은 eBook 리더기가 보급되고 점점 활성화되면서 eBook 시장에도 개인이 직접 책을 만들 수 있는 여러 도구와 플랫폼이제공되고 있습니다.

- 애플
    - [iBooks Author](https://www.apple.com/kr/ibooks-author/)
- 한글과 컴퓨터
    - [의퍼블](https://www.hancom.com/product/productWepublMain.do) (WePubl)
- 교보 문고
    - [PubPle](http://pubple.kyobobook.co.kr/)

본 포스트에서는 마크다운 기반의 전자책 집필 시스템인 GitBook에 대해서 알아봅시다.

### 1.1 주요 기능

- Markdown 언어로 집필 (ex. AsciiDoc, Markdown)
- GitHub 저장소와 프로젝트를 연동하여 저장 가능
- GitBook Editor 지원 - 웹, GUI(legacy 버전)
- 여러 전자책 포멧 지원 (ex, PDF, EPUB, MOBI)
- 여러 플러그인 지원 (ex. etoc, splitter)

## 2. Gitbook 설치

설치 방법은 맥 OS 기반으로 작성되었습니다. GitBook을 설치 하기 위해는 NodeJS가 기본적으로 설치되어 있어야 합니다. 없는 경우에는 아래 명령어로 설치합니다.

```bash
$ brew install nodejs
```

NPM를 통해 gitbook 패키지를 설치합니다.

```bash
$ npm install gitbook-cli -g
$ gitbook --version
```

전자책 포맷과 PDF를 생성하려면 ebook-convert 명령어가 필요합니다.

```bash
$ brew cask install calibre
```

\$PATH 환경변수에 /usr/local/bin 폴더가 포함되어 있어야 합니다.

## 3. 사용방법

### 3.1 첫 GitBook 프로젝트 만들기

아래 명령어로 책의 boilerplate를 생성합니다. 기본적으로 README.md와 SUMMARY.md가 생성됩니다.

```bash
$ gitbook init
```

기본적인 boilerplate 대신 조금 더 구체적인 예를 보고 싶으면 아래 github에서 샘플 예제를 다운로드해서 실행해보세요.

```bash
$ git clone https://github.com/kenshin579/app-korean-catholic-bible.git
$ cd app-korean-catholic-bible/example/gitbook_markup_sample
```

아래 명령어로 웹사이트를 생성하여 브라우저에서도 볼 수 있습니다.

```bash
$ gitbook serve
```

![](image_3.png)

![](image_4.png)

### 3.2 eBooks과 PDF 생성하기

여러 전자책 포맷으로 출력할 수 있습니다.

```bash
$ gitbook pdf ./ ./mybook.pdf
$ gitbook epub ./ ./mybook.epub
$ gitbook mobi ./ ./mybook.mobi
```

![](image_5.png)

![](image_1.png)

## 4. 플러그인

GitBook의 여러 기능을 확장해주는 플러그인을 제공합니다. 어떤 플러그인은 있는지 찾는 방법과 설치 방법을 알아봅시다.

### 4.1 플러그인 찾는 방법

[gitbook 플러그인 사이트](http://plugins.gitbook.com) 에서 원하는 기능을 가진 플러그인을 검색할 수 있습니다.

### 4.2 플로그인 설정 및 설치

루트 디렉터리에 있는 book.json 파일에 원하는 플러그인을 추가하고 필요하면 각 플러그인에 대한 설정도 같이해줍니다.

```bash
$ vi book.json
```

```json
[
  {
    "plugins": ["myPlugin", "anotherPlugin"]
  },
  {
    "pluginsConfig": {
      "myPlugin": ""
    }
  }
]
```

설정이후 추가한 플러그인을 아래 명령어로 설치합니다.

```bash
$ gitbook install
```

### 4.3 추천 플러그인

- etoc : 페이지에서 내용의 Table of Content를 자동으로 만들어주는 기능
    - [https://plugins.gitbook.com/plugin/etoc](https://plugins.gitbook.com/plugin/etoc)
- splitter : 메뉴와 내용 중간 spliter를 움직이도록 해주는 기능
    - [https://www.npmjs.com/package/gitbook-plugin-splitter](https://www.npmjs.com/package/gitbook-plugin-splitter)
- expandable-chapters-small : > icon이 추가되어 클릭하면 확장되고 다시 클릭하면 축소되는 기능
    - [https://plugins.gitbook.com/plugin/expandable-chapters-small](https://plugins.gitbook.com/plugin/expandable-chapters-small)
    - ![](image_6.png)

- toggle-chapters : 한 chapter를 클릭하면 해당 chapter는 확장되고 나머지는 축소되는 기능
    - [https://plugins.gitbook.com/plugin/toggle-chapters](https://plugins.gitbook.com/plugin/toggle-chapters)
    - ![](toggle_chapters.gif)

## 5. FAQ

- 루트 디렉터리에 있는 README.md은 GitHub에서도 같이 사용된다. GitBook에서 다른 README.md로 설정하려면 어떻게 해야 하나?
    - book.json를 아래와 같이 수정한다.

```bash
$ vi book.json
```

```json
"structure" : {
  "readme": "INTRO.md"
}
```

## 6. GitBook Pages Examples

대학에서나 개인 사이트로 GitBook을 많이 사용하고 있습니다. 아래 예제들을 통해서 어떤 다양한 플러그인을 사용하고 GitBook을 어떻게 꾸몄는지 알아보면 좋을 것 같습니다.

- [https://www.gitbook.com/book/jackdougherty/datavizforall](https://www.gitbook.com/book/jackdougherty/datavizforall)
- [https://typescript-kr.github.io/](https://typescript-kr.github.io/)

## 7. 참조 자료

- [https://help.gitbook.com/](https://help.gitbook.com/)
- [https://toolchain.gitbook.com/](https://toolchain.gitbook.com/)
- [https://lab021.gitbooks.io/lab021_manual/gitbook%EC%9D%80-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%82%98%EC%9A%94.html](https://lab021.gitbooks.io/lab021_manual/gitbook%EC%9D%80-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%82%98%EC%9A%94.html)
- [http://blog.appkr.kr/work-n-play/pandoc-gitbook-%EC%A0%84%EC%9E%90%EC%B6%9C%ED%8C%90/](http://blog.appkr.kr/work-n-play/pandoc-gitbook-%EC%A0%84%EC%9E%90%EC%B6%9C%ED%8C%90/)
