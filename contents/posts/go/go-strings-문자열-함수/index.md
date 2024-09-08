---
title: "Go Strings (문자열 함수)"
description: "Go Strings (문자열 함수)"
date: 2021-05-28
update: 2021-05-28
tags:
  - golang
  - string
  - replace
  - split
  - join
  - repeat
  - 스트링
  - 문자열
  - 고랭
---

## 문자열 함수

Golang에서 표준 라이브러리중에 `strings` 패키지에서 많이 유용하게 사용할 수 있는 문자열 함수들을 제공한다. 여러 예제를 통해서 문자열를 다루어보자.

### 1. Search (Contains, Prefix/Suffix, Index)

```go
func TestStrings(t *testing.T) {
	assert.True(t, strings.Contains("test", "st"))
	assert.True(t, strings.ContainsAny("test", "s"))
	assert.True(t, strings.HasPrefix("test", "te"))
	assert.True(t, strings.HasSuffix("test", "st"))
  
  assert.Equal(t, 2, strings.Count("test", "t"))
	assert.Equal(t, 1, strings.Index("test", "e"))
}
```

### 2. Replace (Uppercase/Lowercase, Trim, Map)

```go
func TestStrings(t *testing.T) {
	assert.Equal(t, "f00", strings.Replace("foo", "o", "0", -1))
	assert.Equal(t, "test", strings.ToLower("TEST"))
	assert.Equal(t, "TEST", strings.ToUpper("test"))
	assert.Equal(t, "Test", strings.Trim(" Test  ", " "))
	assert.Equal(t, "Test", strings.TrimSpace(" Test  "))
	f := func(r rune) rune {
		return r + 1
	}
	assert.Equal(t, "bc", strings.Map(f, "ab"))
}
```

> `Map` 함수는 인자로 함수와 문자열을 받고 문자열의 각 character마다 함수를 적용하는 함수이다.

### 3. Split (Split, Fields)

```go
func TestStrings(t *testing.T) {
	assert.Equal(t, []string{"a", "b", "c"}, strings.Split("a,b,c", ","))
  assert.Equal(t, []string{"t", "e", "s", "t"}, strings.Fields("t\t   e s t"))
}
```

> Fields는 문자열을 white space character (unicode.IsSpace로 정의됨) 기준으로 문자열을 `split` 시켜준다

### 4. Concatenate (+, Sprintf, Builder)

`fmt.Sprintf()` 메서드로 원하는 여러 타입을 formatting을 통해서 문자열로 반환해주어 원하는 문자열을 쉽게 만들 수 있다.

```go
func TestStrings(t *testing.T) {
	assert.Equal(t, "hello world", "hello"+" world")
	assert.Equal(t, "data: 123", fmt.Sprintf("%s %d", "data:", 123))
	assert.Equal(t, "3.1416", fmt.Sprintf("%.4f", math.Pi))

	var b strings.Builder
	for i := 3; i >= 1; i-- {
		fmt.Fprintf(&b, "%d...", i)
	}
	b.WriteString("end")
	assert.Equal(t, "3...2...1...end", b.String())
}
```

> `strings.Builde`r에서 제공하는 메서드를 통해서 문자열 조합을 더 빠르고 효과적으로 할수 있는 기능을 제공한다

## 5. Join (Join, Repeat)

```go
func TestStrings(t *testing.T) {
	assert.Equal(t, "a-b", strings.Join([]string{"a", "b"}, "-"))
	assert.Equal(t, "AAAAA", strings.Repeat("A", 5))
}
```

### 6. Format, Convert (strconv)

```go
func TestStrings(t *testing.T) {
	assert.Equal(t, "23", strconv.Itoa(23))
	assert.Equal(t, "ff", strconv.FormatInt(255, 16))

	intValue, _ := strconv.Atoi("23")
	assert.Equal(t, 23, intValue)
}
```


여기서 작성한 예제는 [github](https://github.com/kenshin579/tutorials-go/tree/master/go-strings)를 참고해주세요.


## 참고

- https://yourbasic.org/golang/string-functions-reference-cheat-sheet/
- http://pyrasis.com/book/GoForTheReallyImpatient/Unit46
- https://mingrammer.com/gobyexample/string-functions/
- http://cloudrain21.com/go-how-to-concatenate-strings
- http://pyrasis.com/book/GoForTheReallyImpatient/Unit46/02
- https://golang.org/pkg/strings/
- https://yourbasic.org/golang/string-functions-reference-cheat-sheet/





