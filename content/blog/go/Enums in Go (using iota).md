---
title: 'Enums in Go (using iota)'
date: 2020-12-20 16:05:23
category: 'go'
tags: ["go", "golang", "enums", "iota", "열거형", "고", "고랭"]
---

- iota란?
- 
- iterate하는 방버

# 들어가며



#2.  iota 예제

## 2.1 기본 예제

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

## 2.4 중간 값 다르게 지정하는 방법

### 2.4.1 직접 

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

### 2.4.2 const 그룹별로 나누기

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

##  

## 3.1 ByteSize 상수 값 선언하기

```go
func Example_iota_BYTE_예제() {
	type ByteSize float64

	const (
		_           = iota             // ignore first value by assigning to blank identifier
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



# 참고

* https://stackoverflow.com/questions/64178176/how-to-create-an-enum-in-golang-an-iterate-over-it
* https://stackoverflow.com/questions/57053373/how-to-skip-a-lot-of-values-when-define-const-variable-with-iota/57053431#57053431
* https://yourbasic.org/golang/iota/
* https://golang.org/ref/spec#Iota
* [https://www.popit.kr/%EC%A2%8C%EC%B6%A9%EC%9A%B0%EB%8F%8C-%EA%B0%9C%EB%B0%9C%EA%B8%B0-golang-%EC%97%90%EC%84%9C-enum-%EC%9E%90%EB%A3%8C%ED%98%95-%EC%82%AC%EC%9A%A9%ED%9B%84%EA%B8%B0](https://www.popit.kr/좌충우돌-개발기-golang-에서-enum-자료형-사용후기)/

