# 블로그 : JWT란
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] JWT란?
* Json Web Token
* JSON 형태로 인증토큰을 만들어 통신할때쓰는 인증방식
* 해더에 Authroization 값을 넣어서 Authorization Server로 보내서 인증을 함

- [ ] 왜 사용하나?
* CORS(Cross-origin resource sharing)문제때문에 주로 씀
* 쿠키는 발행한 서버에서만 유효함
	* site a에서 발행한 쿠니는 site b에서 사용할 수 없음
* 토큰은 HTML Body 형태로 전송하기 때문에 다른 도메인에서 API를 호출해야 하는 서비스 구성에 유요함

- [ ] 해더에 JSON을 넣는 거 많이 불편하여 JSON을 base64로 인코딩하여 하나의 문자열로 변환한 다음 JWS(Json Web Signature)를 사용하여 디지털 서명함
ㅁ. JSON은 \n 등의 문자가 있기 때문에 REST API 호출시 HTTP 헤더등에 넣기가 매우 불편함

JWT는 마침표(.) 기준으로 3개로 나눠서 인코딩하고 3개를 조합해서 토큰을 만듬
* JSOE 헤더(JSON Object Signing and Encryption) - 사진의 Header
	* 이 해더는 어떤 식으로 JWT를 해석해야 하는지 명시함
* JWT Claim Set - 사진의 Payload
	* 실제로 데이터가 들어가는 부분

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JWT%EB%9E%80/image_3.png)

* Signature - 사진의 Verify Signature
	* 이 부분이 없으면 누구나 다시 JSOE & Claim Set을 디코딩할 수 있음
	* 해더에서 지정한 알고리즘으로 인코딩하여 signature를 생성함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JWT%EB%9E%80/image_1.png)

- [ ] OAuth와의 차이점
* OAuth
	* OAuth에서 발급한 access_token은 random 스트링으로 토큰 자체에는 특별한 정보를 가지고 있지 않음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JWT%EB%9E%80/image_2.png)

		* Resource Server API에 호출할 때 권리자 권한을 가지고 있어야 함
		* 추가로 DB에서 사용자가 속한 회사 정보를 찾아와야 함
* JWT
	* JWT은 Claim 기반으로 Claim은 사용자에 대한 속성을 의미함
	* 토큰 자체에 정보를 가지고 있음
	* 장점 : 토큰자체에 사용자에 대한 추가 정보를 가지고 있어서 다른 곳(DB)에서 가져올 필요가 없음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JWT%EB%9E%80/image_4.png)

		* 토큰을 생성하는 단계에서는 생성된 토큰을 별도의 서버에서 유지할 필요가 없음
		* Resource 서버에서 사용자 정보를 별도로 계정 시스템에서 조회할 필요가 없음

- [ ] 토큰에 대한 변조 방지는 어떻게 할 수 있나?
ㅁ. 무결성(integrity) : 메시지가 변조되어 않았음을 증명하는 것
ㅁ. 보장하는 방법
* 서명 (signature)

* HMAC 방식
	* 원본 메시지에서 해쉬값을 추출한 후, 이를 비밀키를 이용해서 복호화 시켜서 토큰의 뒤에 붙임

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JWT%EB%9E%80/image_5.png)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* JWT
	* [https://gist.github.com/LeoHeo/c9678154b1dadd85add5862b30e969f8](https://gist.github.com/LeoHeo/c9678154b1dadd85add5862b30e969f8)
	* [https://bcho.tistory.com/999](https://bcho.tistory.com/999)
	* [https://swalloow.github.io/implement-jwt](https://swalloow.github.io/implement-jwt)
* HMAC
	* [https://bcho.tistory.com/807](https://bcho.tistory.com/807)