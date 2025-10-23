---
title: "새로운 기능 및 개선 사항 목록 - 자바10에서의 변화"
description: "새로운 기능 및 개선 사항 목록 - 자바10에서의 변화"
date: 2018-09-11
update: 2018-09-11
tags:
  - java10
  - java
  - jdk
  - openjdk
  - 자바
  - 자바10
---


## 자바10
* **언어**
    * JEP 286: Local Variable Type Inference
* JVM/Compiler
    * JEP 304: Garbage-Collector Interface
    * JEP 307: Parallel Full GC for G1
    * JEP 316: Heap Allocation on Alternative Memory Devices
    * JEP 317: Experimental Java-Based JIT Compiler
* 기타 변경 및 개선사항
    * JEP 296: Consolidate the JDK Forest into a Single Repository
    * JEP 310: Application Class-Data Sharing
    * JEP 312: Thread-Local Handshakes
    * JEP 313: Remove the Native-Header Generation Tool (javah)
    * JEP 314: Additional Unicode Language-Tag Extensions
    * JEP 319: Root Certificates
    * JEP 322: Time-Based Release Versioning

자바10에 추가된 여러 기능 및 개선 사항은 다음 링크를 참조해주세요.

* [http://openjdk.java.net/projects/jdk/10/](http://openjdk.java.net/projects/jdk/10/)
* [https://www.oracle.com/technetwork/java/javase/10-relnote-issues-4108729.html](https://www.oracle.com/technetwork/java/javase/10-relnote-issues-4108729.html)
* [https://dzone.com/articles/whats-new-in-java-10](https://dzone.com/articles/whats-new-in-java-10)

## JEP 286: Local Variable Type Inference
타임 추론이란 자바 컴파일러가 각 메서드 호출과 정의된 메서드 선언문을 보고 인자의 타입을 추론하는 기능을 말합니다. 타임 추론(type inference)은 자바5부터 지속적으로 개선해 왔었습니다.

* Java 5 : 제네릭 메서드와 타입 인지 타입추론
* Java 7 : 다이아몬드 연산자(<>)
* Java 8 : 람다식 인자 타입
* Java 10 : 지역변수 타입추론

### **타입추론 개선 내역**


#### **Java 5 : 제네릭 메서드 타입 추론**
```java
List<String> cs = Collections.<String>emptyList();
```

#### **Java 7 : 다이아몬드 연사자(<>)**
```java
Map<String, List<String>> myMap = new HashMap<String,List<String>>();
```

#### **Java 8 : 람다식 안자 타입**
```java
Predicate<String> nameValidation = (String x) -> x.length() > 0;
```

#### **Java 10 : 지역변수 타입 추론**
자바에서도 var를 도입하여 암시적 타이핑을 지원하게 되었습니다. var는 keyword(ex.abstract)가 아니라 reserved type name이라서 변수, 함수 이름으로도 사용할 수 있습니다.
추가로 var의 도입으로 dynamic type을 지원하는 것은 아닙니다. compiler가 알아서 타입을 추론해서 compile 해주는 것입니다.

**이전 자바**
```java
Map<User, List<String>>** userChannels = new HashMap<>();
```

**자바10**
```java
var userChannels = new HashMap<User, List<String>>();
		Path path = Paths.get("src/web.log");
		try (Stream<String> lines = Files.lines(path)) {
			long warningCount
					= lines
					.filter(line -> line.contains("WARNING"))
					.count();
			System.out.println("Found " + warningCount + " warnings in the log file");
		} catch (IOException e) {
			e.printStackTrace();
		}
		var path = Paths.get("src/web.log");
		try (var lines = Files.lines(path)) {
			var warningCount = lines
					.filter(line -> line.contains("WARNING"))
					.count();
			System.out.println("Found " + warningCount + " warnings in the log file");
		} catch (IOException e) {
			e.printStackTrace();
		}
```

제약사항으로 타입 추론이 안되는 경우도 있습니다.

* nulll로 assign하는 경우

    * ```java
	  test = null;
	  ```
* local 변수가 아닌 경우

* ```java
	  public var x = "hello";
	  ```

* explicit initialization이 없는 경우

    * ```java
	  var x;
	  ```
* initiailization이 있어도 안되는 경우도 있음 - array initializer

    * ```java
	  var arr = {1, 2, 3};
	  ```
* method의 인자로도 안됨

    * ```java
	  public void foo(var x) {}
	  ```
* 람다 표현식에는 explicit target type이 필요함

    * ```java
	  var p = (String str) -> str.length() > 1;
	  ```

var를 사용할때는 주의가 필요합니다. var를 사용하면 어떤 타입인지를 알수 없게 되어 가속성이 떨어지게 됩니다.

```java
//ORIGINAL
List<Customer> x = dbconn.executeQuery(query);

//BAD
var customer = dbconn.executeQuery(query);

//GOOD
var custList = dbconn.executeQuery(query);
```

변수이름에 타입을 추가하여 이름을 사용하여 가독성을 높여주는게 좋습니다.
더 자세한 사항은 java.net에서 제공한 가이드라인( [Style Guidlines for Local Variable Type Inference in Java](http://openjdk.java.net/projects/amber/LVTIstyle.html) )을 참조해주세요.

## 참고

* 로컬 변수 타입 추론
    * [https://www.baeldung.com/java-10-local-variable-type-inference](https://www.baeldung.com/java-10-local-variable-type-inference)
    * [https://blog.codefx.org/java/java-10-var-type-inference/](https://blog.codefx.org/java/java-10-var-type-inference/)
    * [https://www.slideshare.net/OracleDeveloperkr/main-session-java](https://www.slideshare.net/OracleDeveloperkr/main-session-java)
* reserved type이란
    * [https://stackoverflow.com/questions/49102553/what-is-the-conceptual-difference-between-a-restricted-keyword-and-reserved-t](https://stackoverflow.com/questions/49102553/what-is-the-conceptual-difference-between-a-restricted-keyword-and-reserved-t)

