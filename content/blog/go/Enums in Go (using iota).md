---
title: 'Enums in Go (using iota)'
date: 2020-12-20 16:05:23
category: 'go'
tags: ["go", "golang", "enums", "iota", "열거형", "고", "고랭"]
---

#1. 들어가며

Go에서는 Java에서 제공하는 Enums 타입은 존재하지 않는다. 하지만, Go에서도 `iota`를 이용해서 Enums과 같은 상수값을 쉽게 선언하여 사용할 수 있다. 

`iota` 키워드는 `const` 선언에서 사용할 수 있는 predefined identifier로 연속적인 정수 상수 0, 1, 2, ...를 나타낸다. 예제를 통해서 어떻게 사용하는지 알아보자.

```go
//#builtin.go
// iota is a predeclared identifier representing the untyped integer ordinal
// number of the current const specification in a (usually parenthesized)
// const declaration. It is zero-indexed.
const iota = 0 // Untyped int.
```

#2.  iota 예제

## 2.1 기본 예제

`iota`의 시작 값은 0이고 이후부터는 +1 증가된 값으로 선언된다.

```go
func Example_iota_기본() {
  const (
    c0 = iota
    c1 = iota
    c2 = iota
  )

  fmt.Println(c0, c1, c2)
  //Output:
  //0 1 2
}

```

매번 `iota` 키워드를 사용하지 않고 한번만 선언하면 나머지 변수에는 연속적인 값이 선언된다. 

```go
func Example_iota_기본2() {
	const (
		c0 = iota
		c1
		c2
	)

	fmt.Println(c0, c1, c2)
	//Output:
	//0 1 2
}

```



## 2.2 시작 값 변경하기

시작 값도 쉽게 변경할 수 있다. 

```go
func Example_iota_시작값_변경() {
	const (
		c0 = iota + 5
		c1
		c2
	)

	fmt.Println(c0, c1, c2)
	//Output:
	//5 6 7
}

```



## 2.3 중간 값 스킵하기

### 2.3.1 하나의 값을 스킵하는 방법

중간 값을 스킵하려면 `blank identifier`를 사용해서 중간 값을 스킵할 수 있다. 

```go

func Example_iota_중간값_skipped() {
	const (
		c0 = iota + 1
		_
		c1
		c2
	)

	fmt.Println(c0, c1, c2)
	//Output:
	//1 3 4
}
```

### 2.4.2 하나 이상의 값 스킵하는 방법

아래와 같이 하나 이상의 값을 스킵하고 상수 값을 선언하는 방법에 대해서 알아보자. 

> 1, 2, 100, 101, 500, 501 

#### 2.4.2.1 jump해야 하는 값을 직접 계산하기

스킵해야 하는 구간의 값을 직접 계산해서 선언하면 된다. 

```go
func Example_iota_중간값_다르게_지정() {
	//수동으로 계산하기
	const (
		c0 = iota + 1   //1
		c1              //2
		c2 = iota + 98  //100
		c3              //101
		c4 = iota + 496 //500
		c5              //501
	)

	fmt.Println(c0, c1, c2, c3, c4, c5)
	//Output:
	//1 2 100 101 500 501
}
```

#### 2.4.2.2 const 그룹 별로 나눠서 선언하기

jump 뛰어야 하는 구간을 직접 계산하기보다는 아래와 같이 여러 상수 그룹으로 나눠서 선언하면 조금 더 쉽게 선언이 가능하다.

```go
func Example_iota_중간값_다르게_지정2() {
	//수동으로 계산하기
	const (
		c0 = iota + 1 //1
		c1            //2
	)
	const (
		c2 = iota + 100 //100
		c3              //101
	)
	const (
		c4 = iota + 500 //500
		c5              //501
	)

	fmt.Println(c0, c1, c2, c3, c4, c5)
	//Output:
	//1 2 100 101 500 501
}

```

# 3. Enums 예제 모음

Go 언어에서 Enums 식으로 많이 사용할 수 있는 예제들이다. 

## 3.1 ByteSize 상수 값 선언하기

데이터 단위 

데이터 단위 

선언시 Enums 으로 선언하여 사용하

```go
func Example_iota_BYTE_예제() {
	type ByteSize float64

	const (
		_           = iota             // blank identifier로 첫번째는 그냥 무시함
		KB ByteSize = 1 << (10 * iota) //2^(10*1) = 1024
		MB                             //2^(10*2) = 1,048,576
		GB
		TB
		PB
		EB
		ZB
		YB
	)
	var fileSize ByteSize = 4000000000 //4 GB
	fmt.Printf("%.2f GB", fileSize/GB)
	//Output:
	//3.73 GB
}
```



## 3.2 Bitwise로 role 

```go

func Example_iota_bitwise_role_예제() {
	const (
		isAdmin = 1 << iota
		isHeadquarters
		canSeeFinancials

		canSeeAfrica
		canSeeAsia
		canSeeEurope
		canSeeNorthAmerica
		canSeeSouthAmerica
	)

	var myRoles byte = isAdmin | canSeeFinancials | canSeeEurope
	fmt.Printf("%b\n", myRoles)
	fmt.Printf("is admin? %v\n", isAdmin&myRoles == isAdmin)
	fmt.Printf("is HQ? %v\n", isHeadquarters&myRoles == isHeadquarters)
	//Output:
	//100101
	//is admin? true
	//is HQ? false
}

```



## 3.3 Enums iterate

```go
type WeekDay int

func Example_iterate_weekdays() {
	const (
		Sunday WeekDay = iota
		Monday
		Tuesday
		Wednesday
		Thursday
		Friday
		Saturday
		numberOfDays
	)

	for day := WeekDay(0); day < numberOfDays; day++ {
		fmt.Print(" ", day)
	}
	fmt.Println("")
	//Output:
	//Sunday Monday Tuesday Wednesday Thursday Friday Saturday
}

func (d WeekDay) String() string {
	var weekDays = [...]string{
		"Sunday",
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		"Saturday",
	}

	return weekDays[int(d)%len(weekDays)]
}
```



# 4. 마무리

이번 시간에는 Iota을 이용해서 Go 언어에서 Enums을 

포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-enums-iota)에서 확인할 수 있다.

# 5. 참고

* https://stackoverflow.com/questions/64178176/how-to-create-an-enum-in-golang-an-iterate-over-it
* https://stackoverflow.com/questions/57053373/how-to-skip-a-lot-of-values-when-define-const-variable-with-iota/57053431#57053431
* https://yourbasic.org/golang/iota/
* https://golang.org/ref/spec#Iota
* [https://www.popit.kr/%EC%A2%8C%EC%B6%A9%EC%9A%B0%EB%8F%8C-%EA%B0%9C%EB%B0%9C%EA%B8%B0-golang-%EC%97%90%EC%84%9C-enum-%EC%9E%90%EB%A3%8C%ED%98%95-%EC%82%AC%EC%9A%A9%ED%9B%84%EA%B8%B0](https://www.popit.kr/좌충우돌-개발기-golang-에서-enum-자료형-사용후기)/

