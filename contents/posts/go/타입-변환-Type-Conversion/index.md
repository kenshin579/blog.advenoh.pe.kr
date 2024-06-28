---
title: "타입 변환 (Type Conversion)"
description: "타입 변환 (Type Conversion)"
date: 2021-01-16
update: 2021-01-16
tags:
  - golang
  - type
  - conversion
  - cast
  - casting
  - 형변환
  - 타입변환
  - 타입
  - 변환
  - 명시적
  - 캐스팅
---

타입 변환은 데이터 타입을 변경하는 것이다. Java에서는 명시적 타입 변환(explicit type conversion)과 암시적 타입 변환(implicit type conversion) 둘 다 지원하지만, Go에서는 명시적인 타입 변환만을 지원한다.

타입 변환 문법은 아래와 같이 val 값을 타입 T로 변환한다.

```go
T(val)
```

예제에서는 int 형을 float64와 uint32 형으로 변환해주고 있다.

```go
func Example_TypeConversion() {
	var i = 52
	var j float64 = float64(i)
	var k = uint32(j)

	fmt.Println(i)
	fmt.Println(j)
	fmt.Println(k)

	//Output:
	//52
	//52
	//52
}
```



본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-type-conversion)에서 확인할 수 있다.

## 참고

- Go 형변환
    - https://tour.golang.org/basics/13
    - https://www.geeksforgeeks.org/type-casting-or-type-conversion-in-golang/
- Java 형변환
    - https://opentutorials.org/course/1223/5330
