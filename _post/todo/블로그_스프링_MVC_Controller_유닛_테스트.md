# 블로그 : 스프링 MVC Controller 유닛 테스트
* 소개
* 참고

**코멘트**
- [ ] mockMvc는 어떤 역할을 하나?
- [ ] andExpect() 메서드
- [ ] @Mock
- [ ] @InjectMock
- [ ] 아래는 별도의 주제로 다루는게 좋을 듯하다
* MVC Controller
* Exception
* Transactional
* Batch
- [ ] multipartfile 관련 테스트 하는 방법
[http://blog.saltfactory.net/submit-multipart-form-data-and-test-in-spring/](http://blog.saltfactory.net/submit-multipart-form-data-and-test-in-spring/)

- [ ] 현재 프로젝트에서 우리가 사용하는 테스트관련 라이브러리는?
ㅁ. 추가된 라이브러리는 무슨 역할을 하나?

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20MVC%20Controller%20%EC%9C%A0%EB%8B%9B%20%ED%85%8C%EC%8A%A4%ED%8A%B8/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202019-01-02%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2010.24.30.png)

1. 들어가며

* Controller에 대핱 테스트
	* ExceptionHandler에 대한 테스트
		* [블로그 : 스프링 컨트롤러 예외처리](evernote:///view/838797/s7/957b0cdf-c834-4adc-98a7-6f8dafeb2916/957b0cdf-c834-4adc-98a7-6f8dafeb2916/)
* Dao에 대한 테스트

2. 개발 환경 및 기본 설정

* OS : Mac OS
* IDE: Intellij
* Java : JDK 8
* Source code : github
* Dependency Management Tool : Maven

스프링 유닛 테스트를 위해 필요한 메이븐 Maven dependency

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20MVC%20Controller%20%EC%9C%A0%EB%8B%9B%20%ED%85%8C%EC%8A%A4%ED%8A%B8/image_4.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20MVC%20Controller%20%EC%9C%A0%EB%8B%9B%20%ED%85%8C%EC%8A%A4%ED%8A%B8/image_2.png)

**3. 스프링 MVC 유닛 테스트 설정**

3.1 유닛테스트 하려면 설정

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20MVC%20Controller%20%EC%9C%A0%EB%8B%9B%20%ED%85%8C%EC%8A%A4%ED%8A%B8/image_3.png)

- [ ] @RunWith(…)

@ContextConfiguration
- [ ] class로 xml로

@WebAppConfiguration(value=“”) <— ??

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20MVC%20Controller%20%EC%9C%A0%EB%8B%9B%20%ED%85%8C%EC%8A%A4%ED%8A%B8/image_1.png)

- [ ] 목

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20MVC%20Controller%20%EC%9C%A0%EB%8B%9B%20%ED%85%8C%EC%8A%A4%ED%8A%B8/image_5.png)

4. 참고

* 스프링 유닛 테스트
	* [https://www.baeldung.com/integration-testing-in-spring](https://www.baeldung.com/integration-testing-in-spring)
	* [http://effectivesquid.tistory.com/entry/Spring-test-와-Junit4를-이용한-테스트](http://effectivesquid.tistory.com/entry/Spring-test-%EC%99%80-Junit4%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%85%8C%EC%8A%A4%ED%8A%B8)
	* [https://zorba91.tistory.com/entry/JUnit에서-Controller-테스트-코드-작성하기정리](https://zorba91.tistory.com/entry/JUnit%EC%97%90%EC%84%9C-Controller-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%BD%94%EB%93%9C-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0%EC%A0%95%EB%A6%AC)
	* [http://thswave.github.io/java/2015/03/02/spring-mvc-test.html](http://thswave.github.io/java/2015/03/02/spring-mvc-test.html)
	* [https://www.codeproject.com/Articles/1237643/%2FArticles%2F1237643%2FA-Note-on-Unit-Test-Spring-MVC-Applications](https://www.codeproject.com/Articles/1237643/%2FArticles%2F1237643%2FA-Note-on-Unit-Test-Spring-MVC-Applications)
	* [http://blog.marcnuri.com/mockmvc-spring-mvc-framework/](http://blog.marcnuri.com/mockmvc-spring-mvc-framework/)
* jsonPath
	* [https://stackoverflow.com/questions/13745332/count-members-with-jsonpath](https://stackoverflow.com/questions/13745332/count-members-with-jsonpath)
	* [https://github.com/pkainulainen/spring-mvc-test-examples/blob/master/rest-unittest/src/integration-test/java/net/petrikainulainen/spring/testmvc/todo/controller/ITTodoControllerTest.java](https://github.com/pkainulainen/spring-mvc-test-examples/blob/master/rest-unittest/src/integration-test/java/net/petrikainulainen/spring/testmvc/todo/controller/ITTodoControllerTest.java)

[http://blog.woniper.net/272](http://blog.woniper.net/272)
[http://effectivesquid.tistory.com/entry/Spring-test-%EC%99%80-Junit4%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%85%8C%EC%8A%A4%ED%8A%B8](http://effectivesquid.tistory.com/entry/Spring-test-%EC%99%80-Junit4%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%85%8C%EC%8A%A4%ED%8A%B8)
[https://blog.hanumoka.net/2018/04/29/spring-20180429-spring-mvc-junit-test/](https://blog.hanumoka.net/2018/04/29/spring-20180429-spring-mvc-junit-test/)
[http://effectivesquid.tistory.com/entry/Spring-test-%EC%99%80-Junit4%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%85%8C%EC%8A%A4%ED%8A%B8](http://effectivesquid.tistory.com/entry/Spring-test-%EC%99%80-Junit4%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%85%8C%EC%8A%A4%ED%8A%B8)
[http://thswave.github.io/java/2015/03/02/spring-mvc-test.html](http://thswave.github.io/java/2015/03/02/spring-mvc-test.html)
[https://www.codeproject.com/Articles/1237643/%2FArticles%2F1237643%2FA-Note-on-Unit-Test-Spring-MVC-Applications](https://www.codeproject.com/Articles/1237643/%2FArticles%2F1237643%2FA-Note-on-Unit-Test-Spring-MVC-Applications)
[http://blog.marcnuri.com/mockmvc-spring-mvc-framework/](http://blog.marcnuri.com/mockmvc-spring-mvc-framework/)

#unit test# #blog #tistory #스터디중