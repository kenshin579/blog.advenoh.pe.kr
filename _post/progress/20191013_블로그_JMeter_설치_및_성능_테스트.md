# 블로그 : JMeter 설치 및 성능 테스트
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**

- [ ] command 상에서 어떻게 실행하나?
ㅁ. 결과는 어떻게 다시 볼 수 있나?
># jmeter -n -t service_api.jmx -l result_ -e -o ._report_

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JMeter%20%EC%84%A4%EC%B9%98%20%EB%B0%8F%20%EC%84%B1%EB%8A%A5%20%ED%85%8C%EC%8A%A4%ED%8A%B8/image_1.png)

- [ ] 자주 사용하는 결과 요소
* Graph Results, Summary Report, View Results in Table.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JMeter%20%EC%84%A4%EC%B9%98%20%EB%B0%8F%20%EC%84%B1%EB%8A%A5%20%ED%85%8C%EC%8A%A4%ED%8A%B8/image_2.png)

- [ ] web socket 테스트도 가능하다

- [ ] 설정 값 의미
* Ramp-up period (초)
	* 모든 쓰레드를 생성하는데 걸리는 시간
	* ex. 0 : 동시에 모두 생성

- [ ] #samples : 서버에 요청한 횟수

- [ ] API의 한도도 궁금하다.
ㅁ. 어디까지 올라가나?

- [ ] 테스트할 소스코드는 async 관련 테스트를 넣는게 좋을 듯하다

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

설치
># brew install jmeter

-

3. 사용법

4. 참고

* JMeter
	* [https://www.linkedin.com/pulse/building-async-non-blocking-microservices-using-spring-patnaik](https://www.linkedin.com/pulse/building-async-non-blocking-microservices-using-spring-patnaik)
	* [https://homoefficio.github.io/2017/02/19/Blocking-NonBlocking-Synchronous-Asynchronous/](https://homoefficio.github.io/2017/02/19/Blocking-NonBlocking-Synchronous-Asynchronous/)
	* [https://kamang-it.tistory.com/entry/JMeter오픈-소스-부하테스트-툴-설치와-사용-1](https://kamang-it.tistory.com/entry/JMeter%EC%98%A4%ED%94%88-%EC%86%8C%EC%8A%A4-%EB%B6%80%ED%95%98%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%88%B4-%EC%84%A4%EC%B9%98%EC%99%80-%EC%82%AC%EC%9A%A9-1)
	* [https://hwangmin84.tistory.com/21](https://hwangmin84.tistory.com/21)
	* [https://victorydntmd.tistory.com/267](https://victorydntmd.tistory.com/267)

- - - -