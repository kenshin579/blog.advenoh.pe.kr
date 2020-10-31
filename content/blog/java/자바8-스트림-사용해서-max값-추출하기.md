---
title: '자바8 스트림 사용해서 max, min 값 찾기'
date: 2020-010-31 10:23:33
category: 'java'
tags: ["java", "java8", "stream", "list", "max", "min", 스트림", "자바", "자바8", "최대값", "최소값"]
---

# 1. 들어가며

자바8의 스트림 API를 사용해서 List나 배열에서 max, min 값을 찾는 방법에 대해서 알아보자. 

# 2. 스트림을 사용하여 max 값 찾기

## 2.1 숫자 List에서 Max 값 찾기


```java
@Test
public void 숫자_list_max_값_찾기() {
        List<Integer> intList = Arrays.asList(2, 3, 6, 4, 10, 23);
        Integer maxValue = intList.stream()
                .mapToInt(x -> x)
                .max()
                .orElseThrow(NoSuchElementException::new);

        assertThat(maxValue).isEqualTo(23);
}
```



## 2.2 숫자 배열에서 Max 값 찾기

```java
@Test
public void 숫자_array_max_값_찾기() {
        int[] intArr = {3, 2, 6, 10, 234};
        Integer maxValue = Arrays.stream(intArr)
                .max()
                .getAsInt();
        assertThat(maxValue).isEqualTo(234);
}
```

## 2.3 객체 List에서 특정 필드의 최대 값을 찾기

```java
@Test
public void 객체_list에서_나이가_max_값_찾기() {
        int max = 5;
        List<Student> students = IntStream.range(0, max)
                .mapToObj(i -> new Student("name" + i, i + 10))
                .peek(i -> log.info("{}", i))
                .collect(Collectors.toList());

//        Comparator<Student> comparatorByAge = (x1, x2) -> Integer.compare(x1.getAge(), x2.getAge());
        Comparator<Student> comparatorByAge = Comparator.comparingInt(Student::getAge);

        Student studentWithMaxAge = students.stream()
                .max(comparatorByAge)
                .orElseThrow(NoSuchElementException::new);

        assertThat(studentWithMaxAge.getAge()).isEqualTo(14);
}
```



## 2.3 String 배열에서 String 길이가 가장 큰 길이 찾기



```java
@Test
public void array_str에서_가장_긴_string의_길이_찾기() {
        String[] lines = {"Hello", "My", "World11"};
        int maxWidth = Arrays.stream(lines).mapToInt(String::length).max().getAsInt();
        assertThat(maxWidth).isEqualTo(7);
}
```



# 3.정리

이 포스팅에서는 자바8 스트림 API의 max(), min() 메서드를 사용하여 List나 Array에서 최대 값을 찾는 방법을 살펴 보았다. 

예제는 [Github](https://github.com/kenshin579/tutorials-java/blob/master/java8/src/test/java/com/advenoh/streams/MinMaxValueFromListTest.java) 소스를 참고해주세요. 

# 4.참고

- https://stackoverflow.com/questions/52443550/how-to-find-max-length-in-list-of-string-using-streams-in-java
- https://www.baeldung.com/java-collection-min-max
- https://codechacha.com/ko/java8-stream-max-min/
