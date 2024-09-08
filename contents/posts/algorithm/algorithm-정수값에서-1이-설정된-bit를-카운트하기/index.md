---
title: "Algorithm 정수값에서 1이 설정된 bit를 카운트하기"
description: "Algorithm 정수값에서 1이 설정된 bit를 카운트하기"
date: 2018-10-28
update: 2018-10-28
tags:
  - 알고리즘
  - 인터뷰
  - 면접
  - 코드면접
  - 비트
  - 카운트
---

## 1. Problem

정수값에서 1인 비트를 카운트하는 문제입니다.

### 1.1 입력 / 결과

- 7 : 111 —> 3
- 23 : 10111 —> 4
- 13 : 1101 —> 3

## 2. Solution

### 2.1 Approach 1

컴퓨터 공학과 수업 중에 assembly를 다루는 과목은 꼭 필수로 들었던 기억이 납니다. 매우 오래전 얘기긴 하지만, assembly로 과제를 하면서 자연스럽게 비트 연산을 익혔던 것 같습니다.
다시 문제를 풀려고 하니, 솔직히 기억은 나지 않네요. 그래도 AND, OR만 알아도 쉽게 풀 수 있는 문제들이 많이 있습니다.

이진수에서 1이 있는지 확인하려면 맨 끝자리에서 1과 AND 연산하면서 비트를 카운트하면 쉽게 카운트를 할 수 있습니다.

```java
public static int countBits1(int n) {
    int count = 0;
    while (n > 0) {
        count += n & 1; //마지막 bit가 1이면 count함 (AND로 확인)
        n >>= 1; //마지막 bit를 삭제함
    }
    return count;
}
```

이 알고리즘은 정수 값이 0이 될때까지 반복하기 때문에 복잡도는 O(n)이 됩니다. 이것보다 더 빠른 방법은 없을 까요?
브라이언 커니핸 교수님이 고안한 알고리즘은 O(log n)으로 비트를 카운트 할 수 있습니다.

### 2.2 Approach 2 - Brian Kernighan’s Algorithm

![Brian Kernighan](image_1.jpeg)

처음 들어보신 분도 계실 수 있지만, 브라이언 커니핸 ( [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) )이란 분은 초창기 UNIX를 개발하셨고 유닉스에서 자주 사용하는 AWK 명령어도 개발하신 분이십니다. 2000년 이후부터 쭉 프린스턴 대학교에서 교수직으로 일하고 계십니다. 구현은 쉽지만, 이걸 생각해냈다는 게 정말로 대단한 것 같습니다. 기본 알고리즘을 알아보죠.

- N = N AND (N-1)를 정수값이 0이 될때까지 반복한다.
- 반복하는 카운트를 세면 1인 비트를 얻을 수 있다.

```java
public static int countBits2(int number) {
    int count = 0;
    while (number > 0) {
        number &= number - 1;
        count++;
    }
    return count;
}
```

알고리즘은 간단한데 어떻게 이런 결과가 되는지 스텝으로 알아보죠.

```
알고리즘 예제
N = 23 (10111)
AND 22 (10110) —> 22 (10110)
COUNT = 1

N = 22 (10110)
AND 21 (10101) —> 20 (10100)
COUNT = 2

N = 20 (10100)
AND 19 (10011) —> 16 (10000)
COUNT = 3

N = 16 (10000)
AND 15 (01111) —> 0 (00000)
COUNT = 4
```

이 방법 외에도 다양한 알고리즘은 더 많이 존재 합니다 (참고: [Bit Twiddling Hacks](https://graphics.stanford.edu/~seander/bithacks.html) ). 누군가 정말로 열심히 연구하고 공부한 것 같아요.

## 3. Reference

- [https://www.geeksforgeeks.org/count-set-bits-in-an-integer/](https://www.geeksforgeeks.org/count-set-bits-in-an-integer/)
- [https://www.quora.com/How-do-you-count-the-number-of-1-bits-in-a-number-using-only-bitwise-operations](https://www.quora.com/How-do-you-count-the-number-of-1-bits-in-a-number-using-only-bitwise-operations)
- Bit Twiddling Hacks
    - [https://graphics.stanford.edu/~seander/bithacks.html](https://graphics.stanford.edu/~seander/bithacks.html)
