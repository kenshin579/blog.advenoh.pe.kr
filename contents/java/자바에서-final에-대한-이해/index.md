---
title: "자바에서 final에 대한 이해"
description: "자바에서 final에 대한 이해"
date: 2018-09-11
update: 2018-09-11
tags:
  - final
  - java
  - 자바
---

## 1. 개요

```java
final int MAX = 5;
```

위와 같이 final 키워드를 떠올릴 때면 그냥 상수로만 생각할 때가 종종 있습니다. final을 클래스, 메서드, 변수에 선언하면 조금씩 할 수 있는 부분들이 제안됩니다. 너무 당연한 내용이지만, 시간이 지니니까 기억에서 사라져버려서 이번에 다시 한번 상기하기 위해 정리를 해보았습니다.

자바에서 final 키워드는 여러 컨텍스트에서 단 한 번만 할당될 수 있는 entity를 정의할 때 사용됩니다. ( [위키피니아](https://en.wikipedia.org/wiki/Final_%28Java%29) )

final 키워드는 총 3가지에 적용할 수 있습니다. 각각에 대해서 세부적으로 알아보죠.

- final 변수
    - 원시 타입
    - 객체 타입
    - 클래스 필드
    - 메서드 인자
- final 메서드
- final 클래스

## 2. Final 변수

### 2.1 원시 타입

로컬 원시 변수에 final로 선언하면 한번 초기화된 변수는 변경할 수 없는 상수값이 됩니다.

```java
@Test
    public void test_final_primitive_variables() {
    final int x = 1;
    x = 3; //한번 assign되면 변경할 수 없음.
}
```

### 2.2 객체 타입

객체 변수에 final로 선언하면 그 변수에 다른 참조 값을 지정할 수 없습니다. 원시 타입과 동일하게 한번 쓰여진 변수는 재변경 불가합니다. **단, 객체 자체가 immutable하다는 의미는 아닙니다**. 객체의 속성은 변경 가능합니다.

```java
@Test
public void test_final_reference_variables() {
    final Pet pet = new Pet();
    pet = new Pet(); 다른 객체로 변경할수 없음
    pet.setWeight(3); //객체 필드는 변경할 수 있음
}
```

### 2.3 메서드 인자

메서드 인자에 final 키워드를 붙이면, 메서드 안에서 변수값을 변경할 수 없습니다.

```java
public class Pet {
    int weight;
    public void setWeight(final int weight) {
        weight = 1; //final 인자는 메서드안에서 변경할 수 없음
    }
}
```

### 2.4 맴버 변수

클래스의 맴버 변수에 final로 선언하면 상수값이 되거나 write-once 필드로 한 번만 쓰이게 됩니다. final로 선언하면 초기화되는 시점은 생성자 메서드가 끝나기 전에 초기화가 됩니다. 하지만, static이냐 아니냐에 따라서도 초기화 시점이 달라집니다.

- static final 맴버 변수 (static final int x = 1)
    - 값과 함께 선언시
    - 정적 초기화 블록에서 (static initialization block)
- instance final 맴버 변수 (final int x = 1)
    - 값과 함께 선언시
    - 인스턴스 초기화 블록에서 (instance initialization block)
    - 생성자 메서드에서

#### 2.4.1 인스턴스 초기화 블록 vs 정적 초기화 블록

정적 초기화 블록과 인스턴스 초기화 블록의 차이점을 간단하게 알아봅니다.

| 인스턴스 초기화 블록                                         | 정적 초기화 블록                   |
| ------------------------------------------------------------ | ---------------------------------- |
| 객체 생성할때마다 블록이 실행됨 <br />부모 생성자이후에 실행됨 <br />생성자보다 먼저 실행됨 | 클래스 로드시 한번만 블록이 실행됨 |



```java
@Test
public void initializeBlockTest() {
    Cat.s_value = 5; static //초기화 블록 호출됨
    System.out.println("s_value: " + Cat.s_value);

    System.out.println("");
    System.out.println("Cat 객체 생성1");
    Cat cat1 = new Cat();

    System.out.println("");
    System.out.println("Cat 객체 생성2");
    Cat cat2 = new Cat();
    }

    public class Pet {
    public Pet() {
        System.out.println("super construtor : Pet");
    }
}
```

실행결과는 다음과 같습니다. 정적 초기화 블록은 클래스가 로딩되는 시점에 한 번만 호출되고 static 블록 안에서 static 맴버변수를 초기화 할 수 있습니다.

![](image_1.png)

인스턴스 초기화 블록은 객체를 생성할 때마다 호출되고 자식 객체의 생성자가 호출되기 전에 그리고 부모 생성자 이후에실행됩니다.

```java
public class Cat extends Pet {
    final int i_value;
    static int s_value;

    {
        System.out.println("instance initializer block");
        i_value = 3;
        System.out.println("i_value: " + i_value);
        System.out.println("s_value: " + s_value);
    }

    static {
        System.out.println("static initializer block");
//        System.out.println("i_value: " + i_value); //static 블록에서 필드 접근 안됨
        System.out.println("s_value: " + s_value);
    }

    public Cat() {
        System.out.println("contructor: Cat");
    }
}
```

내용이 길었네요. 다음은 메서드와 클래스에 final을 선언하면 어떤 차이가 있는지 알아봅시다.

## 3. Final 메서드

메서드를 final로 선언하면 상속받은 클래스에서 오버라이드가 불가능하게 됩니다. Dog 객체는 Pet의 makeSound() 메서드를 재정의할 수 없습니다. 언제 사용하면 좋을까요? 구현한 코드의 변경을 원하지 않을 때 사용합니다. side-effect가 있으면 안 되는 자바 코어 라이브러리에서 final로 선언된 부분을 많이 찾을 수 있습니다.

```java
public class Pet {
    public final void makeSound() {
        System.out.println("ahaha");
    }
}

public class Dog extends Pet {
    //final로된 메서드는 override할수 없음
    public void makeSound() {
    }
}
```

## 4. Final 클래스

클래스에 final을 선언하면 상속 자체가 안됩니다. 그냥 클래스 그대로 사용해야 합니다. Util 형식의 클래스나 여러 상수 값을 모아둔 Constants 클래스을 final로 선언합니다.

```java
public final class Pet {
}
```

**Pet 클래스가 final 클래스로 선언되어 상속할 수 없음**

```java
public class Dog extends Pet {
}
```

### 4.1 상수 클래스

상수 값을 모아준 클래스는 굳이 상속해서 쓸 이유는 없겠죠?

```java
public final class Constants {
	public static final int SIZE = 10;
}

public class SubConstants extends Constants {
}
```

### 4.2 Util 형식의 클래스

JDK에서 String도 final 클래스로 선언되어 있습니다. 자바의 코어 라이브러리이기 때문에 side-effect가 있으면 안 되겠죠. 다른 개발자가 상속을 해서 새로운 SubString을 만들어 라이브러리로 다른 곳에서 사용하게 되면 유지보수, 정상 실행 보장이 어려워질 수 있습니다.

```java
public final class String
implements java.io.Serializable, Comparable<String>, CharSequence {
}
```

여기서에 작성된 코드는 [github](https://github.com/kenshin579/tutorials-java-examples/tree/master/java-final) 를 참고해주세요.

## 5.참고

- final
    - [https://en.wikipedia.org/wiki/Final\_(Java)](https://en.wikipedia.org/wiki/Final_%28Java%29)
    - [https://www.baeldung.com/java-final](https://www.baeldung.com/java-final)
    - [https://djkeh.github.io/articles/Why-should-final-member-variables-be-conventionally-static-in-Java-kor/](https://djkeh.github.io/articles/Why-should-final-member-variables-be-conventionally-static-in-Java-kor/)
- 초기화 블록
    - [http://freeprog.tistory.com/198](http://freeprog.tistory.com/198)
    - [https://docs.oracle.com/javase/tutorial/java/javaOO/initial.html](https://docs.oracle.com/javase/tutorial/java/javaOO/initial.html)

