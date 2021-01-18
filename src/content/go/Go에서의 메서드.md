---
title: 'Go에서의 메서드'
layout : post
category: go
author: [Frank Oh]
image: ../img/cover-go.png
date: '2021-01-18T21:11:23.000Z'
draft: false
tags: ["go", "golang", "method", "고", "고랭", "메서드"]
---

- method란?

- - 메서드는 함수랑 같지만, receiver 인자가 있는 함수를 말한다
  - 정의된 타입에 모든 값에 메서드를 실행할 수 있다. 

- receiver parameter ()

- - receiver parameter란?

  - - 함수 앞에 정의하는 인자
    - 다른 언어에서는 self, this를 사용하는 대신 GO에서는 receiver parameter를 사용한다

  - conventions

  - - receiver parameter 정의시 convention

    - - single letter
      - first letter of receiver's type name

  - pointer receivers

  - - *가 있는 경우
    - 자동으로 해석되는 케이스 언급

  - 메서드에서 사용할 수 있는 인자

  - - struct 타입
    - non-struct 타입이던 가능함
    - 같은 패키지 안에 정의된 것들만 다른 패키지에 있는 타입을 receive 인자로 사용 안됨

- 함수, 메서드의 pointer indirection 차이점

- - 함수

  - - 함수의 경우에는 포인터 인자는 포인터 인자만 받는다

  - 메서드

  - - value, pointer던 둘바 받을 수 있다

    - - 포인터를 value로 받으면 Go에서 자동으로 해석을 해준다

    - receiver 인자가 pointer가 아니고 호출할 때 &로 호출하며 자동으로 p.Abs() -> (*).Abs() 해석한다





```go
func(reciver_name Type) method_name(parameter_list) (return_type) {
}
```

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

