# 블로그 : React Router v3
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] 2017년 3월에 router v4이 나왔음.
- [ ] 라우터는 사용자가 요청한 URL에 따라서 다른 결과물을 렌더링해줌
- [ ] 리액트 라우터를 사용하면 프로젝트에서는 어떤 경로로 들어오던 똑같은 html 파일과 자바스크립트 파일을 제공함
- [ ] URL에 따라서 지정된 컴포넌트를 렌더링해줌

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20React%20Router%20v3/image_1.png)

- [ ] 리액트 프로젝의 경우 모든 프로젝트의 클라이언트 정보를 코드를 번들링할 떄 한 팡리로 담기 때문에 주소가 변한다고해서 페이지를 새로 로딩할 필요가 없음
ㅁ. Link 라는 컴포넌트를 사용하면 브라우저의 주소만 바꿔주고 페이지를 새로 로딩하지 않음
ㅁ. 브라우저의 주소가 바뀌고 나면 Router 컴포넌트가 이를 인식하여 우리가 정한 컴포넌트를 보여주게됨

- [ ] context는 React 프로젝트에서 전역적으로 사용될 수 있는 객체임
ㅁ. 컴포넌트마다 props 로 전달하기 힘든 경우에 이 기능이 사용됨

- [ ] Cannot read property 'PropTypes' of undefined
ㅁ. react을 16에서 15으로 변경하면 됨

[https://stackoverflow.com/questions/48395565/reactjs-typeerror-cannot-read-property-proptypes-of-undefined](https://stackoverflow.com/questions/48395565/reactjs-typeerror-cannot-read-property-proptypes-of-undefined)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* React Router
	* [https://velopert.com/2937](https://velopert.com/2937)
	* [https://velopert.com/1173](https://velopert.com/1173)
	* [https://velopert.com/3275](https://velopert.com/3275)