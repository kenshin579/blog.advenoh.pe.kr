# 블로그 : AssertJ Unit Test 사용법
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
-
- [ ] Joda-time이란
ㅁ. 날짜 관련 unit test임

1. 들어가며

개발하면서 지금까지 JUnit을 많이 사용해서 유닛 테스트을 작성해왔습니다. 최근에 AssertJ 라이브러리를 알게되면서 기존에 JUnit 4에서 제공하는 메서드보다 훨씬 다양한

더 많이 개선된 것으로 알이잠, ㄴ

쭉 TDD로 계속을 지속적으로 해왔습니다.

하면서 TDD로 계속 개발을 지속적으로 해왔습니다.

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : [github](https://github.com/kenshin579/tutorials-java-examples/tree/master/assertj-unit-test)
* Software management tool : Maven

AssertJ 라이브러리를 사용하려면 아래 메이븐 의존성을 추가해야 합니다.

<dependency>
<groupId>org.assertj</groupId>
<artifactId>assertj-core</artifactId>
<version>3.11.1</version>
</dependency>

3. AssertJ 다루기

3.1

4. 참고

* AssertJ
	* [https://www.baeldung.com/introduction-to-assertj](https://www.baeldung.com/introduction-to-assertj)
	* [http://joel-costigliola.github.io/assertj/](http://joel-costigliola.github.io/assertj/)
	* [http://www.daleseo.com/assertj/](http://www.daleseo.com/assertj/)
	* [https://www.petrikainulainen.net/programming/testing/junit-5-tutorial-writing-assertions-with-assertj/](https://www.petrikainulainen.net/programming/testing/junit-5-tutorial-writing-assertions-with-assertj/)
	* [https://www.popit.kr/junit-assertion에서-assertj로-갈아탈-때-소소한-팁/](https://www.popit.kr/junit-assertion%EC%97%90%EC%84%9C-assertj%EB%A1%9C-%EA%B0%88%EC%95%84%ED%83%88-%EB%95%8C-%EC%86%8C%EC%86%8C%ED%95%9C-%ED%8C%81/)
	* [https://keyholesoftware.com/2018/03/12/fluent-assertions-with-assertj/](https://keyholesoftware.com/2018/03/12/fluent-assertions-with-assertj/)
* AssertJ Example Unit Test
	* [https://github.com/joel-costigliola/assertj-examples](https://github.com/joel-costigliola/assertj-examples)
* JUnit 5
	* [https://junit.org/junit5/](https://junit.org/junit5/)
	* [https://www.baeldung.com/junit-5-preview](https://www.baeldung.com/junit-5-preview)

#unit test# #blog #tistory #스터디중