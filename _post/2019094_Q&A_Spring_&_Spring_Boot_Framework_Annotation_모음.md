# Q&A : Spring & Spring Boot Framework Annotation 모음
Spring & Spring Boot Framework Annotations

스프링과 스프링 부트에서 사용하는 어노테이션이 생각보다 많이 있습니다. 어노테이션 중에서도 같이 사용할 수 있는게 있고 스프링 부트에서만 사용해야 하는 어노테이션이 있어서 사용할 때마다 많이 헷갈릴 때가 종종 있습니다.

[스프링 프레임워크 구루 사이트](https://springframework.guru/spring-framework-annotations/%0A) 에서 잘 정리된 아이디어를 얻어서 제 나름대로 구분하기 쉽게 어노테이션 별로 정리를 해보았습니다. 

[Q&A 전체 목록](https://advenoh.tistory.com/35)

[Q&A : Spring Boot Annotation 모음](evernote:///view/838797/s7/5a43bbbc-52f5-43b5-860b-2d5cb70740cd/5a43bbbc-52f5-43b5-860b-2d5cb70740cd/)
[Q&A : Spring JPA Annotation](evernote:///view/838797/s7/b0547113-7fa4-4383-8c82-25553305fd32/b0547113-7fa4-4383-8c82-25553305fd32/)

[미 답변 질문]

- [ ] Cacheable 어노테이션에서 아래와 같은 경우 key는 어떻게 세팅되나?
ㅁ.

![](Q&A%20%20Spring%20&%20Spring%20Boot%20Framework%20Annotation%20%EB%AA%A8%EC%9D%8C/image_9.png)

- [ ] @EnableWebMvc
ㅁ. 있는 경우와 없는 경우의 차이점

- [ ] @ComponentScan
- [ ] @RestController와 차이점..
- [ ] @MaskFormat
- [ ] @RestControllerAdvice
- [ ] @InitBinder
ㅁ.
[https://www.concretepage.com/spring/spring-mvc/spring-mvc-validator-with-initbinder-webdatabinder-registercustomeditor-example](https://www.concretepage.com/spring/spring-mvc/spring-mvc-validator-with-initbinder-webdatabinder-registercustomeditor-example)

- [ ] @MediaFormValidate
ㅁ. MediaForm alidateAspect는 무슨 역할을 하나?
- [ ] @CrossOrigin
- [ ] @Qualifer는 언제 사용하나?
- [ ] @JpaReadWrite
- [ ] @RepositoryRestController
- [ ] @ControllerAdvice
- [ ] @Order(1)
- [ ] @Cacheable은 어느 메모리에 저장되나?
- [ ] @EnableTransactionManagement
ㅁ. 어노테이션으로 트랜잭션 매니저를 지정해줄 수 있으며, 자바 기반 설정의 경우, PlatformTransactionManager를 구현한 인스턴스(ex. DataSourceTransactionManager)를 찾아 지정함
[https://dayone.me/1SlXzM0](https://dayone.me/1SlXzM0)
[https://cnpnote.tistory.com/entry/SPRING-2-%EA%B0%9C%EC%9D%98-%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98-%EA%B4%80%EB%A6%AC%EC%9E%90%EB%A1%9C-EnableTransactionManagement-%EC%A3%BC%EC%84%9D](https://cnpnote.tistory.com/entry/SPRING-2-%EA%B0%9C%EC%9D%98-%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98-%EA%B4%80%EB%A6%AC%EC%9E%90%EB%A1%9C-EnableTransactionManagement-%EC%A3%BC%EC%84%9D)

![](Q&A%20%20Spring%20&%20Spring%20Boot%20Framework%20Annotation%20%EB%AA%A8%EC%9D%8C/image_1.png)

![](Q&A%20%20Spring%20&%20Spring%20Boot%20Framework%20Annotation%20%EB%AA%A8%EC%9D%8C/image_2.png)

[블로그 : Spring / Spring Boot Annotation 모음](evernote:///view/838797/s7/eca3f1cc-480d-4979-aaad-2ea91014e894/eca3f1cc-480d-4979-aaad-2ea91014e894/)

- - - -

[답변완료]

Spring Core

쉽게 찾기 위해서 알파벳 순으로 정리합니다.

@Autowired

쉽게 찾기 위해서 알파벳 순으로 정리합니다.

설정 위치 : 생성자, 필드, 메서드의 세곳에 적용가능함

@Bean

쉽게 찾기 위해서 알파벳 순으로 정리합니다.

Spring Security

쉽게 찾기 위해서 알파벳 순으로 정리합니다.

@EnableWebSecurity

이 어노테이션은 스프링 보완 어노테이션으로 프로젝트에서 웹 보안을 활성화 시켜줍니다. 어노테이션 자체로를 유효하지 않고 WebSecurityConfigurer를 구현하거나 WebSebSecurityConfigurerAdapter를 확장한 빈으로 설정되어 있으면 됩니다.

참고
* [https://blog.naver.com/kimnx9006/220633299198](https://blog.naver.com/kimnx9006/220633299198)

@EnableGlobalMethodSecurity

이 어노테이션은 메서드 레벨에 보안정책을 적용시켜주는 어노테이션입니다. 3가지 타입이 있습니다.

* securedEnabled : 메서드단에서 사용하는 @Secured 어노테이션을 활성화 시킨다

![](Q&A%20%20Spring%20&%20Spring%20Boot%20Framework%20Annotation%20%EB%AA%A8%EC%9D%8C/image_6.png)

* jsr250Enabled : @RolesAllowed 어노테이션의 사용을 활성화 시킨다.

![](Q&A%20%20Spring%20&%20Spring%20Boot%20Framework%20Annotation%20%EB%AA%A8%EC%9D%8C/image_7.png)

* prePostEnabled : @PreAuthorize와 @PostAuthorize 어노테이션을 활성화 시킨다.

![](Q&A%20%20Spring%20&%20Spring%20Boot%20Framework%20Annotation%20%EB%AA%A8%EC%9D%8C/image_5.png)

![](Q&A%20%20Spring%20&%20Spring%20Boot%20Framework%20Annotation%20%EB%AA%A8%EC%9D%8C/image_4.png)

참고

* [https://www.callicoder.com/spring-boot-spring-security-jwt-mysql-react-app-part-2/](https://www.callicoder.com/spring-boot-spring-security-jwt-mysql-react-app-part-2/)

@AuthenticationPrincipal

이 어노테이션으로 컨트롤러에서 현재 인증된 사용자 정보를 가져올 수 있습니다.

![](Q&A%20%20Spring%20&%20Spring%20Boot%20Framework%20Annotation%20%EB%AA%A8%EC%9D%8C/image_3.png)

참고
* [https://itstory.tk/entry/Spring-Security-현재-로그인한-사용자-정보-가져오기](https://itstory.tk/entry/Spring-Security-%ED%98%84%EC%9E%AC-%EB%A1%9C%EA%B7%B8%EC%9D%B8%ED%95%9C-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%A0%95%EB%B3%B4-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0)

@PreAuthorize

이 어노테이션은 요청이 들어와 함수를 실행하기 전에 권한을 검사합니다.

* hasRole([role]) : 현재 사용자의 권한이 파라미터의 권한과 동일한 경우에 true를 반환한다

![](Q&A%20%20Spring%20&%20Spring%20Boot%20Framework%20Annotation%20%EB%AA%A8%EC%9D%8C/image_8.png)

참고
* [https://steemit.com/kr-dev/@igna84/spring-security-preauthorize-postauthorize](https://steemit.com/kr-dev/@igna84/spring-security-preauthorize-postauthorize)

#q&a #annotation #Spring #java