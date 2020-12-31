---
title: 'Logging in Go'
date: 2020-12-30 15:18:23
category: 'go'
tags: ["go", "golang", "log", "logging", "logrus", 고", "고랭", "로그", "로깅"]
---

#1. 들어가며

Go에 기본으로 포함되어 있는 Log 패키지 사용법에 대해서 알아보자

import

```go
import (
	"log"
)

```



# 2. Log 패키지 사용기

## 2.1 기본 Logger

### 2.1.1 기본 Logger로 화면에 로그찍기

```go
func Test_기본_Logger(t *testing.T) {
	log.Println("Logging") //2020/12/30 10:27:11 Logging
}
```

```go
func Test_기본_Logger_Flags_설정_날짜_시간_표시_X(t *testing.T) {
	log.SetFlags(0)
	log.Println("Logging") //Logging
}
```

```go
func Test_기본_Logger_Flags_설정2(t *testing.T) {
	log.SetFlags(log.Ldate | log.Ltime | log.Llongfile)
	log.SetPrefix("INFO: ")
	log.Println("Logging")

	//INFO: 2020/12/30 15:41:20 /Users/ykoh/GolandProjects/tutorials-go/go-logging/go_logging_test.go:23: Logging
}
```

### 2.1.2 파일로 쓰기

```go
func Test_기본_Logger_File(t *testing.T) {
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

### 2.1.3 화면과 파일에 동시에 로그 찍기

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



## 2.2 Custom Logger



### 2.2.1 Custom Logger 생성하기

```go
var logger *log.Logger

func Test_Custom_Logger(t *testing.T) {
   logger = log.New(os.Stdout, "INFO: ", log.LstdFlags)
   logger.Println("Logging") //INFO: 2020/12/30 10:34:00 Logging
}
```



### 2.2.2 로그 파일로 쓰기

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



### 2.2.3 여러 Logger 생성하는 예제

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


# 4. 마무리

 본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-logging)에서 확인할 수 있다.

# 5. 참고

- http://golang.site/go/article/114-Logging
- https://www.ardanlabs.com/blog/2013/11/using-log-package-in-go.html
- https://jusths.tistory.com/128
- https://www.honeybadger.io/blog/golang-logging/
- https://golang.org/pkg/log/#pkg-examples