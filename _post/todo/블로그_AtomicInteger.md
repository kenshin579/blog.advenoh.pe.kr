# 블로그 : AtomicInteger
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] synchronized 메서드를 사용하지 않고 여러 쓰레드를 제어할 수 있음
- [ ] atomic 클래스는 내부적으로 최신 CPU에서 직접 지원하는 atomic instruction인 compare-and-swap(CAS)를 많이 사용함
- [ ] lock을 하는 synchorniing보다 빠르다

* incrementAndGet() : increment하고 나서 get을 함
* get() : 값을 반환함
* updateAndGet(람다) : 람다 표현을 받아서 update이후에 get을 함
* accumulateAndGet() : IntBinaryOperator 람다 표현식을 받아서 accumulate하는 메서드

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* AtomicInteger
	* [https://winterbe.com/posts/2015/05/22/java8-concurrency-tutorial-atomic-concurrent-map-examples/](https://winterbe.com/posts/2015/05/22/java8-concurrency-tutorial-atomic-concurrent-map-examples/)