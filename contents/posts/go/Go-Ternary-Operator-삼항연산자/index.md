---
title: "Go Ternary Operator (삼항연산자)"
description: "Go Ternary Operator (삼항연산자)"
date: 2021-05-18
update: 2021-05-18
tags:
  - go
  - golang
  - ternary
  - operator
  - 고랭
  - 연산자
  - 삼항
  - 삼항연산자
  - 3항연산자
---


## 삼항연산자란?

삼항 연산자 (Ternary Operator)는 아래 형식으로 if 조건문 대신 사용할 수 있는 문법이다. JavaScript, Java와 같은 여러 언어에서 지원하는 문법이고 아래 코드는 자바의 삼항 연산자이다.

```java
String grade = (math >= 90) ? "pass": "fail";
```

Golang 언어에서 삼항 연산자가 빠진 이유는 심플한 설계를 유지 하기 위해서 Golang에서 빠졌다. 긴 버전 자체가 가독성도 높고 삼항 연산자를 알지 못해도 긴 버전으로는 누구나 쉽게 이해가 가능하여 언어 설계 단계에서 빠졌다.

삼항연산자를 지원하지 않지만, 함수를 이용해서 삼항 연산자 처럼 코딩할 수도 있다. "done" 상태 값인 경우에 true, false를 반환하는 예제이다.

```go

func Example_Ternary_Operator_EqualCheck() {
	checkStatus := func(status string) bool {
		if status == "done" {
			return true
		}
		return false
	}("done")

	fmt.Println(checkStatus)
	//Output: true
}


```

예제 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-ternary)를 참고해주세요.

## 참고

- https://golangdocs.com/ternary-operator-in-golang
- https://needneo.tistory.com/105





