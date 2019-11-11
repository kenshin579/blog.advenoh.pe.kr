# 블로그 : @ModelAttribute
* 들어가며
* 개발 환경
* 사용법
* 참고

코멘트
- [ ] @ModelAttribute를 메서드 레벨에 적용하면 어떻게 되나?
ㅁ. request가 들어오면 @ModelAttribute로 선언된 메서드가 먼저 실행됨
ㅁ. 스프링이 handler 메서드를 실행하기전에 Model 객체에 각 메서드의 반환값을 저장함

-- 매핑되는 클래스안에 다른 클래스가 있는 경우에 어떻게 할 수 있나?-
ㅁ. thumbnail.width 이런 식으로 보내면 매핑이 됨

1. 들어가며

1. 계정 생성하기
2. key로 접근할 수 있음

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

작성한 예제는 이미 [Amazon SDK](https://docs.aws.amazon.com/ko_kr/sdk-for-java/v1/developer-guide/examples-s3.html) 와 [Baeldung](https://www.baeldung.com/aws-s3-java) 에 있는 예제들입니다. 

3.1 Client Connection

1. 코드에서

4. 참고

* @ModelAttribute
	* [https://www.logicbig.com/tutorials/spring-framework/spring-web-mvc/spring-model-attribute-method.html](https://www.logicbig.com/tutorials/spring-framework/spring-web-mvc/spring-model-attribute-method.html)
	* [https://www.boraji.com/spring-4-mvc-modelattribute-annotation-example](https://www.boraji.com/spring-4-mvc-modelattribute-annotation-example)
	* [https://examples.javacodegeeks.com/enterprise-java/spring/spring-modelattribute-annotation-example/](https://examples.javacodegeeks.com/enterprise-java/spring/spring-modelattribute-annotation-example/)

#tistory #blog #스터디중