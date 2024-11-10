---
title: "Q&A Mybatis 관련 질문 모음"
description: "Q&A Mybatis 관련 질문 모음"
date: 2018-07-29
update: 2018-07-29
tags:
  - Q&A
  - faq
  - mybatis
  - db
  - mysql
  - sql
  - database
  - legacy
---

개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.

## Q&A 전체 목록


### <span style="color:orange">[답변완료]</span>

### <span style="color:brown">1. \_long 타입은 뭔가?</span>
![](image_3.png)

- \_long : long 타입으로 매핑된다
- long : Long 타입이 매핑된다



참고
* [http://www.mybatis.org/mybatis-3/ko/configuration.html](http://www.mybatis.org/mybatis-3/ko/configuration.html)

### <span style="color:brown">2. IN (…)안에 list을 넘겨서 처리하는 방법은?</span>

IN에 들어갈 (…) 값을 <foreach> 태그로 값을 생성할 수 있습니다.

![](image_2.png)

참고

* [http://pcdate.blogspot.com/2013/05/mybatis-foreach.html](http://pcdate.blogspot.com/2013/05/mybatis-foreach.html)



### <span style="color:brown">3. association columnPrefix 중첩으로 사용할 때 매핑아 인되는 이슈?</span>

association을 중첩으로 columnPrefix로 매핑하는 경우에는 prefix가 중첩으로 append 되기 때문에 v_r_file_nm 형식으로 작성을 해야 합니다.

**Mybatis Mapper 파일**

```xml
<resultMap id="vodCollectionInfo" type="domain.entity.VodCollection" >
  <result column="vod_collection_seqno" property="vodCollectionNo"/>
  <result column="collection_title" property="collectionTitle"/>
  <association property="vodInfo" resultMap="vodInfo" columnPrefix="v_"/>
</resultMap>

<resultMap id="vodInfo" type="domain.entity.MediaVod" >
  <result column="vod_seqno" property="vodNo"/>
  <result column="vod_title" property="vodTitle"/>
  <association property="resourceInfo" resultMap="mediaResource" columnPrefix="r_"/>
</resultMap>

<resultMap id="mediaResourceMap" type="domain.entity.resource.MediaResource">
  <result column="resource_seqno" property="resourceSeqno"/>
  <result column="file_nm" property="fileName"/>
  <result column="file_size" property="fileSize" javaType="Integer"/>
</resultMap>
```

```xml
<select id="selectAllVodsByVodCollectionWithPaging" parameterType="domain.dto.VodCollectionPageMeta" resultMap="Common.vodCollectionInfo">
        SELECT vc.vod_collection_seqno,
               vc.collection_title,
               v.vod_seqno AS v_vod_seqno,
               v.vod_title AS v_vod_title,
               rv.original_file_nm AS v_r_original_file_nm,
               rv.file_nm AS v_r_file_nm,
               rv.width AS v_r_width,
               rv.height AS v_r_height
        FROM media_vod_collection AS vc
                 INNER JOIN media_vod_collection_mapping AS vcm
                            ON vcm.vod_collection_seqno = vc.vod_collection_seqno
                 INNER JOIN media_vod AS v
                            ON v.vod_seqno = vcm.vod_seqno
                 LEFT JOIN media_resource AS rv
                           ON rv.resource_seqno = v.resource_seqno
        WHERE vc.vod_collection_seqno = #{vodCollectionNo}
    </select>
```



참고

- https://androphil.tistory.com/733?category=423961

----

### <span style="color:orange">[미 답변 질문]</span>

#### - mybatis에서 @Transactional 어노테이션을 사용해서 unit test을 사용할 수 있나?
- 잘 안됨

참고
* [http://barunmo.blogspot.com/2013/06/mybatis.html](http://barunmo.blogspot.com/2013/06/mybatis.html)
* [https://otamot.com/64](https://otamot.com/64)
* [https://wedul.site/133](https://wedul.site/133)
* [https://examples.javacodegeeks.com/enterprise-java/spring/write-transactional-unit-tests-spring/](https://examples.javacodegeeks.com/enterprise-java/spring/write-transactional-unit-tests-spring/)
* [https://mycup.tistory.com/185](https://mycup.tistory.com/185)

#### - mybatis에서 association 속성은 뭔가?
- resultMap에 다른 객체가 있는 경우에 사용하고 assocation은 has one 타입의 관계를 다룬다.
- collection인 경우에는 has many 타입의 관계를 다룰 떄 사용한다.
  ![](image_1.png)

참고
* [http://noveloper.github.io/blog/spring/2015/05/31/mybatis-assocation-collection.html](http://noveloper.github.io/blog/spring/2015/05/31/mybatis-assocation-collection.html)

#### - mybatis에서 namespace를 위한 alias에 대해 지원을 하나?
- 하지 않음

참고
* [https://github.com/mybatis/mybatis-3/issues/1160](https://github.com/mybatis/mybatis-3/issues/1160)

#### - mybatis에서 cdata를 자주 보게 되는데, 사용하는 이유는?

![](image_4.png)

참고

* [https://epthffh.tistory.com/entry/Mybatis-%EC%97%90%EC%84%9C-CDATA-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0](https://epthffh.tistory.com/entry/Mybatis-%EC%97%90%EC%84%9C-CDATA-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
