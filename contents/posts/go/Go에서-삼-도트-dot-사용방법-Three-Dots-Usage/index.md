---
title: "Go에서 삼 도트 (dot) 사용방법 (Three Dots Usage)"
description: "Go에서 삼 도트 (dot) 사용방법 (Three Dots Usage)"
date: 2021-05-08
update: 2021-05-08
tags:
  - go
  - golang
  - dot
  - three
  - 점
  - 고랭
  - 도트
  - 표기법
---

## 1. 들어가며

Go에서 `...` 삼 도트(dot) 사용법에 대해서 알아보자. Go에서는 아래 4가지 방법으로 사용된다.

- 함수의 인자에 가변 인자로 선언하는 경우
- 가변 인자를 인자로 받는 함수에 slice를 넘겨주는 경우
- 배열 리터럴에서 길이 지정하는 경우
- Go 명령어 wildcard로 사용하는 경우

## 2.삼 도트 사용법에 대해서 알아보자

### 2.1 함수의 인자에 가변 인자로 선언하는 경우

```go
func sum(nums ...int) int {
	res := 0
	for _, n := range nums {
		res += n
	}
	return res
}
```

`sum` 함수에 가변 인자를 넘겨주기 위해서는 인자 선언시 `...int`로 선언하면 가변인자가 된다.

```go
func Example_가변인자_함수() {
	total1 := sum(1, 2, 3)
	total2 := sum(1, 2)
	fmt.Println(total1)
	fmt.Println(total2)

	//Output:
	//6
	//3
}
```

`sum` 함수 호출시 인자 값을 2, 3개로 자유롭게 넘겨줄 수 있게 된다.



### 2.2 가변 인자를 인자로 받는 함수에 slice를 넘겨주는 경우

```go
func Example_가변인자_함수에_전달하기() {
	numList := []int{2, 3, 5, 6}
	fmt.Println(sum(numList[0], numList[1], numList[2], numList[3]))
	//...표기법을 통해서 가변인자에 unpack해서 전달할 수 있다
	fmt.Println(sum(numList...))

	//Output:
	//16
	//16
}
```

`sum` 함수는 가변인자로 선언되어 있기 때문에 `sum(1,2,3)`으로 넘겨줘야 하는데, 슬라이스로 선언된 컬렉션을 하나하나 입력하기는 매우 불편한다. 그래서 Go에서는 `slice...` 슬라이스 뒤에 3개의 도트 표기법을 사용하면 Go에서 가변인자에 unpack을 해서 전달해준다.

### 2.3 배열 리터럴에서 길이 지정하는 경우

```go
func Example_array_literal() {
	//배열 리터럴에서 ... 표기법은 리터럴의 요소 수와 동일한 길이를 지정한다
	strList := [...]string{"Frank", "Joe", "Angela"}
	fmt.Println(len(strList))

	//Output: 3
}
```

배열 리터럴에서 `...` 표기법을 사용하면 리터럴의 요소 수와 동일하게 길이를 지정이 된다.



### 2.4 Go 명령어 wildcard로 사용하는 경우

```bash
# 패키지 목록을 지정할 때 ...표기법은 패키지 목록을 wildcard로 사용된다
$ go test ./...
```

Go 명령에서 `...` 표기법은 패키지 목록을 wildcard로 사용하겠다는 의미를 가지고 있다. 위 명령어는 현재 폴더에서 모든 폴더에 있는 테스트 파일을 실행하라는 의미이다.

## 3. 마무리

Go에서 `...` 표기법의 여러 사용방법에 대해서 알아보았고 여기서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-three-dots)에서 확인할 수 있다. 오늘 포스팅은 여기까지...

## 4. 참고

- https://yourbasic.org/golang/three-dots-ellipsis/
- https://blog.learngoprogramming.com/golang-variadic-funcs-how-to-patterns-369408f19085
- https://golangbot.com/variadic-functions/

