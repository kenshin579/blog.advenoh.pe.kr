---
title: "Java Jayway JsonPath 사용법"
description: "Java Jayway JsonPath 사용법"
date: 2019-01-19
update: 2019-01-19
tags:
  - jayway
  - java
  - jsonpath
  - xpath
  - json-path
  - 자바
---

## 1. 들어가며

Jayway JsonPath는 [Stefan Goessner의 JsonPath](https://goessner.net/articles/JsonPath/) 구현을 자바로 포팅한 라이브러리입니다. XML의 가장 큰 장점은 **XPath(XML Path Language)로 XML 문서에서 원하는 부분을 바로 추출** 할 수 있다는 점입니다.

[w3school](https://www.w3schools.com/xml/xpath_syntax.asp) 예제

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book>
        <title lang="en">Harry Potter</title>
        <price>29.99</price>
    </book>
    <book>
        <title lang="en">Learning XML</title>
        <price>39.95</price>
    </book>
</bookstore>
```

위 XML 예제에서 bookstore의 첫 번째 책 요소를 추출하는 XPath 표현은 아래와 같습니다.

- \_bookstore_book[1] : 첫 번째 책 요소를 추출한다
- \_bookstore_book[last()] : 여러 책중 맨 마지막 책을 추출한다

## 2. 개발 환경 및 Maven 의존성 설정

사용한 환경은 아래와 같습니다. 여기서 작성한 소스는 아래 github 링크를 참고해주세요.

- OS : Mac OS
- IDE: Intellij
- Java : JDK 1.8
- Source code : [github](https://github.com/kenshin579/tutorials-java-examples/tree/master/jayway-jsonpath)
- Dependency management tool : Maven

Java Jayway JsonPath를 사용하기 위해서는 아래 Maven 의존성을 추가해야 합니다. 현재 **최신 버전은 2.4.0** (2017/7/5)입니다.

```xml
<dependency>
    <groupId>com.jayway.jsonpath</groupId>
    <artifactId>json-path</artifactId>
    <version>2.4.0</version>
</dependency>
```

JSON 샘플 파일은 [Json Generator](https://next.json-generator.com/41_9W7rWU) 에서 가져왔고 작성한 소스 코드는 실제 Jaway JsonPath 소스를 많이 참조해서 작성했습니다.

### 2.1 Jayway JsonPath Evaluator

JsonPath 표현식에 아직 익숙하지 않다면, [JsonPath Online Evaluator](http://jsonpath.herokuapp.com/) 에 접속해서 표현식을 테스트해보세요.

![](/media/java/Java-Jayway-JsonPath-사용법/image_1.png)

## 3. Jayway JsonPath 사용법

JsonPath의 표기법과 대표적인 연산자를 알아보고 예제를 통해서 어떻게 데이터에 접근하여 가져올 수 있는지 알아보도록하겠습니다. Jayway JsonPath의 연산자, 함수, 필터에 대한 전체 목록은 JsonPath Github를 참조해주세요.

### 3.1 JsonPath 표기법

JsonPath는 2가지 표기법을 사용할 수 있습니다. Dot과 bracket 표현식이 있습니다.

- dot 표현식
    - \$.store.book[0].title
- bracket 표현식
    - \$[’store’][‘book’][0][’title’]

### 3.2 JsonPath 대표적인 연산자 (Operator)

대표적으로 많이 사용하는 연산자입니다.

| **연산자** | **설명** |
| -------- | ------- | 
| \$ | 루트 노드로 모든 Path 표현식은 이 기호로 시작된다. |
| @ | 처리되고 있는 현재 노드를 나타내고 필터 조건자에서 사용된다.|  
| \* | 와일드카드로 모든 요소와 매칭이 된다 |
| . | Dot 표현식의 자식노드 |
| [start:end] | 배열 slice 연산자 |
| [?(\<expression\>)] | 필터 표현식으로 필터 조건자가 참인 경우에 매칭되는 모든 요소를 만을 처리한다 ex. book[?(@.price == 49.99)] |

### 3.3 JsonPath 함수 및 필터

JsonPath 함수는 min(), max(), avg(), length() 등을 제공하고 표현식 맨 마지막에 붙여서 실행할 수 있습니다.

- \$.length() : 요소의 길이를 반환한다. 배열인 경우에는 배열 크기를 반환한다
- \$.range.avg() : 요소 range 배열의 평균 값을 계산한다

JsonPath에서 필터도 제공합니다. 필터 [?(\<expression\>)] 표현 식을 가지며 <expression>에는 논리 연산자(ex. ==, <, >)와 기타연산자(ex. in, size, empty)로 true, false 값을 반환하는 표현 식이 들어갑니다. @는 현재 처리되는 요소를 나타냅니다.

- \$[?(@.age == 23 )] : age가 23인 데이터만 반환한다
- \$[?(@.name == ‘Frank’)] : 이름인 Frank인 데이터만 반환한다

### 3.4 JsonPath 표현식 예제

| JsonPath 표현식 | 결과 및 설명 |
| ------------- | --------- |
| $..* | 전체 요소 (.. 딥 스캔) |
| $[?('pariatur' in @['tags'])] | tags에 pariatur가 있는 모든 사람들 |
| $[?(@.age == 26 )] | age가 26인 모든 사람들 |
| $[0][‘balance’] | 첫번째 사람의 balance |
| $[*]['age'] | 모든 사람들의 나이 |
| $..[’name’][‘first] | 모든 사람들의 이름 |

### 3.5 Java JsonPath 예제

Jayway JsonPath로 원하는 데이터를 추출하려면 parse()와 read()를 사용하면 됩니다. 유닛 테스트로 작성된 여러 버전을 보면 사용법을 쉽게 이해할 수 있습니다.

- static parse() : 여러 입력 타입(ex. String, InputStream, File)에 따라서 JSON을 읽어드리는 정적 메서드이다.
- read() : XPath 표현식을 읽고 해당 데이터를 추출한다
    - <T> T read(String path, Predicate... filters)

### 3.5.1 Id로 검색하기

배열 중에 \_id 값이 ‘5c2c3278acd492387a5223d7'인 데이터를 추출하는 예제입니다.

필터를 사용하여 Id가 같은 데이터만 얻어와서 Object 객체로 반환합니다.

```java
@Test
public void test*id값으로*데이터를_가져오기() {
    String searchId = "5c2c3278acd492387a5223d7";
    Object dataObject = JsonPath.parse(jsonStream).read("\$[?(@._id == '" + searchId + "')]");
    assertTrue(dataObject.toString().contains("Hello, Louella! You have 8 unread messages."));
}
```

**JsonPath Output 결과**

```json
[
    {
    "_id" : "5c2c3278892c4a5335a2d18e",
    "index" : 0,
    "guid" : "bd56abb6-c46b-43e4-b3c7-ca8ad386dd7c",
    …(생략)…
    "greeting" : "Hello, Franklin! You have 6 unread messages.",
    "favoriteFruit" : "banana"
    }
]
```

#### 3.5.2 Filter API를 사용하기

위와 같은 예제이고 Jayway에서 제공하는 Filter API를 사용하여 작성하였습니다. Filter API를 사용하려면, 메서드이름을 익히고 익숙해져야 하므로 그냥 JsonPath 표현식 사용을 추천합니다.

```java
@Test
public void test*id값으로*데이터를\_가져오기() {
    String searchId = "5c2c3278acd492387a5223d7";
    List<Object> lists = JsonPath.parse(jsonStream).read("\$[?(@._id == '" + searchId + "')]");
    assertEquals(1, lists.size());
    assertTrue(lists.get(0).toString().contains("Hello, Louella! You have 8 unread messages."));
}
```

#### 3.5.3 Tags에 특정 값이 있는 모두 사람 찾기

스캔하는 @[’tags’]에 ‘pariatur’ 값이 있는 모든 사람을 찾는 예제입니다. 필터 조건가가 있는 경우에는 결과가 여러 개일 수 있으므로 List로 반환합니다.

```java
@Test
public void test*tags가*있는*사람은*모두() {
    List<Map<String, Object>> dataList = JsonPath.parse(jsonStream).read("\$[?('pariatur' in @['tags'])]");
    assertTrue(dataList.get(0).get("name").toString().contains("Dawn") && dataList.get(0).get("name").toString().contains("Roach"));
    assertTrue(dataList.get(1).get("name").toString().contains("Deloris") && dataList.get(1).get("name").toString().contains("Albert"));
}
```

**JsonPath Output 결과**

```json
[
    {
        …(생략)…
        "tags" : [
        "incididunt",
        "elit",
        "laborum",
        **"pariatur",**
        "amet"
        ],
    },
    {
        …(생략)…
        "tags" : [
        "adipisicing",
        "irure",
        "eu",
        "ullamco",
        **"pariatur"**
        ],
    …(생략)…
]
```

#### 3.5.4 JsonPath 쿼리로 얻은 결과 자바 객체와 자동 매핑하기

지금까지 JsonPath로 쿼리한 결과를 Object로 저장하였지만, 실제 클래스 객체로 결과를 매핑받아 볼 수 있습니다. read() 메서드에 targetType으로 객체(ex. Person)를 넘겨주면 자동으로 캐스팅되어 타입 객체(ex. Person)를 반환합니다.

```java
@Test
public void test*Person객체로*매핑하기() {
    DocumentContext documentContext = JsonPath.parse(this.getResourceAsStream("person.json"));
    Person person = documentContext.read("\$", **Person.class)**;
    assertEquals("Frank Oh", person.getName());
    assertEquals(26, person.getAge());
}
```

#### 3.5.5 JsonPath 함수 사용

첫번째 사람에서 range 속성의 평균 값을 계산하는 예제입니다.

```java
@Test
public void test*jsonpath*함수() {
    DocumentContext documentContext = JsonPath.parse(jsonStream);
    double rangeAvg = documentContext.read("\$[0].range.avg()");
    assertEquals(4.5, rangeAvg, 0);
}
```

**JsonPath Output 결과**

```json
[{
…(생략)…

"range": [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

…(생략)…
}]
```

#### 3.5.6 모든 사람의 총 계좌 잔고 계산하기

이번에도 함수를 사용하였습니다. \$.length()를 사용해서 총 사람의 수를 얻은 다음, 각 사람들의 balance 속성의 값을 얻어 총 합을 구하는 예제입니다.

```java
@Test
public void test*모든*사람의*총*계좌*잔고을*계산하기() throws ParseException {
    NumberFormat formatter = NumberFormat.getCurrencyInstance(Locale.US);

    DocumentContext documentContext = JsonPath.parse(jsonStream);
    int maxSize = documentContext.read("\$.length()");
    double totalAmount = 0.0;

    for (int i = 0; i < maxSize; i++) {
    totalAmount += formatter.parse(documentContext.read("\$[" + i + "]['balance']")).doubleValue();
    }
    assertEquals(15998, (int) totalAmount);
}
```

#### 3.5.7 제일 어린 사람 찾기

마지막 예제는 제일 어린 사람 찾기입니다. #1에서는 \$[\*][‘age] 표현식으로 모든 사람의 나이를 List로 결과를 담습니다. #2에서 제일 최소 나이를 구한 다음, #3에서는 구한 최소 나이의 값이 매칭되는 사람을 얻어 결과를 저장합니다.

```java
@Test
public void test*제일*어린*사람을*찾기() {
    DocumentContext documentContext = JsonPath.parse(jsonStream);
    List<Integer> ageList = documentContext.read("$[**]['age']”); *#1**
    int minAge = ageList.get(ageList.indexOf(Collections.min(ageList))); **#2**
    List<Object> lists = documentContext.read("$[?(@['age'] == " + minAge + ")]”); **#3**
    assertTrue(lists.get(0).toString().contains("Deloris") && lists.get(0).toString().contains("Albert"));
}
```

지금까지 예제를 통해서 Jayway JsonPath 사용법을 알아봤습니다. JSON 데이터를 사용할 때 Gson이나 Jackson 라이브러리를 많이 사용합니다. 이런 라이브러리를 사용해도 원하는 중간값을 얻어올 수 있지만, 빠르고 쉽게 작성하기는 좀 어려움이 있습니다. JsonPath는 이런 부분을 보완해줍니다. 그래서 빠르고 쉽게 체크할 때 많이 사용되어 유닛 테스트를 작성할 때 많이 사용되고 있습니다.

## 4. 참고

- JSONPath
    - [https://goessner.net/articles/JsonPath/](https://goessner.net/articles/JsonPath/)
- Jayway JsonPath
    - [https://github.com/json-path/JsonPath](https://github.com/json-path/JsonPath)
    - [https://www.baeldung.com/guide-to-jayway-jsonpath](https://www.baeldung.com/guide-to-jayway-jsonpath)
    - [https://www.baeldung.com/jsonpath-count](https://www.baeldung.com/jsonpath-count)
    - [https://www.pluralsight.com/blog/tutorials/introduction-to-jsonpath](https://www.pluralsight.com/blog/tutorials/introduction-to-jsonpath)
