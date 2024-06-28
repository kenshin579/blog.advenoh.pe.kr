---
title: "자바 커스텀 어노테이션 만들기"
description: "자바 커스텀 어노테이션 만들기"
date: 2018-11-18
update: 2018-11-18
tags:
  - java
  - annotation
  - 자바
  - 어노테이션
---

## 1. 어노테이션이란

스프링 프레임워크를 사용하면 어노테이션을 자주 사용하게 됩니다. 아래는 스프링 웹 MVC를 사용한 예로 GET HTTP 요청(/helloworld)이 있으면 “Hello World”를 담아서 뷰에 전달되는 코드입니다. 이런 어노테이션은 내부적으로 어떻게 코드화되어 사용되는지 알아봅시다.

```java
@Controller
public class HelloWorldController {
    
    @RequestMapping(value="/helloworld", method=RequestMethod.GET)

    public ModelAndView example() {
        return new ModelAndView("helloworld", "message", "Hello World");
    }
}
```

자바 어노테이션은 JDK5부터 추가된 기능입니다. 어노테이션은 자바 소스코드에 추가적인 정보를 제공하는 메타데이터입니다. 어노테이션은 클래스, 메서드, 변수, 인자에 추가할 수 있습니다. 메타 데이타이기 때문에 비즈니스 로직에 직접적인 영향을 주지 않지만, 이 메타데이터 정보에 따라서 실행 흐름을 변경할 수 있는 코딩이 가능하여 단지 어노테이션 추가만으로 더 깔끔한 코딩이 가능해집니다. 위 예제를 어노테이션 없이 코딩하려면 코딩량도 길어지고 가독성도 많이 떨어지겠죠.

자, 기본적인 어노테이션 선언과 어디에 사용할 수 있는지 간단하게 알아봅시다.

