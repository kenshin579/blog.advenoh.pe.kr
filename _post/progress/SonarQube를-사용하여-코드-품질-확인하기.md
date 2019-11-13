---
title: 'SonarQube를 사용하여 코드 품질 확인하기'
date: 2019-10-31 10:26:33
category: 'java'
tags: ["sonarqube", "unit test", "docker", "pmd", "findbugs", "checkstyle", "코드풀질", "도커"]
---

* Sonarque에서 코드 커버리지 및 유닛테스트 확인
	* 소개
	* 도커로 버전과 랑 그냥 컴벤드 상에서
* 회사에서 개인정보 Import해서 확인하는 방법
	* Export 하는 방법
	* 도커 커스마이징해서 생성하기
		* 도커로 허브에 올리기
	* 실행하기
		* 결과가 동일한지 확인하기

* 들어가며
	* 기본 개념
* 설치 환경
* 사용법
* 참고

# 1. 들어가며

개발 프로젝트를 진행하다보면 코드 품질를 유지하기가 쉽지 않습니다. 특히 다양한 개발자와 같이 협업해서 프로젝트를 진행하는 경우에는 특히 그렀습니다. 서로 코드 스타일도 다르고 또한 서로 코드 리뷰를 한다 하더라도 모든 부분에 대해서 잠재적인 문제점을 파악하기는 쉽지 않습니다. 더욱이 시간이 지나면 지날 수록 코드 복잡도는 높아져서 더욱 문제 파악이 어려워집니다.

## 1.1 다른 정적 도구

이런 이슈로 다양한 정적 분석 도구가 개발되어 왔습니다. 대표적으로 자바에서 많이 사용하는 도구입니다. 개발 IDE에서도 플로그인으로도 제공하여 코드 작성시에도 확인할 수 있습니다.

* PMD
	* 자바용 정적 분석 도구로 중복 코드, 표준 코드 기준, 안티패턴등을 정적 분석을 통해서 알려준다
	* Intellij IDE에서 실행 화면

![](images/20191031/image_2.png)

* FindBugs
	* Maryland 대학에서 개발된 정적 도구로 프로그램에서 잠재적인 버그나 다른 이슈(ex. 성능, 보안)를 찾아주는 도구이다
	* Intellij IDE에서 실행 화면

![](images/20191031/image_3.png)

* CheckStyle
	* 정의된 코드 스타일 규칙에 위반되는 것을 찾아준다
	* 기본적으로 2가지 내장된 규칙(Google과 Sun Style)을 제공한다
	* Intellij IDE에서 실행 화면

![](images/20191031/image_1.png)

## 1.2 SonarQube 정적 도구

위 정적 분석 도구외에도 SonarQube를 많이 사용하고 있습니다. SonarQube는

여러 회사에 많이 사용하는 SonarQube에 대해서 알아보겠습니다. 다른 도우와 같이

코드 정적분석
도구

**특징**
* 25+ 프로그래밍 언어 지원
* Jenkins와 연동하여 자동으로 실행하도록 할 수 있다.

# 2. 구축 환경

맥 환경 기반으로 설치 및 설정을 설명합니다. 그리고 정적 분석을 할 코드는 아래 github를 참고해주세요. Unit Test가 작성되어 있는 springboot-quartz—in-memory 프로젝트로 확인해보겠습니다. Unit Test도 최대한 많이 작성을 했었는데 코드 커버리지가 얼마나 나오고 정적 분석에서 어떤 결과가 나올지 궁금하네요. 단계별로 같이 알아보죠.

* OS : Mac OS
* IDE: Intellij
* Source code : [github](https://github.com/kenshin579/tutorials-java/tree/master/springboot-quartz-in-memory)

# 3. SonarQube 설치

SonarQube를 사용할 수 있는 방법은 2가지입니다. 도커를 사용하거나 직접 패키지를 다운로드해서 설치하는 방법이 있습니다. 도커의 경우에는 이미 SonarQube가 설치된 도커 이미지를 다운로드해서 바로 사용할 수 있는 장점이 있습니다. 도커를 사용하기를 추천드립니다. 하지만, 직접 다운로드하는 방법도 같이 알아 볼게요.

# 3.1 SonarQube 다운로드 및 설치

### 3.1.1 SonarQube 직접 설치 및 설정

### 3.1.2 Docker 사용

SonarQube를 직접 설치하는 번거로움 대신 도커를 사용하는 방법도 있습니다. 이미 SonarQube가 설치된 도커를 찾아서 도커로 실행하면 됩니다.

도커가 없는 경우에는 brew
```bash
$ brew cask install docker
```

# 3. SonarQube 사용법

# 3.1 대시보드
# 3.2 코드 규칙
## 3.2.1 변경
# 3.3 플러그인
## 3.3.1 Doxygen
## 3.3.2 개발 IDE와의 연동 (Intellij)

# 4. 정리

# 5. 참고

* SonarQube
	* [https://www.sonarqube.org](https://www.sonarqube.org/)
	* [https://en.wikipedia.org/wiki/SonarQube](https://en.wikipedia.org/wiki/SonarQube)
	* [https://new93helloworld.tistory.com/378](https://new93helloworld.tistory.com/378)
	* [https://www.popit.kr/내코드를-자동으로-리뷰해준다면-by-sonarqube/](https://www.popit.kr/%EB%82%B4%EC%BD%94%EB%93%9C%EB%A5%BC-%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C-%EB%A6%AC%EB%B7%B0%ED%95%B4%EC%A4%80%EB%8B%A4%EB%A9%B4-by-sonarqube/)
	* [http://www.nextree.co.kr/p2963/](http://www.nextree.co.kr/p2963/)
	* [https://daddyprogrammer.org/post/817/sonarqube-analysis-intergrated-intellij/](https://daddyprogrammer.org/post/817/sonarqube-analysis-intergrated-intellij/)
* PMD, FindBugs, CheckStyle
	* [https://pmd.github.io](https://pmd.github.io/)
	* [http://pseg.or.kr/pseg/infouse/4840](http://pseg.or.kr/pseg/infouse/4840)
	* [https://thefif19wlsvy.tistory.com/57](https://thefif19wlsvy.tistory.com/57)

#blog #tistory
