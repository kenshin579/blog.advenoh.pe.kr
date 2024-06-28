---
title: "Go에서 컬렉션 정렬하는 방법 (Go Sort)"
description: "Go에서 컬렉션 정렬하는 방법 (Go Sort)"
date: 2021-05-09
update: 2021-05-09
tags:
  - go
  - golang
  - comparator
  - sort
  - 고랭
  - 정렬
---

## 1. 들어가며

Go에서는 여러 컬렉션 타입에 대해서 어떻게 정렬할 수 있는지에 대해서 알아보자.

- Primitive 데이터 타입 정렬하기
- Custom comparator로 정렬하기
- Sort interface로 정렬하기
- Map에서 특정 key/value로 정렬하기

## 2.Sort 4가지 방법

### 2.1 Primitive 데이터 타입 정렬하기

Primitive 데이터 타입에 대해서는 아래 함수들을 제공해주고 있다.

- `sort.Ints`
- `sort.Float64`
- `sort.Strings`

```go
func Example_Sort_Int_Primitive_Type() {
	list := []int{4, 2, 3, 1}
	sort.Ints(list)
	fmt.Println(list)

	//Output:
	// [1 2 3 4]
}

func Example_Sort_String_Primitive_Type() {
	list := []string{"d", "f", "a", "y", "e"}
	sort.Strings(list)
	fmt.Println(list)

	//Output:
	// [a d e f y]
}
```



### 2.2 Struct 구조체 정렬하기

사용자 정의 `Comparator` 함수를 정의해서 구조체의 속성값 기준으로 정렬할 수 있다. 아래는 `Employee`의 나이 적은 순으로 정렬한 예제이다.

```go

func Example_Sort_Struct_With_Custom_Comparator() {
	employee := []struct {
		Name string
		Age  int
	}{
		{"Alice", 23},
		{"David", 2},
		{"Eve", 2},
		{"Bob", 25},
	}

	// Sort by age, keeping original order or equal elements.
	sort.SliceStable(employee, func(i, j int) bool {
		return employee[i].Age < employee[j].Age
	})
	fmt.Println(employee)

	//Output:
	//[{David 2} {Eve 2} {Alice 23} {Bob 25}]
}
```



### 2.3 정렬 인터페이스로 구조체 정렬하기

정렬 인터페이스로도 구조체를 정렬할 수 있다. `sort.Sort()` 메서드는 `sort.Interface` 정렬 인터페이스를 인자로 받는다. 정렬 인터페이스는 아래 3가지 `Len(), Less(), Swap()` 메서드를 구현하면 해당 구조체를 정렬할 수 있다.

```go
func Sort(data Interface) {
	n := data.Len()
	quickSort(data, 0, n, maxDepth(n))
}

type Interface interface {
	// Len is the number of elements in the collection.
	Len() int
	// Less reports whether the element with
	// index i should sort before the element with index j.
	Less(i, j int) bool
	// Swap swaps the elements with indexes i and j.
	Swap(i, j int)
}
```

먼저 `Age` 순으로 정렬하기 위해 `ByAge type`을 정의한다. 그리고 정의한 타입에 대해서 위 3가지 메서드를 구현한다.

```go
type Employee struct {
	Name string
	Age  int
}

// ByAge implements sort.Interface based on the Age field.
type ByAge []Employee

func (a ByAge) Len() int {
	return len(a)
}

func (a ByAge) Less(i, j int) bool {
	return a[i].Age < a[j].Age
}

func (a ByAge) Swap(i, j int) {
	a[i], a[j] = a[j], a[i]
}

```

`sort.Sort()` 메서드 인자에 `family` 배열 구조체를 `model.ByAge` 타입 변환해서 정렬시킨다.

```go

func Example_Sort_Any_Collection_By_Implementing_Sort_Interface() {
	family := []model.Employee{
		{"Alice", 23},
		{"Eve", 2},
		{"Bob", 25},
	}
	sort.Sort(model.ByAge(family))
	fmt.Println(family)
	//Output:
	//[{Eve 2} {Alice 23} {Bob 25}]
}
```



### 2.4 Map 의 특정 key나 value 값으로 정렬하기

마지막으로 Map 데이터에서 특정 key나 value 값으로 정렬하는 방법에 대해서 알아보자. 아래 예제에서는 map에서 key 값만 먼저 정렬시킨 후 정렬된 key 값으로 map에서 가져오면 특정 key 값으로 정렬할 수 있다.

```go

func Example_Sort_Map_By_Key_or_Value() {
	m := map[string]int{
		"Alice": 2,
		"Cecil": 1,
		"Bob":   3,
	}

	sortKeys := make([]string, 0, len(m))

	for k := range m {
		fmt.Println("k", k)
		sortKeys = append(sortKeys, k)
	}
	sort.Strings(sortKeys) //keys로 정렬을 함

	//정렬한 keys 값으로 데이터를 출력함
	for _, k := range sortKeys {
		fmt.Println(k, m[k])
	}

	//Output:
	//Alice 2
	//Bob 3
	//Cecil 1
}
```



## 3. 마무리

다양한 방법으로 여러 데이터 타입 배열을 정렬해보았다. 여기서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-data-structure/sort)에서 확인할 수 있다.

## 4. 참고

- https://yourbasic.org/golang/how-to-sort-in-go/
- https://mingrammer.com/gobyexample/sorting-by-functions/
- https://mingrammer.com/gobyexample/sorting/
- http://pyrasis.com/book/GoForTheReallyImpatient/Unit54/01



