---
title: "Go에서의 다형성 (Polymorphism)"
description: "Go에서의 다형성 (Polymorphism)"
date: 2021-06-06
update: 2021-06-06
tags:
  - go
  - golang
  - duck
  - typing
  - duck type
  - polymorphism
  - 다형성
  - 고랭
  - 덕타입
  - 고언어
---

## 다형성 (Polymorphism)

다형성은 객체지향 패러다임에서는 꼭 알아야 하는 특징 중의 하나이다. 기본 개념은 객체 메서드를 호출했을 때, 그 객체의 메서드가 다양한 구현을 할 수 있게 한다. 다형성을 설명할 때 도형이나 동물을 예제로 자주 설명한다. 본 포스팅에서는 동물을 예제로 설명한다.


## Go에서 다형성을 구현하는 방법

Go에서는 다형성을 인터페이스로 구현할 수 있다. Go의 인터페이스를 사용하면 다른 언어보다 더 쉽게 구현이 가능하다. 예제를 통해서 알아보자.

`Dog`와 `Cat`은 소리를 낼 수 있지만, 각각 다른 소리를 낸다. 공통적인 기능은 `Animal` 인터페이스로 정의한다.

```go
type Animal interface {
	makeSound() string
}

type Dog struct {
	name string
	legs int
}

type Cat struct {
	name string
	legs int
}
```

자바의 경우에는 `implements`와 같은 키워드를 사용해서 구현하려는 인터페이스를 명시해줘야 하지만, Go에서는 각 데이터 타입에 대해서 인터페이스 메서드만 구현해주면 명시적으로 정의하지 않고도 인식이 된다.

> Go에서는 덕 타이핑 (`duck typing`)을 지원한다. 덕 타이핑은 클래스 상속이나 명시적인 인터페이스 구현으로 타입을 구분하는 방식이 아니고, 객체가 어떤 타입에 걸맞는 메서드를 지내게 되면 해당 타입으로 간주한다.
>
> "만약 어떤 새가 오리처럼 걷고, 헤엄치고, 꽥꽥거리는 소리를 낸다면 나는 그 새를 오리라 부르겠다."
>
> 오리와 같은 행동을 하면 오리로 간주한다는 의미이다.

```go

func (d *Dog) makeSound() string {
	return d.name + " says 멍멍!"
}
func (c *Cat) makeSound() string {
	return c.name + " says 야옹!"
}
```

`Dog`와 `Cat` 구조체에 대해서 `makeSound()` 메서드를 구현한다.

```go

func NewDog(name string) Animal {
	return &Dog{
		legs: 4,
		name: name,
	}
}

func NewCat(name string) Animal {
	return &Cat{
		legs: 4,
		name: name,
	}
}

func Example_Polymorphism_Interface_사용하는_방법() {
	var dog, cat Animal

	dog = NewDog("초코")
	cat = NewCat("루시")

	fmt.Println(dog.makeSound())
	fmt.Println(cat.makeSound())

	//Output:
	//초코 says 멍멍!
	//루시 says 야옹!
}


```

Unit Test에서 실행해보자. `Dog`와 `Cat`를 별도 생성자로 데이터 타입을 생성한다. 인터페이스 메서드를 호출하면 다른 구조체에 맞게 다른 행동을 하는 것을 확인할 수 있다.

본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-design-pattern/polymorphism)를 참고해주세요.

## 참고

- https://www.sohamkamani.com/golang/2019-03-29-polymorphism-without-interfaces/
- https://golangbot.com/polymorphism/
- https://www.geeksforgeeks.org/polymorphism-in-golang/
- https://golangbyexample.com/runtime-polymorphism-go/
- https://www.popit.kr/golang%EC%9C%BC%EB%A1%9C-%EB%A7%8C%EB%82%98%EB%B3%B4%EB%8A%94-duck-typing/
- https://ko.wikipedia.org/wiki/%EB%8D%95_%ED%83%80%EC%9D%B4%ED%95%91
