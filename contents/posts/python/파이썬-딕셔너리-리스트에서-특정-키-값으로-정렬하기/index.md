---
title: "파이썬 딕셔너리 리스트에서 특정 키 값으로 정렬하기"
description: "파이썬 딕셔너리 리스트에서 특정 키 값으로 정렬하기"
date: 2020-09-03
update: 2020-09-03
tags:
  - python
  - sort
  - key
  - dict
  - 파이썬
  - 정렬
  - 키
  - 딕셔너리
  - 리스트
---

## 1. 들어가며

파이썬에서 딕셔너리 리스트에서 특정 키 값(ex. age)에 따라서 정렬하는 방법에 대해서 알아보자.

```python
student_list = [
  {'name': 'Homer', 'age': 39},
  {'name': 'Homer1', 'age': 20},
  {'name': 'Homer2', 'age': 5},
  {'name': 'Bart', 'age': 10}
]
```

리스트 정렬를 위해 파이썬에서 기본적으로 `list.sort()`와 `sorted()` 함수를 제공한다.

- `list.sort()`
    - 리스트를 직접 수정하여 `in-place` 방식으로 정렬한다
    - list 자료구조에만 사용할 수 있다

```python
def test_simple_sort(self):
  a_list = [3, 2, 1, 7]
  a_list.sort()
  self.assertEqual(a_list, [1, 2, 3, 7])
```

- sorted()
    - 이 함수의 경우에는 정렬된 새로운 리스트를 반환한다
    - iterable한 자료구조에도 사용 가능하다

```python
def test_simple_sorted(self):
  a_list = [3, 2, 1, 7]
  new_list = sorted(a_list)
  self.assertEqual(new_list, [1, 2, 3, 7])
```



## 2. 딕셔너리 리스트 특정 키 값으로 정렬하기

`list.sort()`와 `sorted()` 함수에 인자 값으로 `key` 함수를 지정할 수 있다. 이 `key` 함수의 반환 값이 compare 되어 정렬이 된다

### 2.1 키 함수로 람다 사용

`key` 함수로 딕셔너리에서 age값을 반환하는 [람다함수](https://blog.advenoh.pe.kr/파이썬에서-람다-함수-익숙해지기/)를 지정하여 나이 순으로 정렬한다.

```python
def sort_list_by_age_using_lambda(student_list):
    return sorted(student_list, key=lambda k: k['age'])
```

정렬된 결과를 확인해보면 나이 순으로 잘 정렬된 것을 확인할 수 있다.

```python
def test_sort_list_by_age_using_lambda(self):
  result = sort.sort_list_by_age_using_lambda(self.student_list)
  for i in range(len(result) - 1):
    print(i, result[i].get('age'))
    self.assertLess(result[i].get('age'), result[i + 1].get('age'))
```



### 2.2 키 함수로 itemgetter 사용

자료구조에서 키 나 속성 값을 쉽게 접근하도록 `operator`이라는 모듈에서 여러 함수를 제공해준다. `operator` 모듈에서 `itemgetter()` 메서드를 사용하여 `key` 함수를 지정할 수 있다.

```python
from _operator import itemgetter

def sort_list_by_age_using_itemgetter(student_list):
  return sorted(student_list, key=itemgetter('age'))
```

동일하게 나이 순으로 정렬이 된다.

```python
def test_sort_list_by_age_using_itemgetter(self):
  result = sort.sort_list_by_age_using_itemgetter(self.student_list)
  for i in range(len(result) - 1):
    print(i, result[i].get('age'))
    self.assertLess(result[i].get('age'), result[i + 1].get('age'))
```



### 2.3 여러 키 값으로 정렬시키기

여러 키 값(ex. age -> name) 기준으로도 정렬을 할 수 있다. 릭셔너리에서 나이가 같은 경우에는 이름으로 정렬을 해보자.

람다 함수와 `itemgetter()` 함수 사용시 아래와 같이 지정해주면 된다.

```python
def sort_list_by_two_keys_using_lambda(student_list):
  return sorted(student_list, key=lambda k: (k['age'], k['name']))
```



```python
def sort_list_by_two_keys_using_itemgetter(student_list):
  return sorted(student_list, key=itemgetter('age', 'name'))
```

딕셔너리에서 나이 순으로 정렬하고 같은 나이에 대해서는 이름으로 정렬이 된다.

```python
def test_sort_list_by_two_keys_using_itemgetter(self):
  student_list = [
    {'name': 'Homer', 'age': 39},
    {'name': 'Homer2', 'age': 5},
    {'name': 'Homer3', 'age': 5},
    {'name': 'Bart', 'age': 10},
  ]
  result = sort.sort_list_by_two_keys_using_itemgetter(student_list)
  for i in range(len(result) - 1):
    if result[i].get('age') == result[i + 1].get('age'):
      self.assertLess(result[i].get('name'), result[i + 1].get('name'))
     else:
       self.assertLess(result[i].get('age'), result[i + 1].get('age'))
```

## 3. 정리

sorted() 함수에서 `key` 함수를 지정할 수 있어 여러 키 값의 기준으로 정렬을 쉽게 할 수 있었다. 단일 키외에도 여러 키 값을 기준으로 정렬을 할 수 있다.

## 4. 참고

- https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
- https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
- https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-itemgetter/
- https://wayhome25.github.io/python/2017/03/07/key-function/

