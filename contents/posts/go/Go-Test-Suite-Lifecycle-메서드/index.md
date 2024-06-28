---
title: "Go Test Suite (Lifecycle 메서드)"
description: "Go Test Suite (Lifecycle 메서드)"
date: 2021-07-17
update: 2021-07-17
tags:
  - golang
  - test
  - suite
  - testify
  - before
  - after
  - lifecyle 
  - unit test
  - test suite
---


Golang에서는 [testify](https://github.com/stretchr/testify) library에서 제공하는 여러 기능 (ex. assertion, mocking, suite)를 통해서 쉽게 unit test를 작성할 수 있다. 특정 config 설정에 따라 전체 테스트를 skip 해야 하는 경우가 있다. 이런 경우 Test Suite를 이용하면 해당 케이스를 쉽게 해결할 수 있다.

- ex. cluster_test.go - redis cluster 모드인 경우에만 실행하기

`suite.Run()` 메서드를 실행하면 Suite에 정의된 메서드들이 차례로 실행되기 때문에 그전에 조건을 두어 참인 경우에 `t.Skip()` 메서드를 호출하면 전체 테스트가 skip 처리된다.

```go
func TestExampleTestSuite(t *testing.T) {
	//특정 조건인 경우에 전체 테스트를 실행하지 않을 수 있다
	if isSkip() {
		t.Skip("skipping")
	}
	suite.Run(t, new(ExampleTestSuite))
}

func isSkip() bool {
	return false
}

```


Suite 패키지는 테스트 실행 전후로 여러 인터페이스 제공하여 테스트 전후로 다양한 처리가 가능하다. 여러 life cycle 메서드에 대해서 알아보자. `suite.Run()` 실행 로직을 확인해보면 어떻게 [suite 인터페이스](https://github.com/stretchr/testify/blob/master/suite/interfaces.go) 메서드들이 테스트 실행 life cycle의 어느 시점에 실행되는지 확인할 수 있다.

```go
func Run(t *testing.T, suite TestingSuite) {
  
  ...생략...
  if afterTestSuite, ok := suite.(AfterTest); ok {
						afterTestSuite.AfterTest(suiteName, method.Name)
					}

					if tearDownTestSuite, ok := suite.(TearDownTestSuite); ok {
						tearDownTestSuite.TearDownTest()
					}
  
    ...생략...
}
  º
```

- 전처리
    - `SetupSuite` - suite에서 전체 테스트 실행 전에 한번만 실행된다
    - `SetupTest` - suite에서 각 테스트 실행 전에 실행된다
    - `BeforeTest` - 테스트가 실행하기 전에 `suiteName, testName` 인자를 받아 실행하는 함수이다
- 후처리
    - `AfterTest` - 테스트가 실행후에 suiteName testName 인자를 받아 실행하는 함수이다
    - `TearDownTest` - suite에서 각 테스트 실행후에 실행된다
    - `TestDownSuite` - suite에서 모든 테스트가 실행된 후에 실행된다

Test Suite로 테스트를 작성하려면 `suite.Suite` 구조체를 담는 `struct`를 생성하고 해당 `struct`에 대한 suite 메서드를 정의하면 된다.

```go
type ExampleTestSuite struct {
	suite.Suite
}

func (ets *ExampleTestSuite) SetupSuite() {}

...생략...
func (ets *ExampleTestSuite) TestExample1() {}

```



작성한 전체 [테스트 코드](https://github.com/kenshin579/tutorials-go/blob/master/go-testing/suite_test.go)입니다.

```go
type ExampleTestSuite struct {
	suite.Suite
	TestValue int
}

//suite에서 전체 테스트 실행 전에 한번만 실행된다
func (ets *ExampleTestSuite) SetupSuite() {
	fmt.Println("SetupSuite :: run once")
}

//suite에서 각 테스트 실행 전에 실행된다
func (ets *ExampleTestSuite) SetupTest() {
	fmt.Println("SetupTest :: run setup test")
	ets.TestValue = 5
}

//테스트가 실행하기 전에 suiteName testName 인자를 받아 실행하는 함수이다
func (ets *ExampleTestSuite) BeforeTest(suiteName, testName string) {
	fmt.Printf("BeforeTest :: run before test - suiteName:%s testName: %s\n", suiteName, testName)
}

//TEST ----------------------------------------
func (ets *ExampleTestSuite) TestExample1() {
	fmt.Println("TestExample1")
  assert.Equal(ets.T(), ets.TestValue, 5) //이렇게도 assert 확인할 수 있지만, 
	ets.Equal(ets.TestValue, 5) //assert 체크하려면 이렇게 사용하시면 됩니다.
}

func (ets *ExampleTestSuite) TestExample2() {
	fmt.Println("TestExample2")
}

//TEST ----------------------------------------

//테스트가 실행후에 suiteName testName 인자를 받아 실행하는 함수이다
func (ets *ExampleTestSuite) AfterTest(suiteName, testName string) {
	fmt.Printf("AfterTest :: suiteName:%s testName: %s\n", suiteName, testName)
}

//suite에서 각 테스트 실행후에 실행된다
func (ets *ExampleTestSuite) TearDownTest() {
	fmt.Println("TearDownTest :: run before after test")
}

//suite에서 모든 테스트가 실행된 후에 실행된다
func (ets *ExampleTestSuite) TearDownSuite() {
	fmt.Println("TearDownSuite :: run once")
}

func TestExampleTestSuite(t *testing.T) {
	//특정 조건인 경우에 전체 테스트를 실행하지 않을 수 있다
	if isSkip() {
		t.Skip("skipping")
	}
	suite.Run(t, new(ExampleTestSuite))
}

func isSkip() bool {
	return false
}

```



테스트를 실행해서 Life cycle를 확인해볼까요?

```bash
=== RUN   TestExampleTestSuite
SetupSuite :: run once
--- PASS: TestExampleTestSuite (0.00s)
=== RUN   TestExampleTestSuite/TestExample1
SetupTest :: run setup test
BeforeTest :: run before test - suiteName:ExampleTestSuite testName: TestExample1
TestExample1
AfterTest :: suiteName:ExampleTestSuite testName: TestExample1
TearDownTest :: run before after test
    --- PASS: TestExampleTestSuite/TestExample1 (0.00s)
=== RUN   TestExampleTestSuite/TestExample2
SetupTest :: run setup test
BeforeTest :: run before test - suiteName:ExampleTestSuite testName: TestExample2
TestExample2
AfterTest :: suiteName:ExampleTestSuite testName: TestExample2
TearDownTest :: run before after test
TearDownSuite :: run once
    --- PASS: TestExampleTestSuite/TestExample2 (0.00s)
PASS
```

## 참고

- https://brunoscheufler.com/blog/2020-04-12-building-go-test-suites-using-testify

- https://pkg.go.dev/github.com/stretchr/testify/suite

  





