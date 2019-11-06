# 블로그 : 자바 쓰레드풀 - ExecutorService
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
-

1. 들어가며

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%94%20%EC%93%B0%EB%A0%88%EB%93%9C%ED%92%80%20-%20ExecutorService/image_5.png)

- [ ] 목적 : 쓰레드 풀을 통해서 어플리이션의 쓰레드를 관리하겠다.

자바에서의 쓰레드 풀
* Executor
	* 정해진 설정 쓰레드 풀로 생성된다
	* custom fine-tuning이 필요없을때 사용
* (I) Executors :
	* execute() : 단일 메서드을 가지고 있음 (실행을 위해 runnable 인터페이스 인스턴스를 받음)
* (I) ExecutorService :
	* 더 많은 메서드를 제공함 (테스트 과정, 터미네이션)
	* future.get() 호출시 실행됨
* ThreadPoolExecutor : 더 많은 기능을 제공함 (corePoolSize, maximumPoolSize, keepAliveTime)
* ScheduledThreadPoolExecutor : ThreadPoolExecutor을 확장한 클래스임
* 기타
	* Runnable
		* exception도 throw하지 않고 결과값도 반환할 수 없다
	* Callabe
		* exception도 처리 가능하고 결과값도 반환할 수 있음

Executors :

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%94%20%EC%93%B0%EB%A0%88%EB%93%9C%ED%92%80%20-%20ExecutorService/image_7.png)

ExecutorService :

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%94%20%EC%93%B0%EB%A0%88%EB%93%9C%ED%92%80%20-%20ExecutorService/image_2.png)

ThreadPoolExecutor
- [ ] ThreadPoolExecutor is decorated with an immutable wrapper, so it cannot be reconfigured after creation.
- [ ] 대부분의 설정은 Executors static 메서드에 정의되어 있음

* corePoolSize : core 쓰레드 수
* maximumPoolSize : 모든 코어 쓰레드가 비지하고 더 많은 태스트가 추가되면 풀 크기가 maximumPoolSize만큰 늘어남
* keepAlive : 과도한 쓰레드로 생성된 쓰레드가 생존할 수 있는 idle 상태로 있을 수 있는 시간
	* 60로 설정하면 : 60초동안 idle이면 쓰레드를 dispose하겠다는 의미임.

설정
설명
Executors.newCachedThreadPool()

* corePoolsize: 0
* maximumPoolSize:Integer.MAX_VALUE
* keepAliveTime:60

poolsize 0이라서 처음에는 쓰레드는 전혀 받지 않음.

ㅁ.the cached thread pool may grow without bounds to accommodate any amount of submitted tasks. But when the threads are not needed anymore, they will be disposed of after 60 seconds of inactivity.
ㅁ.a lot of short-living tasks in your application.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%94%20%EC%93%B0%EB%A0%88%EB%93%9C%ED%92%80%20-%20ExecutorService/image_1.png)

Executors.newFixedThreadPool(2)

* corePoolsize: 2
* maximumPoolSize: 2
* keepAliveTime: 0

- [ ] the amount of simultaneously running tasks is less or equal to two at all times

- [ ] Otherwise some of these tasks may be put into a queue to wait for their turn.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%94%20%EC%93%B0%EB%A0%88%EB%93%9C%ED%92%80%20-%20ExecutorService/image_3.png)

Executors.newSingleThreadExecutor()

* corePoolsize: 1
* maximumPoolSize: 1
* keepAliveTime: 0

The single thread executor is ideal for creating an event loop.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%94%20%EC%93%B0%EB%A0%88%EB%93%9C%ED%92%80%20-%20ExecutorService/image_4.png)

Executors.newScheduledThreadPool(5)

* corePoolsize: 5
* maximumPoolSize: Integer.MAX_VALUE
* keepAliveTime: 0

ScheduledThreadPoolExecutor

* schedule() : execute a task once after a specified delay;
* scheduleAtFixedRate : delay 이후 period 값에 따라 계속 반복
* scheduleWithFixedDelay : task간의 delay 이후 반복적으로 실행됨

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%94%20%EC%93%B0%EB%A0%88%EB%93%9C%ED%92%80%20-%20ExecutorService/image_8.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%94%20%EC%93%B0%EB%A0%88%EB%93%9C%ED%92%80%20-%20ExecutorService/image_6.png)

ForkJoinPool
- [ ] JDK7에 추가됨
- [ ] spawning multiple tasks in recursive algorithms 문제를 해결해줌
- [ ] work stealing algorithm을 구현함
ㅁ. 새로운 쓰레드를 생성하지 않음
-

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* 자바 쓰레드 풀
	* [https://www.baeldung.com/thread-pool-java-and-guava](https://www.baeldung.com/thread-pool-java-and-guava)
	* [https://okky.kr/article/447253](https://okky.kr/article/447253)
	* [http://limkydev.tistory.com/55](http://limkydev.tistory.com/55)
	* [http://hamait.tistory.com/612](http://hamait.tistory.com/612)
* ExecutorService
	* [https://www.baeldung.com/java-executor-service-tutorial](https://www.baeldung.com/java-executor-service-tutorial)