본 포스팅에 작성한 예제 코드는 [github](https://github.com/kenshin579/tutorials-java-examples/tree/master/custom-annotation) 에 작성되어 있습니다.

## 2. 어노테이션의 기본 사용

### 2.1 어노테이션 타입

어노테이션은 3가지 타입이 존재합니다.

- 마커 어노테이션 (Maker Annotation)
    - @NewAnnotation
- 싱글 값 어노테이션 (Single Value Annotation)
    - @NewAnnotation(id=10)
- 멀티 값 어노테이션 (Multi Value Annotation)
    - @NewAnnotation(id=10, name=“hello”, roles= {“admin”, “user"})

#### 2.1.1 마커 어노테이션

@Override 나 @Deprecated와 같은 어노테이션처럼 표시만 해두는 어노테이션입니다. 메서드없이 선언하면 마커 어노테이션이 됩니다.

```java
public @interface MakerAnnotation {
}
```

추가 정보 없이 클래스나 메서드위에 추가합니다.

```java
@MakerAnnotation
public class UsingMakerAnnotation {
}
```

### 2.1.2 싱글 값 어노테이션
하나의 값만 입력받을 수 있는 어노테이션입니다.

```java
@SingleValueAnnotation(id = 1)
public class UsingSingleValueAnnotation {
}
```

어노테이션 선언에 하나의 메서드만 있으면 싱글 값 어노테이션으로 선언됩니다.

```java
public @interface SingleValueAnnotation {
    int id();
}
```

#### 2.1.3 멀티 값 어노테이션
어노테이션에 여러 값들을 지정할 수 있습니다.

```java
@MultiValueAnnotation(id = 2, name = "Hello", roles = {"admin", "users"})
public class UsingMultiValueAnnotation {

@MultiValueAnnotation(id = 10) //name = user, roles = {“anonymous’}로 지정된다
public void testMethod() {
}
}
```

여러 값을 입력받으려면 여러 메서드를 선언하면 됩니다. 추가로 default 키워드로 기본값을 선언할 수 있습니다. 위 코드 라인 #4번에 user와 roles을 지정하지 않아 기본값으로 name = “users”, roles = {“anonymous”}로 지정되었습니다.

```java
public @interface MultiValueAnnotation {
  int id();
  String name() default "user”; //미지정시 기본 값으로 user가 지정된다**
  String[] roles() default {"anonymous"};
}

```

### 2.2 어노테이션 배치하는 곳
아래 예제처럼 어노테이션은 클래스, 필드 변수, 메서드 인자, 로컬변수위에 선언할 수 있습니다.

```java
@MakerAnnotation
public class AnnotationPlacement {

    @MakerAnnotation
    String field;

    @MakerAnnotation
    public void method1(@MakerAnnotation String str) {
        @MakerAnnotation
        String test;
    }
}

```

커스텀 어노테이션을 어떻게 생성하고 사용할 수 있는지 알아보기 전에 기본적으로 자바에서 제공하는 어노테이션을 한번 살펴보겠습니다.

## 3. 빌드인 어노테이션
자바 언어에서 제공되는 어노테이션들입니다.

- **자바 코드에 적용되는 어노테이션**
    - @Override
        - 어버라이드되는 메서드로 표시하는 역할을 한다
        - 어노테이션을 추가한 메서드가 부모 클래스나 인터페이스에 존재하지 않으면 컴파일 오류를 발생시킨다
    - @Deprecated
        - 메서드를 더 이상 사용하지 않음으로 표시한다
        - 메서드가 사용되면 컴파일 경고를 발생시킨다
    - @SuppressWarnings
        - 컴파일시 발생하는 경고를 무시하도록 컴파일에게 알려주는 역할을 한다

- **자바7이후부터 추가된 어노테이션**
    - @SafeVarargs
    - 자바7에 추가된 어노테이션이다
        - 메서드가 가변인자인 경우에 잘 못 실행될 수 있는 경고 문구를 무시하도록 하는 어노테이션이다.
          ![](image_2.png)

            * 어버라이드가 안되는 메서드에만 사용 가능하다
                * final, static 메서드, 생성자, private 메서드 (자바9부터)
            * [예제 코드 참조](https://beginnersbook.com/2018/05/java-9-safevarargs-annotation/)
        * @FunctionalInterface
            * 자바8부터 추가된 어노테이션으로 함수 인터페이스로 선언할때 사용된다
        * @Repeatable
            * 같은 어노테이션을 여러번 선언할 수 있도록 해주는 어노테이션이다
              ![](image_3.png)
            * [예제 코드 참조](https://www.javabrahman.com/java-8/java-8-repeating-annotations-tutorial/)

- **다른 어노테이션에 적용되는 어노테이션 - 메타 어노테이션(Meta Annotation)**

    - @Retention
    - @Documented
    - @Target
    - @Inherited

위 메타 어노테이션은 커스텀 어노테이션을 작성할 때 사용하는 어노테이션입니다. 각각 어떤 역할을 하는지는 다음 섹션에서 알아보도록 하겠습니다.

## 4. 커스텀 어노테이션

### 4.1 메사 어노테이션

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)

public @interface MyAnnotation {
    String name();
    String value();
}

@MyAnnotation(name = "someName", value = "Hello World")
public class TheClass {
}
```

2개의 String 값을 받을 수 있는 간단한 커스텀 어노테이션 예제입니다. 각각의 메타 어노테이션이 어떤 의미를 가지고 있는지 알아볼게요.

- @Target
    - 이 어노테이션은 선언한 어노테이션이 적용될 수 있는 위치를 결정한다
    - ElementType Enum에 선언된 값
        - TYPE : class, interface, enum에 적용된다.
        - FIELD : 클래스 필드 변수
        - METHOD : 메서드
        - PARAMETER : 메서드 인자
        - CONSTRUCTOR : 생성자
        - LOCAL_VARIABLE : 로컬 변수
        - ANNOTATION_TYPE : 어노테이션 타입에만 적용된다
        - PACKAGE : 패키지
        - TYPE_PARAMETER : 자바8부터 추가된 값으로 제네릭 타입 변수에 적용된다. (ex. MyClass<T>)
        - TYPE_USE : 자바8부터 추가된 값으로 어떤 타입에도 적용된다 (ex. extends, implements, 객체 생성시등등)
        - [자바8 타입 어노테이션](https://www.logicbig.com/tutorials/core-java-tutorial/java-8-enhancements/type-annotations.html)
        - MODULE : 자바9부터 추가된 값으로 모듈에 적용된다
- @Retention
    - 어노테이션이 어느레벨까지 유지되는지를 결정짓는다.
    - RetentionPolicy Enum에 선언된 값
    - SOURCE : 자바 컴파일에 의해서 어노테이션은 삭제된다
    - CLASS : 어노테이션은 .class 파일에 남아 있지만, runtime에는 제공되지 않는 어노테이션으로 Retention policy의 기본 값이다 \* RUNTIME : runtime에도 어노테이션이 제공되어 자바 reflection으로 선언한 어노테이션에 접근할 수 있다
- @Inherited
    - 이 어노테이션을 선언하면 자식클래스가 어노테이션을 상속 받는다
- @Documented
    - 이 어노테이션을 선언하면 새로 생성한 어노테이션이 자바 문서 생성시 자바 문서에도 포함시키는 어노테이션이다.
- @Repeatable
    - 자바8에 추가된 어노테이션으로 반복 선언을 할 수 있게 해준다

### 4.2 커스텀 어노테이션 생성

커스텀 어노테이션을 이용해 생성한 예제들입니다.

**예제1 - 클래스에 선언**

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface MyAnnotation {
    String name();
    String value();
}

@MyAnnotation(name = "someName", value = "Hello World")
public class TheClass {
}
```

**예제2 - 클래스 필드에 선언**

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public @interface MyAnnotation {
    String name();
    String value();
}

public class TheClass {
    @MyAnnotation(name = "someName", value = "Hello World")
    public String myField = null;
}
```

**예제3 - 메서드에 선언**

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface MyAnnotation {
    String name();
    String value() default "기본 값";
}

public class TheClass {
    @MyAnnotation(name = "doThisMethod", value = "Hello World")
    public void doThis() {
    }

    @MyAnnotation(name = "doThatMethod")
    public void doThat() {
    }
}
```

### 4.3 자바 리플렉션으로 커스텀 어노테이션 사용해보기
프로그램 실행 시 커스텀 어노테이션을 사용한 곳과 지정한 값들을 얻어오려면 자바 리플렉션을 사용해야 합니다. 자바 리플렉션을사용해서 선언한 어노테이션 값을 얻어오는 건 비슷비슷해서 예제 3번으로만 설명하도록 하겠습니다.

```java
public class MethodAnnotationExecutor {
    public static void main(String[] args) throws NoSuchMethodException {
        Method method = TheClass.class.getMethod("doThis”); //자바 리플렉션 getMethod로 메서드 doThis를 얻어온다
        Annotation[] annotations = method.getDeclaredAnnotations(); //메서드에 선언된 어노테이션 객체를 얻어온다


        for (Annotation annotation : annotations) {
            if (annotation instanceof MyAnnotation) {
                MyAnnotation myAnnotation = (MyAnnotation) annotation;
                System.out.println("name: " + myAnnotation.name()); //어노테이션에 지정한 값을 프린트한다

                System.out.println("value: " + myAnnotation.value());
            }
        }

        Annotation annotation = TheClass.class.getMethod("doThat") 
                            .getAnnotation(MyAnnotation.class); //메서드 doThat에 선언된 MyAnnotation의 어노테이션 객체를 얻어온다


        if (annotation instanceof MyAnnotation) {
            MyAnnotation myAnnotation = (MyAnnotation) annotation;
            System.out.println("name: " + myAnnotation.name());
            System.out.println("value: " + myAnnotation.value());
        }
    }
}

```

![](image_1.png)

커스텀 어노테이션을 어떻게 생성하고 사용하는지 간단하게 알아보았습니다. 커스텀 어노테이션을 생성해서 사용하면 반복적으로 코딩해야 하는 부분들도 많이 줄일 수 있고 더 비즈니스로직에 집중할 수 있는 장점이 있습니다. 스프링에서도 자주 사용되고 또한 요사이 많이 뜨고 있는 롬보크( [Lombok](http://wonwoo.ml/index.php/post/1607) )도 여러 어노테이션을 많이 지원하는 라이브러리입니다.

지금 개발하는 프로젝트가 있다면 한번 커스컴 어노테이션으로 적용해보는 것도 좋을 것 같습니다.

## 5. 참고

- 자바 어노테이션
    - [https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94\_%EC%96%B4%EB%85%B8%ED%85%8C%EC%9D%B4%EC%85%98](https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94_%EC%96%B4%EB%85%B8%ED%85%8C%EC%9D%B4%EC%85%98)
    - [http://tutorials.jenkov.com/java/annotations.html](http://tutorials.jenkov.com/java/annotations.html)
    - [https://jdm.kr/blog/216](https://jdm.kr/blog/216)
    - [https://www.javatpoint.com/custom-annotation](https://www.javatpoint.com/custom-annotation)
    - [https://elfinlas.github.io/2017/12/14/java-annotation/](https://elfinlas.github.io/2017/12/14/java-annotation/)
    - [https://howtodoinjava.com/java/annotations/complete-java-annotations-tutorial/](https://howtodoinjava.com/java/annotations/complete-java-annotations-tutorial/)
- SafeVarargs 어노테이션
    - [https://beginnersbook.com/2018/05/java-9-safevarargs-annotation/](https://beginnersbook.com/2018/05/java-9-safevarargs-annotation/)
- Repeable 어노테이션
    - [https://dzone.com/articles/repeatable-annotations-in-java-8-1](https://dzone.com/articles/repeatable-annotations-in-java-8-1)
    - [https://www.javabrahman.com/java-8/java-8-repeating-annotations-tutorial/](https://www.javabrahman.com/java-8/java-8-repeating-annotations-tutorial/)
- 사용예
    - [http://www.nextree.co.kr/p5864/](http://www.nextree.co.kr/p5864/)
    - [https://examples.javacodegeeks.com/core-java/java-9-annotations-example/](https://examples.javacodegeeks.com/core-java/java-9-annotations-example/)
    - [https://elfinlas.github.io/2017/12/14/java-custom-anotation-01/](https://elfinlas.github.io/2017/12/14/java-custom-anotation-01/)
    - [http://tutorials.jenkov.com/java-reflection/annotations.html](http://tutorials.jenkov.com/java-reflection/annotations.html)
    - [https://elfinlas.github.io/2017/12/14/devnote01/](https://elfinlas.github.io/2017/12/14/devnote01/)
