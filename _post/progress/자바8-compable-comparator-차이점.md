---
title: '자바 Comparable과 Comparator의 차이점'
date: 2020-03-15 19:56:00
category: 'java'
tags: ["java", "java8", "comparator", "comparing", "comparable", "sort", "자바", "자바8", "정렬"]
---

자바에서 객체 정렬시 사용되는 Comparator와 Comparable 인터페이스간의 차이점을 알아보겠습니다. 

예제로 작성한 코드는 github [java-compare](https://github.com/kenshin579/tutorials-java/tree/master/java-compare) 모듈을 참고해주세요.

## Comparable vs. Comparator

Comparable와 Comparator 인터페이스는 컬렉션을 정렬할 때 정렬규칙을 설정하는데 사용됩니다. 

Collections.sort() 정렬시 사용되는 .... 



차이점은 아래와 같습니다. 

- Comparable
  - 정렬할 대상 객체에 Comparable 인터페이스를 implements해서 
- Comparator
  - 정렬할 대상 객체를 직접 수정할 수 없는 경우에 Comparator 인터페이스를 사용해서 정렬할 수 있다



## 정렬할 대상 객체

정렬할 대상 객체는 다음과 같습니다. 

## 

\- comparable, comparator

- compareTo(Object o) 메서드를 구현하느냐 compare(Object o1, Object o2) 메서드를 구현하느냐가 전부다.
- comparable
- - 정렬 대상 클래스에 Comparable implements을 추가하고 compareTo(Player p)를 구현하는 방법
- comparator
- - 정렬 대상 클래스의 코드를 직접 수정할 수 없을 경우, 사용한다

\- comparing은 뭔가?

- extract해서 comparator를 만들어줌??

\- 정렬되는 기준은 어떻게 되나?

- Zero : 값이 같은 경우
- negative : s1 < s2
- Positive :  s1 > s2

## 객채 정렬하기



# 참고

* https://www.baeldung.com/java-8-sort-lambda
* https://www.daleseo.com/java-comparable-comparator/
* https://www.baeldung.com/java-comparator-comparable
* https://gmlwjd9405.github.io/2018/09/06/java-comparable-and-comparator.html
* https://www.leveluplunch.com/java/tutorials/007-sort-arraylist-stream-of-objects-in-java8/
* [https://velog.io/@agugu95/Java-%EA%B0%9D%EC%B2%B4-%EC%A0%95%EB%A0%AC%EA%B3%BC-%EB%B9%84%EA%B5%90](https://velog.io/@agugu95/Java-객체-정렬과-비교)
