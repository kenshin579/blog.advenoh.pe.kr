# 블로그 : 리액트 js
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] spring boot + crud 기본 예제를 이해하고 quartz 스케줄링 목록을 볼수 있는 코드를 작성하자

- [ ] this.props.info는 뭔가?

라이브러리
* 라우터
	* react-router
	* next.js
	* after.js
* 상태관리
	* Redux
	* MobX

- [ ] webpack
ㅁ. 여러 파일을 한개로 결합하기 위해서 사용함

- [ ] babel
ㅁ. 새로운 자바 스크립트 문법을 사용하기 위해서 babel 도구를 사용함

- [ ] jsx
ㅁ. javascript로 생성해야 하는 걸 보다 쉽게 작성할 수 있도록 해줌
ㅁ. 규칙
* 모든 태그는 닫아야 함
* 두개 이상의 엘리먼트는 무조건 하나의 엘리먼트로 감싸져 있어야 함

Hi, Shane.

I told my friend that u served in the korean army as Katusa so my friend hope to see if you could do the simultaneous translation next weds from 11~2pm.

It’s volunteer work, though.
Anyway, I will explain the situation over the phone. Thx.

I told my friend that u served in the Korean army as Katusa so my friend think that u would be much better.

설치
># yarn global add create-react-app

생성
># create-react-app hello-react
># yarn start

조건부 렌더링

- [ ] JSX에서 조건부 렌더링할 때는 삼항 연사자나 AND 연사자를 사용함
ㅁ. IF를 사용하려면 IIFE를 사용해야 함

-

[https://velopert.com/3613](https://velopert.com/3613)

4편 : Props와 State

- [ ] 리액트 컴포넌트에서는 2가지 데이터가 있음
* props
	* 부모 컨포넌트 -> 자식 컨포넌트에게 주는 값
	* 자신 컨포넌트는 값을 받기만할 수 있고 수정할 수 없음
* state
	* 컴포넌트 내부에서 선언하며 내부에서 값을 변경할 수 있다

- [ ] props값은 name=“…”이런식으로 태그의 속성을 설정해주는 것처럼 해준다.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EB%A6%AC%EC%95%A1%ED%8A%B8%20js/image_2.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EB%A6%AC%EC%95%A1%ED%8A%B8%20js/image_3.png)

- [ ] state에 있는 값을 바뀌기 위해서는 this.setState를 사용해야 함.
ㅁ. 리액트에서는 이 함수가 호출되면 컴포넌트가 리렌더링 되도록 설계되어있음

- [ ] setState는 객체의 깊은 값까지는 확인하지 못함

이벤트 설정
* 이벤트 이름은 camelCase(ex. onClick)으로 설정해야 함
* 이벤트에 전달해주는 값은 함수여야 함

Chap5 : LifeCycle API
- [ ] 컨포넌트가 브라우저에 나타날때, 사라질때, 업데이트될 때 호출되는 API임

컴포넌트 초기 생성

* contructor
	* 컴포넌트가 새로 만들어질 때마다 호출됨
* componentWillMount : 이건 v16.3부터 deprecated됨
* componentDidMount : 컴포넌트가 화면에 나타나게 될 떄 호출됨
	* 해당 컴포넌트에서 필요로하는 데이터를 요청할 때 (axios, fetch로)

컴포넌트 업데이트

[https://velopert.com/3631](https://velopert.com/3631)

* componentWillReceiveProps : v16.3부터 deprecated
* getDerivedStateFromProps : props로 받아온 값을 state로 동기화 하는 작업을 해줘야 하는 경우에 사용함
* shouldComponentUpdate : true, false를 반환함
	* 우리가 작성한 로직에 따라서 true, false을 반한하면 해당 조건에 render 함수를 호출하거나 하지 않게 됨
* componentWillUpdate : shouldComponentUpdate가 true인 경우에만 호출됨 v16.3부터 deprecated됨
	* 애니메이션 효과를 호기화, 이벤트 리스너를 없애는 작업을 함
	* 이 함수가 호출되고 나서 render()가 호출됨
* getSnapshotBeforeUpdate : render() 호출이후에 호출됨
* componentDidUpdate : render() 호출한 다음에 발생함
	* this.props, this.state가 바뀌어 있음

컴포넌트 제거

* componentWillUnmount : 컨포넌트가 더 이상 필요없을 때
	* 등록된 이벤트를 제거할 때 clearTimeout할 때

컴포넌트에 에러 발생

- [ ] render() 함수에서 오류가 발생하면 리액트 앱이 크래쉬됨, 이럴때 사용할 수 있는 메서드

* componentDidCatch : 을 통해서 오류를 잡아주면 됨

Chap6 : Input 상태 관리하기

PhoneForm 만들기

input 다루기

- [ ] onChange 이벤트가 발생하면, e.target.value값을 통하여 이벤트 객체에 담겨 있는 현재 텍스트 값을 읽어올 수 있고
이 값을 state의 name 속성에 설정하면 됨

-

**Computed property names**
- [ ] [] bracket 안의 표현식이 computed되어 property 이름으로 사용된다

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EB%A6%AC%EC%95%A1%ED%8A%B8%20js/image_4.png)

* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#Computed_property_names

부모 컴포넌트에게 정보 전달하기

- [ ] state안에 있는 값을 부모 컴포넌트에게 전달해주는 방법
* 부모 컴포넌트에서 메서드 만들기
* 부모 메서드를 자식에게 전달
* 자식 내부에서 호출함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EB%A6%AC%EC%95%A1%ED%8A%B8%20js/image_1.png)

Chap7 : 배열 다루기 생성과 렌더링

- [ ] 리액트에서는 state 내부의 값을 직접적으로 수정하면 안됨
ㅁ. push, splice, unshift, pop을 사용하면 안됨
ㅁ. 새 배열을 만들어내는 함수는 ok : concat, slice, map, filter

데이터 추가

Chap8 : 배열 다루기 제거와 수정

데이터 제거

Chap9 : 불변성을 지키는 이유와 업데이트 최적화

데이터 필터링 구현하기

- [ ] App 컴포넌트의 상태가 업데이트 되면, 컴포넌트의 리렌더링이 발생하게 되고,
컴포넌트가 리렌더링되면 그 컴포넌트의 자식 컴포넌트도 리렌더링됩니다.

Chap10 : 앞으로의 공부 방향

ㄴㅇㄹ

- - - -

**스터디 목록**

* 리액트는 무엇인가?
* 리액트 프로젝트 시작하기
* JSX
* props와 state
* LifeCycle API
* input 상태 관리하기
* 배열 다루기 생성과 렌더링
* 불변성을 지키는 이유와 업데이트 최적화
* 앞으로의 공부방향

* Todo List
	* [https://velopert.com/3480](https://velopert.com/3480)
* API 연동 실습 (axios)
	* [https://velopert.com/3503](https://velopert.com/3503)
* Redux
	* 목차
		* [https://velopert.com/3365](https://velopert.com/3365)
		* 카운터 만들기
		* 멀티 카운터 만들기
		* immutable.js 익히기
		* Ducks 구조와 react-actions 익히기
		* 주소록에 Redux 끼얹기

	* [리덕스(Redux)를 왜 쓸까? 그리고 리덕스를 편하게 사용하기 위한 발악 (i)](https://velopert.com/3528)
	* [리덕스(Redux)를 왜 쓸까? 그리고 리덕스를 편하게 사용하기 위한 발악 (ii)](https://velopert.com/3533)
	* [Redux 를 통한 React 어플리케이션 상태 관리 :: 목차](https://velopert.com/3365)
	* [리덕스 미들웨어, 그리고 비동기 작업 (외부데이터 연동)](https://velopert.com/3401)
	* 카운터
* React 라우터
	* [https://velopert.com/3411](https://velopert.com/3411)

4. 참고

* 리액트
	* [https://velopert.com/3613](https://velopert.com/3613)

* 소스 예제 검색
	* [http://www.springboottutorial.com/spring-boot-react-full-stack-crud-maven-application](http://www.springboottutorial.com/spring-boot-react-full-stack-crud-maven-application)
	* [https://www.jeejava.com/spring-boot-reactjs-crud-example/](https://www.jeejava.com/spring-boot-reactjs-crud-example/)
	* [https://www.callicoder.com/spring-boot-rest-api-tutorial-with-mysql-jpa-hibernate/](https://www.callicoder.com/spring-boot-rest-api-tutorial-with-mysql-jpa-hibernate/)
	* [https://stormpath.com/blog/crud-application-react-spring-boot-user-authentication](https://stormpath.com/blog/crud-application-react-spring-boot-user-authentication)
	* [https://spring.io/guides/tutorials/react-and-spring-data-rest/](https://spring.io/guides/tutorials/react-and-spring-data-rest/)
	* [https://medium.com/coding-crackerjack/spring-boot-and-reactjs-a50367d56521](https://medium.com/coding-crackerjack/spring-boot-and-reactjs-a50367d56521)