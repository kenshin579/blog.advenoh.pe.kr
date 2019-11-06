# 블로그 : JPA one-to-many 단방양, 양반양에 ...
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**

- [ ] insertable=false은 언제 사용하고 어떤 sql 문구가 나오나?
-

-- one-to-many mapping하는 방법 2가지-
**1. uni-directional mapping**
- [ ] @ManyToOne 어노테이션을 child entity에 추가하기

Post
Comment
추가 annotation은 없음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JPA%20one-to-many%20%EB%8B%A8%EB%B0%A9%EC%96%91,%20%EC%96%91%EB%B0%98%EC%96%91%EC%97%90%20.../image_3.png)

**2. bidirectional mapping**
- [ ] 이걸 하는 목적은 부모 엔티티(ex. post)에서 자식 엔티티 (ex. comments) 목록을 유지 관리하고 부모 엔티티를 통해서 자식 엔티티를 유지하고 검색/조회할 수 있게 하는 것임
ㅁ. hiberate의 state transition과 dirty checking 기능으로 가능함

- [ ] @OneToMany 어노테이션을 parent side
- [ ] @ManyToOne 어노테이션을 child side

Post
Comment

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JPA%20one-to-many%20%EB%8B%A8%EB%B0%A9%EC%96%91,%20%EC%96%91%EB%B0%98%EC%96%91%EC%97%90%20.../image_2.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20JPA%20one-to-many%20%EB%8B%A8%EB%B0%A9%EC%96%91,%20%EC%96%91%EB%B0%98%EC%96%91%EC%97%90%20.../image_1.png)

* 장점
	* comments를 post에 저장하도록 자동으로 insert sql을 만들어줌

* 단점
	* bidirectional mapping을 하면 매우 tightly하게 coupling이 되어 있음
	* post.getComments()하면 로드되지 않았으며 DB에서 모든 comments를 조회함 - 성능 이슈
		* comments라 로드되는 것을 제안을 둘수 없음 - paginate가 안됨
	* post 엔티티를 통해서 comments를 로딩하면 정렬을 할 수 없음
		* @OrderColumn 어노테이션을 추가해서 default 정렬 순서를 지정할수 있지만, 성능 이슈가 있음
	* 자주 LazyInitializationException 예외가 발생함

- [ ] bidirectional mapping에서의 문제점 (모두 다 검색한다)에 대한 해결책은 없나?
ㅁ.

- [ ] bidirectional mapping 언제 사용하는게 좋은 가?
* 자식 엔티티의 수가 제한되어 있을 때
* tight coupling이 필요할 경우에
	* 예로. Survey
		* 부모 엔티티 - Question
		* 자식 엔티티 - Options (최대 4, 5정도)
			* Question을 가져올 때 Options도 같이 조회해야 함

- [ ] @JoinColumn 는 foreign key column 지정할 때 사용하는 어노테이션

[❲코드분석❳ analyzing-jpa-hibernate-tutorials](evernote:///view/838797/s7/ef966571-dada-4994-8b88-2154dae65f4d/ef966571-dada-4994-8b88-2154dae65f4d/)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* JPA - one-to-many mapping
	* [https://www.callicoder.com/hibernate-spring-boot-jpa-one-to-many-mapping-example/](https://www.callicoder.com/hibernate-spring-boot-jpa-one-to-many-mapping-example/)
	* [https://www.baeldung.com/hibernate-one-to-many](https://www.baeldung.com/hibernate-one-to-many)