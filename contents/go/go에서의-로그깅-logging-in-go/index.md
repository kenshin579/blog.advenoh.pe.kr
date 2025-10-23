---
title: "Go에서의 로그깅 (Logging in Go)"
description: "Go에서의 로그깅 (Logging in Go)"
date: 2021-01-02
update: 2021-01-02
tags:
  - go
  - golang
  - log
  - logging
  - logger
  - logrus
  - 고
  - 고랭
  - 로그
  - 로깅
---

## 1. 들어가며

Go 표준 패키지 중에 log에서 로깅에 필요한 기본 메서드를 제공한다. 표준 출력 stdout, stderr외에 파일로 로그를 저장하는 방법, 그리고 로그 포맷 변경해서 출력하는 방법 등에 대해서 알아보자.

추가 설치 없이 log 패키지를 import 하면 바로 사용할 수 있다.

```go
import "log"
```

## 2. Log 패키지 사용방법

### 2.1 기본 Logger

log 패키지에서는 여러 Logger 지원을 위해 Logger 타입을 제공한다.

```go
type Logger struct {
   mu     sync.Mutex // ensures atomic writes; protects the following fields
   prefix string     // prefix on each line to identify the logger (but see Lmsgprefix)
   flag   int        // properties
   out    io.Writer  // destination for output
   buf    []byte     // for accumulating text to write
}

...생략...
var std = New(os.Stderr, "", LstdFlags) //<-- 이미 생성해 두고 있다. 
```

#### 2.1.1 기본 Logger로 화면에 로그찍기

`log.New()` 함수로 새로운 Logger를 생성할 수 있다. 하지만, 아래와 같이 별도 logger 생성 없이도 바로 사용이 가능하다. log 패키지에서 std 표준 Logger를 미리 생성해두기 때문이다.

```go
func Test_Basic_Logger(t *testing.T) {
	log.Println("Logging") //2020/12/30 10:27:11 Logging

```

`log.SetFlags(0)`을 지정하면 날짜/시간 포맷없이 메시지만 출력된다.

```go
func Test_Basic_Logger_Flags_Setting_DateTime_Display_X(t *testing.T) {
	log.SetFlags(0)
	log.Println("Logging") //Logging
}
```
여러 flag 옵션을 지정하여 log 포맷을 변경해보자. or 연산자를 이용해서 여러 옵션을 같이 지정한다. 아래와 옵션은 Prefix INFO도 추가하고 포멧은 날짜/시간외에 실행 파일도 출력하는 옵션이다.

```go
func Test_Basic_Logger_Flags_Setting2(t *testing.T) {
	log.SetFlags(log.Ldate | log.Ltime | log.Llongfile)
	log.SetPrefix("INFO: ")
	log.Println("Logging")

	//INFO: 2020/12/30 15:41:20 /Users/ykoh/GolandProjects/tutorials-go/go-logging/go_logging_test.go:23: Logging
}
```

