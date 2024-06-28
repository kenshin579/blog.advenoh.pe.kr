---
title: "파이썬에서 람다 함수 익숙해지기"
description: "파이썬에서 람다 함수 익숙해지기"
date: 2020-08-30
update: 2020-08-30
tags:
  - python
  - lambda
  - anonymous
  - function
  - 파이선
  - 람다
  - 이름없는함수
  - 익명함수
---


## 1. 람다란?

파이쎤에서도 이름 없는 함수인 람다 표현식을 지원한다. syntax는 아래와 같다. 파이썬에서는 bracket (ex. { })을 지원하지 않아 single line으로만 작성해야 한다. 람다에서 multi-line을 작성하려면 별도 함수로 빼서 작성하면 된다.

```python
lambda 인자 : 표현식
```

### 1.1 람다 표현식으로 함수 생성 및 호출해보기

람다 함수를 생성하고 호출해보자. 람다는 변수에 저장할 수 있다. 호출은 일반함수와 동일하다.

```python
def test_lambda_single_parameter1(self):
  plus_ten_lambda = lambda x: x + 10
  result = plus_ten_lambda(1)
  self.assertEqual(result, 11)
```

변수에 저장하지 않고도 람다 함수를 정의하고 인자로 넘겨주어 바로 호출할 수 있다.

```python
def test_lambda_single_parameter2(self):
  result = (lambda x: x + 10)(1)
  self.assertEqual(result, 11)
```

람다 함수에서 2개 이상의 인자를 갖는 함수의 예제이다.

```python
def test_lambda_multiple_parameters(self):
	result = (lambda x, y: x + y)(1, 2)
	self.assertEqual(result, 3)
```


### 1.2. Map, Filter, Reduce 예제

파이썬에서 람다를 인자로 받는 대표적인 함수들에 대해서 알아보자.

### 1.2.1 map

`map` 함수는 `입력함수`를 `입력리스트`의 `item`에 적용하는 함수이고 리스트의 데이터 형태를 변경할 때 자주사용하는 함수이다. syntax는 다음과 같다.

```python
map(입력함수, 입력리스트)
```

0 ~ 4값의 리시트의 각 `item`에 +1을 하는 예제이다.

```python
def test_map(self):
  result = list(map(lambda x: x + 1, range(5)))
  self.assertEqual(result, [1, 2, 3, 4, 5])
```



### 1.2.2 filter

`filter` 함수도 입력리스트의 `item`에 입력함수를 적용하고 결과적으로 참을 반환하는 `item`만 처리하는 함수이다.

``` python
filter(입력함수, 입력리스트)
```

리스트에서 5 이상인 경우의 데이터를 반환하는 예제이다.

```python
def test_filter(self):
  result = list(filter(lambda x: x > 5, range(10)))
  self.assertEqual(result, [6, 7, 8, 9])

```

### 1.2.3 reduce

`reduce` 함수는 리스트의 첫번째, 두번째 `item`을 인자로 받아 하나의 값을 반환하고 최종적으로 단일 값을 반환하는 함수이다.

```python
reduce(입력함수, 입력리스트)
```

reduce 함수를 통해서 최종 합을 구하는 예제이다.

```python
from functions import reduce

def test_reduce(self):
  result = reduce(lambda x, y: x + y, [1, 2, 3])
  self.assertEqual(result, 6)
```

## 2. 정리

파이썬에서 지원하는 람다 표현식에 대해서 알아보았다. 람다 함수는 이름 없는 함수로 별도의 함수로 정의하지 않고 간단하게 작성할 수 있는 장점이 있다. 이런 이유로 람다 함수를 인자로 넘겨주어 자주 사용한다.

## 3. 참고

* https://wikidocs.net/64
* https://dojang.io/mod/page/view.php?id=2359
* https://book.pythontips.com/en/latest/map_filter.html
