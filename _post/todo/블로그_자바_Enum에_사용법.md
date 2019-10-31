# 블로그 : 자바 Enum에 사용법
* 들어가며
* 사용법
* 참고

**코멘트**
- [ ] type safe란
ㅁ. Type safe하다는 건 타입을 판별할 수 있어 Run-time시가 아닌 compile-time에 타입 문제를 잡을 수 있다. (JavaScript은 type-safe하지 않다)
ㅁ. [https://m.blog.naver.com/PostView.nhn?blogId=jerrypop&logNo=40117130140&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F](https://m.blog.naver.com/PostView.nhn?blogId=jerrypop&amp;logNo=40117130140&amp;proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)
ㅁ. [http://dololak.tistory.com/17](http://dololak.tistory.com/17)

- [ ] Enum constants are implicitly static and final and you can not change their value once created.
- [ ] JDK 7부터 switch문에서 enum 사용가능
- [ ] EnumMap, EnumSet 추가됨
* < 64 상수 값 : EnumSet은 RegularEnumSet 클래스를 사용
* > 64 상수 값 : JumboEnumSet을 사용함
- [ ] Enum은 new operator로 생성하지 않고 Enum 상수값이 처음 불리면 Enum 클래스가 생성됨

- [ ] EnumMap이란?

-

1. 들어가며
Enum 잘 사용하는 방법.
Thinking in 자바를 참조

3. 참고

* 책
	* Thinking in Java
	* Effective Java - 6장 열거 타입과 애너테이션
* Enum
	* [https://github.com/jojoldu/blog-code/tree/master/enum-uses](https://github.com/jojoldu/blog-code/tree/master/enum-uses)
	* [https://github.com/jojoldu/blog-code/tree/master/java/enum-mapper](https://github.com/jojoldu/blog-code/tree/master/java/enum-mapper)

[책 : Thinking in Java 4th Ed](evernote:///view/838797/s7/cbd70d0e-e3f2-42ad-aba5-12df5a54fbe3/cbd70d0e-e3f2-42ad-aba5-12df5a54fbe3/)

참고
[https://javarevisited.blogspot.com/2011/08/enum-in-java-example-tutorial.html](https://javarevisited.blogspot.com/2011/08/enum-in-java-example-tutorial.html)
[https://bluepoet.me/2012/07/18/%EB%B2%88%EC%97%AD%EC%9E%90%EB%B0%94-enum%EC%9D%98-10%EA%B0%80%EC%A7%80-%EC%98%88%EC%A0%9C/](https://bluepoet.me/2012/07/18/%EB%B2%88%EC%97%AD%EC%9E%90%EB%B0%94-enum%EC%9D%98-10%EA%B0%80%EC%A7%80-%EC%98%88%EC%A0%9C/)
[http://hamait.tistory.com/383](http://hamait.tistory.com/383)
[https://tetzzang.com/%EC%9E%90%EB%B0%94%EC%9D%98-enum-%EB%8C%80%ED%95%98%EC%97%AC-%EA%B0%84%EB%8B%A8-%EC%98%88%EC%A0%9C-%ED%8F%AC%ED%95%A8/](https://tetzzang.com/%EC%9E%90%EB%B0%94%EC%9D%98-enum-%EB%8C%80%ED%95%98%EC%97%AC-%EA%B0%84%EB%8B%A8-%EC%98%88%EC%A0%9C-%ED%8F%AC%ED%95%A8/)
[http://woowabros.github.io/tools/2017/07/10/java-enum-uses.html](http://woowabros.github.io/tools/2017/07/10/java-enum-uses.html)

[http://www.nextree.co.kr/p11686/](http://www.nextree.co.kr/p11686/)

[http://iilii.egloos.com/4343065/](http://iilii.egloos.com/4343065/)
[http://bluepoet.me/2012/07/18/%EB%B2%88%EC%97%AD%EC%9E%90%EB%B0%94-enum%EC%9D%98-10%EA%B0%80%EC%A7%80-%EC%98%88%EC%A0%9C/](http://bluepoet.me/2012/07/18/%EB%B2%88%EC%97%AD%EC%9E%90%EB%B0%94-enum%EC%9D%98-10%EA%B0%80%EC%A7%80-%EC%98%88%EC%A0%9C/)

[http://godpage.tistory.com/entry/java-Enum-%EC%A0%95%EB%A6%AC](http://godpage.tistory.com/entry/java-Enum-%EC%A0%95%EB%A6%AC)

#tistory #blog #스터디중