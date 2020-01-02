# 블로그 : Thread...
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
-

1. 들어가며

—

ForkJoinPool
Java 7 에서 도입
풀에 있는 모든 스레드가 풀에 submit 된 태스크 또는 다른 태스크에 의해 생성된 태스크를 찾아서 실행하는 방식으로 노는 스레드를 최소화하는 work-stealing 개념 포함
ExecutoreService는 트랜잭션 처리 같은 독립적인 태스크를 처리하는데 적합하고, ForkJoinPool은 작게 나누어 재귀적 실행으로 분할 정복 가능한 태스크를 처리하는데 적합
[ForkJoinPool.commonPool](http://ForkJoinPool.commonPool) ()로 공용 스레드 풀 쉽게 생성 가능
CompletableFuture의 *Async 메서드 호출 시 별도의 Executor를 인자로 넘기지 않으면 기본값으로 ForkJoinPool에서 할당받은 스레드로 비동기 처리

—

방법 1. 그냥 쓰레드 하나로 천만번을 순회하면서 숫자를 센다. (6초 걸림)

방법2. ForkJoinPool 을 사용해서 리프가 100개 일 때까지 분활(fork)해서 각각의 수치를 위로 합쳐서(join) 계산한다. 쓰레드 4개를 골고루 사용하며 대신 태스크 객체는 분활한 만큼 만들어 지게 된다.(2.5초 걸림)

방법3. 그냥 ThreadPoolExecutor 로 쓰레드 4개를 만든 후에 각각 천만개/4 로 나뉘어진 영역에 대해 순회하면서 숫자를 계산해서 합친다. ( 2초 걸림) ForkJoinPool 보다 더 빠르네요? 네 그렇습니다. 쓸 때없는 객체 생성이 없어졌기때문이에요.

방법4. 저렇게 쓰레드 4개가 거의 동일한 일을 하게 된다면 ForkJoinPool 이 오히려 독이겠지만 하나의 쓰레드가 굉장히 오래 걸리고 나머지 3개의 쓰레드는 금방 끝이나는 경우는?? 네 이 경우는 ForkJoinPool 이 빛을 발하게 됩니다. (ThreadPoolExecutor 4초 , ForkJoinPool 3초)

* 참고로 newFixedThreadPool 이런 팩토리 함수를 이용해서 만들어지는 것이 ThreadPoolExecutor 이다.즉 ThreadPoolExecutor 의 매개변수를 적절히 조절하면 newFixedThreadPool 나 newCachedThreadPool 에 해당하는 것들을 직접 만들 수 있다는 말

균일한 작업량의 쓰레드 배분이면 쓰레드풀이 더 좋고
차이가 많이 나면 포크조인이 더 좋고

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* Thread
	* [https://hamait.tistory.com/612](https://hamait.tistory.com/612)