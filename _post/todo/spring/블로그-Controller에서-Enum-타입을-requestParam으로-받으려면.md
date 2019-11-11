# 블로그 : Controller에서 Enum 타입을 requestParam으로 받으려면
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] controller에서 Enum 타입으로 바로 저장하려면 converter 설정을 해야 한다.
ㅁ. converter를 설정하지 않아도 그냥 매핑이 되지만, /LIVE_ID3/1234 <— 이런식으로 사용해야 하는데, REST API에서는 underscore을 사용하지 않음. 그래서 converter가 필요함
ㅁ.[https://stackoverflow.com/questions/4617099/spring-3-0-mvc-binding-enums-case-sensitive](https://stackoverflow.com/questions/4617099/spring-3-0-mvc-binding-enums-case-sensitive)
ㅁ. [https://www.devglan.com/spring-boot/enums-as-request-parameters-in-spring-boot-rest](https://www.devglan.com/spring-boot/enums-as-request-parameters-in-spring-boot-rest)
[https://kunner.com/entry/toby%EC%9D%98%EC%8A%A4%ED%94%84%EB%A7%81-13%EC%9E%A5-%EC%8A%A4%ED%94%84%EB%A7%81-MVC-2](https://kunner.com/entry/toby%EC%9D%98%EC%8A%A4%ED%94%84%EB%A7%81-13%EC%9E%A5-%EC%8A%A4%ED%94%84%EB%A7%81-MVC-2)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Controller%EC%97%90%EC%84%9C%20Enum%20%ED%83%80%EC%9E%85%EC%9D%84%20requestParam%EC%9C%BC%EB%A1%9C%20%EB%B0%9B%EC%9C%BC%EB%A0%A4%EB%A9%B4/image_1.png)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

	* [http://wonwoo.ml/index.php/post/896](http://wonwoo.ml/index.php/post/896)