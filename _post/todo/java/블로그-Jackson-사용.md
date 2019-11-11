# 블로그 : Jackson 사용
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] jackons에서 serialize와 deselize에 대해서 알아보자
- [ ] @JsonSerialize(converter = LocalDateTimeToStringConverter.class)
- [ ] @JsonDeserialize(using = CustomDateTimeDeserializer.class)

- [ ] writeValueAsString해서 datetime을 출력하면 아래처럼 됨
ㅁ.
{"time":{"hour":20,"minute":49,"second":42,"nano":99000000,"dayOfYear":19,"dayOfWeek":"THURSDAY","month":"JANUARY","dayOfMonth":19,"year":2017,"monthValue":1,"chronology":{"id":"ISO","calendarType":"iso8601"}}}

[https://stackoverflow.com/questions/41749539/how-to-serialize-localdatetime-with-jackson](https://stackoverflow.com/questions/41749539/how-to-serialize-localdatetime-with-jackson)

-- map을 json string으로 프린트하려면-
new ObjectMapper().writeAsString(map);

1. 들어가며

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Jackson%20%EC%82%AC%EC%9A%A9/image_1.png)

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

4. 참고

* Jackson
	* [https://thepracticaldeveloper.com/2018/07/31/java-and-json-jackson-serialization-with-objectmapper/](https://thepracticaldeveloper.com/2018/07/31/java-and-json-jackson-serialization-with-objectmapper/)
	* [https://www.logicbig.com/tutorials/misc/jackson/json-serialize-deserialize-converter.html](https://www.logicbig.com/tutorials/misc/jackson/json-serialize-deserialize-converter.html)
	* [https://stackoverflow.com/questions/3269459/how-to-serialize-joda-datetime-with-jackson-json-processer](https://stackoverflow.com/questions/3269459/how-to-serialize-joda-datetime-with-jackson-json-processer)
	* [https://www.baeldung.com/jackson-serialize-dates](https://www.baeldung.com/jackson-serialize-dates)
	* [https://www.lesstif.com/pages/viewpage.action?pageId=24445204](https://www.lesstif.com/pages/viewpage.action?pageId=24445204)
	* [https://touk.pl/blog/2016/02/12/formatting-java-time-with-spring-boot-using-json/](https://touk.pl/blog/2016/02/12/formatting-java-time-with-spring-boot-using-json/)
	* [https://stackoverflow.com/questions/29571587/deserializing-localdatetime-with-jackson-jsr310-module](https://stackoverflow.com/questions/29571587/deserializing-localdatetime-with-jackson-jsr310-module)