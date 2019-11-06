# 블로그 : Mockito 사용법
* 들어가며

	* Mockito
		* 버전 1 vs 2
			* 버전 2. [https://github.com/mockito/mockito/wiki/What%27s-new-in-Mockito-2](https://github.com/mockito/mockito/wiki/What%27s-new-in-Mockito-2)
	* Powermock과의 차이점
		* private, static
		* 다른 포스팅에서 다루도록 함 (일단 언급)
* 개발 환경
* 사용법
	* 어노테이션 없이 vs. 어노테이션 차이점
	* 어노테이션 정리
		* @Mock, @Spy, @Captor, @InjectMocks
	* mock
		* return
		* void
	* spy
		* return
		* void
	* verify
	* throw
	* captor
	* abstract에 대한 spying or mocking
		* [블로그 : 추상 클래스에 대한 mock 테스트](evernote:///view/838797/s7/adf1e23e-7184-46da-8b13-b879de7a9081/adf1e23e-7184-46da-8b13-b879de7a9081/)
	* MockitoRule
	* argument matchers란?
		* custom으로 생성하는 방법?
* 참고

**코멘트**
- [ ] @Mock
- [ ] @InjectMocks
ㅁ. @Mock이나 @Spy로 되어 있는 객체를 자신의 맴버 클래스와 일치하면 주입시킴

- [ ] @RunWith 없어도 잘 돌아가던데, 왜 그런가?
ㅁ.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Mockito%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_8.png)

- [ ] @PowerMockRunnerDelegate
ㅁ.

- [ ] deep level인 autowired 속성을 mocking하는 방법
ㅁ. 아직 해결책 못찾음
[https://stackoverflow.com/questions/37440940/mockito-inject-nested-bean](https://stackoverflow.com/questions/37440940/mockito-inject-nested-bean)
[https://stackoverflow.com/questions/19812651/mockito-creating-nested-mock-objects](https://stackoverflow.com/questions/19812651/mockito-creating-nested-mock-objects)
[https://www.petrikainulainen.net/programming/testing/writing-clean-tests-it-starts-from-the-configuration/](https://www.petrikainulainen.net/programming/testing/writing-clean-tests-it-starts-from-the-configuration/)
[https://stackoverflow.com/questions/24819683/replace-deep-level-autowired-dependencies-with-mockings-in-spring](https://stackoverflow.com/questions/24819683/replace-deep-level-autowired-dependencies-with-mockings-in-spring)
[https://www.reddit.com/r/java/comments/2uq7hk/how_to_mock_out_a_deeply_nested_class_in_spring/](https://www.reddit.com/r/java/comments/2uq7hk/how_to_mock_out_a_deeply_nested_class_in_spring/)

- [ ] mockito에서 consecutive한 answer을 list로 제공하려면
ㅁ.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Mockito%20%EC%82%AC%EC%9A%A9%EB%B2%95/7D2DEA29-11F2-417A-AFA5-F16A332A7E28.png)

[https://stackoverflow.com/questions/9911397/mocking-generic-number-of-consecutive-responses-from-partial-mock-with-mockito](https://stackoverflow.com/questions/9911397/mocking-generic-number-of-consecutive-responses-from-partial-mock-with-mockito)

- [ ] 객체의 필드 값을 verify하기 위해서는 argumentcaptor를 사용하면 됨
[https://stackoverflow.com/questions/1142837/verify-object-attribute-value-with-mockito](https://stackoverflow.com/questions/1142837/verify-object-attribute-value-with-mockito)

- [ ] Spring에서 @Value 값 인젝션하는 방법
[https://stackoverflow.com/questions/9209952/spring-value-injection-in-mockito](https://stackoverflow.com/questions/9209952/spring-value-injection-in-mockito)

- [ ] @Spy와 @mock의 차이점
ㅁ. @Spy는 real 객체를 생성함
ㅁ. @Mock 어노테이션은 목 인스턴스를 생성하고 인젝션해주는 어노테이션이고 실제 객체를 생성하지 않고 mockito가 해당 클래스를 위한 목개체를 생성하도록 한다

[https://howtodoinjava.com/mockito/mockito-annotations/](https://howtodoinjava.com/mockito/mockito-annotations/)
[https://jojoldu.tistory.com/239](https://jojoldu.tistory.com/239)

- [ ] powermock도 같이 사용하고 싶다면, @Rule을 사용하면 됨
ㅁ. 생각처럼 잘 안됨. pom.xml에 추가된 mockito와 powermock 버전 호환이 중요한 것으로 판단됨
[https://blog.jayway.com/2011/05/19/powermock-for-integration-testing/](https://blog.jayway.com/2011/05/19/powermock-for-integration-testing/)

- [ ] LinkageError 처리
ava.lang.LinkageError: loader constraint violation: loader (instance of org_powermock_core_classloader_MockClassLoader) previously initiated loading for a different type with name "javax_management_MBeanServ
ㅁ. 해결 : @PowerMockIgnore("javax.management.*")
[https://stackoverflow.com/questions/16520699/mockito-powermock-linkageerror-while-mocking-system-class](https://stackoverflow.com/questions/16520699/mockito-powermock-linkageerror-while-mocking-system-class)

- [ ] mockito로는 primitive type은 assign할 수 없음
ㅁ. Reflection을 사용하면 됨
ReflectionTestUtils.setField(mediaLiveComponent, "phase", "local”);

- [ ] 스프링 controller단과 mockito를 같이 사용하고 verify하는 과정에서 UnfinishedVerificationException이 발생함
ㅁ. 해결책은 못찾음
[https://stackoverflow.com/questions/15904584/mockito-gives-unfinishedverificationexception-when-it-seems-ok](https://stackoverflow.com/questions/15904584/mockito-gives-unfinishedverificationexception-when-it-seems-ok)

- [ ] controller단 테스트에서 mock하는 방법
ㅁ. 해결되지만, 다른 test에서 영향을 받아서 null로 인식됨
ㅁ. test-config.xml & application-bean.xml에 같은 속성 설정이 있어서 어떤 것이 로드되는지 잘 이해가 안됨. (같은 값이 있는 경우)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Mockito%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_7.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Mockito%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_1.png)

[https://stackoverflow.com/questions/19299513/spring-junit-how-to-mock-autowired-component-in-autowired-component](https://stackoverflow.com/questions/19299513/spring-junit-how-to-mock-autowired-component-in-autowired-component)

ㅁ.원인 : 스프링은 테스트 실행시 application context을 기본적으로 캐싱함
[https://stackoverflow.com/questions/25360963/spring-should-i-use-dirtiescontext-on-every-class](https://stackoverflow.com/questions/25360963/spring-should-i-use-dirtiescontext-on-every-class)

[https://stackoverflow.com/questions/35766927/how-recreate-only-selected-spring-context-in-spring-tests?rq=1](https://stackoverflow.com/questions/35766927/how-recreate-only-selected-spring-context-in-spring-tests?rq=1)
[https://stackoverflow.com/questions/21239875/does-spring-dirtiescontext-reload-spring-context](https://stackoverflow.com/questions/21239875/does-spring-dirtiescontext-reload-spring-context)

[https://stackoverflow.com/questions/18696375/spring-test-mock-one-dependency](https://stackoverflow.com/questions/18696375/spring-test-mock-one-dependency)

1. 들어가며

Mockito history

PowerMock은 Mockito가 지원하지 않는 케이스들(ex. private method, static method)

* private method
* static method

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

maven 의존성

mockito annotations

3. 사용법

그냥 plain으로 mock, spy까지 하고나서
annotation 방식으로 하면….

@Mock을 사용하면 Mockito.mock을 수동으로 할 필요는 없음.

@Mock 사용하지 않을 경우
@Mock 사용하는 경우

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Mockito%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_4.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Mockito%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_6.png)

- [ ] initMocks(this)를 하면, @Mock으로 선언된 객체를 만들어냄.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Mockito%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_5.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Mockito%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_2.png)

@InjectMocks이란
ㅁ. 클래스 A에 다른 클래스 B를 포함하는 경우, B의 클래스에 대해서 mock을 할 수 있는 방법이 없나?
ㅁ. @InjectMocks 어노테이션은 @Mock이나 @Spy 어노테이션으로 선언된 목 객체를 자신의 맴버 클래스와 일치하면 주입시켜주는 어노테이션이다.
#. 어노테이션을 사용하지 않고 직접 코드로 하려면 어떻게 해야 하나?

- [ ] @Spy
ㅁ. @Mock은 완전 dummy 객체를 만든다면, @Spy은 실제 메서드를 호출할 수 있음.

- [ ] ArgumentCaptor
ㅁ. argument matcher와 비슷한 기능을 제공하고 argument matcher와 다르게 별도의 클래스를 만들 필요가 없음? (anwer처럼?)
ㅁ. verification에만 사용가능함

- [ ] Whitebox.invokeMethod(systemUnderTest, "privateMethodUnderTest")
ㅁ. powermock에서 private한 메서드를 실행할 수 있음

4. 참고

* Mockito Documentation
	* 버전 1
		* [http://static.javadoc.io/org.mockito/mockito-core/1.10.19/org/mockito/Mockito.html](http://static.javadoc.io/org.mockito/mockito-core/1.10.19/org/mockito/Mockito.html)
	* 버전 2
		* [http://static.javadoc.io/org.mockito/mockito-core/2.24.0/org/mockito/Mockito.html](http://static.javadoc.io/org.mockito/mockito-core/2.24.0/org/mockito/Mockito.html)
* Mockito
	* [https://www.vogella.com/tutorials/Mockito/article.html](https://www.vogella.com/tutorials/Mockito/article.html)
	* [https://www.baeldung.com/mockito-series](https://www.baeldung.com/mockito-series)
	* [https://semaphoreci.com/community/tutorials/stubbing-and-mocking-with-mockito-2-and-junit](https://semaphoreci.com/community/tutorials/stubbing-and-mocking-with-mockito-2-and-junit)
	* [https://riptutorial.com/mockito/topic/2055/getting-started-with-mockito](https://riptutorial.com/mockito/topic/2055/getting-started-with-mockito)
	* [https://www.thecuriousdev.org/improve-junit-tests-mockito-powermock/](https://www.thecuriousdev.org/improve-junit-tests-mockito-powermock/)
	* [https://github.com/in28minutes/MockitoTutorialForBeginners](https://github.com/in28minutes/MockitoTutorialForBeginners)
	* [https://bestalign.github.io/2016/07/10/intro-mockito-2/](https://bestalign.github.io/2016/07/10/intro-mockito-2/)
	* [https://www.baeldung.com/mockito-annotations](https://www.baeldung.com/mockito-annotations)
	* [https://jdm.kr/blog/222](https://jdm.kr/blog/222)
	* [http://wonwoo.ml/index.php/post/1453](http://wonwoo.ml/index.php/post/1453)
	* [http://www.springboottutorial.com/spring-boot-unit-testing-and-mocking-with-mockito-and-junit](http://www.springboottutorial.com/spring-boot-unit-testing-and-mocking-with-mockito-and-junit)
	* [http://thswave.github.io/java/2015/03/02/spring-mvc-test.html](http://thswave.github.io/java/2015/03/02/spring-mvc-test.html)
	* [https://bestalign.github.io/2016/07/08/intro-mockito-1/](https://bestalign.github.io/2016/07/08/intro-mockito-1/)
	* [https://www.baeldung.com/mockito-verify](https://www.baeldung.com/mockito-verify)
	* [https://github.com/mockito/mockito/wiki/Mockito-features-in-Korean](https://github.com/mockito/mockito/wiki/Mockito-features-in-Korean)
	* [https://www.baeldung.com/mockito-void-methods](https://www.baeldung.com/mockito-void-methods)
	* [https://dzone.com/articles/mockito-mock-vs-spy-in-spring-boot-tests](https://dzone.com/articles/mockito-mock-vs-spy-in-spring-boot-tests)
	* [https://www.baeldung.com/java-spring-mockito-mock-mockbean](https://www.baeldung.com/java-spring-mockito-mock-mockbean)
	* [https://stackoverflow.com/questions/10906945/mockito-junit-and-spring](https://stackoverflow.com/questions/10906945/mockito-junit-and-spring)
	* [https://www.luckyryan.com/2013/08/24/unit-test-controllers-spring-mvc-test/](https://www.luckyryan.com/2013/08/24/unit-test-controllers-spring-mvc-test/)
	* [https://stackoverflow.com/questions/38258950/is-there-a-way-to-verify-that-a-method-on-spring-controller-was-called-using-moc](https://stackoverflow.com/questions/38258950/is-there-a-way-to-verify-that-a-method-on-spring-controller-was-called-using-moc)
	* [https://blog.parasoft.com/love-spring-testing-even-more-with-mocking-and-unit-test-assistant](https://blog.parasoft.com/love-spring-testing-even-more-with-mocking-and-unit-test-assistant)
	* [https://www.baeldung.com/mockito-2-lazy-verification](https://www.baeldung.com/mockito-2-lazy-verification)
	* [https://samerabdelkafi.wordpress.com/2013/07/01/junit-test-with-mockito-and-spring/](https://samerabdelkafi.wordpress.com/2013/07/01/junit-test-with-mockito-and-spring/)
	* [https://javacodehouse.com/blog/mockito-tutorial/](https://javacodehouse.com/blog/mockito-tutorial/)
	* [https://www.baeldung.com/mockito-argument-matchers](https://www.baeldung.com/mockito-argument-matchers)
	* [https://www.toptal.com/java/a-guide-to-everyday-mockito](https://www.toptal.com/java/a-guide-to-everyday-mockito)
* Mockito Tutorial
	* [https://www.vogella.com/tutorials/Mockito/article.html](https://www.vogella.com/tutorials/Mockito/article.html)
* Setter 없이 필드값을 세팅하는 방법
	* [https://stackoverflow.com/questions/28758883/best-practice-setting-a-field-without-setters-in-a-unit-test](https://stackoverflow.com/questions/28758883/best-practice-setting-a-field-without-setters-in-a-unit-test)
* Abstract 클래스 관련 Unit Test
	* [https://www.baeldung.com/junit-test-abstract-class](https://www.baeldung.com/junit-test-abstract-class)
	* [https://gualtierotesta.wordpress.com/2015/01/28/tutorial-java-abstract-classes-testing/](https://gualtierotesta.wordpress.com/2015/01/28/tutorial-java-abstract-classes-testing/)
	* [https://blogs.agilefaqs.com/2013/12/05/mocking-only-abstract-methods-using-mockito-partial-mocking/](https://blogs.agilefaqs.com/2013/12/05/mocking-only-abstract-methods-using-mockito-partial-mocking/)
* Spring with Mockito
	* [https://samerabdelkafi.wordpress.com/2013/07/01/junit-test-with-mockito-and-spring/](https://samerabdelkafi.wordpress.com/2013/07/01/junit-test-with-mockito-and-spring/)
* Spy vs. Mock
	* [https://myshittycode.com/2014/03/13/mockito-effective-partial-mocking/](https://myshittycode.com/2014/03/13/mockito-effective-partial-mocking/)
* Powermock
	* [https://blog.codecentric.de/en/2016/03/junit-testing-using-mockito-powermock/](https://blog.codecentric.de/en/2016/03/junit-testing-using-mockito-powermock/)

#unit test# #blog #tistory #스터디중