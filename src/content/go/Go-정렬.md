---
title: 'Go에서 컬렉션 정렬하는 방법 (Go Sort)'
layout : post
category: 'go'
author: [Frank Oh]
image: ../img/cover-go.png
date: '2021-05-09T08:40:23.000Z'
draft: false
tags: ["go", "golang", "comparator", "sort", "고랭", "정렬"]
---

# 1. 들어가며

Go에서는 여러 컬렉션 타입에 대해서 어떤 방식으로 정렬할 수 있는지에 대해서 알아보자.

- Primitive data type에 대한 정렬
- 
- Custom comparator로 정렬
- custom data structure 정렬
- map에서 특정 key/value로 정렬
- 정렬 인터페이스를 이용한 구조체 정렬하기

# 2.Sort 3가지 방법

2.1 

```
func Example_Sort_Int_Primitive_Type() {
	list := []int{4, 2, 3, 1}
	sort.Ints(list)
	fmt.Println(list)

	//Output:
	// [1 2 3 4]
}

```



# 3. 마무리

Go에서 `...` 표기법의 여러 사용방법에 대해서 알아보았고 여기서 작성한 코드는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-three-dots)에서 확인할 수 있다. 오늘 포스팅은 여기까지... 

# 4. 참고

- https://yourbasic.org/golang/how-to-sort-in-go/
- https://mingrammer.com/gobyexample/sorting-by-functions/
- https://mingrammer.com/gobyexample/sorting/
- http://pyrasis.com/book/GoForTheReallyImpatient/Unit54/01



