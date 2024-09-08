---
title: "자바8 스트림 사용해서 List -> Map 형태로 변환하는 방법"
description: "자바8 스트림 사용해서 List -> Map 형태로 변환하는 방법"
date: 2020-04-20
update: 2020-04-20
tags:
  - java
  - java8
  - stream
  - list
  - map
  - 스트림
  - 자바
  - 자바8
  - 리스트
  - 맵
---


## 1. 들어가며

객체 `List`를 `Map` 형태로 변환할 때 아래와 같이 loop을 돌면서 `Map`에 내용을 채운다. 자바8에 도입된 스트림을 사용해서 `List` -> Map으로 어떻게 변환하는지 알아보자.

```java
@Test
public void convert_students_to_map_of_nameVsAge_beforeJava8() {
		int max = 3;
		List<Student> students = TestUtil.getStudentSample(max);
		Map<String, Integer> nameVsAgeMap = new HashMap<>();
		Student student;
  
		for (int i = 0; i < students.size(); i++) {
			student = students.get(i);
			nameVsAgeMap.put(student.getName(), student.getAge());
		}
		assertThat(nameVsAgeMap.size()).isEqualTo(max);
}
```

## 2. List -> Map 변환

### 2.1 자바8에서 스트림 사용하여 List에서 Map으로 변환하기

collect()는 스트림의 요소들을 우리가 원하는 자료형으로 변환해준다. Collectors 라는 라이브러리가 기본적인 메서드들을 제공해주는데 `Map` 형태로 변환해주는 toMap()을 사용해서 List -> Map으로 변환해주면 된다.

예제에서는 Map의 key, value 값이 되는 Student의 name, age를 `toMap()`의 인자로 넘겨주어 실제 `Map` 자료형으로 만들어 준다.

```java
@Test
public void convert_students_to_map_of_nameVsAge() {
		int max = 3;
		List<Student> students = TestUtil.getStudentSample(max);

		Map<String, Integer> nameVsAgeMap = students
				.stream()
				.collect(Collectors.toMap(
						i1 -> i1.getName(),
						i2 -> i2.getAge())
				);

		assertThat(nameVsAgeMap.size()).isEqualTo(max);
		log.info("nameVsAgeMap : {}", nameVsAgeMap);
}
```

메서드 참조를 통해 람다 표현 식을 더 간결하게 작성 할 수 있다.

```java
@Test
public void convert_students_to_map_of_nameVsAge_method_reference() {
   int max = 3;
   List<Student> students = TestUtil.getStudentSample(max);

   //method reference
   Map<String, Integer> nameVsAgeMap = students
         .stream()
         .collect(Collectors.toMap(
               Student::getName,
               Student::getAge)
         );

   assertThat(nameVsAgeMap.size()).isEqualTo(max);
}
```
id : Student 형태의 `Map` 자료형으로 변환해주는 예제이다.

```java
@Test
public void convert_students_to_map_of_idVsStudent() {
		int max = 3;
		List<Student> students = TestUtil.getStudentSample(max);

		Map<Integer, Student> idVsStudentMap = IntStream.range(0, max).boxed()
				.collect(Collectors.toMap(
						i1 -> i1 + 1,
						i2 -> students.get(i2)
				));

		idVsStudentMap.forEach((it, it2) -> log.info("{}", it));

		assertThat(idVsStudentMap.size()).isEqualTo(max);

}
```

### 2.2 List안에 중복 데이터가 있는 경우 - 예외 발생

List -> Map 으로 변환하는 과정에서 `Map`에 중복된 키가 있는 경우에는 `java.lang.IllegalStateException: Duplicate key` 예외가 발생한다.

```java
@Test
public void 중복키가_존재하는_경우_IllegalStateException_발생() {
		int max = 3;
		List<Student> students = TestUtil.getStudentSample(max);
		students.add(new Student("name1", 30)); //중복 이름 추가

		//throw 발생함 - java.lang.IllegalStateException: Duplicate key
		assertThatThrownBy(() -> students.stream()
				.collect(Collectors.toMap(
						Student::getName,
						Student::getAge)
				)).hasMessage("Duplicate key name1 (attempted merging values 11 and 30)");
}
```

위와 같이 중복이 발생하는 경우를 대비해서 `toMap()`의 3번째 인자에 mergeFunction 메서드를 제공할 수 있다. `MergeFunciton` 인자에는 `Map` 저장시 중복을 어떻게 처리할 지 로직을 담을 수 있다.

> `(oldValue, newValue) -> oldValue` 중복이 있는 경우에는 oldValue 값을 선택한다

```java
@Test
public void 중복키가_존재하는_경우_3rd_인자에_merge함수로_해결() {
		int max = 3;
		List<Student> students = TestUtil.getStudentSample(max);
		students.add(new Student("name1", 30)); //중복 이름 추가

		Map<String, Integer> nameVsAgeMap = students
				.stream()
				.collect(Collectors.toMap(
						Student::getName,
						Student::getAge,
						(oldValue, newValue) -> {
							log.info("oldValue : {} newValue : {}", oldValue, newValue);
							return oldValue;
						})
				);

		assertThat(nameVsAgeMap.size()).isEqualTo(max);

}
```

## 3. 마무리

자바 8의 스트림을 사용해서 List -> Map 형태로 변환해주는 방식을 알아보았다. 자바 8전의 코드 스타일보다 스트림 형태로 작성 코드들이 훨씬 더 코드를 빠르게 이해할 수 있는 장점이 있는 듯하다.

전체 소스는 [github](https://github.com/kenshin579/tutorials-java/blob/master/java8/src/test/java/com/advenoh/streams/ConvertListToMapTest.java)를 참고해주세요

## 4. 참고

* List -> Map 변환
    * https://mkyong.com/java8/java-8-convert-list-to-map/
    * https://www.baeldung.com/java-list-to-map
    * https://stackoverflow.com/questions/20363719/java-8-listv-into-mapk-v
* Stream
    * https://codechacha.com/ko/java8-stream-collect/
