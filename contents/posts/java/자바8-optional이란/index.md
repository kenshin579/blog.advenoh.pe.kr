---
title: "자바8 Optional이란"
description: "자바8 Optional이란"
date: 2018-07-29
update: 2018-07-29
tags:
  - java
  - java10
  - jdk
  - optional
  - openjdk
  - 자바
  - 자바8
series: "자바8"
---

## 1. Optional이란

Optional은 null을 대신하기 위해 만들어진 새로운 코어 라이브러리 데이터 타입입니다. Optional 클래스는 null이나 null이 아닌 값을 담을 수 있는 클래스입니다. 이미 다른 언어(ex. Scala)에 존재하는 기능으로 자바에서는 JDK8에 포함 되었습니다. 기존에 null을 사용하면 어떤 문제점이 있고 Optional을 통해서 어떻게 코드가 개선되는지 알아봅시다.

자바로 개발하다 보면 NullPointerException(NPE)을 자주 만나게 됩니다. 아래 코드와 같이 객체가 null이고 null이 된 값을 쓰게 되면 NPE가 발생합니다.

```java
@Test(expected = NullPointerException.class)
public void testOldJavStyle_throw_NPE() {
    String str = null;
    System.out.println(str.charAt(0)); //NPE 발생
}
```

NPE를 해결하기 위해서는 null에 대한 조건문을 추가해야 합니다. Null은 값이 없음을 나타내려는 의도로 개발되었지만, null를도입함으로써 코드의 가독성이 많이 떨어지고 유지보수가 어렵다는 문제점만 가지게 되었습니다. Optional 클래스를 사용하면 코드가 어떻게 달라지는지 확인해보겠습니다. Null 체크하는 조건문이 없어지면서 코드가 훨씬 깔끔해집니다.

```java
//null 조건문
@Test
public void testOldJavStyle_checkNull() {
    String str = "test";
    if (str != null) {
        System.out.println(str.charAt(0));
    }
}

//Optional 사용
@Test
public void testOptionalJavaStyle_checkNull() {
    String str = "test";
    Optional<String> optStr = Optional.ofNullable(str);
    optStr.ifPresent(s -> System.out.println(s.charAt(0)));
}
```

## 2. Optional 사용해보기

### 2.1 Optional 객체 생성하기

Optional 클래스에서는 3가지 정적 팩토리 메서드를 제공합니다.

- Optional.empty() : 빈 Optional 객체 생성한다
- Optional.of(value) : value값이 null이 아닌 경우에 사용한다
- Optional.ofNullable(value) : value값이 null인지 아닌지 확실하지 않은 경우에 사용한다

**1. Optional.empty()**

```java
Optional<String> optStr = Optional.empty();
```

Optional.empty()는 empty Optional 객체를 생성합니다.

**2. Optional.of(value)**

```java
String str = "test";
Optional<String> optStr1 = Optional.of(str);
```

Optional.of()는 null이 아닌 객체를 담고 있는 Optional 객체를 생성합니다.

null이 아닌 객체를 생성하기 때문에 null을 넘겨서 생성하면 NPE이 발생하게 됩니다.

```java
String nullStr = null;
Optional<String> optStr2 = Optional.of(nullStr); NPE 발생
```

**3. Optional.ofNullable(value)**

```java
String str = "test";
Optional<String> optStr1 = Optional.ofNullable(str);
```

null인지 아닌지 확신할 수 없는 객체를 담고자 할 때Optional.ofNullable()를 통해서 Optional 객체를 생성합니다.

null이 넘어 올 경우에는 empty Optional 객체를 생성합니다.

```java
Optional<String> optStr2 = Optional.ofNullable(null); //empty Optional 객체를 반환함
```

### 2.3 Optional이 담고 있는 객체에 접근 및 사용방법

Optional이 담고 있는 객체에 접근하는 여러 메서드의 사용방법에 대해서 알아보겠습니다.

- ifPresent(함수)
- null인 경우에 default 값 반환
    - orElse(T other) : 비어 있으며 인자를 반환한다
    - orElseGet(Supplier<? extends T> other) : 함수형 인자의 반환값을 반환한다
- null인 경우에 예외를 throw
    - orElseThrow(Supplier<? extends X> exceptionSupplier) : 인자 함수에서 생성된 예외를 던진다

