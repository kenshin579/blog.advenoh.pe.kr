# 블로그 : OAuth 2.0
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
-- oauth의 목적은 access token을 발급 받는 것이다.-

- [ ] Bearer 인증이란
* API에 접속하기 위해서는 access token을 API 서버에 제출해서 인증을 하는 방식
* OAuth에서 고안된 방법

- [ ] Bearer 사용방법
ㅁ.아래와 같이 해더값을 만들어서 보내면 됨
* header
	* api server : server.example.com
	* path : resource
	* access_token : mF_9.B5f-4.1JqM
* ex. GET /resource HTTP/1.1 Host: server.example.com Authorization: Bearer mF_9.B5f-4.1JqM

-- oauth 기본 구성-
일반
OAuth

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_10.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_6.png)

- [ ] OAuth를 이용해서 Resource 서버에 접속하기 위해서는 우선 Resource Server에 등록하는 과정이 필요함

절차
설명

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_9.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_15.png)

- [ ] 등록시 공통적인 필요한 부분
* clientID : 지금 만들고 있는 app의 식별자
* client secret : 그것에 대한 비밀번호 (노출되면 안됨)
* authorized redirect uri : resource 서버가 authorized code를 전달해주는 주소임

- [ ] Oauth의 첫번쨰 절차는 Resource Owner가 resource server에게 client의 접근을 승인한다는 것을 알려줘야 함

설명

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_8.png)

- [ ] 버튼 : 저런 형태의 주소의 링크로 제공하면 됨

* scope : 사용하고자 하는 기능

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_12.png)

예. 로그인 링크

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_1.png)

링크 클릭시 로그인이 안되어 있으면 응답으로
로그인 화면을 응답값으로 보내줌

로그인시 확인하는 값은
* client_id, scope, redirect_uri

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_2.png)

- [ ] scope의 b,c 권한을 줄건지 확인하는 페이지를 보냄

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_5.png)

user id : 1, scope : b,c를 권한을 허용했다는 내용을 DB에 저장함
- [ ] resource sever는 client가 등록된 client가 맞는지 확인하기 위해서 resource owner를 통해서 client에게 authorization code를 전달함

ㅁ. 임시 코드 : authorization code
절차
설명

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_4.png)

header에 location 주소를 담아서 응답으로 보냄
resource owner의 browser에서 client로 redirect되고 client는 authorization code : 3을 알게된다.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_7.png)

여기까지 토큰 발급 전단계까지 상태임

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_11.png)

client가 resource server로 정보를 보냄
* client_secret : 이 포함됨
- [ ] oauth의 핵심인 access token의 값을 발급받는 과정

절차
설명

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_13.png)

인증을 했기 때문에 authorization code를 지움
ㅁ. 다시 인증을 하지 않음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_14.png)

- [ ] API가 무엇인지, access token을 이용해서 api를 호출하는 방법

* Bearer 헤더테 access token을 넣어서 (추천방식)
* access_token params로 전달해서

- [ ] access token은 수명이 있음.
ㅁ. 수명이 다했을 때 새로운 access token을 발급 받는 방법 (refresh token)

절차
설명

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_3.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20OAuth%202.0/image_16.png)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* OAuth 2.0
	* [https://opentutorials.org/module/3668](https://opentutorials.org/module/3668)
	* [https://www.tutorialspoint.com/spring_boot/spring_boot_google_oauth2_sign_in](https://www.tutorialspoint.com/spring_boot/spring_boot_google_oauth2_sign_in)
	* [https://augustines.tistory.com/128](https://augustines.tistory.com/128)
	* [https://www.baeldung.com/spring-security-5-oauth2-login](https://www.baeldung.com/spring-security-5-oauth2-login)
	* [https://www.popit.kr/spring-security-oauth2-%EC%86%8C%EC%85%9C-%EC%9D%B8%EC%A6%9D/](https://www.popit.kr/spring-security-oauth2-%EC%86%8C%EC%85%9C-%EC%9D%B8%EC%A6%9D/)
	* [https://jojoldu.tistory.com/168](https://jojoldu.tistory.com/168)
* Bearer 인증이란
	* [https://gist.github.com/egoing/cac3d6c8481062a7e7de327d3709505f](https://gist.github.com/egoing/cac3d6c8481062a7e7de327d3709505f)