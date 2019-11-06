# 블로그 : 자바8 CompletableFuture이란
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] 기본에 Future 사용을 어떻게 했나?

1. 들어가며

* JDK5
	* Future
* JDK8
	* CompletableFuture
	* (I) CompletionStage

[https://m.blog.naver.com/2feelus/220714398973](https://m.blog.naver.com/2feelus/220714398973)
[https://mahmoudanouti.wordpress.com/2018/01/26/20-examples-of-using-javas-completablefuture/](https://mahmoudanouti.wordpress.com/2018/01/26/20-examples-of-using-javas-completablefuture/)

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법
ExecutorService + Future로 실행하는 예제

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_2.png)

3.1 CompletableFuture로 실행
- [ ] CompletableFuture는 (I) Future을 구현하고 있음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/0B2B2965-2CEC-47A4-A577-19718DABB031.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_8.png)

- [ ] CompletedFuture 인자로 넘겨주면 get을 하면 바로 실행됨
ㅁ. 이건 언제 사용하나?

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_1.png)

- [ ] future 실행을 취소하는 예제

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_9.png)

3.2 간단하게 실행하는 방법? (executor 실행없임)

- [ ] runAsync, supplyAsync()은 CompletableFuture 인스턴스를 바로 생성해줌; 인자로는 Runnable & Supplier 함수를 받음

* Runnable : no 인자, no return
* Supplier: no 인자, return 값

바로 실행된다.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_11.png)

3.3 async 실행에 대하 결과 처리
- [ ] thenApply() 함수는 결과에 대한 처리를 할 수 있음.(Future을 반환함)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_17.png)

- [ ] 반값하지 앖으려면… thenAccept()

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/105E3D3F-B91A-40AC-BD39-8D0CD3B02B87.png)

- [ ] no 인자, no return : thenRun() 사용

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_5.png)

3.4 Future 합치기

- [ ] thenCompose() : sequential

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_18.png)

- [ ] thenCombine : 독립된 Future의 결과를 합치기

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_7.png)

- [ ] thenAcceptBoth() : 인자를 주지 않고 결과만 합치기

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_3.png)

- [ ] thenApply()와 thenCompose()의 차이점

ㅁ. thenApply() : 그전 결과를 transform하는데 사용함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_10.png)

ㅁ. thenCompose() : thenApply()와 비슷하지만, new CompletionStage()를 반환함
#. 잘 이해 안됨

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_4.png)

- [ ] 여러 Future를 동시 실행예제

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_12.png)

3.5 오류 처리
- [ ] try/catch 대신 handle() 메서드를 통해서 처리함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_13.png)

3.6 async 메서드

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/9BBF4E22-1FEF-4827-B56D-7A114CBEA55C.png)

- [ ] thenApplyAsync vs thenApply

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EC%9E%90%EB%B0%948%20CompletableFuture%EC%9D%B4%EB%9E%80/image_15.png)

[https://stackoverflow.com/questions/47489338/what-is-the-difference-between-thenapply-and-thenapplyasync-of-java-completablef](https://stackoverflow.com/questions/47489338/what-is-the-difference-between-thenapply-and-thenapplyasync-of-java-completablef)

**4. 자바9 추가 API**

[https://www.baeldung.com/java-9-completablefuture](https://www.baeldung.com/java-9-completablefuture)

4. 참고

* CompletableFuture
	* [https://www.callicoder.com/java-8-completablefuture-tutorial/](https://www.callicoder.com/java-8-completablefuture-tutorial/)
	* [https://www.baeldung.com/java-completablefuture](https://www.baeldung.com/java-completablefuture)
	* [https://dzone.com/articles/20-examples-of-using-javas-completablefuture](https://dzone.com/articles/20-examples-of-using-javas-completablefuture)
	* [https://www.callicoder.com/java-8-completablefuture-tutorial/](https://www.callicoder.com/java-8-completablefuture-tutorial/)
	* [http://devidea.tistory.com/entry/Java8-CompletableFuture-%EC%A0%95%EB%A6%AC](http://devidea.tistory.com/entry/Java8-CompletableFuture-%EC%A0%95%EB%A6%AC)
	* [https://medium.com/@chanhyeonglee/completable-future-%EA%B0%80%EC%9D%B4%EB%93%9C-%ED%8C%8C%ED%8A%B82-eb82768f095d](https://medium.com/@chanhyeonglee/completable-future-%EA%B0%80%EC%9D%B4%EB%93%9C-%ED%8C%8C%ED%8A%B82-eb82768f095d)
	* [https://github.com/HomoEfficio/dev-tips/blob/master/Java%20CompletableFuture%20%EC%82%AC%EC%9A%A9%20%EC%8A%A4%ED%83%80%EC%9D%BC.md](https://github.com/HomoEfficio/dev-tips/blob/master/Java%20CompletableFuture%20%EC%82%AC%EC%9A%A9%20%EC%8A%A4%ED%83%80%EC%9D%BC.md)
	* [https://dzone.com/articles/20-examples-of-using-javas-completablefuture](https://dzone.com/articles/20-examples-of-using-javas-completablefuture)
	* [https://mahmoudanouti.wordpress.com/2018/01/26/20-examples-of-using-javas-completablefuture/](https://mahmoudanouti.wordpress.com/2018/01/26/20-examples-of-using-javas-completablefuture/)
* Unit Test
	* [https://medium.com/@Mumuksia/completablefuture-practical-guide-e4564f332f83](https://medium.com/@Mumuksia/completablefuture-practical-guide-e4564f332f83)
* ThreadPool
	* [https://www.baeldung.com/thread-pool-java-and-guava](https://www.baeldung.com/thread-pool-java-and-guava)
* Future vs CmpletableFuture
	* [https://www.callicoder.com/java-8-completablefuture-tutorial/](https://www.callicoder.com/java-8-completablefuture-tutorial/)

#tistory #blog #스터디중