**1. IfPresent(함수)**
Optional 객체가 non-null이 경우에 인자로 넘긴 함수를 실행하는 메서드입니다. Optional 객체가 null이면 인자로 넘긴 함수는 실행되지 않습니다.

```java
@Test
public void test_1_otional_usage_ifPresent() {
    String str = "test";
    Optional<String> optStr1 = Optional.ofNullable(str);
    optStr1.ifPresent(s -> System.out.println(s.charAt(0))); t 프린트

    Optional<String> optStr2 = Optional.ofNullable(null);
    optStr2.ifPresent(s -> System.out.println(s.charAt(0))); print 안됨
}
```

**2. orElse**
Optional에 담고 있는 객체가 null이 경우에 대신할 수 있는 값을 반환하는 메서드입니다.

```java
@Test
public void test_2_otional_usage_orElse() {
    Optional<String> optStr = Optional.ofNullable(null);
    String result = optStr.orElse("test"); //null이면 test를 반환함
    System.out.println(result); //test
}
```

**3. orElseGet**
orElse와 유사하지만, 다른 점은 메서드를 인자로 받고 함수에서 반환한 값을 반환하게 되어 있습니다.

```java
@Test
public void test_2_otional_usage_orElseGet() {
    Optional<String> optStr = Optional.ofNullable(null);
    String result = optStr.orElseGet(this::getDefaultValue);
    System.out.println(result); //default
}

private String getDefaultValue() {
    LOG.info("calling getDefaultValue");
    return "default";
}
```

**4. orElse와 orElseGet의 차이점**
결과적으로 사용하는데 orElse와 orElseGet의 차이점이 없어 보이지만, 아래 코드를 보면 orElseGet()의 경우에는 null인 경우에만 인자로 넘긴 함수가 실행되는 것을 알 수 있습니다. orElse 메서드 사용 시에만 주의하면 됩니다.

```java
@Test
public void test_optional_usage_diff_orElse_orElseGet() {
    String str = "test";
    String result1 = Optional.ofNullable(str).orElse(getDefaultValue()); null이 아니여도 getDefaultValue() 함수는 실행함
    LOG.info("orElse result: {}", result1);

    String result2 = Optional.ofNullable(str).orElseGet(this::getDefaultValue); getDefaultValue() 실행하지 않음
    LOG.info("orElseGet result: {}", result2);
}
```

![](image_1.png)

**5. orElseThrow**
null인 경우에 기본 값을 반환하는 대신 예외를 던질 수 있습니다.

```java
@Test(expected = IllegalArgumentException.class)
public void test_3_optional_usage_orElseThrow() {
    String str = null;
    String result = Optional.ofNullable(str).orElseThrow(IllegalArgumentException::new);
    LOG.info("result {}", result);
}
```

## 3. Stream에서 Optional 사용법

### 3.1 filter(Predicate) : 조건에 따라 요소들 필터링하기

filter()는 인자로 받은 Predicate 함수의 결과가 true인 모든 요소만을 새로운 스트림으로 반환하는 Stream API입니다. 즉, 조건에 맞는 것만 필터링한다고 이해하시면 됩니다. Optional 없이 구현한 버전과 Optional을 사용한 예제입니다.





```java
//Optional 없이 사용
private boolean isLastNameFrank(Person person) {
    if (person != null && person.getLastName() != null) {
        return person.getLastName().toLowerCase().equals("frank");
    }
    return false;
}

//Optional 사용
private boolean isLastNameFrank(Person person) {
    return Optional.ofNullable(person)
    .map(Person::getLastName)
    .map(String::toLowerCase)
    .filter(s -> s.equals("frank")).isPresent();
}
```

```java
@Test
public void test_1_stream_usage_filter_with_optional() {
    Map<Person, Boolean> personVsExpectedMap = new HashMap<Person, Boolean>() {{
        put(new Person("Frank", "Oh"), true); **Person 객체와 기대 결과를 저장함**
        put(new Person(null, "Oh"), false);
        put(new Person("David", "Oh"), false);
        put(new Person("John", "Oh"), false);
    }};

    boolean expectedResult;
    for (Person person : personVsExpectedValueMap.keySet()) {
        expectedResult = personVsExpectedValueMap.get(person);
        assertEquals(expectedResult, **isLastNameFrank** (person));
    }
}
```



