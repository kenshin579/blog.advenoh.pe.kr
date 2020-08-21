---
title: '자바8 HashMap 보다 간결하고 효과적으로 작성하기'
date: 2020-08-18 19:56:00
category: 'java'
tags: ["java", "java8", Map", "HashMap", "putIfAbsent", "computeIfAbsent", "compute", "computeIfPresent", "getOrDefault", "자바", "자바8", "맵"]
---

자바8부터 HashMap에 여러 메서드들이 추가되었다. 

- putIfAbsent() : 
- computeIfAbsent()
- compute()
- computeIfPresent()
- merge() : 

이런 메서드를 사용해서 조금 더 간결하면서 효율적으로 코드를 작성해보자

## 1. putIfAbsent() vs. computeIfAbsent()

- sdf


```java
 @Test
    public void putIfAbsent() {
        Map<String, Integer> stringLengthMap = new HashMap<>();
        stringLengthMap.put("John", 5);

        assertThat(stringLengthMap.putIfAbsent("John", 10)).isEqualTo(5); //존재하는 경우, value값을 반환한다
        assertThat(stringLengthMap.size()).isEqualTo(1);

        assertThat(stringLengthMap.putIfAbsent("John2", 10)).isNull(); //없는 경우, null로 반환하고 map에 저장함
        assertThat(stringLengthMap.size()).isEqualTo(2);
    }
```



## 2. compute() vs. computeIfPresent() vs merge()

## 3. getOrDefault()

정리 내용입니다.

# 참고

* http://tech.javacafe.io/2018/12/03/HashMap/
* https://www.baeldung.com/java-hashmap
