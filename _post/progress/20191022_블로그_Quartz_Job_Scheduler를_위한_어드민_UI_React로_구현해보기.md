# 블로그 : Quartz Job Scheduler를 위한 어드민 UI React로 구현해보기
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
-

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

3.5 Job History 기능

[Quartz Job History 스키마 정리하기](evernote:///view/838797/s7/e352142e-715a-4b66-b091-8c28d1689465/e352142e-715a-4b66-b091-8c28d1689465/)

Job History는 Quartz Cluster를 구성하는 데는 필요없지만, Quartz Scheduler용 어드민 UI 메인 페이지에 추가로 넣으면 좋을 것 같아서 이번에 작업을 같이 했었습니다. 이 내용은 어드민 UI 포스팅에서 다루도록 할께요.

3.5.1 Job History DB 스키마 구성

3.5.2 JPA 관계

3.5.3

* 설정
	* QuartzConfiguration : dataSource 추가함
* Job History 기능
	* ScheduleServiceImpl에서 추가함
	* Job History DB 스키마
	* JPA : 관계 정리

4. 정리
-

5. 참고

* Job History
	* [https://dzone.com/articles/using-obsidian-maintenance](https://dzone.com/articles/using-obsidian-maintenance)
	* [http://obsidianscheduler.com/wiki/Main_Page](http://obsidianscheduler.com/wiki/Main_Page)
	* [http://demo.obsidianscheduler.com/#/activity](http://demo.obsidianscheduler.com/#/activity)
* React valid
	* [https://leejungdo.com/blog/2019/01/26/React에서-인풋-필드-validate하기.html](https://leejungdo.com/blog/2019/01/26/React%EC%97%90%EC%84%9C-%EC%9D%B8%ED%92%8B-%ED%95%84%EB%93%9C-validate%ED%95%98%EA%B8%B0.html)

#blog #quartz