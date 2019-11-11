# 블로그 : Powermock 사용법
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**

- [ ] @PrepareForTest
ㅁ. powermock에서 mockStatic(BeanUtils.class)을 사용하려면 @PrepareForTest 어노테이션을 선언해야 함

- [ ] java.lang.LinkageError: loader constraint violation: loader (instance of org_powermock_core_classloader_MockClassLoader) previously initiated loading for a different type with name "javax_management_MBeanServer”
ㅁ. 해결 : @PowerMockIgnore("javax.management.*")
[https://stackoverflow.com/questions/16520699/mockito-powermock-linkageerror-while-mocking-system-class](https://stackoverflow.com/questions/16520699/mockito-powermock-linkageerror-while-mocking-system-class)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Powermock%20%EC%82%AC%EC%9A%A9%EB%B2%95/image_1.png)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* Powermock
	* [http://blog.naver.com/PostView.nhn?blogId=loopbit&logNo=221309295191&categoryNo=0&parentCategoryNo=0&viewDate=¤tPage=1&postListTopCurrentPage=1&from=postView&userTopListOpen=true&userTopListCount=5&userTopListManageOpen=false&userTopListCurrentPage=1](http://blog.naver.com/PostView.nhn?blogId=loopbit&amp;logNo=221309295191&amp;categoryNo=0&amp;parentCategoryNo=0&amp;viewDate=&amp;currentPage=1&amp;postListTopCurrentPage=1&amp;from=postView&amp;userTopListOpen=true&amp;userTopListCount=5&amp;userTopListManageOpen=false&amp;userTopListCurrentPage=1)
	* [https://examples.javacodegeeks.com/core-java/mockito/powermock-mockito-integration-example/](https://examples.javacodegeeks.com/core-java/mockito/powermock-mockito-integration-example/)

#unit test# #blog #tistory #스터디중