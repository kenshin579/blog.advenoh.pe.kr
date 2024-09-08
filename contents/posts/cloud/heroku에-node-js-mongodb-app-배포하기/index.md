---
title: "Heroku에 Node.js+MongoDB App 배포하기"
description: "Heroku에 Node.js+MongoDB App 배포하기"
date: 2018-08-21
update: 2018-08-21
tags:
  - heroku
  - node
  - 하루쿠
  - 클라우드
  - 노드
  - 몽고
  - 배포
  - 가상화
  - mongo
  - mongodb
  - vm
  - virtualization
  - cloud
---

## 1. Heroku란

헤로쿠(Heroku)는 [PaaS](https://blogs.msdn.microsoft.com/eva/?p=1383)(Platform as a Service)형태의 클라우드 서비스입니다. 헤로쿠는 터미널이나 웹에서 필요한 여러 티어(ex. DB)를 쉽게 생성하고 연동시킬 수 있습니다. 최초 버전에서는 Ruby 언어만 지원하였지만, 현재는 메이저급 언어 대부분을 지원하고 있습니다.

### 1.1 Heroku Features

* Git 명령어로 앱을 배포함
* 앱 배포 시 경량 가상화 컨테이너인 Dynos에서 실행됨
* 여러 언어를 지원함 (Ruby, Java, Node.js, Scala, Clojure, Python, Php, Go)
* 애드온(Add-ons)
    * DB와 같은 여러 백엔드 서비스를 제공함(ex. redis, mongodb, mysql)
    * Elements 마켓장소에서 필요한 애드온을 찾아 설치할 수 있음

* 구독 가격
    * 무료
        * 공짜 Dyno 시간이 주어짐(ex. 기본 550 hrs부터 시작)
        * 30분 동안 사용하지 않는 경우에는 sleep 모드로 전환됨
        * 재 접속시에는 wakeup하는 시간으로 응답시간이 늦어질 수 있음

    * 유료 - 3가지 구독 서비스가 있음

## 2. Heroku 시작하기

### 2.1 Heroku 계정 만들기

먼저 [Heroku](http://www.heroku.com/) 사이트에 들어가 계정을 만들어야 합니다.

### 2.2 Heroku CLI 설치

터미널에서 Heroku 앱을 관리할 수 있도록 Heroku CLI (Command Line Interface)를 설치합니다. 이 포스팅에서는 맥 기반으로 설명되어 있습니다. 그외에 OS는 [Heroku 설치 가이드](https://devcenter.heroku.com/articles/heroku-cli)를 참조해주세요.

```bash
$ brew install heroku
$ heroku --version
heroku/7.7.10 darwin-x64 node-v10.8.0
```

### 2.3 Heroku 로그인

Heroku관련 작업을 하려면 먼저 로그인 명령어로 Heroku 계정에 로그인해야 합니다.

```bash
$ heroku login
```

![Heroke 로그인](7D19A750-9227-4555-A898-E1E87BAB3565.png)

### 2.4 필수 명령어

Heroku를 배포할때 git를 사용하기 때문에 git가 있어야 합니다. 맥 OS에서는 Xcode가 설치되어 있으면 기본적으로 터미널에서 사용할 수 있습니다.

```bash
$ git --version
git version 2.15.2 (Apple Git-101.1)
```

## 3. Sample 코드 생성, 코드 수정 및 배포

실제 개발과정을 보면 처음에 프로젝트 생성한 이후 코드 수정, 개발환경에서의 테스트, 서버로 배포하는 이런 과정을 계속 반복하게 됩니다. Heroku 클라우드에 개발하는 코드 어떻게 쉽게 반영할 수 있는지 알아보죠.

### 3.1 Sample 프로젝트 생성

Heroku에서 기본적으로 제공하는 샘플 프로젝트를 다운로드합니다.

```bash
$ mkdir -p ~/src
$ cd src
$ git clone https://github.com/heroku/node-js-getting-started.git
$ cd node-js-getting-started
```

### 3.2 개발환경에서 실행하기

앱에 필요한 Node.js 모듈를 설치하고 앱을 구동해보죠.

```bash
$ npm install
$ npm start
```

![Sample WebApp](image_13.png)

### 3.3 Heroku 클라우드에 배포하기

```bash
$ heroku create
Creating app... done, ⬢ nameless-falls-97478
https://nameless-falls-97478.herokuapp.com/ | https://git.heroku.com/nameless-falls-97478.git
```

먼저 create 명령어로 Heroku에 관련 Git 저장소와 빈 앱을 생성합니다.

* 앱 주소
    * [https://nameless-falls-97478.herokuapp.com/](https://nameless-falls-97478.herokuapp.com/)

* Heroke Git 저장소
    * [https://git.heroku.com/nameless-falls-97478.git](https://git.heroku.com/nameless-falls-97478.git)

create 옵션에 이름을 지정하지 않으면 임의의 이름(ex. 여기서는 nameless-falls-97478로 생성)으로 생성합니다. 앱 생성 이후에도 apps:rename 옵션으로 앱 이름 변경이 가능합니다.

```bash
$ heroku apps:rename newname
```
이제 실제로 Heroku 클라우드에 배포해보죠. Git 명령어로 Heroku 저장소에 푸시하면 배포가 완료됩니다. 참 쉽죠? ㅋㅋ

```bash
$ git push heroku master
```

![Heroku Cloud에 배포하기](image_9.png)

소스가 올라가면 빌드 과정을 거치고 공개 주소에 접속해 웹 앱에 접속할 수 있습니다. 빌드 과정이후 Heroku에서 웹 앱을 시작하는 시작점은 Procfile 파일에 정의되어 있습니다.

```bash
$ cat Procfile
web: node index.js
```

Procfile이 없은 경우에는 package.json에 정의된 start script로 시작합니다.

## 3.3 배포된 사이트 오픈하기

잘 배포되었는지 브라우저에서 확인해봅니다. 브라우저가 오픈되고 공개 주소로 접속되고 페이지가 정상적으로 로드되는 것을 볼수 있습니다.

```bash
$ heroku open
```

![배포된 사이트 오픈하기](F8ADA800-156E-4335-BF77-EF1811E865EE.png)

### 3.4 코드 수정이후 다시 배포하기

이제 코드 수정한 이후에 다시 배포하는 과정을 거쳐보죠. 메인 페이지 (views/pages/index.ejs)에서 타이틀 부분을 수정합니다.

![WebApp 수정하기](image_7.png)

로컬환경에서 수정이 잘됐는지 확인 이후 이상없으면 코드를 commit합니다.

```bash
$ npm start
$ git add .
$ git commit -m “Update index.”
[master cd8508b] Update index.
2 files changed, 1003 insertions(+), 1 deletion(-)
create mode 100644 package-lock.json
```

Heroku에 배포하고 반영 잘됐는지 브라우저를 오픈해서 확인합니다. 변경한 타이틀이 잘 로드가 되네요.

```bash
$ git push heroku master
$ heroku open
```

![Sample WebApp](D9D5222B-0850-42E7-A92E-844DDE63B0B0.png)

웹 앱이 Heroku에서 구동될 때 로그를 확인하고 싶으면, logs 옵션으로 확인이 가능합니다.

```bash
$ heroku logs --tail
```

![Heroku Log](A925BBD7-96F3-4F38-9F0C-DB2A6B7492F5.png)

## 4. Add-on MongoDB 설치후 Node.js와 연동하기

Add-on 마켓장소에는 많은 수의 데이터 저장소(ex. Postgres, Redis, MongoDB, MySQL)를 지원하고 있습니다. 이 예제에서는 MongoDB add-on을 설치하고 작성하고 있는 Node.js와 연동하는 부분을 다루어 보도록 하겠습니다.

### 4.1 MongoDB 설치

MongoDB add-on을 추가합니다.

```bash
$ heroku addons:create mongolab
```

![MongoDB Add-On 설치](image_8.png)

명령어외에도 [직접 마켓장소](https://elements.heroku.com/addons)에서 접속해서 add-on을 추가할 수 있습니다.

![Heroku Add-ons Site](image_5.png)

### 4.2 MongoDB와 연동

mLab MongoDB를 추가하면 Heroku 환경변수에 MONGODB_URI가 추가됩니다. MongoDB 주소는 아래와 같습니다.

```bash
$ heroku config:get MONGODB_URI
mongodb://heroku_vfwj5vcl:spb8kerqhucborfd974cdbiqe8@ds125862.mlab.com:25862/heroku_vfwj5vcl
```

명령어로 MongoDB에 접속할 수도 있지만, 개인적으로 MongoDB GUI client(Studio 3T)로 접속해보았습니다. 아래는 Studio 3T에서 새로운 연결 정보를 입력하는 화면입니다.

![MongoDB Studio 3T](5926F9E1-214D-483F-AA14-2A078EB229B7.png)

DB에 연결이후 앱에 필요한 데이터를 입력합니다. dummy 데이터로는 기존에 작성된 데이터를 사용하였습니다. ([데이터 링크](https://github.com/kenshin579/app-keep-countdown-timer/blob/master/data/data.json))

```json
db.timers.insert([
{
  "timer_description": "한글 단어 공부",
  "timer_interval": {
    "hours": 0,
    "minutes": 30
  },
  "timer_total": {
    "hours": 2,
    "minutes": 30,
    "seconds": 30
  },
  "timer_status": true,
  "start_date": "2017-04-01"
},
…
]
```

### 4.3 코드 수정

앞서 MongoDB에 입력한 데이터를 브라우저에서 /timers에 접속시 json값을 가져오는 코드를 작성해보도록 하겠습니다. 먼저 MongoDB를 Node.js에서 사용하기 위해서는 mongoose 모듈이 필요합니다. Npm 명령어로 mongoose 모듈를 설치합니다.

```bash
$ npm install --save mongoose
```

앱에서 MongoDB로 접속하는 데 필요한 파일을 생성하고 기존 코드를 수정합니다. 원하는 document 구조에 맞게 schema 파일을 생성합니다.

```bash
$ mkdir -p models
$ vim models/timer.js
```

```javascript
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const timerSchema = new Schema({
    timer_description: {
        type: String, unique: true
    },
    timer_interval: {
        hours: {type: Number},
        minutes: {type: Number}
    },
    timer_total: {
        hours: {type: Number},
        minutes: {type: Number},
        seconds: {type: Number}
    },
    timer_status: {
        type: Boolean
    },
    start_date: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('timer', timerSchema);
```

메인 index.js 파일을 수정합니다. RESTful API /timers 접속 시 모든 데이터를 조회 가능하도록 구현합니다.

```bash
$ vim index.js
```

```javascript

const express = require('express')
const path = require('path')
const PORT = process.env.PORT || 5000
const mongoose = require('mongoose');

// CONNECT TO MONGODB SERVER
MONGODB_URI='mongodb://heroku_vfwj5vcl:spb8kerqhucborfd974cdbiqe8@ds125862.mlab.com:25862/heroku_vfwj5vcl'
mongoose.connect(MONGODB_URI);

// DEFINE MODEL
const Timers = require('./models/timer');

express()
  .use(express.static(path.join(__dirname, 'public')))
  .set('views', path.join(__dirname, 'views'))
  .set('view engine', 'ejs')
  .get('/', (req, res) => res.render('pages/index'))
  .get('/timers', (req, res) => {
    Timers.find((err, timers) => {
      if(err) return res.status(500).send({error: 'database failure'});
      res.json(timers);
    })
  })
  .listen(PORT, () => console.log(`Listening on ${ PORT }`))
```

지금까지 작성한 코드는 [github](https://github.com/kenshin579/blog-node-js-getting-started.git)에 업로드 되어 있습니다.

### 4.4 재배포 확인

다시 Heroku에 배포하고 확인해보죠.

```bash
$ npm start
$ git add .
$ git commit -m "added mongodb code"
[master 0bf189b] added mongodb code
  5 files changed, 194 insertions(+), 1 deletion(-)
  create mode 100644 models/timer.js

$ git push heroku master
$ heroku open 
```

![Heroku WebApp](image_14.png)

## 5. Appendix

### 5.1 기존 App Heroku에 배포하기

기존에 작성한 Node.js 프로젝트에 Heroku를 배포해보았습니다. 실제 적용 과정은 위 샘플 프로젝트와 크게 다르지 않습니다.

* [https://github.com/kenshin579/app-keep-countdown-timer](https://github.com/kenshin579/app-keep-countdown-timer)

먼저 Procfile 파일 생성합니다.

```bash
$ vim Procfile
web: node app.js
```

create 명령어로 Heroku 앱을 생성합니다.

```bash
$ heroku create app-keep-countdown-timer
Creating ⬢ app-keep-countdown-timer... done
https://app-keep-countdown-timer.herokuapp.com/ | https://git.heroku.com/app-keep-countdown-timer.git
```

MongoDB add-on을 생성해서 주소를 얻어옵니다.

```bash
$ heroku addons:create mongolab
$ heroku config:get MONGODB_URI
```

새로 얻은 MongoDB 주소를 코드에 반영하고 MongoDB에 dummy 데이터를 로드합니다.

```bash
$ node data/populate.js
```

로컬 환경에서 이상이 없으면, commit해서 Heroku에 배포합니다.

```bash
$ git add .
$ git commit -m "added mongodb code"
[master 0bf189b] added mongodb code
 5 files changed, 194 insertions(+), 1 deletion(-)
 create mode 100644 models/timer.js

$ git push heroku master
$ heroku open 
```

![WebApp - Countdown Timer](image_3.png)

### 5.2 명령어 모음

이미 언급된 Heroku 명령어외에 사용시 알면 유용한 명령어를 모아 보았습니다.

* heroku run bash - 실행중인 app에 bash 실행한다

![Heroku CLI - run bash](image_4.png)

* heroku ps - 실행중인 process를 볼수 있습니다. 현재 남아 있는 dyno 시간도 알 수 있다

![Heroku CLI - ps](image_11.png)

* heroku list - Heroku으로 등록된 앱을 보여준다

![Heroku CLI - list](image_16.png)

* heroku ps:stop - 실행중인 app을 멈춘다

![Heroku CLI - ps:stop](image_10.png)

## 6. 참고

* IaaS, PaaS, SaaS
    * [https://blogs.msdn.microsoft.com/eva/?p=1383](https://blogs.msdn.microsoft.com/eva/?p=1383)

* Heroku Docs
    * [https://devcenter.heroku.com/categories/reference](https://devcenter.heroku.com/categories/reference)


