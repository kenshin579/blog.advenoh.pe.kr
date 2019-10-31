# 블로그 : git merge 와 rebase의 차이점
* 들어가며
* 개발 환경
* 사용법ㅑ
* 참고

**코멘트**
- [ ] 프로젝트시 정확한 차이점이 무엇이고 무엇이 최선의 선택인가?
ㅁ. 스터디가 필요하다!!!
- [ ] 다른 곳에서는 작업시 flow가 어떻게 되나?
ㅁ.
[http://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html](http://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html)
[http://blog.naver.com/PostView.nhn?blogId=tmondev&logNo=220763012361](http://blog.naver.com/PostView.nhn?blogId=tmondev&amp;logNo=220763012361)
[https://backlog.com/git-tutorial/kr/stepup/stepup2_8.html](https://backlog.com/git-tutorial/kr/stepup/stepup2_8.html)
[https://ko.atlassian.com/git/articles/git-team-workflows-merge-or-rebase](https://ko.atlassian.com/git/articles/git-team-workflows-merge-or-rebase)

- [ ] push한 것을 어떻게 rollback하나?
ㅁ. Revert commit을 하면 push할 commit이 생김
ㅁ. push하면 reverse “…”로 push됨

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20git%20merge%20%EC%99%80%20rebase%EC%9D%98%20%EC%B0%A8%EC%9D%B4%EC%A0%90/image_1.png)

참고
* [https://jupiny.com/2019/03/19/revert-commits-in-remote-repository/](https://jupiny.com/2019/03/19/revert-commits-in-remote-repository/)

1. 들어가며

이 핑계 저 핑계로 Git에 대해서 너무 몰라서 동료에게 계속 같은 걸 물어보고 있는 저를 발견해서 시간을 내서 모르는 부분에 대해서 다시 정리를 해보았습니다. 회사내에서 자주 사용하는 Gitkraken도 익힐 수 있는 시간도 가져보았어요. 역시 조금만 검색을 해도 모르는 부분을 더 채울 수 있는 듯합니다. 알아야 스트래스도 덜 받게 되는 것 같아요.

자 그면 merge와 rebase를 어떻게 하는지 알아보고 차이점에 대해서 알아보겠습니다.

여러 명이 같이 개발하다보면 merge시 conflict이 발생하는 경우가 종종 있습니다. 회사내 Git flow 정책에 따라서 개발…
Git의 기본도 잘 이해하지 못하고 있어서 시간을 내서 전체는 아니더라도 잘 모르는 부분은 다시 정리해보자. 계속 물어보기도 미안해진다 ㅜㅜ

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* Amazon S3
	* [https://d2.naver.com/helloworld/5626759](https://d2.naver.com/helloworld/5626759)
	* [https://blog.axosoft.com/learn-git-merging-rebasing/](https://blog.axosoft.com/learn-git-merging-rebasing/)

#tistory