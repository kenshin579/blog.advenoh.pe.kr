---
title: "M1 맥북에서 Memongo 실행하기"
description: "M1 맥북에서 Memongo 실행하기"
date: 2023-02-25
update: 2023-02-25
tags:
  - m1
  - mac
  - mongo
  - mongodb
  - go
  - golang
  - 몽고
  - 맥북
  - memongo
---

M1 맥북 + `golang` + `memongo` 조합으로 개발하고 있다면 아래와 같은 오류 메시지를 보게 되고 어떻게 해결하면 되는지 검색하게 된다. 팀에 새로운 분들이 올 때마다 설정하는 방법을 까먹게 되어 다시 정리해둔다.

`memongo`를 M1에서 실행하면 아래와 같이 `memongo`를 다운로드하는 과정에서 시스템 아키텍처가 맞지 않다고 오류 메시지를 던지고 실행이 안 되는 것을 볼 수 있다.

```bash
=== RUN   TestMongoTestSuite
{"time":"2023-02-25T17:15:24.374615+09:00","level":"FATAL","prefix":"-","file":"db.go","line":"17","message":"memongo does not support automatic downloading on your system: your architecture, arm64, is not supported"}

```

해결책은 2가지가 있고 개인적으로 매번 옵션을 기억해서 하기보다는 그냥 기본 설정은 두고 다운로드한 MongoDB binary를 사용하도록 하는 게 조금 더 편한듯해서 2번 방식으로 실행하는 것을 추천한다.

## 1.Memongo 옵션 설정

`arm64` 아키텍처일때 다운로드해야 하는 URL을 넣는 방법으로 M1에서 실행시킬 수 있다.

```go
opts := &memongo.Options{
		ShouldUseReplica: true,
		MongoVersion:     "4.2.1",
		LogLevel:         2,
	}

	if runtime.GOARCH == "arm64" {
		if runtime.GOOS == "darwin" {
			// Only set the custom url as workaround for arm64 macs
			opts.DownloadURL = "https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-4.2.1.tgz"
		}
	}

	mongoServer, err := memongo.StartWithOptions(opts)
```



## 2.Custom MongoDB binary 사용

MongoDB binary를 다운로드하고 환경변수, `MEMONGO_MONGOD_BIN`, `PATH` 값을 설정해주면 다운로드하지 않고 이미 설치된 binary를 사용하도록 할 수 있다. 혹시 실행 시 문제가 발생하는 경우에는 아주 가끔 `pkill`로 `mongod`를 kill 해줘야 하는 경우도 있다.

brew로 mongodb를 설치한다.

```bash
$ brew tap mongodb/brew
$ brew update
$ brew install mongodb-community@4.2
```

MongoDB 가 잘 설치되어 있는지 확인한다.

```bash
$ mongo --version
MongoDB shell version v4.2.21
git version: b0aeed9445ff41af07449fa757e1f231bce990b3
allocator: system
modules: none
build environment:
    distarch: x86_64
    target_arch: x86_64
```

사용 중인 shell의 설정값에 필요한 환경 변수를 추가한다. 참고로 GoLand에서 실행하는 거면 shell 설정 수정 이후 애플리케이션을 다시 시작해줘야 한다.

```bash
$ vim ~/.zshrc
export MEMONGO_MONGOD_BIN=/opt/homebrew/opt/mongodb-community@4.2/bin/mongod
export PATH=$PATH:/opt/homebrew/opt/mongodb-community@4.2/bin
```



다시 [memongo_test.go](https://github.com/kenshin579/tutorials-go/blob/master/go-memongo/memongo_test.go)를 실행해보면 잘 실행되는 걸 확인할 수 있다.

```bash
=== RUN   TestMongoTestSuite
[memongo] [INFO]  Starting MongoDB with options &memongo.Options{ShouldUseReplica:true, Port:57585, CachePath:"", MongoVersion:"4.2.1", DownloadURL:"", MongodBin:"/opt/homebrew/opt/mongodb-community@4.2/bin/mongod", Logger:(*log.Logger)(nil), LogLevel:0, StartupTimeout:10000000000, Auth:false}
--- PASS: TestMongoTestSuite (2.21s)
=== RUN   TestMongoTestSuite/TestQuery
[{_id ObjectID("63f9c767d1ef4a0debb6f01a")} {type Oolong} {rating 7} {vendor [C]}]
    --- PASS: TestMongoTestSuite/TestQuery (0.00s)
PASS
```



## 참고

- https://www.mongodb.com/docs/v4.2/tutorial/install-mongodb-on-os-x/
- https://github.com/nodkz/mongodb-memory-server/issues/422
- https://github.com/benweissmann/memongo
- https://github.com/tryvium-travels/memongo
