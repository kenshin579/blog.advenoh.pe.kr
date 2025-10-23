---
title: "Lombok 기본 사용법 익히기"
description: "Lombok 기본 사용법 익히기"
date: 2018-12-16
update: 2018-12-16
tags:
  - lombok
  - java
  - annotation
  - 자바
  - 어노테이션
---

## 1. 들어가며
Lombok는 자바에서 작성해야 하는 boilerplate code(ex. getter/setter, constructor, toString)를 선언한 어노테이션을 통해서 자동으로 생성해주는 라이브러리입니다.

코드 자체가 더 간결해져 가독성도 높아지고 더 빠르게 개발할 수 있는 장점이 있습니다. 하지만, Lombok 사용 시 주의가 필요한 부분이 분명히 존재합니다. (참조 : Lombok Pitfall)
그래서 올바로 알고 주의해서 사용하기를 권장합니다. 이 포스팅에서는 자주 사용되는 어노테이션 위주로 작성하도록 하겠습니다.

## 2. 환경 설정

아래 환경 기반으로 코드가 작성되어 있습니다. IDE에서 Lombok 플러그인을 설치해야 어노테이션이 인식됩니다.

- OS: Mac OS
- IDE: Intelij
- Java : JDK 11
- Source code : [github](https://github.com/kenshin579/tutorials-java-examples/tree/master/java-lombok)
- Software management tool : Maven
- IDE Plugin :  Lombok Plugin

![](image_2.png)

* Java Bytecode Decompiler : Enable - class 파일을 decompile 해서 소스를 볼 수 있다

pom.xml 파일에 lombok dependency를 추가해줍니다.

```xml
<dependency>
  <groupId>org.projectlombok</groupId>
  <artifactId>lombok</artifactId>
  <version>1.18.4</version>
</dependency>
```

## 3. 대표적인 예제

자주 사용되는 어노테이션 위주로 살펴보도록 하겠습니다.

- @NonNull
- @Getter, @Setter
- @ToString
- @AllArgsConstructor, @AllArgsConstructor, @NoArgsConstructor
- @EqualsAndHashCode
- @Builder
- @Data
- @Slf4j, @Log, @Log4j, @Log4j2
- Lombok Configuration

### @NonNull

메서드나 생성자 인자에 @NunNull 어노테이션을 추가하면 Lombok가 null 체크 구문을 생성해줍니다.

```java
//Lombok 사용
public class NonNullExample extends Something {
    private String name;

    public NonNullExample(@NonNull Person person) {
        super("Hello");
        this.name = person.getName();
    }
}
```

```java
//바닐라 자바
public class NonNullExample extends Something {
    private String name;

    public NonNullExample(@NonNull Person person) {
        super("Hello");
        if (person == null) {
            throw new NullPointerException("person is marked @NonNull but is null");
        } else {
            this.name = person.getName();
        }
    }
}
```

위와 같이 바닐라 버전의 자바 소스를 보고 싶다면 IDE에서 Java Bytecode Decompiler 플러그인 활성화 이후 해당 class를 클릭하면 소스코드를 직접 확인할 수 있습니다.

### @Getter, @Setter

클래스 필드에 대한 getter와 setter 메서드를 생성해주고 여러 옵션으로 다양한 코드를 자동생성할 수 있습니다. Setter는 필드가 final이 아닌 필드에 대해서 메서드가 생성됩니다.

- 클래스 전체에 적용

- 각 클래스 필드에 적용

- 메서드의 접근제어자 변경

    - @Setter(AccessLevel.PROTECTED)

- 메서드 체이닝 (setter)

    - @Accessors(chain = true)



**Lombok 사용**

```java
//Ex1 - Lombok
@Getter
@Setter
public class Person {
    String name;
    int age;
}

//Ex1 - 바닐라 자바
public class Person {
    String name;
    int age;

    public Person() {
    }

    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
```

```java
//Ex2 - Lombok
//접근 제어자
public class PersonAccessLevel {
    @Getter
    @Setter
    String name;

    @Setter(AccessLevel.PROTECTED)
    int age;
}

//Ex2 - 바닐라 자바
public class PersonAccessLevel {
    String name;
    int age;

    public PersonAccessLevel() {
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    protected void setAge(int age) {
        this.age = age;
    }
}
```

```java
//Ex3 - Lombok
//메서드 체이닝
@Setter
@Accessors(chain = true)
public class PersonSetterChain {
    String name;

    int age;
}

//Ex3 - 바닐라 자바
public class PersonSetterChain {
    String name;
    int age;

    public PersonSetterChain() {
    }

    public PersonSetterChain setName(String name) {
        this.name = name;
        return this;
    }

    public PersonSetterChain setAge(int age) {
        this.age = age;
        return this;
    }
}
```

### @ToString

클래스의 toString 메서드를 자동으로 생성해주고 옵션을 주어 toString에 제외 시킬 필드 속성도 지정할 수 있습니다.

- 메서드에서 제외시킬 필드 지정

    - @ToString.Exclude

- 메서드에서 추가하고 싶은 필드 지정


```java
//Ex1 - Lombok
@ToString
public class Person {
    String name;
    int age;
}

//Ex1 - 바닐라 자바
public class Person {
    String name;
    int age;

    public Person() {
    }

    public String toString() {
        return "Person(name=" + this.name + ", age=" + this.age + ")";
    }
}
```

```java
//Ex2 - Lombok
@ToString
public class PersonExclude {
    @ToString.Include
    String name;

    @ToString.Exclude
    int age;
}

//Ex2 - 바닐라 자바
public class PersonExclude {
    String name;
    int age;

    public PersonExclude() {
    }

    public String toString() {
        return "PersonExclude(name=" + this.name + ")";
    }
}
```

### @EqualsAndHashCode

equals()와 hashCode()를 자동 생성해주는 어노테이션입니다.

- 제외시킬 필드 지정
    - @EqualsAndHashCode.Exclude

바닐라 자바 코드가 너무 길어서 간출렸습니다. 실제 코드는 컴파일된 클래스 파일으로 확인해보세요.

```java
//Ex1 - Lombok
@EqualsAndHashCode
public class Person {
    String name;
    int age;
}

//Ex1 - 바닐라 자바
public class Person {
    String name;
    int age;

    public Person() {
    }

    public boolean equals(Object o) {
        ….
    }

    protected boolean canEqual(Object other) {
        return other instanceof Person;
    }

    public int hashCode() {
        int PRIME = true;
        int result = 1;
        Object $name = this.name;
        int result = result * 59 + ($name == null ? 43 : $name.hashCode());
        result = result * 59 + this.age;
        return result;
    }
}
```

```java
//Ex2 - Lombok
@EqualsAndHashCode
public class PersonExclude {
    String name;
    @EqualsAndHashCode.Exclude
    int age;
}

//Ex2 - 바닐라 자바
public class PersonExclude {
    String name;
    int age;

    public PersonExclude() {
    }

    public boolean equals(Object o) {
       ….
    }

    protected boolean canEqual(Object other) {
        return other instanceof PersonExclude;
    }

    public int hashCode() {
        int PRIME = true;
        int result = 1;
        Object $name = this.name;
        int result = result * 59 + ($name == null ? 43 : $name.hashCode());
        return result;
    }
}
```

### @NoArgsConstructor, @AllArgsConstructor, @RequiredArgsContructor

생성자를 자동으로 생성해주는 어노테이션입니다. 필드 선언순서에 따라 생성자 인자가 정해집니다. 나중에 리펙토링을 하게 되면 인자 순서가 변경될 수 있다는 점을 기억하면 좋을 것 같습니다.

- NoArgsConstructor : 인자 없는 생성자
- AllArgsConstructor : 모든 필드를 인자로 받는 생성자
- RequiredArgsContructor(staticName=“of") : static factory 메서드를 생성함

```java
//Ex1 - Lombok
@NoArgsConstructor
public class PersonNoArgs {
    String name;
    int age;
}

//Ex1 - 바닐라 자바
public class PersonNoArgs {
    String name;
    int age;

    public PersonNoArgs() {
    }
}
```

```java
//Ex2 - Lombok
@RequiredArgsConstructor(staticName = "of")
@AllArgsConstructor(access = AccessLevel.PROTECTED)
public class PersonArgs {
    String name;
    int age;
}

//Ex2 - 바닐라 자바
public class PersonArgs {
    String name;
    int age;

    private PersonArgs() {
    }

    public static PersonArgs of() {
        return new PersonArgs();
    }

    protected PersonArgs(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

### @Data

@Data 어노테이션은 아래 모든 어노테이션이 적용되는 어노테이션입니다.

- @ToString
- @EqualsAndHashCode
- @Getter, @Setter
- @RequiredArgsConstructor

```java
//Lombok 사용
@Data
public class Person {
    String name;
    int age;
}

//바닐라 자바
public class Person {
    String name;
    int age;

    public Person() {
    }

    public String getName() {
        return this.name;
    }

...
    public String toString() {
        return "Person(name=" + this.getName() + ", age=" + this.getAge() + ")";
    }
}
```

### @Builder

어노테이션 하나로 [Builder Pattern](https://en.wikipedia.org/wiki/Builder_pattern#Java) 을 생성해줍니다. 빌더 패턴은 여러 설정하고 객체를 만들어주는 패턴입니다. 더 자세한 내용은 아래 참조를 확인해주세요.

```java
//Lombok 사용
@Builder
@ToString
public class Car {
    private int wheels;
    private String color;

    public static void main(String[] args) {
        System.out.println(Car.builder().color("red").wheels(2).build());
    }
}

/* OUTPUT
Car(wheels=2, color=red)
*/ 

//바닐라 자바
public class Car {
    private int wheels;
    private String color;

    public static void main(String[] args) {
        System.out.println(builder().color("red").wheels(2).build());
    }

    Car(int wheels, String color) {
        this.wheels = wheels;
        this.color = color;
    }

    public static Car.CarBuilder builder() {
        return new Car.CarBuilder();
    }

    public String toString() {
        return "Car(wheels=" + this.wheels + ", color=" + this.color + ")";
    }

    public static class CarBuilder {
        private int wheels;
        private String color;

        CarBuilder() {
        }

        public Car.CarBuilder wheels(int wheels) {
            this.wheels = wheels;
            return this;
        }

        public Car.CarBuilder color(String color) {
            this.color = color;
            return this;
        }

        public Car build() {
            return new Car(this.wheels, this.color);
        }

        public String toString() {
            return "Car.CarBuilder(wheels=" + this.wheels + ", color=" + this.color + ")";
        }
    }
}
```

### @Slf4j, (@Log, @Log4j, @Log4j2, etc)

원하는 로깅 프레임워크를 선택해서 선언하면 보다 쉽게 로그를 사용할 수 있습니다.

```java
//Lombok 사용
@Builder
@ToString
public class Car {
    private int wheels;
    private String color;

    public static void main(String[] args) {
        System.out.println(Car.builder().color("red").wheels(2).build());
    }
}

/* OUTPUT
Car(wheels=2, color=red)
*/ 

//바닐라 자바
public class Car {
    private int wheels;
    private String color;

    public static void main(String[] args) {
        System.out.println(builder().color("red").wheels(2).build());
    }

    Car(int wheels, String color) {
        this.wheels = wheels;
        this.color = color;
    }

    public static Car.CarBuilder builder() {
        return new Car.CarBuilder();
    }

    public String toString() {
        return "Car(wheels=" + this.wheels + ", color=" + this.color + ")";
    }

    public static class CarBuilder {
        private int wheels;
        private String color;

        CarBuilder() {
        }

        public Car.CarBuilder wheels(int wheels) {
            this.wheels = wheels;
            return this;
        }

        public Car.CarBuilder color(String color) {
            this.color = color;
            return this;
        }

        public Car build() {]
            return new Car(this.wheels, this.color);
        }

        public String toString() {
            return "Car.CarBuilder(wheels=" + this.wheels + ", color=" + this.color + ")";
        }
    }
}

```

### Lombok Configuration

Lombok에서 제공하는 기능에 대해서 사용하지 못하게 하는 설정등이 가능합니다. 프로젝트 루트에 lombok.config 파일을 생성해서 원하는 설정를 key=value 형식으로 작성하면 됩니다. 구체적인 설정은 해당 [Lombok Configuration system](https://projectlombok.org/features/configuration) 을 참조해주세요.

예 - 설정(@NonNull 사용 금지)

```properties
lombok.nonNull.flagUsage=error
```

IDE에서는 표시되지 않지만, 컴파일시 오류가 발생합니다.

![](AF8820D7-66DA-4A4C-97F3-67FB7C867D8A.png)

## 4. 참고

- Lombok
    - [http://jnb.ociweb.com/jnb/jnbJan2010.html](http://jnb.ociweb.com/jnb/jnbJan2010.html)
    - [https://projectlombok.org/](https://projectlombok.org/)
    - [http://www.vogella.com/tutorials/Lombok/article.html](http://www.vogella.com/tutorials/Lombok/article.html)
    - [http://www.daleseo.com/lombok-popular-annotations/](http://www.daleseo.com/lombok-popular-annotations/)
    - [https://projectlombok.org/features/all](https://projectlombok.org/features/all)
    - [http://edoli.tistory.com/99](http://edoli.tistory.com/99)
    - [https://codeburst.io/how-to-write-less-and-better-code-or-project-lombok-d8d82eb3e80a](https://codeburst.io/how-to-write-less-and-better-code-or-project-lombok-d8d82eb3e80a)
    - [https://www.baeldung.com/intro-to-project-lombok](https://www.baeldung.com/intro-to-project-lombok)
- Lombok Pitfall
    - [http://kwonnam.pe.kr/wiki/java/lombok/pitfall](http://kwonnam.pe.kr/wiki/java/lombok/pitfall)
    - [https://www.popit.kr/실무에서-lombok-사용법/](https://www.popit.kr/%EC%8B%A4%EB%AC%B4%EC%97%90%EC%84%9C-lombok-%EC%82%AC%EC%9A%A9%EB%B2%95/)
- Lombok Config
    -  [https://projectlombok.org/features/configuration](https://projectlombok.org/features/configuration)
- Builder 패턴
    -  [https://en.wikipedia.org/wiki/Builder_pattern#Java](https://en.wikipedia.org/wiki/Builder_pattern#Java)
