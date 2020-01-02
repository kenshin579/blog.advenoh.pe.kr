# 블로그 : 자바 디자인 패턴: Builder
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**

Lombok로 생성하는것도 알아보자
- [ ] @Builder로도 보여주면 좋을 것 같다.

1. 들어가며

빌더 패턴은 객체의 여러 값을 조합해서 만들어주는 패턴임.

Team team = Team.builder()
.name("맨유")
.playCount(3)
.victoryPoint(6)
.winCount(2)
.drawCount(0)
.loseCount(1)
.scorePoint(4)
.build();

출처: [http://multifrontgarden.tistory.com/207](http://multifrontgarden.tistory.com/207) [우리집앞마당]

**Builder** - 복잡한 인스턴스 조립하기
- [ ] 미리 parameter를 설정(어떻게 객체를 만들겠다하는)하고 객체를 만들어주는 패턴인 것 같다.

**관련패턴**
- [ ] Template Method 패턴
ㅁ. Builder 패턴에서는 Director 역할이 Builder역할을 제어한다. vs. Template Method 패턴에서는 상위 클래스가 하위 클래스를 제어한다.

- [ ] Composite 패턴
ㅁ.Builder 패턴에 의해 만들어진 생성물은 Composite 패턴이 되는 경우가 있다.

- [ ] Facade 패턴
ㅁ. Builder 패턴의 Director 역할은 Builder 역할의 복잡한 메서드를 조합해서 인스턴스를 구축하는 단순한 인터페이스를 외부에 제공하는 것이다.
ㅁ. Facade 패턴의 Facade 역할은 내부 모듈을 조합해서 작업하기 위한 단순한 인터페이스를 외부에 제공한다.

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

 
 
4. 참고

* 빌더 패턴
	* [https://jdm.kr/blog/217](https://jdm.kr/blog/217)
	* [http://multifrontgarden.tistory.com/207](http://multifrontgarden.tistory.com/207)

	* [https://01010011.blog/2016/12/29/java8-consumer-supplier-%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-builder-pattern-%EA%B5%AC%ED%98%84/](https://01010011.blog/2016/12/29/java8-consumer-supplier-%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-builder-pattern-%EA%B5%AC%ED%98%84/)
	* 소스코드
		* media_api : LiveParameter

#tistory #blog #스터디중