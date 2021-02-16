---
title: 'Go에서의 메서드'
layout : post
category: go
author: [Frank Oh]
image: ../img/cover-go.png
date: '2021-01-18T21:11:23.000Z'
draft: false
tags: ["go", "golang", "method", "receiver", "parameter", "고", "고랭", "메서드"]
---

Go에서는 함수외에도 메서드를 제공한다. 메서드는 리시버 인자(Receiver Parameter)를 가진 함수를 말한다. 기능적으로 보면 일반 함수와는 차이점이 없고 아래 문법과 같이 func 키워드와 메서드이름 사이에 리시버 인자를 추가할 수 있다.

```go
func (receiver_name Type) methodName(parameter_list) (return_type) {

```

# 1. Go 메서드 예제

## 1.1 리시버 인자 (Receiver Parameter)가 있는 메서드

### 1.1.1 밸류 리시버 (Value Receiver)

```go
type Car struct {
	brand   string
	color   string
	mileage int
	speed   int
}

func (c Car) Color() string {
	return c.color
}
```
`Car` 타입의 값을 메서드 형식으로 반환하려면 메서드 이름 앞에 리시버 인자로 `Car` 타입을 선언하면 된다. `Color()` 메서드에서는 `c.color` 값을 반환한다.

```go
func Example_Method_Value_Receiver() {
	hyundaiCar := Car{"현대", "빨강", 10000, 0}
	//fmt.Println("hyundaiCar", hyundaiCar)

	fmt.Println(hyundaiCar.Color())

	//Output:
	//빨강
}
```

객체지향 프로그래밍 언어에서 지원하는 메서드처럼 dot(.)으로 메서드를 호출한다. `hyundaiCar.Color()` 메서드를 호출해 자동차 색깔을 출력하였다. 

### 1.1.2 포인터 리시버 (Pointer Receiver)

위 예제에서는 리시버 인자를 밸류 인자로 선언하였기 때문에 메서드 실행후에는 데이터 타입 값에 반영이 안된다. 메서드 실행이후 변경된 값을 유지하면 포인터 리시버를 사용해야 한다. 

```go
func (c *Car) SpeedUp(s int) {
	c.speed += s
}
```
`SpeedUp()` 메서드에서는 `c.speed` 값을 증가하는 메서드로 포인터 리시버로 선언해줘야 메서드 실행이후에 변경된 값이 유지가 된다. 

```go
func Example_Method_Pointer_Receiver() {
	hyundaiCar := Car{"현대", "빨강", 10000, 0}
	fmt.Println("hyundaiCar", hyundaiCar)

	hyundaiCar.SpeedUp(10)
	fmt.Println("hyundaiCar", hyundaiCar) //증가된 값

	//Output:
	//hyundaiCar {현대 빨강 10000 0}
	//hyundaiCar {현대 빨강 10000 10}
}
```

`hyundaiCar.SpeedUp(10)` 메서드 실행이후에도 증가된 값으로 출력된다. 

### 1.1.3 메서드에 대한 컨벤션

메서드 정의시에는 Go에서는 아래와 같은 컨벤션을 일반적으로 따른다. 

- 리시버 인자 정의
  - 리시버 인자의 변수 이름은 리시버 타입 이름의 첫 글자를 사용한다
  - 변수는 한 글자로 선언한다
- 밸류 vs 포인터 선언
  - 값을 변경할 필요가 없는 경우에는 배류 리시버로 선언해야 하지만, 통일성을 위해서 밸류와 포인터를 섞어서 선언하지 않고 포인터로 선언한다

### 1.1.4 비구조체(Non-struct)가 있는 메서드

지금까지 구조체 타입에 대해서만 메서드를 정의했다. 비구조체 타입에 대한 메서드를 정의하는 것도 가능하지만, 주의가 필요하다. 리시버 타입의 정의와 메서드의 정의가 동일한 패키지 내에 있어야 한다.


```go
func (f float64) ceil() float64 {
	return math.Ceil(float64(i))
}
```
`float64` 타입과 `ceil()` 메서드는 같은 패키지 레벨이 존재하지 않기 때문에 컴파일 오류가 발생한다. 

```go

type myFloat float64

func (m myFloat) ceil() float64 {
	return math.Ceil(float64(m))
}

func Example_Method_Non_Struct_Type() {
	v := myFloat(1.3)
	fmt.Println(v)

	//Output:
	//1.3
}
```

비구조체를 리시버 인자를 받으려면 float64를 별도 타입으로 선언하여 사용하며 메서드를 만들면 가능해진다. 

## 1.2 메서드와 포인터 역참조 (Pointer indirection/dereference)

포인터를 다루는 데 있어서 함수와 메서드간의 차이점이 존재한다. 

- 함수는 포인터 인자만 받을 수 있다.
- 메서드는 리시버 인자로 포인터와 value (todo : 여기서 부터 작성하면 됨)

```go
func Example_Indirection_Func_Pointer_Parameter() {
	r := Rectangle{
		height: 10,
		width:  3,
	}

	//area(r) //컴파일 오류 - 함수는 포인터 인자만 받을 수 있음
	area(&r)

	//Output:
	//30
}
```



함수, 메서드의 pointer indirection 차이점

- 함수

  - 함수의 경우에는 포인터 인자는 포인터 인자만 받는다

- 메서드

  - pointer receiver
    - 함수는 인자로 포인터만 받을 수 있음

- 메서드는 pointer, value 값을 둘다 받을 수 있음

     - pointer이면 자동으로 (&pointer)로 실행됨

  - value receiver
    - 함수는 그냥 value만 받을 수 있음
    - 메서드는 pointer, value값을 받을 수 있음
      - pointer이면 자동으로 (*pointer)로 실행됨
  - 
  - value, pointer던 둘바 받을 수 있다
    - 포인터를 value로 받으면 Go에서 자동으로 해석을 해준다
  - receiver 인자가 pointer가 아니고 호출할 때 &로 호출하며 자동으로 p.Abs() -> (*).Abs() 해석한다

# 정리

본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-type-assertions)에서 확인할 수 있다.

# 참고

- https://tour.golang.org/methods/4
- http://golang.site/go/article/17-Go-%EB%A9%94%EC%84%9C%EB%93%9C
- https://gobyexample.com/methods
- https://golangbot.com/methods/
- https://hoony-gunputer.tistory.com/entry/golang-part4Method-Pointer-and-Method-Interface-Stringers-Error-Readers
- https://go101.org/article/method.html
- https://www.geeksforgeeks.org/methods-in-golang/
- 

