# 블로그 : 스프링 DI 설정 방법
* 들어가며
	* 의존이란? 왜 필요한가? 장점
	* DI를 통한 의존처리
* 스프링의 DI 설정방법 - 3가지
	* Setter, Constructor, Field 방식의 인젝션

	* 어노테이션 이용한 DI (@Component, @Autowired) + 정의 파일 (scan 방식) - 컴포넌트 스캔 방식
	* Bean 정의 파일을 이요한 DI (annotation을 이곳에 설정함)
	* JavaConfig 이용한 DI (@Configuration, @Bean) <— 이거 이해 잘 안됨

	* 의존 자동 주입?
		* @Autowired, @Qualifier
* 빈 생명주기
	* 컨테이너 초기화와 종료
	* 빈 객체의 라이프 사이클
* 참고

1. 들어가며

스프링에서 DI(Dependency Injection) 의존성 주입 기능을 제공합니다. 이 개념은 프로그램에서 객체 간의 의존성을 낮추기 위해서 코드상으로 의존성을 맺는 것이 아니라 외부의 설정파일(ex. Bean xml)을 통해서 정의할 수 있는 디자인 패턴중에 하나입니다. [마틴 파울러](https://en.wikipedia.org/wiki/Martin_Fowler) 에 의해서 제시된 용어입니다. 

DI란
장점

Quote

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20DI%20%EC%84%A4%EC%A0%95%20%EB%B0%A9%EB%B2%95/image_4.png)

2. 스프링 DI 설정하는 방법

스프링에서 DI 설정은 총 3가지 방법으로 의존성을 세팅할 수 있습니다.

* 어노테이션을 이용한 의존성 주입
* Bean 정의 파일을 이용한 의존성 주입
* JavaConfig을 이용한 의존성 주입

2.1 어노테이션을 이용한 의존성 주입 (컴포넌트 스캔 방식)

JavaConfig으로 할 수 있음

@Autowired
@Component
의미가 뭔가

@Qualifer

[http://websystique.com/spring/spring-dependency-injection-annotation-beans-auto-wiring-using-autowired-qualifier-resource-annotations-configuration/](http://websystique.com/spring/spring-dependency-injection-annotation-beans-auto-wiring-using-autowired-qualifier-resource-annotations-configuration/)
[https://www.logicbig.com/tutorials/spring-framework/spring-core/javaconfig-with-componnet-scan.html](https://www.logicbig.com/tutorials/spring-framework/spring-core/javaconfig-with-componnet-scan.html)

2.2 Bean 정의 파일을 이용한 의존성 주입

2.3 JavaConfig을 이용한 의존성 주입
ㄴㅇㄹ

3. 빈 생명주기

빈 생성시 …
@PostConstruct
@PreDestory

3. 참고

* 책
	* 
![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20DI%20%EC%84%A4%EC%A0%95%20%EB%B0%A9%EB%B2%95/image_3.jpeg)
	* 
* 의존성 주입
	* [https://ko.wikipedia.org/wiki/의존성_주입](https://ko.wikipedia.org/wiki/%EC%9D%98%EC%A1%B4%EC%84%B1_%EC%A3%BC%EC%9E%85)
	* [https://en.wikipedia.org/wiki/Dependency_injection](https://en.wikipedia.org/wiki/Dependency_injection)
* 스프링 DI
	* [http://ooz.co.kr/175](http://ooz.co.kr/175)
	* [http://www.mimul.com/pebble/default/2018/03/30/1522386129211.html](http://www.mimul.com/pebble/default/2018/03/30/1522386129211.html)
	* [https://www.baeldung.com/constructor-injection-in-spring](https://www.baeldung.com/constructor-injection-in-spring)
	* [https://www.baeldung.com/spring-annotations-resource-inject-autowire](https://www.baeldung.com/spring-annotations-resource-inject-autowire)
	* [https://www.baeldung.com/spring-injecting-collections](https://www.baeldung.com/spring-injecting-collections)
* DI 종류
	* [https://www.tutorialspoint.com/spring/spring_dependency_injection.htm](https://www.tutorialspoint.com/spring/spring_dependency_injection.htm)
* 스프링 DI 패턴에 대한 유닛 테스트
	* [https://dzone.com/articles/spring-di-patterns-the-good-the-bad-and-the-ugly](https://dzone.com/articles/spring-di-patterns-the-good-the-bad-and-the-ugly)

- - - -

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20DI%20%EC%84%A4%EC%A0%95%20%EB%B0%A9%EB%B2%95/image_1.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20DI%20%EC%84%A4%EC%A0%95%20%EB%B0%A9%EB%B2%95/image_5.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20DI%20%EC%84%A4%EC%A0%95%20%EB%B0%A9%EB%B2%95/image_6.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%8A%A4%ED%94%84%EB%A7%81%20DI%20%EC%84%A4%EC%A0%95%20%EB%B0%A9%EB%B2%95/image_2.png)

#tistory #blog #스터디중