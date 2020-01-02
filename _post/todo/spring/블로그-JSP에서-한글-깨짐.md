# 블로그 : JSP에서 한글 깨짐
* 들어가며
* 개발 환경
* 사용법
* 참고

1. 들어가며

* jsp pageEncoding=“UTF-8"
* server.xml에서 URIEnconding=“UTF-8” 추가

jsp에서 한글 표시
<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="UTF-8" %>

POST, GET으로 한글을 보낼 때의 처리는?
[https://dololak.tistory.com/123](https://dololak.tistory.com/123)

- [ ] Tomcat에서 한글 인코딩 설정
[http://pshcode.tistory.com/57](http://pshcode.tistory.com/57)

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

작성한 예제는 이미 [Amazon SDK](https://docs.aws.amazon.com/ko_kr/sdk-for-java/v1/developer-guide/examples-s3.html) 와 [Baeldung](https://www.baeldung.com/aws-s3-java) 에 있는 예제들입니다. 

4. 참고

* JSP에서 한글 깨짐
	* [http://fruitdev.tistory.com/64](http://fruitdev.tistory.com/64)
	* [http://javaengine.tistory.com/106](http://javaengine.tistory.com/106)
* HTTP 요청과 응답에 대한 인코딩 처리
	* [https://dololak.tistory.com/123](https://dololak.tistory.com/123)
* Intellij에서 Tomcat 한글 깨지는 이슈
	* [http://pshcode.tistory.com/57](http://pshcode.tistory.com/57)
	* [http://shovel-ing.blogspot.com/2013/06/intellij-tomcat.html](http://shovel-ing.blogspot.com/2013/06/intellij-tomcat.html)

#tistory #blog #스터디중