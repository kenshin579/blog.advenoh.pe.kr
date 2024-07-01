---
title: "파이썬 : 커맨트 라인에서 명령어 옵션들 argparse 모듈를 이용해서 쉽게 파싱하기"
description: "파이썬 : 커맨트 라인에서 명령어 옵션들 argparse 모듈를 이용해서 쉽게 파싱하기"
date: 2018-11-04
update: 2018-11-04
tags:
  - python
  - argparse
  - command
  - option
  - cli
  - 파이썬
  - 명령어
  - 옵션
---

## 1. argparse 모듈이란?

셀이나 리눅스 명령어를 실행할 때 많은 옵션이 존재합니다. 아래는 pip 명령어(파이썬 패키지 관리자)의 옵션 목록입니다. Flag 형태의 옵션(ex. --no-color)이나 입력값을 받을 수 있는 옵션(ex. --log <path>)도 있습니다.

![](image_6.png)

이런 옵션을 파이썬에서 구현하려면 어떻게 해야 할까요? 실제 구현한다면, 실행 명령어를 인자로 받아서 parse 하는 과정이 필요합니다. 직접 구현하기는 좀 부담스럽죠. 셀이나 여러 언어에서 이런 부분들을 별도의 모듈로 제공합니다. 파이썬에서는 커맨트parsing 라이브러리는 getopt, argparse, docopt가있습니다. 이 중에서 파이썬에서 많이 사용되는 **argparse** 를 알아보도록 하겠습니다.

## 2. argparse 옵션 알아보기

argparse는 파이썬 표준 라이브러리에 포함되어 있어 별도로 설치할 필요는 없습니다. 모듈을 사용하기 위해 import로 추가만 해주면 됩니다.

```python
import argparse
```

## 2.1 help 도움말 옵션 추가하기

커맨트 라인에서 대부분의 명령어는 도움말을 제공합니다. 옵션 -h 이나 --help 으로 명령어 옵션들에 대한 설명을 확인할 수 있습니다. argparse 모듈에서는 도움말 옵션은 기본으로 추가됩니다.

```python
parser = argparse.ArgumentParser(description="This is test script”) # 실행하는 스크립트의 설명 내용도 담을 수 있다
parser.parse_args()
```

-h 옵션을 주면 argparse 모듈에서 알아서 명령어에 대한 기본 설명과 옵션을 잘 정리해서 보여줍니다.

![](image_2.png)

### 2.2 Flag 형태 옵션 추가하기

커맨트 라인에서 flag 형태의 옵션이 가장 많이 사용됩니다. Flag 옵션(-v, --verbosity)이 주어졌을 때 실행하는 옵션입니다. add_argument() 함수를 통해서 여러 옵션에 대해서 설정할 수 있습니다. 아래와 같이 dash 입력으로 short와 long 옵션을 지정할 수 있고 해당 옵션에 대한 설명은 help= 키워드에 지정하면 됩니다. **action 키워드에 ’store_true’로 지정** 하면 해당 옵션이 명시될 때 True 값이 지정되고 없으면 False로 지정됩니다.

- Short Option : single dash (-)
- Long Option : double dash (--)

```python
parser = argparse.ArgumentParser()
parser.add_argument( **"-v", "--verbosity", action='store_true', help="enable verbosity"** )
args = parser.parse_args()
if args.verbosity: # True인 경우에 실행 된다.
print("verbosity enabled")
```

![](image_4.png)

### 2.3 옵션에 Value 값 입력 받기

특정 옵션에 대한 value 값도 입력을 받을 수 있습니다. 예를 들면, 아래와 같이 날짜, 숫자, String 값등을 입력받을 수 있습니다.

```bash
$ ./08_argparse_get_value_options2.py --date 2018-09-22 -m hello -n 1234
```

```python
parser = argparse.ArgumentParser()
parser.add_argument("--date", action='store', dest="date", help="date input")
parser.add_argument("-m", action='store', dest="message", type=str, help="enter message")
parser.add_argument("-n", action='store', dest="number", type=int, help="enter number")
args = parser.parse_args()
print("args", args)
```

- action=’store’ : action을 store로 지정하면 입력한 값을 dest 변수에 저장한다
- dest : 입력한 값이 저장되는 변수이다
    - ex. message 변수에 입력한 메시지가 저장된다
- type: 입력한 값에 대한 타입도 지정할 수 있다
    - 입력한 값이 정수가 아닌 경우에는 ‘error: argument -n invalid int value’ 오류가 출력된다

![](image_1.png)

### 2.4 입력한 값에 대한 유효 검사하기

int나 String과 같은 타입(ex. int)에 대해서는 기본적으로 유효 검사를 해줍니다. 하지만, 날짜와 같은 타입은 별도의 함수 구현이 필요합니다. 입력한 날짜가 YYYY-MM-DD 포맷인지는 strptime() 함수를 실행해서 포맷이 아닌 경우에는 Exception을 띄우도록 해서 체크를 할 수 있습니다.

```python
def valid_date_type(arg_date_str):
    try:
        datetime.datetime.strptime(arg_date_str, "%Y-%m-%d")

        return arg_date_str
    except ValueError:
        msg = "Given Date ({0}) not valid! Expected format, YYYY-MM-DD!".format(arg_date_str)

        raise argparse.ArgumentTypeError(msg)

parser = argparse.ArgumentParser()
parser.add_argument("--date", action='store', dest="date", type=valid_date_type, help="date input")
parser.add_argument("-m", action='store', dest="message", type=str, help="enter message")
parser.add_argument("-n", action='store', dest="number", type=int, help="enter number")
args = parser.parse_args()
print("args", args)
```

![](image_3.png)

### 2.5 선택 집합 세트에서 입력값을 선택하기

choices 키워드로 정해진 선택 집합 세트에서만 입력값을 줄 수 있도록 설정할 수 있습니다.

```python
parser = argparse.ArgumentParser()
parser.add_argument("--count", action='store', choices=["ack-time", "send-time"],

                    help="count the given string from log files")
args = parser.parse_args()
print("args", args)
```

- choices : list에 정해진 값중에 하나면 선택할 수 있다
    - ex. choices=[‘apple’, ‘orange’]

![](image_5.png)

이 외에도 다양한 옵션 설정이 있지만, 자주 사용되는 옵션으로만 정리해보았습니다.

소스 코드는 [github](https://github.com/kenshin579/tutorials-python/tree/master/argparse) 를 참조해주세요.

## 3. 참고

- Parsing LIbraries
- [https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)
- Argparse 모듈
    - [https://docs.python.org/ko/3.7/library/argparse.html](https://docs.python.org/ko/3.7/library/argparse.html)

    - [https://docs.python.org/3/howto/argparse.html](https://docs.python.org/3/howto/argparse.html)