여러 flag 옵션에 대한 설명은 [Go Docs](https://golang.org/pkg/log/#pkg-examples )을 참고해주세요.

```go
const (
   Ldate         = 1 << iota     // the date in the local time zone: 2009/01/23
   Ltime                         // the time in the local time zone: 01:23:23
   Lmicroseconds                 // microsecond resolution: 01:23:23.123123.  assumes Ltime.
   Llongfile                     // full file name and line number: /a/b/c/d.go:23
   Lshortfile                    // final file name element and line number: d.go:23. overrides Llongfile
   LUTC                          // if Ldate or Ltime is set, use UTC rather than the local time zone
   Lmsgprefix                    // move the "prefix" from the beginning of the line to before the message
   LstdFlags     = Ldate | Ltime // initial values for the standard logger
)
```

#### 2.1.2 파일로 쓰기

파일로 로그를 쓰기 위해서는 먼저 저장될 파일을 `os.OpenFile()`로 생성하고 파일 포인터를 `log.SetOutput()` 함수로 지정하면 `log.Println()` 사용시 파일로 쓰여지게 된다.

```go
func Test_Basic_Logger_File(t *testing.T) {
	logFile, err := os.OpenFile("logfile.txt", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		panic(err)
	}
	defer logFile.Close()

	log.SetOutput(logFile) //로그 출력 위치를 파일로 변경

	printMsgLog("test msg")
	log.Println("End of Program")
}
```

#### 2.1.3 화면과 파일에 동시에 로그 찍기

동시에 로그를 파일과 화면에 출력하도록 설정할 수도 있다. `io.MultiWriter()` 함수로 파일 포인터와 os.Stdout를 지정하여 복수 Writer를 생성하고 `log.SetOutput()`로 지정하면 복수 target으로 로그를 쓰게 된다.

```go
func Test_Multiple_Outputs(t *testing.T) {
   logFile, err := os.OpenFile("logfile.txt", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
   if err != nil {
      panic(err)
   }
   defer logFile.Close()

   multiWriter := io.MultiWriter(logFile, os.Stdout)
   log.SetOutput(multiWriter)

   printMsgLog("test msg")
   log.Println("End of Program")
}

func printMsgLog(msg string) {
   log.Print(msg)
}
```



### 2.2 Custom Logger

`log.New()` 함수로 Custom Logger를 생성해서 로그를 출력해보자.

```go
func New(out io.Writer, prefix string, flag int) *Logger {
	return &Logger{out: out, prefix: prefix, flag: flag}
}
```

`log.New()` 함수는 3가지 인자 값에 따라서 여러 Logger를 생성할 수 있다.

- 1st : 로그 output 지정
    - 표준콘솔출력(os.Stdout), 표준에러(os.Stderr), 파일포인터등을 지정할 수 있다
- 2nd : 로그 Prefix
    - 프로그래명, 카테고리등을 표시할 수 있다
- 3rd : 로그 포멧 설정 옵션

#### 2.2.1 Custom Logger 생성하기

아래 예제는 표준출력으로 로그를 보내는 logger를 만들어 로깅을 하는 코드이다. "INFO: "라는 prefix와 날짜/시간을 출력하는 Logger를 생성해서 출력한다.

```go
var logger *log.Logger

func Test_Custom_Logger(t *testing.T) {
   logger = log.New(os.Stdout, "INFO: ", log.LstdFlags)
   logger.Println("Logging") //INFO: 2020/12/30 10:34:00 Logging
}
```

#### 2.2.2 로그 파일로 쓰기

2.1.2에서와 같이 파일 Logger를 생성해서 로그를 파일로 쓰는 예제이다. `log.New()`의 첫번째 인자에 파일 포인터를 넘겨 파일로 출력한다.

```go
func Test_Custom_Logger_File(t *testing.T) {
   // 로그파일 오픈
   logFile, err := os.OpenFile("logfile.txt", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
   if err != nil {
      panic(err)
   }
   defer logFile.Close()

   logger = log.New(logFile, "INFO: ", log.Ldate|log.Ltime|log.Lshortfile)
   printMsgLogger("test msg")
   logger.Println("End of Program")
}

func printMsgLogger(msg string) {
	logger.Print(msg)
}

```



#### 2.2.3 여러 Logger 생성하는 예제

다음 예제는 여러 Logger 타입을 생성해서 출력하는 예제이다.

```go
type Logger struct {
   Trace *log.Logger
   Warn  *log.Logger
   Info  *log.Logger
   Error *log.Logger
}

var myLogger Logger

func logInit(traceHandle io.Writer, infoHandle io.Writer, warningHandle io.Writer, errorHandle io.Writer) {
   myLogger.Trace = log.New(traceHandle, "[TRACE] ", log.Ldate|log.Ltime|log.Lshortfile)
   myLogger.Info = log.New(infoHandle, "[INFO] ", log.Ldate|log.Ltime|log.Lshortfile)
   myLogger.Warn = log.New(warningHandle, "[WARNING] ", log.Ldate|log.Ltime|log.Lshortfile)
   myLogger.Error = log.New(errorHandle, "[ERROR] ", log.Ldate|log.Ltime|log.Lshortfile)
}

func Test(t *testing.T) {
   logInit(ioutil.Discard, os.Stdout, os.Stdout, os.Stderr)
   myLogger.Info.Println("Starting the application...")
   myLogger.Trace.Println("Something noteworthy happened")
   myLogger.Warn.Println("There is something you should know about")
   myLogger.Error.Println("Something went wrong")

   //[INFO] 2020/12/30 15:43:40 go_logging_test.go:46: Starting the application...
   //[WARNING] 2020/12/30 15:43:40 go_logging_test.go:48: There is something you should know about
   //[ERROR] 2020/12/30 15:43:40 go_logging_test.go:49: Something went wrong
}
```


## 4. 마무리

이번 포스팅에서는 Go에서 기본으로 포함된 log 패키지를 사용해서 로깅하는 방법에 대해서 알아보았다. Go 표준 패키지 log 외에도 다른 log framework(ex. logrus)도 종종 사용한다. logrus에 대한 내용은 다음 포스팅에서 알아보자.

본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-logging)에서 확인할 수 있다.

## 5. 참고

- http://golang.site/go/article/114-Logging
- https://www.ardanlabs.com/blog/2013/11/using-log-package-in-go.html
- https://jusths.tistory.com/128
- https://www.honeybadger.io/blog/golang-logging/
- https://golang.org/pkg/log/#pkg-examples
