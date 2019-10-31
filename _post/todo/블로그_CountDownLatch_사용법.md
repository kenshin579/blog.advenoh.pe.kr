# 블로그 : CountDownLatch 사용법
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] CountDownLatch는
ㅁ. CountDownLatch는 다른 쓰레드가 시작하기전에 기다리도록 도와주는 클래스이다.
ㅁ. 쓰레드 관련해서 unit test을 작성할 때 많이 사용된다.

- [ ] CyclicBarrier는
ㅁ. 쓰레드 셋에서 한 지점(barrier)에 모두 다 도달하기까지 서로를 기다린다

1. 들어가며

CountDownLatch는 여러 쓰레드를 컨트롤 할때 사용합니다. CountDownLatch는 counter 필드를 가지고 있고 이 값이

[https://www.baeldung.com/java-countdown-latch](https://www.baeldung.com/java-countdown-latch)

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github

CountDownLatch는 JDK에 포함된 클래스입니다.

3. 사용법

4. 참고

* CountDownLatch
	* [https://www.baeldung.com/java-countdown-latch](https://www.baeldung.com/java-countdown-latch)
	* [https://www.geeksforgeeks.org/countdownlatch-in-java/](https://www.geeksforgeeks.org/countdownlatch-in-java/)
	* [http://tutorials.jenkov.com/java-util-concurrent/countdownlatch.html](http://tutorials.jenkov.com/java-util-concurrent/countdownlatch.html)
* CyclicBarrier
	* [https://www.baeldung.com/java-cyclicbarrier-countdownlatch](https://www.baeldung.com/java-cyclicbarrier-countdownlatch)