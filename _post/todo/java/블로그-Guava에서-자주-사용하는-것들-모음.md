# 블로그 : Guava에서 자주 사용하는 것들 모음
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**

- [ ] CacheLoader는 local 캐싱
ㅁ. Map형태인 cache.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Guava%EC%97%90%EC%84%9C%20%EC%9E%90%EC%A3%BC%20%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%20%EA%B2%83%EB%93%A4%20%EB%AA%A8%EC%9D%8C/image_1.png)

- [ ] 캐싱에서 Eviction 할때 정책이 있음
* Size-based Eviction
* Timed Eviction

* Reference-based Eviction

- [ ] 삭제시
* Explicit Removals
	* cache invalidate하면 됨
* Remove Listeners
	* 캐쉬된 값이 지워지는 경우 후작업을 처리할수 있도록 Listener를 등록할수 있음
	* 비동기 Listener도 사용가능함

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* Guava CacheLoader
	* [https://www.baeldung.com/guava-cache](https://www.baeldung.com/guava-cache)
	* [https://helloino.tistory.com/130](https://helloino.tistory.com/130)
* Google Guava
	* [http://zetcode.com/articles/guava/](http://zetcode.com/articles/guava/)
	* [https://github.com/tfnico/guava-examples](https://github.com/tfnico/guava-examples)