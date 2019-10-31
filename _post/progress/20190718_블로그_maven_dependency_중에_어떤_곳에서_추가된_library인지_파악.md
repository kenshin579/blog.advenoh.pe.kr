# 블로그 : maven dependency 중에 어떤 곳에서 추가된 library인지 파악
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
-

intellij

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20maven%20dependency%20%EC%A4%91%EC%97%90%20%EC%96%B4%EB%96%A4%20%EA%B3%B3%EC%97%90%EC%84%9C%20%EC%B6%94%EA%B0%80%EB%90%9C%20library%EC%9D%B8%EC%A7%80%20%ED%8C%8C%EC%95%85/image_3.png)

원하는 dependency 선택이후 Root -> Selection하면 root dependency를 알 수 있음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20maven%20dependency%20%EC%A4%91%EC%97%90%20%EC%96%B4%EB%96%A4%20%EA%B3%B3%EC%97%90%EC%84%9C%20%EC%B6%94%EA%B0%80%EB%90%9C%20library%EC%9D%B8%EC%A7%80%20%ED%8C%8C%EC%95%85/image_1.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20maven%20dependency%20%EC%A4%91%EC%97%90%20%EC%96%B4%EB%96%A4%20%EA%B3%B3%EC%97%90%EC%84%9C%20%EC%B6%94%EA%B0%80%EB%90%9C%20library%EC%9D%B8%EC%A7%80%20%ED%8C%8C%EC%95%85/image_2.png)

># mvn dependency:tree

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20maven%20dependency%20%EC%A4%91%EC%97%90%20%EC%96%B4%EB%96%A4%20%EA%B3%B3%EC%97%90%EC%84%9C%20%EC%B6%94%EA%B0%80%EB%90%9C%20library%EC%9D%B8%EC%A7%80%20%ED%8C%8C%EC%95%85/image_4.png)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* Maven Dependency
	* [https://stackoverflow.com/questions/49634923/can-the-intellij-external-maven-library-tell-where-the-dependencies-are-from](https://stackoverflow.com/questions/49634923/can-the-intellij-external-maven-library-tell-where-the-dependencies-are-from)