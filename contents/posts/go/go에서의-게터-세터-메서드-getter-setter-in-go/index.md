---
title: "Go에서의 게터, 세터 메서드 (Getter, Setter in Go)"
description: "Go에서의 게터, 세터 메서드 (Getter, Setter in Go)"
date: 2021-01-14
update: 2021-01-14
tags:
  - go
  - golang
  - setter
  - getter
  - encapsulation
  - 고
  - 고랭
  - 캡슐화
  - 게터
  - 세터
---

캡슐화는 내부 속성값을 외부에서 직접적으로 접근하게 못 하게 하고 공개된 메서드 (ex. getter, setter)로만 접근하여 내부 값을 보호하는 역할을 한다. 즉, 내부 구현을 감추고 데이터 체크를 통해서 유효한 값만 저장하게 한다.

Go에서 getter, setter 메서드를 어떻게 만드는지 아래 Person 구조체를 사용해서 작성해보자.

> `name, age`는 소문자이여서 외부에서 접근할 수 없다

```go
type Person struct {
	name string
	age  int
}
```

## Setter

- `Setter`는 `SetFoo()`와 같이 만들면 된다
    - 외부에서 메서드를 호출하기 위해서 메서드 첫글자는 대문자로 한다
- `Setter`에서는 리시버 인자는 포이터 리시버(`Pointer receiver`)가 필요하다
    - 메서드 실행후 변경된 값을 반환해야 하기 때문이다
- `Setter`에서 data validation 로직을 넣어 유효성 체크를 할 수 있다

```go
func (p *Person) SetName(name string) error {
	if name == "" {
		return errors.New("invalid name")
	}
	p.name = name
	return nil
}
```

`SetName` setter메서드는 name을 인자로 받아서 `Person` 구조체에 name에 값을 저장한다. `name`이 없는 경우에는 `Error`를 반환한다.

## Getter

- `Getter`는 Get을 붙이지 않고 변수 이름으로만 지정한다
    - ex. `GetName()` - X
    - ex. `Name()` - O
    - `GetName()`을 붙혀서 코드를 작성해도 동작하는데는 이상이 없지만, go convension에 의해서 get은 쓰지 않는다

```go
func (p Person) Name() string {
	return p.name
}
```


> `Getter`는 값만 반환하기 때문에 포인터 리시버 인자가 필요가 없다. 하지만, 일관성을 위해 포인터 리시버로 선언하는 게 좋다.

```go
func (p *Person) Name() string {
   return p.name
}
```


본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-getter-setter)에서 확인할 수 있다.

## 참고

- https://www.socketloop.com/tutorials/golang-implement-getters-and-setters
- https://johngrib.github.io/wiki/golang-cheatsheet/
- https://golang.org/doc/effective_go.html?#Getters

