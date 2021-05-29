---
title: 'Go Strings (문자열 함수)'
layout : post
category: 'go'
author: [Frank Oh]
image: ../img/cover-go.png
date: '2021-05-28T18:18:23.000Z'
draft: false
tags: ["go", "golang", "string", "strings", "search", "replace", "split", "join", "repeat", "스트링", "문자열", "고랭", "치환"]
---

- search (contains, prefix/sufifx, index)
- replace (uppercase/lowercase, trim)
- concatenate (sprintf, +, builder)
- split (split, fields)
- Join (repeat)
- format, convert (strconv.itoa, formatint)

# 문자열 함수

Golang에서 표준 라이브러리중에 strings 패키지에서 많이 유용하게 사용할 수 있는 문자열 함수들을 제공한다. 여러 예제를 통해서 문자열를 다루어보자. 

## 1. Search (Contains, Prefix/Suffix, Index)

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



## 2. Replace (Uppercase/Lowercase, Trim)

```go

```



## 3. Split (split, fields)

```

```



## 4. Concatenate (+, Sprintf, builder)

```

```



## 5. Join (join, repeat)

```

```



## 6. Format, Convert (strconv)



```

```




# 참고

- https://yourbasic.org/golang/string-functions-reference-cheat-sheet/
- http://pyrasis.com/book/GoForTheReallyImpatient/Unit46
- https://mingrammer.com/gobyexample/string-functions/
- http://cloudrain21.com/go-how-to-concatenate-strings
- http://pyrasis.com/book/GoForTheReallyImpatient/Unit46/02
- https://golang.org/pkg/strings/
- https://yourbasic.org/golang/string-functions-reference-cheat-sheet/





