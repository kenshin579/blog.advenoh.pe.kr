# 블로그 : HTTPClient4 사용법과 WireMock으로 유닛테스트 작성하기
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] connection retry 하는 예제도 넣자.

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

**3.1 httpclient4**

<dependency>
<groupId>commons-io</groupId>
<artifactId>commons-io</artifactId>
<version>2.4</version>
</dependency>
<dependency>
<groupId>org.apache.httpcomponents</groupId>
<artifactId>httpclient</artifactId>
<version>4.3.2</version>
</dependency>

4. 참고

* Apache HttpClient
	* [https://stackoverflow.com/questions/12059278/how-to-post-json-request-using-apache-httpclient](https://stackoverflow.com/questions/12059278/how-to-post-json-request-using-apache-httpclient)
	* [https://www.mkyong.com/java/apache-httpclient-examples/](https://www.mkyong.com/java/apache-httpclient-examples/)
* Apache HttpClient 4
	* [https://www.baeldung.com/httpclient-guide](https://www.baeldung.com/httpclient-guide)
	* [https://www.baeldung.com/httpclient4](https://www.baeldung.com/httpclient4)
	* [https://inyl.github.io/programming/2017/09/14/http_component.html](https://inyl.github.io/programming/2017/09/14/http_component.html)
* HttpPost Retry
	* [https://somethingididnotknow.wordpress.com/2013/06/11/httppost-requests-executed-multiple-times-apache-httpclient/](https://somethingididnotknow.wordpress.com/2013/06/11/httppost-requests-executed-multiple-times-apache-httpclient/)
	* [http://www.ivanopt.com/http-get-request-set-timeout-retry-time-java/](http://www.ivanopt.com/http-get-request-set-timeout-retry-time-java/)
	* [https://memorynotfound.com/apache-httpclient-httprequestretryhandler-example/](https://memorynotfound.com/apache-httpclient-httprequestretryhandler-example/)
	* [https://stackoverflow.com/questions/22827291/force-retry-on-specific-http-status-code/22827553](https://stackoverflow.com/questions/22827291/force-retry-on-specific-http-status-code/22827553)
* WireMock
	* [http://wiremock.org/docs/getting-started/](http://wiremock.org/docs/getting-started/)
	* [https://www.baeldung.com/introduction-to-wiremock](https://www.baeldung.com/introduction-to-wiremock)

#tistory #blog #스터디중