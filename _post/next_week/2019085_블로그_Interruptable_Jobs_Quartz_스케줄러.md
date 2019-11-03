# 블로그 : Interruptable Jobs Quartz 스케줄러
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] 각 노드에서 시간이 sync가 안된 노드인 경우에는 잘못된 결과를 초래할 수 있음
ㅁ. timestamp을 기준으로 서로 ??

- [ ] JobDetail에서 job’s recoverable property = true로 하면 job 실행중에 scheduler가 다운되어도 다른 working scheduler가 픽업해서 실행할 수 있음

-

1. 들어가며

* Cluster Mode
	* RAMJobStore 대신 JDBC JobStore을 사용하면 됨
	* JDBC JobStore : 어플리케이션이 중지되고 다시 시작된 후에라도 스케줄링 정보를 유지하여 scheduler가 실행되도록 설계됨
		* **JobStoreTX - 이걸 사용하면 됨**
			* store jobs and triggers in a database via JDBC
			* 모든 action(ex. job 추가)에 대해서 transaction으로 처리함 (calling commit() or rollback())
			* 트랜젝션을 제어하고 싶은 경우, 서버환경 없이 어플리케이션을 운영하려고 할때 사용
		* JobStoreCMT :
			* JDBC with JTA container-managed transactions
			* 어플리케이션 서버 환경에서 어플리케이션이 운영되며 컨테이너가 트랜잭션을 관리하도록 하고 싶은 경우 사용됨 (이해 안됨)
			* [https://stackoverflow.com/questions/7697757/is-it-ok-to-use-jobstoretx-instead-of-jobstorecmt-for-quartz-jobs-in-seam](https://stackoverflow.com/questions/7697757/is-it-ok-to-use-jobstoretx-instead-of-jobstorecmt-for-quartz-jobs-in-seam)
			* [https://stackoverflow.com/questions/9552718/what-is-the-difference-between-jta-and-a-local-transaction](https://stackoverflow.com/questions/9552718/what-is-the-difference-between-jta-and-a-local-transaction)
* cluster 실행시 주의사항
	* random load-balancing algorithm을 사용함
	* job 하나를 cluster내의 특정 node에서 실행시킬 수 없다
		* 해결 : cluster node로 실행하되 다른 DB 테이블을 사용하고 다른 설정을 더 해야 한다고 함
	* 각 노드의 clock이 동기화 되어 있어야 함. (실행시간을 timestamp로 관리하고 있음)
	* Cluster에서 실행중인 전체 목록을 가져오려면
		* scheduler instance에서 query를 하면 실행중인 jobs만 알려줌
		* 해결 : DB에서 직접 query해서 가져와야 함

**Quartz DB 테이블**
- [ ] QRTZ_SCHEDULER_STATE 테이블에 scheduler가 추가됨

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Interruptable%20Jobs%20Quartz%20%EC%8A%A4%EC%BC%80%EC%A4%84%EB%9F%AC/image_6.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Interruptable%20Jobs%20Quartz%20%EC%8A%A4%EC%BC%80%EC%A4%84%EB%9F%AC/image_5.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Interruptable%20Jobs%20Quartz%20%EC%8A%A4%EC%BC%80%EC%A4%84%EB%9F%AC/image_4.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Interruptable%20Jobs%20Quartz%20%EC%8A%A4%EC%BC%80%EC%A4%84%EB%9F%AC/image_2.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Interruptable%20Jobs%20Quartz%20%EC%8A%A4%EC%BC%80%EC%A4%84%EB%9F%AC/image_1.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Interruptable%20Jobs%20Quartz%20%EC%8A%A4%EC%BC%80%EC%A4%84%EB%9F%AC/image_3.png)

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

cluster 세팅하는 방법
* quartz.properties
	* JDBC JobStore로 설정
* load the database with 스케줄 정보 (jobs and triggers)
* start each quartz node

4. 참고

* Quartz Cluster
	* [https://stackoverflow.com/questions/12626380/quartz-scheduler-in-cluster-environment](https://stackoverflow.com/questions/12626380/quartz-scheduler-in-cluster-environment)
	* [http://k2java.blogspot.com/2011/04/quartz.html](http://k2java.blogspot.com/2011/04/quartz.html)
	* [https://medium.com/@Hronom/spring-boot-quartz-scheduler-in-cluster-mode-457f4535104d](https://medium.com/@Hronom/spring-boot-quartz-scheduler-in-cluster-mode-457f4535104d)
	* [https://github.com/HomoEfficio/dev-tips/blob/master/Spring%201.5.*%20-%20Quartz%20Scheduler%20%EC%97%B0%EB%8F%99.md](https://github.com/HomoEfficio/dev-tips/blob/master/Spring%201.5.*%20-%20Quartz%20Scheduler%20%EC%97%B0%EB%8F%99.md)
	* [https://blog.naver.com/pure137/220305990400](https://blog.naver.com/pure137/220305990400)
	* [https://gist.github.com/ihoneymon/8e039a7d63e82f209826](https://gist.github.com/ihoneymon/8e039a7d63e82f209826)
	* [https://objectpartners.com/2013/07/09/configuring-quartz-2-with-spring-in-clustered-mode/](https://objectpartners.com/2013/07/09/configuring-quartz-2-with-spring-in-clustered-mode/)
	* [https://stackoverflow.com/questions/1187882/quartz-jobstore-with-spring-framework](https://stackoverflow.com/questions/1187882/quartz-jobstore-with-spring-framework)
* Quartz with Mysql
	* [http://xkcb.blogspot.com/2013/08/how-to-use-quartz-22-with-spring-32x-on.html](http://xkcb.blogspot.com/2013/08/how-to-use-quartz-22-with-spring-32x-on.html)
	* [https://medium.com/viithiisys/quartz-scheduler-with-mysql-database-506a608cf7a8](https://medium.com/viithiisys/quartz-scheduler-with-mysql-database-506a608cf7a8)
	* [https://medium.com/@ChamithKodikara/spring-boot-2-quartz-2-scheduler-integration-a8eaaf850805](https://medium.com/@ChamithKodikara/spring-boot-2-quartz-2-scheduler-integration-a8eaaf850805)
	* [http://teknosrc.com/how-setup-quartz-scheduler-server-with-mysql-database/](http://teknosrc.com/how-setup-quartz-scheduler-server-with-mysql-database/)
* Interrupt Job
	* [http://unserializableone.blogspot.com/2012/04/interrupt-quartz-job-that-doing-io.html](http://unserializableone.blogspot.com/2012/04/interrupt-quartz-job-that-doing-io.html)
* Timestamp
	* [https://www.epochconverter.com/](https://www.epochconverter.com/)
* Cron Expression
	* [https://www.freeformatter.com/cron-expression-generator-quartz.html](https://www.freeformatter.com/cron-expression-generator-quartz.html)
* Jobs 시작하기
	* [https://dzone.com/articles/using-quartz-for-scheduling-with-mongodb](https://dzone.com/articles/using-quartz-for-scheduling-with-mongodb)

#tistory #blog