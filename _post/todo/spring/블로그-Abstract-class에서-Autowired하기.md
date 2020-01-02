# 블로그 : Abstract class에서 @Autowired하기
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] abstract class에서 @autowired를 사용하면 문제가 있나?
ㅁ.왜 이런 식으로 getBean을 하는 걸까? @Autowired을 사용하면 안되는 이유가 있나?
ㅁ. admin에서는 MediaRepository 클래스가 부모 & 자식 중복으로 있음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Abstract%20class%EC%97%90%EC%84%9C%20@Autowired%ED%95%98%EA%B8%B0/image_1.png)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* Amazon S3
	* [http://blog.maaloe.com/2008/11/spring-autowired-doesnt-work-in.html](http://blog.maaloe.com/2008/11/spring-autowired-doesnt-work-in.html)