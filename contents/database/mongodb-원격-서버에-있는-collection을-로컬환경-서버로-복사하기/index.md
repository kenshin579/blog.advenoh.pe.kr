---
title: "Mongodb 원격 서버에 있는 Collection을 로컬환경 서버로 복사하기"
description: "Mongodb 원격 서버에 있는 Collection을 로컬환경 서버로 복사하기"
date: 2022-07-24
update: 2022-07-24
tags:
  - mongo
  - clone
  - backup
  - dump
  - import
---

개발 시 원격에 있는 데이터를 로컬환경에 그대로 복사해서 테스트할 필요가 종종 생긴다. [그전 포스팅](https://blog.advenoh.pe.kr/mongodb-collection-cloning하는-방법/)에서는 같은 서버에서 collection을 cloning 하는 방법에 대해서 알아보았다면, 이번에는 원격에서 로컬환경으로 cloning 하는 방법에 대해서 알아보자.

## 1.mongodump

`mongodump` 명령어는 `mongo` shell 명령어가 아니라 MongoDB 설치 시 같이 설치되는 command line 명령어이다. `mongodump`는 mongodb의 data를 export 해주는 도구이다.

- `--host` : 호스트 명
- `--por`t : 포터
- `-u` : 사용자
- `-p` : 암호
- `--db` : database 이름

```bash
$ mongodump --host remotehost --port 27017 -u username -p 'password' --db clone
2022-07-24T22:45:15.852+0900    writing clone.inventory to dump/clone/inventory.bson
2022-07-24T22:45:15.854+0900    writing clone.inventory3 to dump/clone/inventory3.bson
2022-07-24T22:45:15.857+0900    writing clone.inventoryclone to dump/clone/inventoryclone.bson
2022-07-24T22:45:15.862+0900    done dumping clone.inventoryclone (3 documents)
2022-07-24T22:45:15.862+0900    done dumping clone.inventory (3 documents)
2022-07-24T22:45:15.862+0900    done dumping clone.inventory3 (3 documents)
```

실행 후 백업되는 데이터는 `dump/database_이름` 폴더 안에 백업 파일이 생성된다.

```bash
$ cd dump/clone
$ ls 
inventory.bson               inventory.metadata.json      inventory3.bson              inventory3.metadata.json     inventoryclone.bson          inventoryclone.metadata.json
```

## 2.mongoimport

dump 뜬 데이터를 `mongoimport`로 로컬환경에 생성하려면 `mongoimport`를 사용하면 된다.

- `--uri` : mongodb 주소를 입력한다
- `-d` : database 이름
- `-c` : collection 이름

```bash
$ mongoimport --uri "mongodb://localhost:27017" -d clone2 -c inventory inventory.metadata.json
2022-07-24T22:56:53.354+0900    connected to: mongodb://localhost:27017
2022-07-24T22:56:53.381+0900    1 document(s) imported successfully. 0 document(s) failed to import.
```

## 정리

이미 파악한 분도 계시겠지만, mongodump, mongoimport 명령어를 사용하면 아래와 같이 여러 시스템으로 cloning이 가능해진다.

- 원격 서버 -> 로컬환경
- 원격 서버 -> 다른 원격 서버
- 로컬환경 -> 로컬환경

## 참고

- https://www.mongodb.com/docs/database-tools/mongodump/

  

  
