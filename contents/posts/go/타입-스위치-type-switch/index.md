---
title: "타입 스위치 (Type switch)"
description: "타입 스위치 (Type switch)"
date: 2021-01-16
update: 2021-01-16
tags:
  - go
  - golang
  - type
  - switch
  - 형스위치
  - 타입스위치
  - 고
  - 고랭
---

티입 스위치는 형 단언을 실행하여 해당 변수의 타입이 스위치 문의 조건에 일치하는 블럭을 실행한다. 타입 스위치 선언문은 형 단언 `variable.(T)`와 같은 구문을 가진다. 그러나 T는 `type` 키워드로 대체된다.

인자로 넘겨진 `i` 변수의 실제 타입에 따라서 각 케이스 블럭 구문이 실행된다.

```go

func typeSwitchTest(i interface{}) {
	switch v := i.(type) {
	case nil:
		fmt.Println("x is nil")
	case int:
		fmt.Println("x is", v)
	case bool, string:
		fmt.Println("x is bool or string")
	default:
		fmt.Printf("type unknown %T\n", v)
	}
}
```
여러 인자 값에 따라서 스위치 구문이 실행된다.

```go

func Example_TypeSwitch() {
	typeSwitchTest("value")
	typeSwitchTest(23)
	typeSwitchTest(true)
	typeSwitchTest(nil)
	typeSwitchTest([]int{})

	//Output:
	//x is bool or string
	//x is 23
	//x is bool or string
	//x is nil
	//type unknown []int
}
```

본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-type-switch)에서 확인할 수 있다.

## 참고

* https://yourbasic.org/golang/type-assertion-switch/
* https://riptutorial.com/go/example/14736/type-switch
* https://www.geeksforgeeks.org/type-switches-in-golang/
* https://tour.golang.org/methods/16

