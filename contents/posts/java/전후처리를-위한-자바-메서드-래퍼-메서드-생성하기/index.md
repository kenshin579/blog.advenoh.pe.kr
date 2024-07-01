---
title: "전후처리를 위한 자바 메서드 래퍼 메서드 생성하기"
description: "전후처리를 위한 자바 메서드 래퍼 메서드 생성하기 - pre and post processing for java wrapper method"
date: 2018-08-26
update: 2018-08-26
tags:
  - java
  - wrapper
  - pre processing
  - post processing
  - 자바
  - 래퍼
  - 메서드
  - 전후처리
---

## 1.개요

코딩을 하다 보면 어떤 작업을 하기 전에 전후 처리가 필요할 때가 종종 생깁니다. 전처리(pre-processing)에서는 실제 작업을 수행하기 전에 필요한 세팅을 하고 후처리(post-processing)에서는 cleanup 정도의 작업을 하게 됩니다. 이런 전후 처리를 여러 번 할 때에는 별도의 메서드로 구현해두면 좋습니다. 몇 개의 예제를 보면서 알아보죠.

## 2.예제

### 2.1 파일에 텍스트 String 값 쓰기

파일에 쓰려면 기본적으로 파일 스트림을 열고 텍스트를 쓰고 나서 파일 스트림을 닫아야 합니다. 파일 스트림을 여닫는 부분을 전후처리로 만들어봅시다.

writeLineToFile 메서드는 3개의 인자로 받습니다. 파일 이름, 스트링 값, 그리고 람다 함수를 인자로 넘겨주고 있습니다. 람다 함수로 넘겨주는 메서는 전후처리 중간에 실행될 부분입니다.

```java
@Test
public void testWriteLineToFileWrapper() throws IOException {
    writeLineToFile("output.txt", "this is a test", (printWriter, line) -> {
        printWriter.print(line);
    });
}
```

람다 함수로 넘겨줄 인터페이스를 정의합니다.

```java
private interface FileWrite {
	void writeToFile(PrintWriter pw, String line);
}
```

writeLineToFile 메서드에서는 전처리 코드, 넘겨 받은 함수 실행, 그리고 마지막으로 후처리 코드로 마무리합니다.

```java
private static void writeLineToFile(final String fileName, String line, FileWrite fileWrite) throws IOException {
    LOG.info("pre 처리 : open file");
    FileWriter fileWriter = new FileWriter(fileName);
    PrintWriter printWriter = new PrintWriter(fileWriter);

    fileWrite.writeToFile(printWriter, line);

    LOG.info("post 처리 : close file");
    printWriter.close();
}
```

### 2.2 Unit test에서 static final로 선언된 상수값을 변경하여 테스트하기

기존에 선언한 static final 상수 값을 변경하면서 unit test를 작성하려면 reflection을 사용해서 상수 값을 변경해줘야 합니다. static final 값을 한번 변경하면 변경된 값으로 계속 유지되기 때문에 다른 unit test의 결과가 fail로 떨어질 수 있습니다. 그래서 테스트 이후에는 기존 값으로 원복시켜줘야 합니다. 실제 작성된 코드를 보죠.

static final로 선언된 상수 값입니다.

```java
public class Constants {
	public static final Integer SIZE = 10;
}
```

Unit Test에서 상수 값을 다른 값으로 변경하고 테스트하는 코드를 짠다면, 아래 코드와 같겠죠.

```java
@Test
public void testExecuteAndResetConstantValueWithoutInterface() throws Exception {
    int newSize = 3;

    int originalSize = Constants.SIZE;
    setFinalStaticIntField(Constants.class, "SIZE", newSize);
    LOG.info("pre 처리 - SIZE: {}", Constants.SIZE);

    //변경된 값으로 테스트함. 
    assertEquals(newSize, Constants.SIZE);

    setFinalStaticIntField(Constants.class, "SIZE", originalSize);
    LOG.info("post 처리 - SIZE: {}", Constants.SIZE);
}
```

매번 다른 SIZE 값으로 unit test를 작성한다면, #2.1에서 했던 것처럼 인터페이스를 정의하고 refactoring하는게 낫겠죠.

```java
@Test
public void testExecuteAndResetConstantValue() throws Exception {
    int newId = 3;

    //내부적으로 Constant값을 3으로 세팅했다가 기존값으로 원복시킴
    executeAndResetConstantValue(newId, () -> {
        LOG.info("Constants: {}", Constants.SIZE);
    });
}
```

전후처리 하는 코드아래 메서드로 refactoring합니다.

```java
private static void executeAndResetConstantValue(int newSize, Task task) throws NoSuchFieldException, IllegalAccessException {
    int originalSize = Constants.SIZE;
    //pre 처리 - 인자 값으로 세팅함
    setFinalStaticIntField(Constants.class, "SIZE", newSize);
    LOG.info("pre 처리 - SIZE: {}", Constants.SIZE);

    //실행
    task.execute();

    //post 처리 - 기존 값으로 원복함
    setFinalStaticIntField(Constants.class, "SIZE", originalSize);
    LOG.info("post 처리 - SIZE: {}", Constants.SIZE);
}
```

reflection을 이용해서 static final을 상수값을 변경하는 메서드는 dzone 사이트에서 참조하였습니다. (참고 - static final field 변경)

```java
private static void setFinalStaticIntField(Class<?> clazz, String fieldName, Object value) throws NoSuchFieldException, IllegalAccessException {
    Field field = clazz.getDeclaredField(fieldName);
    field.setAccessible(true);

    Field modifiers = Field.class.getDeclaredField("modifiers");
    modifiers.setAccessible(true);
    modifiers.setInt(field, field.getModifiers() & ~Modifier.FINAL);

    field.set(null, value);
}
```

인터페이스 선언하는 부분입니다.

```java
private interface Task {
    void execute();
}
```

인터페이스는 인자도 없고 반환 값도 없는 void 이여서 Runnable 인터페이스를 그냥 사용해도 무방합니다.

```java
private static void executeAndPrePostProcessWithRunnable(int newSize, Runnable r) throws NoSuchFieldException, IllegalAccessException {
    int originalSize = Constants.SIZE;
    //pre 처리 - 인자 값으로 세팅함
    setFinalStaticIntField(Constants.class, "SIZE", newSize);
    LOG.info("pre 처리 - SIZE: {}", Constants.SIZE);

    //실행
    r.run();

    //post 처리 - 기존 값으로 원복함
    setFinalStaticIntField(Constants.class, "SIZE", originalSize);
    LOG.info("post 처리 - SIZE: {}", Constants.SIZE);
}
```

- 지금까지 작성된 코드는 [github](https://github.com/kenshin579/tutorials-java-examples/tree/master/java8)에 올려줘 있습니다.

    - com.java.examples.prepost

    - - Constants
    - PrePostTest
    - FinalFieldChangeTest

## 3. 참고

- 전후처리
    - [https://www.javacodegeeks.com/2013/05/a-simple-application-of-lambda-expressions-in-java-8.html](https://www.javacodegeeks.com/2013/05/a-simple-application-of-lambda-expressions-in-java-8.html)
    - [https://stackoverflow.com/questions/43599406/create-generic-java-method-wrapper-for-pre-and-post-processing](https://stackoverflow.com/questions/43599406/create-generic-java-method-wrapper-for-pre-and-post-processing)
- static final field 변경
    - [https://dzone.com/articles/how-to-change-private-static-final-fields](https://dzone.com/articles/how-to-change-private-static-final-fields)
- 함수 인터페이스
    - [http://multifrontgarden.tistory.com/125](http://multifrontgarden.tistory.com/125)
