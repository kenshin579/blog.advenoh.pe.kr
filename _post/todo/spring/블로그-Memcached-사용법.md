# 블로그 : Memcached 사용법
* 개요
* 설치
* 기능
	* Cluster?
	* Sharing?
* 사용법
	* sdfsf
	* 스프링에서 …
* 개발
	* 내부적으로는 어떻게 사용하냐? 스프링에서??
	* com.google.code.simple-spring-memcached
* 참고

1. Memcached란

- [ ] 특징, 기능
* clustering을 지원하지 않는다
* 빠른 속도 보장
* client는 sharding을 직접 구현해야 한다
	* SSM에서 해줌

2. 설치 및 실행
># brew install memcached

실행
_usr_local_opt_memcached_bin_memcached

># ps aux | grep memcached

># brew install telnet

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Memcached%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_3.png)

**3. Memcached 명령어**

모니터링

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Memcached%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_1.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Memcached%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_2.png)

[https://www.solanara.net/solanara/memcached](https://www.solanara.net/solanara/memcached)

4. 참고

* memcached
	* [https://jdm.kr/blog/137](https://jdm.kr/blog/137)
	* [https://m.blog.naver.com/PostView.nhn?blogId=akaroice&logNo=220298608077&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F](https://m.blog.naver.com/PostView.nhn?blogId=akaroice&amp;logNo=220298608077&amp;proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)
* 비교
	* [https://db-engines.com/en/system/Memcached%3BRedis](https://db-engines.com/en/system/Memcached%3BRedis)
	* [https://aws.amazon.com/ko/elasticache/redis-vs-memcached/](https://aws.amazon.com/ko/elasticache/redis-vs-memcached/)
	* [http://postitforhooney.tistory.com/entry/DBRedisRedis에-대해서-공부하기-Redis-vs-Ehcache-vs-Memcached-비교하며-파악하기](http://postitforhooney.tistory.com/entry/DBRedisRedis%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0-Redis-vs-Ehcache-vs-Memcached-%EB%B9%84%EA%B5%90%ED%95%98%EB%A9%B0-%ED%8C%8C%EC%95%85%ED%95%98%EA%B8%B0)
	* [http://americanopeople.tistory.com/148](http://americanopeople.tistory.com/148)
	* [http://brownbears.tistory.com/43](http://brownbears.tistory.com/43)
* java library
	* [https://www.quora.com/What-is-the-best-memcached-Java-client-library](https://www.quora.com/What-is-the-best-memcached-Java-client-library)
	* [http://www.mimul.com/pebble/default/2011/04/15/1302866610452.html](http://www.mimul.com/pebble/default/2011/04/15/1302866610452.html)
	* [http://fnil.net/xmemcached/](http://fnil.net/xmemcached/)

[https://gist.github.com/tomysmile/ba6c0ba4488ea51e6423d492985a7953](https://gist.github.com/tomysmile/ba6c0ba4488ea51e6423d492985a7953)
[https://d2.naver.com/helloworld/151047](https://d2.naver.com/helloworld/151047)
[https://www.tutorialspoint.com/memcached/](https://www.tutorialspoint.com/memcached/)
[https://memcached.org/](https://memcached.org/)

#tistory #blog #스터디중