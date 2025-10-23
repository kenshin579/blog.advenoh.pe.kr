---
title: "새로운 기능 및 개선 사항 목록 - 자바 Beyond에서의 변화"
description: "새로운 기능 및 개선 사항 목록 - 자바 Beyond에서의 변화"
date: 2018-09-10
update: 2018-09-10
tags:
  - java
  - upgrade
  - JEP
  - 자바
  - 개선사항
---

## 자바 Beyond

- JEP 301: Enhanced Enums - 현재 보류중

- JEP 302: Lambda Leftovers - Candidate

- JEP 305: Pattern Matching - Candidate
- JEP ???: Data Classes
- JEP 312: Switch Expressions - Proposed to Target (JDK12)
- JEP 326: Raw String Literals - Candidate

자바의 릴리스 주기가 6개월로 변경되면서 새로운 기능, 개선사항들이 빠르게 반영될 것으로 기대하고 있습니다. 아직 반영되지는 않았지만, 추후 자바 버전에서 반영될 것으로 기대되는 부분을 정리해보았습니다.

## JEP 301: Enhanced Enums - 현재 보류 상태

이 제안 문서는 현재 보류된 상태입니다. 나중에 도입될 수 있어서 어떤 개선 사항인지 간단하게 알아봅니다.
Enum에서도 제너릭을 지원하고 Enum에 정의된 상수 값에 대해 보다 정교한 타입(shaper type)을 지원하는 것입니다.
참고로, Enum은 자바5에 추가된 기능으로 JVM에서는 Enum에 대한 별로의 처리는 없고 컴파일러가 Enum을 일반 클래스로 변환합니다.
개선전
개선후

```java
//개선전
enum Bar {
  ONE,
  TWO
}

//개선후
enum Bar<X> {
  ONE<>(String.class),
  TWO<>(Integer.class);

  Bar(X x) { ... }
}

Class<String> cs = Bar.ONE.getClazz(); //uses shaper typing of enum constant
```

### 참고

