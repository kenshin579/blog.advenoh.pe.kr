# 블로그 : hibernate 2nd level cache란
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] hibernate 2nd level cache?
* 1st 캐시
	* session scoped cache임
	* JPA에서 각 entity가 persistent context에 한번 로딩됨
* 2nd 캐시
	* session-factory scoped
	* 모든 session간에 공유할 수 있음
	* 설정
		* pom에 hibernate-ehcache 추가
		* Entity에 어노테이션 추가

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20hibernate%202nd%20level%20cache%EB%9E%80/image_1.png)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* Amazon S3
	* [https://www.baeldung.com/hibernate-second-level-cache](https://www.baeldung.com/hibernate-second-level-cache)