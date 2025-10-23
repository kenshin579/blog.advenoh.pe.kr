---
title: "타입 단언 (Type Assertion)"
description: "타입 단언 (Type Assertion)"
date: 2021-01-16
update: 2021-01-16
tags:
  - go
  - golang
  - type
  - assertion
  - 타입
  - 형단언
  - 타입단언
  - 단언
  - 고
  - 고랭
---


Go는 타입 단언(Type assertion)을 통해서 인터페이스 `i` 변수가 타입 `T`인지를 확인하고 인터페이스의 실제 구현된 타입의 값을 가져올 수 있다.

```go
value := i.(T)
```

타입 단언 문법으로 인터페이스 `i` 변수가 타입 `T`인지 확인하고 실제 값을 `value` 변수에 값을 할당한다. 타입 단언 사용 시 주의해야 하는 사항은 다음과 같다.

- `i` 변수는 인터페이스이여야 한다
    - 인터페이스 `i`가 실제 값을 가지고 있지 않은 경우에는 panic이 발생한다
- `T`는 `i` 인터페이스를 구현한 타입인지를 확인하다
    - 타입 T의  인터페이스의 메서드를 구현하고 있지 않으면 panic이 발생한다

타입 단어 예제에서 사용할 인터페이스와 메서드이다. `Person, Phone` 인터페이스의 메서드는 `Student` 구조체 데이터 타입에 맞게 구현했다.

```go

type Person interface {
	getName() string
}

type Phone interface {
	getPhone() string
}

type Student struct {
	name  string
	age   int
	phone string
}

func (c Student) getName() string {
	return c.name
}

func (c Student) getPhone() string {
	return c.phone
}
```

## 1.타입 단언 예제


### 1.1 정상적으로 타입 단언하는 경우

#### 1.1.1 실제 구조체로 타입 단언하는 경우

```go
func Example_TypeAssertion_인터페이스_데이터_타입_Student_값을_가져온다() {
	var p Person = Student{"Frank", 13, "1111"}
	fmt.Println(p.getName())

	s := p.(Student) //Person -> Student - student의 실제 값을 가져온다.
	fmt.Println(s.getName())
	fmt.Println(s.getPhone())

	//Output:
	//Frank
	//Frank
	//1111
}
```

인터페이스 `p` 변수는 `Student` 구조체 값을 보유하고 있다. `p.(Student)` 타입 단언으로 `p` 인터페이스값에서 실제 `Student` 구조체 값을 얻어와 해당 데이터 타입의 메서드를 실행했다.

#### 1.1.2 다른 인터페이스로 타입 단언하는 경우

```go
func Example_TypeAssertion_다른_인터페이스로_값을_가져온다() {
	var p Person = Student{"Frank", 13, "1111"}

	ph := p.(Phone) //Person -> Phone
	fmt.Println(ph.getPhone())

	//Output:
	//1111
}
```

`Person` 인터페이스에서 다른 인터페이스인 `Phone`으로 타입 단언을 하여 `Phone` 인터페이스의 메서드를 실행할 수 있었다.

### 1.2 타입 단언시 panic이 발생하는 경우

타입 단언시 발생할 수 있는 에러에 대해서 알아보자.

#### 1.2.1 인터페이스가 타입 T의 동적 값을 가지고 있지 않는 경우

```go
//타입 T가 인터페이스를 구현하고 있지 않기 때문에 컴파일 에러가 발생한다
func Example_TypeAssertion_인터페이스가_타입_T의_동적_값을_소유하지_않을_경우_컴파일_에러가_발생한다() {
	//var p Person = Student{"Frank", 13, "1111"}
	//value := p.(string) //impossible type assertion: string does not implement person (missing getName method)
	//fmt.Printf("%v, %T\n", value, value)

	//Output:
}
```

타입 단언 시 `i.(T)` 타입 `T`가 인터페이스 메서드를 구현하고 있지 않으면, 인터페이스 `i`가 타입 `T`의 동적 값을 보유할 수 없기 때문에 `impossible type assertion` 컴파일 에러가 발생한다.

#### 1.2.2 인터페이스가 타입 T의 실제 값을 가지고 있지 않는 경우

타입 `T`는 구현된 메서드가 있지만, 인터페이스 `i`가 실제 값을 가지고 있지 않으면 Go에서 런타임시 panic이 발생한다.

```go
func Example_TypeAssertion_인터페이스가_타입_T의_실제_값을_가지고_있지_않는_경우_panic이_발생한다() {
	var p Person = nil
	//value := p.(Student) //panic: interface conversion: go_type_assertions.Person is nil, not go_type_assertions.Student
	value, ok := p.(Student)
	fmt.Printf("(%v, %T), ok: %v\n", value, value, ok)

	//Output:
	//({ 0 }, go_type_assertions.Student), ok: false
}

```

런타임시 panic 발생을 피하려면 타입 단언 시 ok 반환 값을 추가로 받으면 된다. `ok` 변수를 통해서 타입 `T`가 인터페이스 `i`를 구현했는지, `i`가 실제 타입 `T`를 갖고 있는지 확인할 수 있다. 모두 만족하면 `ok`는 `true`를 반환하고 아닌 경우에는 `false`를 반환한다.

```go
	value, ok := p.(Student)
```



#### 1.2.3 다른 인터페이스가 타입 T를 구현하지 않고 있는 경우

```go
type Animal interface {
	walk()
}

func Example_TypeAssertion_다른_인터페이스가_타입_T를_구현하지_않고_있으면_panic이_발생한다() {
	var p Person = Student{"Frank", 13, "1111"}
	//value := p.(Animal) //panic: interface conversion: go_type_assertions.Student is not go_type_assertions.Animal: missing method walk
	value, ok := p.(Animal)
	fmt.Printf("(%v, %T) %v\n", value, value, ok)

	//Output:
	//(<nil>, <nil>) false
}

```

`Student` 구조체는 `Animal` 인터페이스를 구현하지 않았기 때문에 `p.(Animal)` 타입 단언시 panic이 발생한다.

## 정리

타입 단언은 인터페이스 변수에서 실제 타입 값을 얻어와 해당 타입에 맞는 메서드를 실행할 때 사용된다.

본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-type-assertions)에서 확인할 수 있다.

## 참고

- Type assertions
    - https://yourbasic.org/golang/type-assertion-switch/
    - https://feel5ny.github.io/2017/11/18/Typescript_05/
    - https://pronist.tistory.com/92
    - https://tour.golang.org/methods/15
    - https://www.geeksforgeeks.org/type-assertions-in-golang/
    - https://www.sohamkamani.com/golang/type-assertions-vs-type-conversions/
    - https://hoonyland.medium.com/%EB%B2%88%EC%97%AD-interfaces-in-go-d5ebece9a7ea
    - https://velog.io/@kykevin/Go%EC%9D%98-Interface
- Type conversions
    - https://tour.golang.org/basics/13

