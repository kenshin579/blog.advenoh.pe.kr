# 블로그 : ThreadLocal에 대한 설명
* 소개
	* 왜 사용하나?
* 참고

**1. 소개**
자바 1.2 버전부터 제공되고 있지만 아직 다수의 개발자들이 잘 몰라서 활용을 잘 못하는 기능이 하나 있는데, 그 기능이 바로 쓰레드 단위로 로컬 변수를 할당하는 기능이다.
hreadLocal을 이용하면 쓰레드 영역에 변수를 설정할 수 있기 때문에, 특정 쓰레드가 실행하는 모든 코드에서 그 쓰레드에 설정된 변수 값을 사용할 수 있게 된다

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20ThreadLocal%EC%97%90%20%EB%8C%80%ED%95%9C%20%EC%84%A4%EB%AA%85/image_1.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20ThreadLocal%EC%97%90%20%EB%8C%80%ED%95%9C%20%EC%84%A4%EB%AA%85/image_2.png)

**2. ThreadLocal의 기본 사용법**

**2.1 활용도**
ThreadLocal은 한 쓰레드에서 실행되는 코드가 동일한 객체를 사용할 수 있도록 해 주기 때문에 쓰레드와 관련된 코드에서 파라미터를 사용하지 않고 객체를 전파하기 위한 용도로 주로 사용되며, 주요 용도는 다음과 같다.

* 사용자 인증정보 전파 - Spring Security에서는 ThreadLocal을 이용해서 사용자 인증 정보를 전파한다.
 트랜잭션 컨텍스트 전파 - 트랜잭션 매니저는 트랜잭션 컨텍스트를 전파하는 데 ThreadLocal을 사용한다.*
* 쓰레드에 안전해야 하는 데이터 보관

**3. 참고**

* 사용법과 활용
	* [http://javacan.tistory.com/entry/ThreadLocalUsage](http://javacan.tistory.com/entry/ThreadLocalUsage)

#자바 #스터디중 #threadlocal #blog #java #thread #tistory