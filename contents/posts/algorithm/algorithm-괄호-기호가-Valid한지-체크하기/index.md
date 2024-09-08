---
title: "Algorithm 괄호 기호가 Valid한지 체크하기"
description: "Algorithm 괄호 기호가 Valid한지 체크하기"
date: 2018-07-29
update: 2018-07-29
tags:
  - 알고리즘
  - 인터뷰
  - 면접
  - 코드면접
  - 괄호
---

## 1. Problem
괄호 기호가 OPEN, CLOSE 매칭이 제대로 되도록 확인하는 코드 문제입니다.

```java
public boolean solution(String str) {
...
}
```

**1.1 입력 / 결과**
입력 가능한 String 값은 아래와 같습니다.

- ()()() —> true
- )( —> false
- ((()))()() —> true

## 2. Solution

### 2.1 Approach 1

이 문제를 쉽게 해결하는 방법은 **스택 자료구조**를 이용하는 것입니다.
기본 아이디어는 다음과 같습니다.

1. String의 한 char씩 스킨한다
1. OPEN\_괄호 ‘(‘ 을 만나면 스택에 push하고
1. CLOSE\_괄호 ‘)’를 만나면 스택에서 pop을 한다.
1. 스택에 아무것도 남아 있지 않으면, valid한 괄호인것으로 판단할 수 있다

```java
public boolean solution(String str) {
    char[] chars = str.toCharArray();
    Stack<Character> stack = new Stack<>();

    if (str.length() % 2 != 0) {
        return false;
    }

    if (chars[0] == ')') {
        return false;
    }

    for (char ch : chars) {
        if (ch == '(') {
            stack.push(ch);
        } else {
            // close parenthesis
            stack.pop();
        }
    }
    return stack.isEmpty();
}
```

소스코드는 [github](https://github.com/kenshin579/tutorials-interview-questions/blob/master/src/main/java/com/google/ValidParenthesis.java) 에서도 확인할 수 있습니다.

## 3. Reference

- [https://hongku.tistory.com/251](https://hongku.tistory.com/251)
