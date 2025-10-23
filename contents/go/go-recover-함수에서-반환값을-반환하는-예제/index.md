---
title: "Go Recover 함수에서 반환값을 반환하는 예제"
description: "Go Recover 함수에서 반환값을 반환하는 예제"
date: 2022-08-07
update: 2022-08-07
tags:
  - golang
  - go
  - recover
  - return
  - panic
---


Validation API 함수를 개발하는 과정에서 복잡한 expression을 evaluation 하는 과정에서 잘못된 표현식의 경우에는 panic이 발생하는 경우가 있었다. panic이 발생하여 `recover()` 함수로 서버가 죽지 않게 되어 있지만, Validation API의 경우에는 client에 잘못된 표현 식이라는 응답 값을 내려줘야 한다.

## 1.panic(), recover() 함수

`recover()` 함수에서 어떻게 반환값을 리턴할 수 있는지 알아보자. 오늘 사용할 Golang 내장함수들이다.

- `panic()`
    - `panic()` 함수가 실행되면 즉시 멈춘다
    - 함수에 `defer` 함수를 모두 실행한 후 종료한다
- `recover()`
    - 자바에서는 `try ~ catch` 구문을 사용하여 예외 처리를 하는 것처럼 `recover()` 함수도 비슷한 역할을 한다
    - `panic` 이 발생한 프로그램이 종료되는 것을 막고 복구한다
    - `defer`와 같이 사용해야 한다



```go
func main() {
	f()
	fmt.Println("Returned normally from f.")
}

func f() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f", r)
		}
	}()
	fmt.Println("Calling g.")
	g(0)
	fmt.Println("Returned normally from g.")
}

func g(i int) {
	if i > 3 {
		fmt.Println("Panicking!")
		panic(fmt.Sprintf("%v", i))
	}
	defer fmt.Println("Defer in g", i)
	fmt.Println("Printing in g", i)
	g(i + 1)
}

```



g() 함수에서 `panic`이 발생하고 `defer` 함수들이 call stack에 쌓인 순서대로 실행이 된 것을 볼 수 있다. 그리고 `f()` 함수에 정의된 `defer`함수 실행시 `recover()` 함수를 실행하면서 패틱 상태를 다시 정상 상태로 복구하여 나머지 `f()` 함수의 코드를 실행한다.

```bash
$ go run main.go
Printing in g 0
Printing in g 1
Printing in g 2
Printing in g 3
Panicking!
Defer in g 3
Defer in g 2
Defer in g 1
Defer in g 0
Recovered in f 4
Returned normally from f.
```



## 2.recover() 함수에서 반환 값 리턴하기

`recover()` 함수에 반환 값을 반환하려면 `MyFunc()`의 Return 값에 이름을 부여하여 부여한 이름변수에 값을 지정하면 `recover()` 함수 실행후 반환 값으로 리턴이 된다.

```go

func main() {
	myFunc, err := MyFunc()
	fmt.Println("myFunc:", myFunc)
	fmt.Println("err:", err)
}

type Response struct {
	Message string
}

func MyFunc() (resp Response, err error) {
	defer func() {
		if r := recover(); r != nil {
			err = errors.New(fmt.Sprint(r))
			resp = Response{
				Message: "failure",
			}
		}
	}()
	panic("test")
	return Response{Message: "success"}, nil
}

```

Unit Test로 실행하여 확인해보면 반환 값이 `Response{Message:"failure"}`로 리턴되는 것을 확인할 수 있다.

```go
func TestMyFunc(t *testing.T) {
	resp, err := MyFunc()
	assert.Error(t, err)
	assert.Equal(t, Response{
		Message: "failure",
	}, resp)
}
```

## 3.recover()에서 stack trace 출력하기

Panic 발생 후 recover를 하고 stack trace를 출력하여 조금 더 디버깅을 쉽게 하려면 Debug 패키지에 포함된 `PrintStack()` 함수를 사용한다.

```go

func MyFunc() (resp Response, err error) {
	defer func() {
		if r := recover(); r != nil {
			debug.PrintStack()
			err = errors.New(fmt.Sprint(r))
			resp = Response{
				Message: "Failure",
			}
		}
	}()
	panic("test")
	return Response{Message: "Success"}, nil
}
```

`debug.PrintStack()` 함수에 의해서 stack trace가 아래와 같이 출력된다.

```bash
goroutine 1 [running]:
runtime/debug.Stack()
        /opt/homebrew/opt/go/libexec/src/runtime/debug/stack.go:24 +0x68
runtime/debug.PrintStack()
        /opt/homebrew/opt/go/libexec/src/runtime/debug/stack.go:16 +0x20
main.MyFunc.func1()
        /Users/user/GolandProjects/tutorials-go/go-recover/return-value/main.go:22 +0x48
panic({0x104a5b6e0, 0x104a6bc68})
        /opt/homebrew/opt/go/libexec/src/runtime/panic.go:838 +0x204
main.MyFunc()
        /Users/user/GolandProjects/tutorials-go/go-recover/return-value/main.go:29 +0x74
main.main()
        /Users/user/GolandProjects/tutorials-go/go-recover/return-value/main.go:10 +0x20
myFunc: {Failure}
err: test

```


## 4.참고

- http://golang.site/go/article/20-Go-defer%EC%99%80-panic
- https://github.com/kenshin579/tutorials-go/pull/287
- https://stackoverflow.com/questions/68554968/why-does-go-panic-recover-to-return-value-with-local-variable-not-work
- https://stackoverflow.com/questions/19934641/go-returning-from-defer
- https://stackoverflow.com/questions/33167282/how-to-return-a-value-in-a-go-function-that-panics
- https://golangbot.com/panic-and-recover/