- Enum 개선사항
    - [http://openjdk.java.net/jeps/301](http://openjdk.java.net/jeps/301)
    - [https://www.infoq.com/news/2017/01/java-enhanced-enums](https://www.infoq.com/news/2017/01/java-enhanced-enums)

## JEP 302: Enhancements to Lambda Expressions : Lambda Leftovers - 상태: Candidate

### 1. 사용하지 않는 lambda 인자를 underscore로 표현

람다 인자에서 사용되지 않는 변수는 underscore로 표현해 가독성을 높여주는 기능입니다.

```java
//개선전
Map<String, Integer> numbers = new HashMap<>();
numbers.forEach(( **k**, v) -> System.out.println(v*2)); k를 사용하지 않음

개선후
numbers.forEach(( **\_**, v) -> System.out.println(v*2));
```

### 2. 인자 은닉화

변수 은닉화(variable shadowing)란 inner 스코프에서 정의된 변수가 outer 스코프에서 정의된 동일한 변수 이름을 가지는 경우를 일컫습니다.

```java
public class Shadow {
    private int value = 0;

    public void shadowTheVar(){
        int value = 5; //위 field의 값은 숨겨지게 됨
    }
}
```

인자 은닉화 개선 내용은 Inner 스코프에서도 동일한 변수를 선언할 수 있도록 하는 것입니다.

```java
//개선전
String s = "hello";

if(finished) {
    String s = "bye"; // 오류, s 변수는 이미 선언됨
}

Predicate<String> ps = s -> s.isEmpty(); // 오류, s 변수는 이미 선언됨
  

//개선후
Map<String, Integer> map = /* ... */
String key = "theInitialKey";

map.computeIfAbsent(key, _ -> {
   String key = "theShadowKey"; // 이게 가능해짐
   return key.length();
});
```

### 3. 옵션: 함수 호출에 대한 명확성에 대한 개선\*\*

오버로딩된 여러 메서드를 호출할 타임을 명시하지 않아도 컴파일러가 알아서 잘 추론하여 컴파일 해주는 기능입니다.

```java
//개선전
private void m(Predicate<String> ps) { /* ... */ }
private void m(Function<String, String> fss) { /* ... */ }

private void callingM() {
    m((String s) -> s.isEmpty()); //타입으로 바로 알 수 있음

    m(s -> s.isEmpty()); //컴파일러는 어떤 메서드를 호출할지 모름
}

//개선후
private void m(Predicate<String> ps) { /* ... */ }
private void m(Function<String, String> fss) { /* ... */ }

private void callingM() {
    m(s -> s.isEmpty()); //가능하게 하겠다. 
}
```

### 참고

- 람다 개선 작업
    - [http://openjdk.java.net/jeps/302](http://openjdk.java.net/jeps/302)
    - [https://www.infoq.com/news/2017/01/java10-lambda-leftovers](https://www.infoq.com/news/2017/01/java10-lambda-leftovers)

## JEP ???: Data Classes

데이터 클라스란 데이터를 담고 로직 구현이 없는 순수한 데이터 객체를 말합니다. 데이터 속성에 접근하기 위한 여러 메서드(ex. getter, setter)를 가집니다. DTO(Data Transfer Object)나 VO(Value Object)이라고도 합니다.

데이터 클라스 작성하려면 기본적으로 getter, setter, equals, hashCode등과 같은 메서드를 개발자가 만들어줘야 했는데, 이 JEP에서 제안하는 것은 컴파일러가 알아서 생성하도록 하는 기능입니다. 이 아이디어는 스칼라의 case, 코틀린의 데이터 클래스에서 가져왔습니다.

- Scala - 케이스 클래스
    - case class Coordinate (lat: Double, lon : Double)
- Kotlin - 데이터 클래스
    - data class Coordinate(val lat: Double, val lon: Double)

```java
//개선전
public class Coordinate {
    private double lat;
    private double lon;
    public Coordinate(double lat, double lon) {
    this.lat = lat;
    this.lon = lon;
    }
// Getters/Setters, toString(), equals(), hashCode(), etc. 필요
}

//개선후
//자바 데이터 클래스 (제안)
record Coordinate(double lat, double lon) {}
```

자바 데이터 클래스 (제안)
record Coordinate(double lat, double lon) {}
데이터 클래스를 지원함으로써 코드도 더 간결해지는 장점도 생기게 됩니다. 객체 패턴 매칭(JEP 305)을 지원하면 더 쉽고 빠르게 코드를 작성할 수 있게 됩니다.

```java
interface Shape { }
record Point(int x, int y);
record Rect(Point p1, Point p2) implements Shape;
record Circle(Point center, int radius) implements Shape;

switch (shape) {
     case Rect(Point(var x1, var y1), Point(var x2, var y2)): ...
     case Circle(Point(var x, var y), int r): ...
     ....
}
```

### 참고

- 데이터 객체
    - [https://refactoring.guru/smells/data-class](https://refactoring.guru/smells/data-class)
    - [https://jungwoon.github.io/common%20sense/2017/11/16/DAO-VO-DTO/](https://jungwoon.github.io/common%20sense/2017/11/16/DAO-VO-DTO/)
    - [http://cr.openjdk.java.net/~briangoetz/amber/datum.html](http://cr.openjdk.java.net/~briangoetz/amber/datum.html)
    - [https://www.infoq.com/news/2018/02/data-classes-for-java](https://www.infoq.com/news/2018/02/data-classes-for-java)
- 다른 언어
    - [https://www.baeldung.com/kotlin-data-classes](https://www.baeldung.com/kotlin-data-classes)

## JEP 305 : Pattern Matching - Candidate

이 JEP에서는 matches 키워드를 도입하고 switch 패턴 매칭 개선 작업을 다루고 있습니다.

컴파일러는 **x matches Integer i** 구문을 개선전의 코드(아래코드)로 인식합니다.
**Integer i** 문은 **type test pattern** 이라고 하고 i은 새로운 변수의 선언으로 인식합니다.
타켓 변수(ex. obj)가 Integer 인스턴스이면 Integer로 캐스팅하고 i 변수를 블록에서 사용할 수 있는 코드로 해석합니다.

```java
//개선전
String formatted = "unknown";
if (obj instanceof Integer) {
    int i = (Integer) obj;
    formatted = String.format("int %d", i);
} else if (obj instanceof Byte) {
    byte b = (Byte) obj;
    formatted = String.format("byte %d", b);
} else if (obj instanceof Long) {
    long l = (Long) obj;
    formatted = String.format("long %d", l);
} else if (obj instanceof Double) {
    double d = (Double) obj;
    formatted = String.format(“double %f", d);
} else if (obj instanceof String) {
    String s = (String) obj;
    formatted = String.format("String %s", s);
}

//개선후
String formatted = "unknown";
if (obj matches Integer i) {
    formatted = String.format("int %d", i);
} else if (obj matches Byte b) {
    formatted = String.format("byte %d", b);
} else if (obj matches Long l) {
    formatted = String.format("long %d", l);
} else if (obj matches Double d) {
    formatted = String.format(“double %f", d);
} else if (obj matches String s) {
    formatted = String.format("String %s", s);
}
```

기존 자바에서의 switch문은 Number, String, Enum만 매칭이 가능했는데, 이 개선작업이 포함되면 객체도 매칭이 가능해집니다.

```java
String formatted;
switch (obj) {
    case Integer i: formatted = String.format("int %d", i); break;
    case Byte b:    formatted = String.format("byte %d", b); break;
    case Long l:    formatted = String.format("long %d", l); break;
    case Double d:  formatted = String.format(“double %f", d); break;
    default:        formatted = String.format("String %s", s);
}
```

### 참고

- 개선작업
    - [http://openjdk.java.net/jeps/305](http://openjdk.java.net/jeps/305)
    - [http://cr.openjdk.java.net/~briangoetz/amber/pattern-match.html](http://cr.openjdk.java.net/~briangoetz/amber/pattern-match.html)
