# 블로그 : H2 사용법 & Intellij Database에서 연동
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**

1. 들어가며

H2는 오픈소스 경량 데이터베이스입니다.

Intellij에서 Database Tool과

[http://www.h2database.com/html/main.html](http://www.h2database.com/html/main.html)
[https://o7planning.org/en/11893/integrating-spring-boot-jpa-and-h2-database](https://o7planning.org/en/11893/integrating-spring-boot-jpa-and-h2-database)

특징

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

># brew install h2

># brew services start h2

[http://localhost:8082/login.jsp?jsessionid=2162ad5a53cdcabd58ab1f526957bc94](http://localhost:8082/login.jsp?jsessionid=2162ad5a53cdcabd58ab1f526957bc94)

H2 설정하기

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20H2%20%EC%82%AC%EC%9A%A9%EB%B2%95%20&%20Intellij%20Database%EC%97%90%EC%84%9C%20%EC%97%B0%EB%8F%99/image_1.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20H2%20%EC%82%AC%EC%9A%A9%EB%B2%95%20&%20Intellij%20Database%EC%97%90%EC%84%9C%20%EC%97%B0%EB%8F%99/image_2.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20H2%20%EC%82%AC%EC%9A%A9%EB%B2%95%20&%20Intellij%20Database%EC%97%90%EC%84%9C%20%EC%97%B0%EB%8F%99/image_5.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20H2%20%EC%82%AC%EC%9A%A9%EB%B2%95%20&%20Intellij%20Database%EC%97%90%EC%84%9C%20%EC%97%B0%EB%8F%99/image_6.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20H2%20%EC%82%AC%EC%9A%A9%EB%B2%95%20&%20Intellij%20Database%EC%97%90%EC%84%9C%20%EC%97%B0%EB%8F%99/image_3.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20H2%20%EC%82%AC%EC%9A%A9%EB%B2%95%20&%20Intellij%20Database%EC%97%90%EC%84%9C%20%EC%97%B0%EB%8F%99/image_4.png)

3. 사용법

4. 참고

* H2 설치 및 사용법
	* [https://en.wikipedia.org/wiki/H2_(DBMS](https://en.wikipedia.org/wiki/H2_%28DBMS) )
	* [https://jojoldu.tistory.com/234](https://jojoldu.tistory.com/234)
	* [https://www.tutorialspoint.com/h2_database/](https://www.tutorialspoint.com/h2_database/)
	* [http://www.h2database.com/html/cheatSheet.html](http://www.h2database.com/html/cheatSheet.html)