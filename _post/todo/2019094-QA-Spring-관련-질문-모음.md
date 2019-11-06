---
title: 'Q&A : Spring 관련 질문 모음'
date: 2018-7-29 14:54:31
category: 'spring'
tags: ["Q&A", QA", "faq", spring", "java", "스프링"]
---

개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.

스프링관련 어노테이션은 이곳으로 옮겨서 정리를 했습니다.

### <span style="color:orange">[미 답변 질문]</span>

#### - LinkedMultiValueMap
#### - RestClient가 뭔가?
#### - @WebListener
      ㅁ. 이건 스프링 어노테이션은 아니고 servlet 어노테이션이며 클래스엔 선언하면 servlet listener component을 정의해준다
      [https://www.concretepage.com/java-ee/jsp-servlet/weblistener-annotation-example-in-servlet-3-with-servletcontextlistener](https://www.concretepage.com/java-ee/jsp-servlet/weblistener-annotation-example-in-servlet-3-with-servletcontextlistener)
      [https://www.logicbig.com/tutorials/java-ee-tutorial/java-servlet/web-listener-example.html](https://www.logicbig.com/tutorials/java-ee-tutorial/java-servlet/web-listener-example.html)
      [https://nine01223.tistory.com/309](https://nine01223.tistory.com/309)

#### - smart life cycle이란
      ㅁ.

* [http://www.gitshah.com/2014/04/how-to-setup-fixed-shutdown-sequence.html](http://www.gitshah.com/2014/04/how-to-setup-fixed-shutdown-sequence.html)
* [https://javaslave.tistory.com/48](https://javaslave.tistory.com/48)
* [http://wonwoo.ml/index.php/post/1820](http://wonwoo.ml/index.php/post/1820)
* [https://blog.outsider.ne.kr/766](https://blog.outsider.ne.kr/766)

#### - @Repository
      ㅁ. <context:component-scan>에의해서 스프링 빈으로 자동 등록됨
      ㅁ. JPA 전용 예외가 발생하면 스프링이 추상화한 예외로 변환해줌.
      #. 리포지토리 계층에서 JPA 예외인 NoResultException이 발생하면 스프링이 추상화한 예외인 EmptyResultDataAccessException으로 변환해서 서비스 계층에 반환함
      ㅁ. 서비스 계층은 JPA에 의존적인 에외를 처리하지 않아도 됨

#### - 런타입에 인터페이스를 구현할 방법
      ㅁ.

참고

- [https://okky.kr/article/442004](https://okky.kr/article/442004)
- [https://medium.com/@lofidewanto/creating-spring-bean-dynamically-in-the-runtime-d9e32c41d286](https://medium.com/@lofidewanto/creating-spring-bean-dynamically-in-the-runtime-d9e32c41d286)
- [https://stackoverflow.com/questions/15284851/spring-3-dynamic-autowiring-at-runtime-based-on-another-object-attribute](https://stackoverflow.com/questions/15284851/spring-3-dynamic-autowiring-at-runtime-based-on-another-object-attribute)
- [https://stackoverflow.com/questions/40105044/inject-spring-bean-dynamically](https://stackoverflow.com/questions/40105044/inject-spring-bean-dynamically)

* [ ] @SiteSwitchable

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_15.png)

---

### <span style="color:orange">[답변완료]</span>

### <span style="color:brown">1. @RequestMapping에서 consumes와 produces의 차이점?</span>

- consumes
  _ 요청에 매핑할 컨첸츠 타입을 설정한다 (Accept)
  _ 받을 타입을 설정한다
- produces
  _ 응답으로 내려줄 컨텐츠의 타입을 설정한다 (Content-Type을 변경함)
  _ 여러 값을

ㅁ.Accept 와 content-Type 에 대한 접근 허용을 사용하기 위해 header 라는 속성을 사용했다면, 3.1부터는 consumes 와 produces 로 나눠 사용할 수 있다.

- consumes : content-Typed의 접근 허용을 설정함
- produces : accept의 접근 허용을 설정함

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_12.png)

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_9.png)

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_1.png)

참고

- [http://syaku.tistory.com/277](http://syaku.tistory.com/277)
- [http://heenkim.blogspot.com/2013/12/rest_19.html](http://heenkim.blogspot.com/2013/12/rest_19.html)
- [https://hilucky.tistory.com/12](https://hilucky.tistory.com/12)

### <span style="color:brown">2. 컨트롤러 단에서 produces가 있는 것과 없는 것의 차이점은?</span>

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/2F07CE9A-4FE0-4AE0-AE8B-F2BE2530B5F3.png)

있는 경우
없는 경우

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/CF5A62A3-8443-4FCE-86EC-0417D0834C04.png)

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/AB2A9AAC-3851-4952-9982-656FFBCB3F85.png)

#### - @ModelAttribute(“employee”)
      ㅁ. 넘겨온 데이터가 오브젝트 Employee에 매팅된다
      [https://hongku.tistory.com/123](https://hongku.tistory.com/123)
      [http://springmvc.egloos.com/535572](http://springmvc.egloos.com/535572)

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_2.png)

#### - @MessageMapping
#### - @MessageExceptionHandler
#### - @SendToUser(destinations = "\_topic_error", broadcast = false)
#### - @ExceptionHandler
      ㅁ. exception이 발생하면 처리할 메시드를 어노테이션으로 지정할 수 있음

#### - Principle 인자는 뭔가?
      ㅁ. 현재 로그인한 사용자의 정보를 보냄

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_18.png)

#### - exceptioncontroller에 대한 unit test
      [https://stackoverflow.com/questions/14605287/write-junit-test-for-exceptionhandler](https://stackoverflow.com/questions/14605287/write-junit-test-for-exceptionhandler)

::- @CreatedBy::
[https://springbootdev.com/2018/03/13/spring-data-jpa-auditing-with-createdby-createddate-lastmodifiedby-and-lastmodifieddate/](https://springbootdev.com/2018/03/13/spring-data-jpa-auditing-with-createdby-createddate-lastmodifiedby-and-lastmodifieddate/)

#### - @InjectMocks @Mocks의 차이점
      [https://stackoverflow.com/questions/16467685/difference-between-mock-and-injectmocks](https://stackoverflow.com/questions/16467685/difference-between-mock-and-injectmocks)

#### - @ASync
      ㅁ.설정을 필요함

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_8.png)

ㅁ.별로의 쓰레드로 실행됨

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_4.png)

[http://springboot.tistory.com/38](http://springboot.tistory.com/38)

#### - Authorization:Bearer는 뭔가?
      ㅁ. Bearer authentication은 token authentication이라고도 하고 HTTP auth. scheme이다.
      ㅁ. bearer token은 암호된 스트링값으로 로그인 요청시 응답값으로 서버에서 생성된다.
      ㅁ. 클라언트는 제한된 자원에 요청시 Authorization header에 이 값을 토큰 값으로 보내야 한다
      ㅁ. Bearer authen.은 HTTPS 통해서만 사용되어야 함
      [https://swagger.io/docs/specification/authentication/bearer-authentication/](https://swagger.io/docs/specification/authentication/bearer-authentication/)

#### - @Service(“ms)”로 이름을 변경하면 무슨 의미인가?
      ㅁ. getBean을 할때 ms로 클래스를 얻어올 수 있다
      [https://www.journaldev.com/21435/spring-service-annotation](https://www.journaldev.com/21435/spring-service-annotation)

#### - 스프링에서 mix해서 사용하는 방법 - XML와 JavaConfig
      [https://memorynotfound.com/mixing-xml-java-config-spring/](https://memorynotfound.com/mixing-xml-java-config-spring/)

#### - @EnableWebMvc
      ㅁ. Enable Spring MVc specific annotation like @Controller
      ㅁ. <mvc:annotation-driven/> 와 같은 의미
      [http://javaonfly.blogspot.com/2017/01/spring-mvc-java-based.html](http://javaonfly.blogspot.com/2017/01/spring-mvc-java-based.html)

#### - @Scheduled(cron = “0 0 0 \* \* ?”)
      ㅁ. 매일 자정에 한번 실행됨

#### - @RestController
      ㅁ. 스프링4부터 추가됨. REST API 전용으로 작성하는 경우 @Controller 대신사용함
      ㅁ. 이 어노테이션을 사용하면 @ResponseBody 어노테이션을 생략할 수 있음

#### - RestTemplate
      ㅁ. JdbcTemplate처럼 RestTemplate으로 RESTful service에 접근할 수 있음
      [https://vnthf.github.io/blog/Java-RestTemplate%EC%97%90-%EA%B4%80%ED%95%98%EC%97%AC/](https://vnthf.github.io/blog/Java-RestTemplate%EC%97%90-%EA%B4%80%ED%95%98%EC%97%AC/)

#### - @PostConstruct

* DI 컨테이너에 의해 인스턴스 변수에 무언가 인젝션된 다음에 호출된다
* 인젝션된 값으로 초기 처리를 할때 사용함 (다른 방법 : 생성자에서 초기 처리를 하면 됨)

#### - afterPropertiesSet()은 언제 호출되나
      ㅁ. InitializingBean implements해서 afterPropertiesSet()을 구현하면 스프링에서 초기화 시점에 알아서 호출함
      ㅁ. @PonstConsturct이후에 호출됨
      [https://blog.outsider.ne.kr/766](https://blog.outsider.ne.kr/766)
      [http://wonwoo.ml/index.php/post/1820](http://wonwoo.ml/index.php/post/1820)

#### - use-defefault-filters=“false”의 의미는
      ㅁ. 기본 패키지에서 @Conponent, @Service, @Repository와 같은 스트레오애노테이션을 제외하고(use-default-filters="false") @Controller로 표현된 클래스만 빈으로 등록하겠다.는 의미
      ㅁ. media 서버는 왜 잘 동작하고 admin는 잘 동작을 하지 않음 <—

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202019-01-03%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.35.23.png)

[http://atin.tistory.com/556](http://atin.tistory.com/556)
[http://kimddochi.tistory.com/92](http://kimddochi.tistory.com/92)
[https://blog.hanumoka.net/2018/08/07/spring-20180807-spring-bean-scan/](https://blog.hanumoka.net/2018/08/07/spring-20180807-spring-bean-scan/)
[https://docs.spring.io/spring/docs/2.5.x/reference/beans.html](https://docs.spring.io/spring/docs/2.5.x/reference/beans.html)

#### - @EnableWebMvc
      ㅁ. <context:annotation-config> 태그에 해당됨 (스프링4 입문에서 언급됨 - 근데 이게 맞나? - Wrong)
      ㅁ. 이 어노테이션을 JavaConfig에 설정하는 것만으로 어노테이션 베이스이스프링 MVC가 유효가 됨
      ㅁ. <mvc:annotation-driven/>과 동일한 설정

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_6.png)

[http://wonwoo.ml/index.php/post/1590](http://wonwoo.ml/index.php/post/1590)
[https://www.baeldung.com/spring-enable-annotations](https://www.baeldung.com/spring-enable-annotations)

#### - @Value을 사용하려면,
      ㅁ. @PropertySource로 파일 지정하고 PropertySource…를 추가하면 됨

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_13.png)

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_11.png)

#### - @AuthenticationPrincipal 어노테이션은 무엇인가?
      ㅁ. 현재 로그인한 사용자 객체를 인자에 주입할 수 있음

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_10.png)

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_19.png)

[https://itstory.tk/entry/Spring-Security-현재-로그인한-사용자-정보-가져오기](https://itstory.tk/entry/Spring-Security-%ED%98%84%EC%9E%AC-%EB%A1%9C%EA%B7%B8%EC%9D%B8%ED%95%9C-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%A0%95%EB%B3%B4-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0)

#### - javax.validation.ValidationException: HV000183: Unable to initialize 'javax.el.ExpressionFactory'. Check that you have the EL dependencies on the classpath 오류 발생시
      ㅁ. 원인 setup()에서 mock과controller를 넘기니까 아래 오류가 발생함

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_5.png)

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_7.png)

해결 : pom.xml에 el-impl을 추가함

![](Q&A%20%20Spring%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_3.png)

[https://stackoverflow.com/questions/19451814/java-lang-noclassdeffounderror-javax-el-propertynotfoundexception-when-i-send-i/22114584](https://stackoverflow.com/questions/19451814/java-lang-noclassdeffounderror-javax-el-propertynotfoundexception-when-i-send-i/22114584)
