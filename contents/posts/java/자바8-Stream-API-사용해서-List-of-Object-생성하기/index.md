---
title: "자바8 Stream API 사용해서 List of Object 생성하기"
description: "자바8 Stream API 사용해서 List of Object 생성하기"
date: 2020-06-29
update: 2020-06-29
tags:
  - java
  - java8
  - stream
  - object
  - lambda
  - 람다
  - 자바
  - 스트림
  - 객체
---

자바8에 도입된 스트림 API에 조금 더 익숙해지기 위해 loop으로 자주 사용하던 코딩을 스트림 API로 변환해보자.

## 1. Loop 사용해서 객체 리스트 생성하기 - 자바8 이전

자바8 전 버전에서는 아래와 같은 방식으로 for loop을 사용해서 작성한다.

```java
@Test
public void generate_list_of_obj_before_Java8() {
		List<Student> students = new ArrayList<>();
		for (int i = 0; i < MAX; i++) {
			students.add(new Student("name" + i, i + 10));
		}
		assertThat(students.size()).isEqualTo(MAX);

}
```

## 2. Stream API 사용해서 객체 리스트 생성하기 - 자바8 이후

`IntStream.range()`를 사용해서 for문을 대체할 수 있다. 그리고 `mapToObj()`는 원시 스트림을 객체 스트림으로 변환해준다. 여기서는 Student 객체를 생성해서 반환하고 최종적으로 List 형으로 생성한다.

```java
@Test
public void convert_intstream_list_of_obj() {
		List<Student> students = IntStream.range(0, MAX)
				.mapToObj(i -> new Student("name" + i, i + 10))
				.collect(Collectors.toList());

		assertThat(students.size()).isEqualTo(MAX);
}
```

## 정리

for문을 대신하여 Stream API를 사용할 수 있는 간단한 예제를 같이 보았다. 다음 포스팅에도 다양한 스트림 방식으로 코딩하는 방법에 대해서 알아보자.

## 참고

* http://jtuts.com/2017/04/21/create-list-range-integers-using-java-8/
* https://stackoverflow.com/questions/22649978/java-8-lambda-can-i-generate-a-new-arraylist-of-objects-from-an-intstream

