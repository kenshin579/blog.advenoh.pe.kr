---
title: "jq - 명령어 JSON 처리기 사용법"
description: "jq - 명령어 JSON 처리기 사용법"
date: 2023-01-27
update: 2023-01-27
tags:
  - jq
  - gojq
  - json
---

`jq`는 자주 사용하지는 않지만, 필요할 때는 용이하게 사용하는 경우가 종종 있어서 기록상 블로그에 남겨둡니다.

## jq 사용법 모음

### 1. jq로 array에서 특정 필드로 매칭되는 필드 값을 추출하려면?


아래와 같은 json array에서 특정 필드, `id`가 매칭되는 item에서 원하는 필드를 추출하면 `jq` 쿼리는 어떻게 작성하면 될까요?

```json
[
  {
    "id": "e0a65e34-b516-4f49-bb08-7108dc104046",
    "name": "Frank",
    "country": "KR"
  },
  {
    "id": "423be8de-9c04-4f0e-8ff0-545a8cb175b4",
    "name": "David",
    "country": "KR"
  },
  {
    "id": "61adaddd-525e-4a81-a4eb-7fb99b46cc05",
    "name": "Angela",
    "country": "US"
  }
]

```


`jq`의 `select(bool)` syntax는 bool 표현 식이 참이 되는 값을 선택하는 함수여서 아래와 같이 쿼리를 작성하면 id가 매칭되는 item이 선택되고 보고자 하는 필드를 선택해서 출력하면 된다.

```bash
$ cat json/ex2.json | jq '.[] | select(.id == "423be8de-9c04-4f0e-8ff0-545a8cb175b4") | {name, country}'
{
  "name": "David",
  "country": "KR"
}
```

### 2. JSON 문자열에서 배열의 수를 출력하려면?

배열의 수는 `length` 함수로 얻을 수 있다.

```bash
$ echo '[{"username":"user1"},{"username":"user2"}]' | jq '. | length'
```

참고

- https://phpfog.com/count-json-array-elements-with-jq/


## 참고

- https://stackoverflow.com/questions/51184524/get-parent-element-id-while-parsing-json-data-with-jq
- https://stackoverflow.com/questions/18592173/select-objects-based-on-value-of-variable-in-object-using-jq
- https://stedolan.github.io/jq/manual/#select(boolean_expression)
- https://www.44bits.io/ko/post/cli_json_processor_jq_basic_syntax