---
title: "Go에서의 메서드 (Method in Go)"
description: "Go에서의 메서드 (Method in Go)"
date: 2021-02-19
update: 2021-02-19
tags:
  - golang
  - method
  - receiver
  - parameter
  - pointer
  - 메서드
  - 리시버
  - 인자
  - 포인터
---


Go에서는 함수외에도 메서드를 제공한다. 메서드는 리시버 인자(Receiver Parameter)를 가진 함수를 말한다. 기능적으로 보면 일반 함수와 별 차이가 없고 아래 문법과 같이 func 키워드와 메서드이름 사이에 리시버 인자를 추가할 수 있다.

```go
func (receiver_name Type) methodName(parameter_list) (return_type) {

```

## 1. Go 메서드 예제

### 1.1 리시버 인자 (Receiver Parameter)가 있는 메서드

#### 1.1.1 밸류 리시버 (Value Receiver)

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

Go에서 메서드는 객체지향 프로그래밍 언어에서 지원하는 메서드처럼 dot(.)으로 메서드를 호출한다. `hyundaiCar.Color()` 메서드를 호출해 자동차 색깔을 출력하였다.

#### 1.1.2 포인터 리시버 (Pointer Receiver)

위 예제에서는 리시버 인자를 밸류 인자로 선언하였기 때문에 메서드 실행 후에는 데이터 타입 값에 반영이 안된다. 메서드 실행이후 변경된 값을 유지하려면 포인터 리시버를 사용해야 한다.

```go
func (c *Car) SpeedUp(s int) {
	c.speed += s
}
```
`SpeedUp()` 메서드에서는 `c.speed` 값을 증가하는 메서드로 포인터 리시버로 선언해줘야 메서드 실행 이후에 변경된 값이 계속 유지가 된다.

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

`hyundaiCar.SpeedUp(10)` 메서드 실행 이후에도 증가된 값으로 출력되는 것을 확인할 수 있다.

#### 1.1.3 메서드에 대한 컨벤션

메서드 정의 시 Go에서는 아래와 같은 컨벤션을 일반적으로 따른다.

- 리시버 인자 정의
    - 리시버 인자의 변수 이름은 리시버 타입 이름의 첫 글자를 사용한다
    - 변수는 하나의 글자로만 선언한다
- 밸류 vs 포인터 선언
    - 값을 변경할 필요가 없는 경우에는 배류 리시버로 선언해야 하지만, 통일성을 위해서 밸류와 포인터를 섞어서 선언하지 않고 포인터로 선언한다 (참고 : *Head First Go*)

> 밸류와 포인터를 섞어서 사용하는 곳도 있어서 팀내에 협의한 켄벤션으로 통일해서 사용하면 될 것 같다.

#### 1.1.4 비구조체(Non-struct)가 있는 메서드

지금까지 구조체 타입에 대해서만 메서드를 정의했다. 비구조체 타입에 대한 메서드를 정의하는 것도 가능하지만, 주의가 필요하다. 리시버 타입의 정의와 메서드의 정의는 동일한 패키지 내에 있어야 한다.


```go
func (f float64) ceil() float64 {
	return math.Ceil(float64(i))
}
```
위 예제에서는 `float64` 타입과 `ceil()` 메서드가 같은 패키지 레벨에 존재하지 않아서 컴파일 오류가 발생한다.

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

비구조체를 리시버 인자로 받으려면 `float64`를 별도 타입으로 선언하면 메서드로 선언이 가능해진다.

### 1.2 메서드와 포인터 역참조 (Pointer indirection/dereference)

포인터를 다루는 데 있어서 함수와 메서드간의 차이점이 존재한다. 어떤 차이점이 있는지 예제를 통해서 알아보자.

- 함수에 포인터 인자로 선언한 인자는 포인터 인자만 인자로 받을 수 있다
- 메서드의 리시버 인자의 경우에는 포인터와 밸류 인자 둘 다 받을 수 있다

```go
func area(r *Rectangle) {
	fmt.Println(r.height * r.width)
}

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

area(r *Rectangle) 함수의 인자는 포인터 인자로 선언되어 밸류 값을 넘기면 컴파일 오류가 발생하고 포인터 인자만을 넘길 수 있다.



```go
func (r *Rectangle) area() {
	fmt.Println(r.height * r.width)
}

func Example_Indirection_Method_Pointer_Receiver() {
	r := Rectangle{
		height: 10,
		width:  3,
	}

	r.area()
	(&r).area()

	//Output:
	//30
	//30

}
```

r.area(), r은 포인터가 아닌 밸류 값이지만, 포인터 리시버 인자의 메서드가 호출될 때 Go에서 자동으로 r.area() -> (&r).area()로 해석을 해서 실행해준다.

리시버 인자가 밸류인 경우에도 함수와 메서드의 차이점을 알아보자.



```go
func perimeter(r Rectangle) {
	fmt.Println(2 * (r.height * r.width))
}

func Example_Indirection_Func_Value_Parameter() {
	r := Rectangle{
		height: 10,
		width:  3,
	}

	//perimeter(&r) //컴파일 오류 - 함수는 value 인자만 받을 수 있음
	perimeter(r)

	//Output:
	//60
}
```

`perimeter(r Rectangle)` 함수는 밸류 인자로 선언되어 `perimeter(&r)` 포인터 값을 인자로 넘겨주면 컴파일 오류가 발생한다.



```go
func (r Rectangle) perimeter() {
	fmt.Println(2 * (r.height * r.width))
}

func Example_Indirection_Method_Value_Receiver() {
	r := Rectangle{
		height: 10,
		width:  3,
	}

	r.perimeter()
  (&r).perimeter()

	//Output:
	//60
	//60
}
```

리시버 인자의 경우,  (&r).perimeter() 호출 시 Go는 리시버 인자는 밸류 인자로 선언되어 (*r).perimeter()로 자동으로 해석해서 실행해준다.

## 정리

Go에서는 함수와 메서드가 존재를 한다. 메서드는 함수에 리시버 인자를 추가한 버전으로 생각하면 이해하기 쉽다. 본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-methods)에서 확인할 수 있다.

## 참고

- https://tour.golang.org/methods/4
- http://golang.site/go/article/17-Go-%EB%A9%94%EC%84%9C%EB%93%9C
- https://gobyexample.com/methods
- https://golangbot.com/methods/
- https://hoony-gunputer.tistory.com/entry/golang-part4Method-Pointer-and-Method-Interface-Stringers-Error-Readers
- https://go101.org/article/method.html
- https://www.geeksforgeeks.org/methods-in-golang/
