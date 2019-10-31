# 블로그 : ModelMapper란
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] web + app 일때 다른 데이터를 반환할 때 어떻게 디자인을 하면 좋을지 고민해보자.
- [ ] ProperMap이란?
ㅁ. PropertyMap은 특정 소스와 대상 유형에 대한 속성 간의 매핑을 정의함
ㅁ. PropertyMap을 상속하고 configure()으로 mapping을 정의할 수 있음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20ModelMapper%EB%9E%80/image_1.png)

ㅁ. addMapping(…)을 사용시 mapping한 정보는 ModelMapper에 의해서 해석됨

참고
* [https://stackoverflow.com/questions/49003929/how-to-use-explicit-map-with-java-8-and-modelmapper](https://stackoverflow.com/questions/49003929/how-to-use-explicit-map-with-java-8-and-modelmapper)
* [https://www.isaacbroyles.com/2018/07/15/model-mapper.html](https://www.isaacbroyles.com/2018/07/15/model-mapper.html)
* [http://modelmapper.org/javadoc/org/modelmapper/PropertyMap.html](http://modelmapper.org/javadoc/org/modelmapper/PropertyMap.html)

- [ ] EDSL
ㅁ. PropertyMap은 EDSL(Embedded Domain Specific Language)를 사용소스 및 대상 메서드와 값을 서로 매핑하는 방법을 정의함
ㅁ

* map().setName(source.getFirstName());
* map().setLastName(source.surName);

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* Model Mapper
	* [https://github.com/amdegregorio/ModelMapperExample](https://github.com/amdegregorio/ModelMapperExample)
	* [https://www.baeldung.com/entity-to-and-from-dto-for-a-java-spring-application](https://www.baeldung.com/entity-to-and-from-dto-for-a-java-spring-application)
	* [http://modelmapper.org/getting-started/](http://modelmapper.org/getting-started/)
	* [https://auth0.com/blog/automatically-mapping-dto-to-entity-on-spring-boot-apis/](https://auth0.com/blog/automatically-mapping-dto-to-entity-on-spring-boot-apis/)
	* [https://mllab.tistory.com/328](https://mllab.tistory.com/328)
	* [https://stackoverflow.com/questions/28703401/conversion-of-dto-to-entity-and-vice-versa](https://stackoverflow.com/questions/28703401/conversion-of-dto-to-entity-and-vice-versa)
	* [http://mapstruct.org/](http://mapstruct.org/)
	* [https://www.baeldung.com/mapstruct](https://www.baeldung.com/mapstruct)
	* [https://www.youtube.com/watch?v=W5O7ydSXpUk](https://www.youtube.com/watch?v=W5O7ydSXpUk)
	* [https://softwareengineering.stackexchange.com/questions/198520/entity-to-dto-usage](https://softwareengineering.stackexchange.com/questions/198520/entity-to-dto-usage)
	* [https://bulldogjob.com/articles/287-converter-pattern-in-java-8](https://bulldogjob.com/articles/287-converter-pattern-in-java-8)
	* [https://www.javadevjournal.com/spring/data-conversion-spring-rest-api/](https://www.javadevjournal.com/spring/data-conversion-spring-rest-api/)
	* [https://rmannibucau.wordpress.com/2014/04/07/dto-to-domain-converter-with-java-8-and-cdi/](https://rmannibucau.wordpress.com/2014/04/07/dto-to-domain-converter-with-java-8-and-cdi/)
	* [https://www.youtube.com/watch?v=y4RyLdEKhbA&list=WL&index=13&t=13s](https://www.youtube.com/watch?v=y4RyLdEKhbA&amp;list=WL&amp;index=13&amp;t=13s)
* 예제 소스 참고
	* [https://github.com/SeoJinHyuk14/KakaoPay1](https://github.com/SeoJinHyuk14/KakaoPay1)