# 블로그 : Sonarque로 unit test 커버리지 확인
* 들어가며
* 개발 환경
* 사용법
	* 설치 및 설정
		* .m2/settings.xml 파일
		* pom.xml 수정
	* IDE에서 plugin
	* Sonarqube 실행

* 참고

**코멘트**
 
 
- [ ] 도커 이미지 다운로드
># docker pull sonarqube

- [ ] docker 다시 실행했을 때 기존 reload가 되나?
Demon 실행
># docker run -d -v app-data:/data --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube

[https://stackoverflow.com/questions/41067032/how-to-stop-relaunch-docker-container-without-losing-the-changes](https://stackoverflow.com/questions/41067032/how-to-stop-relaunch-docker-container-without-losing-the-changes)

- [ ] maven 실행
># mvn clean package sonar:sonar -Dmaven.test.skip=false -Dmaven.test.failure.ignore=true

- [ ] qa에서 sonarqube 규칙을 어떻게 다운로드할 수 있나?
ㅁ. Quality Profiles > Back up

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Sonarque%EB%A1%9C%20unit%20test%20%EC%BB%A4%EB%B2%84%EB%A6%AC%EC%A7%80%20%ED%99%95%EC%9D%B8/image_2.png)

[https://docs.sonarqube.org/latest/instance-administration/quality-profiles/](https://docs.sonarqube.org/latest/instance-administration/quality-profiles/)
[https://stackoverflow.com/questions/39021149/export-sonar-rules-with-description-to-excel](https://stackoverflow.com/questions/39021149/export-sonar-rules-with-description-to-excel)
[https://gaebalsaebalcha.tistory.com/17](https://gaebalsaebalcha.tistory.com/17)

- [ ] sonarqube에서 테스트 커버리지는 왜 안보여지나?
ㅁ. 테스트가 실행이 안되서 그러함

># mvn clean package -Dmaven.test.skip=trueㅜㅐ

- [ ] test가 failure로 떨어져도 sonarqube에서 unit test 반영되도록 하기
ㅁ. -Dmaven.test.failure.ignore=true

[https://dzone.com/articles/separating-integration-and](https://dzone.com/articles/separating-integration-and)
[https://dzone.com/articles/integration-jenkins-jacoco-and-sonarqube](https://dzone.com/articles/integration-jenkins-jacoco-and-sonarqube)
[http://ayetgin.blogspot.com/2016/12/java-unit-test-code-coverage-with-sonarqube-maven-jococo.html](http://ayetgin.blogspot.com/2016/12/java-unit-test-code-coverage-with-sonarqube-maven-jococo.html)

- [ ] 설정파일

<a href='pom.xml'>pom.xml</a>

<a href='settings.xml'>settings.xml</a>

- [ ] v6.5버전으로 실행해서 rule을 뽑을 수 있나?
ㅁ. 있고

1. Key 검색
[http://sonarqube2.tmonc.net/sonar/api/qualityprofiles/search?](http://sonarqube2.tmonc.net/sonar/api/qualityprofiles/search?)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Sonarque%EB%A1%9C%20unit%20test%20%EC%BB%A4%EB%B2%84%EB%A6%AC%EC%A7%80%20%ED%99%95%EC%9D%B8/image_3.png)

[http://localhost:9000/api/qualityprofiles/backup?profileKey=AW3dtRHNLXtBACa7ZD38](http://localhost:9000/api/qualityprofiles/backup?profileKey=AW3dtRHNLXtBACa7ZD38)

AW3dtG7PLXtBACa7ZDnj

AV5Lngcs7rkPUI7urh-p

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* SonarQube + Docker
	* [https://medium.com/@SlackBeck/java-개발자를-위한-maven-sonarqube-docker로-시작하는-코드-정적-분석-1d6a33f27dc](https://medium.com/@SlackBeck/java-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-maven-sonarqube-docker%EB%A1%9C-%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-%EC%BD%94%EB%93%9C-%EC%A0%95%EC%A0%81-%EB%B6%84%EC%84%9D-1d6a33f27dc)
* SonarQube
	* [https://kwonnam.pe.kr/wiki/java/sonarqube](https://kwonnam.pe.kr/wiki/java/sonarqube)
	* [https://sarc.io/index.php/java/510-sonarcube-sonarscanner-source-code](https://sarc.io/index.php/java/510-sonarcube-sonarscanner-source-code)
	* [https://taetaetae.github.io/2018/02/08/jenkins-sonar-github-integration/](https://taetaetae.github.io/2018/02/08/jenkins-sonar-github-integration/)
	* [https://www.baeldung.com/sonar-qube](https://www.baeldung.com/sonar-qube)
	* [https://www.c-sharpcorner.com/article/step-by-step-sonarqube-setup-and-run-sonarqube-scanner/](https://www.c-sharpcorner.com/article/step-by-step-sonarqube-setup-and-run-sonarqube-scanner/)
	* [https://myinbox.tistory.com/122](https://myinbox.tistory.com/122)
	* [https://daddyprogrammer.org/post/817/sonarqube-analysis-intergrated-intellij/](https://daddyprogrammer.org/post/817/sonarqube-analysis-intergrated-intellij/)
	* [https://www.lesstif.com/pages/viewpage.action?pageId=39126262](https://www.lesstif.com/pages/viewpage.action?pageId=39126262)
* 기타
	* [https://confluence.curvc.com/pages/viewpage.action?pageId=13631519](https://confluence.curvc.com/pages/viewpage.action?pageId=13631519)
	* [https://www.popit.kr/%EB%82%B4%EC%BD%94%EB%93%9C%EB%A5%BC-%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C-%EB%A6%AC%EB%B7%B0%ED%95%B4%EC%A4%80%EB%8B%A4%EB%A9%B4-by-sonarqube/](https://www.popit.kr/%EB%82%B4%EC%BD%94%EB%93%9C%EB%A5%BC-%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C-%EB%A6%AC%EB%B7%B0%ED%95%B4%EC%A4%80%EB%8B%A4%EB%A9%B4-by-sonarqube/)
	* [https://www.lesstif.com/pages/viewpage.action?pageId=39126262](https://www.lesstif.com/pages/viewpage.action?pageId=39126262)