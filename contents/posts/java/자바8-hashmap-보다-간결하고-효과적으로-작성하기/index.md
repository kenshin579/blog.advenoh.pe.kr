---
title: "자바8 HashMap 보다 간결하고 효과적으로 작성하기"
description: "자바8 HashMap 보다 간결하고 효과적으로 작성하기"
date: 2020-02-30
update: 2020-02-30
tags:
  - java
  - java8
  - map
  - hashmap
  - compute
  - 자바
  - 자바8
  - 맵
  - putIfAbsent
  - computeIfPresent
  - compute
  - putIfAbsent
---

자바8부터 `HashMap`에 여러 메서드들이 추가되었고 이런 메서드를 사용해서 `HashMap`을 조금 더 간결하면서 효율적으로 사용하는 방법에 대해서 알아보겠습니다.

- `putIfAbsent()`
- `computeIfAbsent()`
- `compute()`
- `computeIfPresent()`
- `merge()`
- `getOrDefault()`

작성된 코드는 [java8-hashmap](https://github.com/kenshin579/tutorials-java/tree/master/java8-hashmap)을 참고해주세요.

## 1. putIfAbsent() vs. computeIfAbsent()

2가지 메서드의 공통점은 key의 존재 여부에 따라서 새로운 key와 value 값을 추가하는 메서드입니다.

#### putIfAbsent

putIfAbsent는 2개의 인자를 받습니다.

```java
default V putIfAbsent(K key, V value) 
```

- key : Map의 key 값
- value :  value 값
- 반환 값
    - key 값이 존재하는 경우
        - Map의 value 값을 반환한다
    - key 값이 존재하지 않는 경우
        - key와 value를 Map에 저장하고 null을 반환하다


```java
@Test
public void putIfAbsent() {
  Map<String, Integer> map = new HashMap<>();
  map.put("John", 5);

  assertThat(map.putIfAbsent("John", 10)).isEqualTo(5); //존재하는 경우, value값을 반환한다
  assertThat(map.size()).isEqualTo(1);

  assertThat(map.putIfAbsent("John2", 10)).isNull(); //없는 경우, null로 반환하고 map에 저장함
  assertThat(map.size()).isEqualTo(2);
}
```

#### computeIfAbsent

`computeIfAbsent` 2개의 인자를 받습니다.

```java
default V computeIfAbsent(K key, Function<? super K, ? extends V> mappingFunction)
```
- key : Map의 키 값
- mappingFunction
    - `mappingFunction` 람다 함수는 key 값이 존재하지 않을 때만 실행된다
- 반환값
    - key 값이 존재하는 경우
        - map안에 있는 value을 반환한다
    - key 값이 존재하지 않는 경우
        - Map에 새로운 key와 value(`mappingFunction` 람다 함수를 실행한 결과) 값을 저장한다


```java
@Test
public void computeIfAbsent() {
  Map<String, Integer> map = new HashMap<>();
  map.put("John", 5);

  assertThat(map.computeIfAbsent("John", key -> key.length())).isEqualTo(5); //존재하면 value값을 반환함
  assertThat(map.size()).isEqualTo(1);

  //없으면 2번째 인자 함수를 실행한 결과를 반환하고 map에도 추가가 된다
  assertThat(map.computeIfAbsent("John2", key -> key.length())).isEqualTo("John2".length());
  assertThat(map.get("John2")).isNotNull();
  assertThat(map.size()).isEqualTo(2);

  assertThat(map.computeIfAbsent("John3", key -> null)).isNull();
  assertThat(map.size()).isEqualTo(2);
}

```


## 2. compute() vs. computeIfPresent() vs merge()

3개의 메서드들은 모두 Map의 value 값을 업데이트할 때 사용됩니다.

#### compute

`compute는` key와 `remappingFunction을` 인자로 받고 key가 존재해야, value값을 인자로 넘겨준 `remappingFunction` 람다 함수의 결과로 업데이트가 됩니다. key 값이 존재하지 않는 경우에는 `NullPointerException이` 발생합니다.

```java
default V compute(K key,
        BiFunction<? super K, ? super V, ? extends V> remappingFunction)
```


```java
@Test
public void compute() {
    Map<String, Integer> map = new HashMap<>();
    map.put("john", 20);
    map.put("paul", 30);
    map.put("peter", 40);

    map.compute("peter", (k, v) -> v + 50);
    assertThat(map.get("peter")).isEqualTo(40 + 50);
}
```

#### computeIfPresent

```java
default V compute(K key,
                  BiFunction<? super K, ? super V, ? extends V> remappingFunction)
```

결과 값

- key 값이 존재하는 경우
    - `remappingFunction` 람다 함수 실행 결과로 value 값이 업데이트가 된다
- key가 존재하지 않는 경우
    - null을 반환한다

```java
@Test
public void computeIfPresent() {
  Map<String, Integer> map = new HashMap<>();
  map.put("john", 20);
  map.put("paul", 30);
  map.put("peter", 40);

  map.computeIfPresent("kelly", (k, v) -> v + 10);
  assertThat(map.get("kelly")).isNull();

  map.computeIfPresent("peter", (k, v) -> v + 10);
  assertThat(map.get("peter")).isEqualTo(40 + 10);
}
```

#### merge


```java
default V merge(K key, V value,
                BiFunction<? super V, ? super V, ? extends V> remappingFunction)
```

결과 값

- key 값이 존재하는 경우

    - Case 1 : `remappingFunction` 람다 함수의 결과가 null 아니면
        - `remappingFunction` 람다 함수 실행 결과로 value 값이 업데이트가 된다
    - Case 2 : `remappingFunction` 람다 함수의 결과가 null 이면
        - map에서 해당 key를 삭제한다

- key가 존재하지 않는 경우

    - Map에 key, value값이 추가된다



```java
@Test
public void merge() {
  Map<String, Integer> map = new HashMap<>();
  map.put("john", 20);
  map.put("paul", 30);
  map.put("peter", 40);

  //key값이 존재를 하면, 해당 key의 값을 remapping 함수의 결과 값으로 바꾼다
  map.merge("peter", 50, (k, v) -> map.get("john") + 10);
  assertThat(map.get("peter")).isEqualTo(30);

  //key가 존재하고 remapping 함수의 결과가 null이면 map에서 해당 key를 삭제한다
  map.merge("peter", 30, (k, v) -> map.get("nancy"));
  assertThat(map.get("peter")).isNull();
  assertThat(map.size()).isEqualTo(3);

  //key가 존재하지 않으면 key, value값을 추가함
  map.merge("kelly", 50, (k, v) -> map.get("john") + 10);
  assertThat(map.get("kelly")).isEqualTo(50);
  assertThat(map.size()).isEqualTo(4);

}
```

## 3. getOrDefault()

`getOrDefault` 가 반환하는 값은 아래와 같습니다.

```java
default V getOrDefault(Object key, V defaultValue)
```

- key 값이 존재하는 경우
    - Map의 value값을 반환한다
- key 값이 존재하지 않는 경우
    - `defaultValue`을 반환한다

```java
 @Test
public void getOrDefault() {
  String str = "aagbssdf";
  Map<Character, Integer> map1 = new HashMap<>();
  Map<Character, Integer> map2 = new HashMap<>();

  //getOrDefault 사용하지 않는 경우
  for (char c : str.toCharArray()) {
    if (map2.containsKey(c)) {
      map2.put(c, map2.get(c) + 1);
    } else {
      map2.put(c, 1);
    }
  }

  //getOrDefault 사용하는 경우
  for (char c : str.toCharArray()) {
    map1.put(c, map1.getOrDefault(c, 0) + 1);
  }

  assertThat(map1).isEqualTo(map2);
}
```

## 참고

* http://tech.javacafe.io/2018/12/03/HashMap/
* https://www.baeldung.com/java-hashmap
* https://docs.oracle.com/javase/8/docs/api/java/util/Map.html
