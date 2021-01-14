---
title: 'Getter, Setter in Go'
layout : post
category: go
author: [Frank Oh]
image: ../img/cover-go.png
date: '2021-01-14T16:05:23.000Z'
draft: false
tags: ["go", "golang", "setter", "getter", "encapsulation", "고", "고랭", "캡슐화"]
---

- setter

- - pointer reciever가 필요함
  - data validation 체크

- getter

- - go convention에 의해서 getter는 필드 이름만 사용함
  - getter의 경우에는 pointer receiver parameter가 필요없지만, 일관성을 위해 pointer reciever를 사용하자

캡슐화는 내부 속성 값을 외부에서 직접적으로 접근하게 못하게 하고 공개된 메서드들 (ex. getter, setter)로만 접근하게 한다. 내부 구현을 감추고 데이터 체크를 통해서 유효한 값만 저장

처리가 되지 않게 데이터 

data validation 체크 로직을 통해서 

# Setter

내부 속성 값을 관리할 수 있다. 



 노출되지 않게 하고 

Go에서 getter / setter를 만들어보자. 

직접적으로 외부로 부터 감추고 특정한 함수로만 접근하게 

내부 속성을 직접 변경하는 것을 방지하고 데이터 체크를 통해서 invalida

- 정보 은닉 (information hiding)
- 
- en
- 내부 
- data validation

# Getter





본 포스팅에서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-enums-iota)에서 확인할 수 있다.

# 참고

- https://www.socketloop.com/tutorials/golang-implement-getters-and-setters
- https://johngrib.github.io/wiki/golang-cheatsheet/
- https://golang.org/doc/effective_go.html?#Getters