Stream의 여러 API를 더 잘 이해하기 위해서는 실제 구현 코드를 보면 람다 함수가 내부적으로 어떻게 호출되는지 이해하기가 더 쉽습니다. filter는 Predicate 함수를 인자로 넘겨주고 스트림에서Predicate으로 넘긴 함수를 실행하고 그 결과가 true이면 스트림의 this를 넘기고 아닌 경우에는 실제 반환하는 결과는 Optional 타입임을 확인할 수 있습니다.

```java
@Test
public void test_1_stream_usage_filter_with_optional() {
    Map<Person, Boolean> personVsExpectedMap = new HashMap<Person, Boolean>() {{
        put(new Person("Frank", "Oh"), true); **Person 객체와 기대 결과를 저장함**
        put(new Person(null, "Oh"), false);
        put(new Person("David", "Oh"), false);
        put(new Person("John", "Oh"), false);
    }};

    boolean expectedResult;
    for (Person person : personVsExpectedValueMap.keySet()) {
        expectedResult = personVsExpectedValueMap.get(person);
        assertEquals(expectedResult, **isLastNameFrank** (person));
    }
}
```

참고로 Predicate<? super T>의 의미는 Predicate의 유형 매개변수가 T 또는 T의 상위유형이어야 한다는 의미이다. T에 들어갈 수 있는 lower bound가 정해집니다. 예를 들면, List<? super Integer>인 경우에는 List<Integer>, List<Number>, List<Object>가 포함됩니다. Integer 클래스는 Number와 Object를 상속받은 자식 클래스입니다. 제네릭에 대한 더 자세한 내용은 [StackOverflow](https://stackoverflow.com/questions/2827585/what-is-super-t-syntax) 를 참조해주세요.

### 3.2 map() : 요소들의 값 형태 변환하기

**map(Function<? super T,? extends R> mapper)**

map()은 요소 값의 형태를 변환하는 Stream API입니다. 아래 코드에서는 String 리스트를 Optional로 랩핑해서 map으로 size를 얻어올 수 있습니다. null인 경우에는 orElse() 메서드로 default 값을 반환합니다.

```java
@Test
public void test_2_stream_usage_map_with_optional() {
    List<String> strArray = Arrays.asList("frank", "angela", "david");
    Optional<List<String>> optArray = Optional.of(strArray);

    int size = optArray
          .map(List::size) //map에서 list를 size로 변환함
          .orElse(0);
    assertEquals(3, size);

    optArray = Optional.ofNullable(null);
    size = optArray.map(List::size).orElse(1);
    assertEquals(1, size);
}

```

filter() 함수의 경우에는 Predicate 함수 인터페이스이기 때문에 결과를 boolean을 반환해야 하지만, map() 함수는 Function 함수 인터페이스를 사용하기 때문에 여러 형태의 결과로 반환할 수 있습니다. 코드에서는 List를 int 형태로 변환해서 반환합니다.

```java
@FunctionalInterface
public interface Function<T, R> {
    R apply(T t); //R 타입을 반환함<
   ...(생략)...
}
```

### 3.3 flatMap() : 요소를 flat하고나서 map으로 값 형태를 반환하기

```java
flatMap(Function<? super T,? extends Stream<? extends R>> mapper)
```

flatMap의 경우에는 요소가 Primitive 타입이 아니라 여러 Optional<Optional>>으로 된 타입인 경우에는 flatMap을 사용해야 합니다. Optional의 외에 Stream인 경우에도 [[1,2,3], [2,3,4]]이런 형태의 데이터는 flatMap을 사용해서 처리합니다. 더 자세한 설명은 아래 링크를 참조해주세요 (Map Vs. FlatMap)

```java
@Test
public void test_3_stream_usage_flatMap() {
    PersonOpt person = new PersonOpt("Oh", "Frank");
    Optional<PersonOpt> personOpt = Optional.of(person);

    Character firstCharOfFirstName = personOpt
            .flatMap(PersonOpt::getFirstName) //getFirstName의 반환값이 Optional이기 때문에 flatMap을 사용해야 함
            .map(s -> s.charAt(0)) //요소가 pritimive 타입이기 때문에 map을 사용함
            .orElse('0');
    assertEquals(new Character('F'), firstCharOfFirstName);
}
```



## 4. 자바9에 추가된 Optional 메서드

JDK9에서 3가지 메서드가 추가되었습니다. 각각 기존 사용을 알아봅시다.

- or() : Optional이 empty인 경우에 다른 Optional을 반환한다

- ifPresentOrElse() : Optional에 값이 존재하면 action 수행하고 아닌 경우에는 else 부분을 수행한다

- stream() : Optional 객체를 Stream 객체로 변환하기 위해 사용된다



### 4.1 or() : Optional이 empty인 경우에 다른 Optional을 반환

JDK9 이전에는 Optional 객체가 empty이면 orElse()나orElseGet()을 사용해서 default 값을 반환했습니다. JDK9부 터는 or() 메서드로 Optional이 empty이면 값 대신 다른 Optional을 반환하는 메서드가 추가되었습니다. 예제를 보면 더 쉽게 이해할 수 있습니다.

```java
@Test
public void test_jdk9_optional_or() {
    String str = null;
    Optional<String> defaultOpt = Optional.of("default");
    Optional<String> strOpt = Optional.ofNullable(str);

    Optional<String> result = strOpt.or(() -> defaultOpt); //default optional을 반환함
    assertEquals("default", result.get());
}
```

### 4.2 ifPresentOrElse() : Optional에 값이 존재하면 action 수행하고 아닌 경우에는 else 부분을 수행

JDK9이전에는 IfPresent 메서드만 있었다면 JDK9부터는 Optional이 empty인 경우에 Else로 추가되어 많이 편리해졌습니다.

```java
@Test
public void test_jdk9_ifPresentOrElse() {
    String str = null;
    Optional<String> strOpt = Optional.ofNullable(str);
    strOpt.ifPresentOrElse(
            s -> System.out.println("string : " + s),
            () -> System.out.println("null value”) //empty인 경우에 이 부분 수행됨
    );
}}
```



## 4.3 stream() : Optional 객체를 Stream 객체로 변환하기 위해 사용

JDK8에 추가된 Stream은 여러 API를 통해 collection을 함수형 방식으로 쉽게 조작이 가능하게 하는 기능입니다. Optional에 stream()을 추가함으로써 기존의 Stream API를 사용 할 수 있게 되었습니다. 이 예제에서는 Optional을 Stream으로 변경한이후 Stream의 함수를 사용한 예제입니다.

```java
@Test
public void test_jdk9_stream() {
    String str = "frank";
    Optional<String> strOpt = Optional.of(str);
    strOpt.stream().map(String::toUpperCase).forEach(System.out::println);
}
```



## 5. 참고

포스팅 작성된 소스 코드는 [github](https://github.com/kenshin579/tutorials-java-examples/tree/master/java-optional) 에서 확인가능합니다.

- 함수형 인터페이스
![](image_2.png)
![](image_3.jpeg)

- Scala에서 Option
    - [https://danielwestheide.com/blog/2012/12/19/the-neophytes-guide-to-scala-part-5-the-option-type.html](https://danielwestheide.com/blog/2012/12/19/the-neophytes-guide-to-scala-part-5-the-option-type.html)
- Optional 사용법
    - [http://www.daleseo.com/java8-optional-after/](http://www.daleseo.com/java8-optional-after/)
    - [https://softwareengineering.stackexchange.com/questions/364211/why-use-optional-in-java-8-instead-of-traditional-null-pointer-checks](https://softwareengineering.stackexchange.com/questions/364211/why-use-optional-in-java-8-instead-of-traditional-null-pointer-checks)
    - [https://www.baeldung.com/java-optional](https://www.baeldung.com/java-optional)
- Streams
    - [https://m.blog.naver.com/PostView.nhn?blogId=2feelus&logNo=220695347170&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F](https://m.blog.naver.com/PostView.nhn?blogId=2feelus&logNo=220695347170&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)
- Generis syntax
    - [https://stackoverflow.com/questions/2827585/what-is-super-t-syntax](https://stackoverflow.com/questions/2827585/what-is-super-t-syntax)
- Map vs FlatMap
    - [https://code.i-harness.com/ko-kr/q/1972c92](https://code.i-harness.com/ko-kr/q/1972c92)
    - [https://jaepils.github.io/java/2018/06/27/java-time-Instant.html](https://jaepils.github.io/java/2018/06/27/java-time-Instant.html)
- JDK9 optional
    - [https://www.baeldung.com/java-9-optional](https://www.baeldung.com/java-9-optional)
    - [https://aboullaite.me/java-9-enhancements-optional-stream/](https://aboullaite.me/java-9-enhancements-optional-stream/)
