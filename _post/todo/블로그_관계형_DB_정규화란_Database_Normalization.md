# 블로그 : 관계형 DB 정규화란 (Database Normalization)
* 정규화란
	* 정규화란
* 이상현상
* 함수 종속
* 정규형
	* 제1정규형
	* 제2정규형
	* 제3정규형
	* 보이스/코드 정규형
	* 제4정규형
	* 제5정규형
* 참고

1. DB 정규화란 (Database Normalization)

관계형 데이터베이스에서 설계가 잘못되면 데이터 중복으로 인해 …

데이터 중복을 최소화하는 게

데이터 중복을 최소화하는 데 목적을 두고 있습ㄴ

똑같은 데이터가 여러개 존재하는 데이터 중복성을 허용하지 않는다. 데이터가 중복되면

이런 현상을 제거하면서 데이터베이스를 올바르게 설계해 나가는 과정을 정규화라고 함.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_39.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_21.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_26.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_11.png)

**01 정규화의 개념과 이상 현상**
- [ ] 정규화는 데이터베이스를 설계한 후 설계 결과물을 검증하기 위해 사용하기도 한다.
ㅁ. 데이터베이스를 잘못 설계하면 불필요한 데이터 중복이 발생하여 릴레이션에 대한 데이터의 삽입, 수정, 삭제 연산을 수행할때 부작용이 발생함
ㅁ. 올바르게 설계해 나가는 과정이 정규화

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_16.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_27.png)

1.2.1 삽입 이상
- [ ] 새 데이터를 삽입하기 위해 원치 않는 불필요한 데이터도 함께 삽입해야 하는 문제를 삽입이상이라고 함.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_7.png)

**1.2.2 갱신 이상**
- [ ] 릴레이션의 중복된 투플들 중 일부만 수정하여 데이터가 불일치하게 되는 모순이 발생하는 것을 갱신 이상이라고 함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_1.png)

**1.2.3 삭제 이상**
- [ ] 릴레이션에서 투플을 삭제하면 꼭 필요한 데이터까지 함께 삭제하여 데이터가 손실되는 연쇄 삭제 현상을 삭제이상이라고 함
ㅁ. 김용욱 고객의 다른 정보도 없어지게 됨. - 삭제시 이벤트 참여를 취소를 해서.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_30.png)

- [ ] 정규화를 수행하려면 먼저 릴레이션을 구성하는 속성들간의 관련성을 판단할 수 있어야 함
ㅁ. 함수적 종속성
- [ ] 릴레이션에 함수적 종속성이 하나 존재하면 정규화를 통해 릴레이션을 분해함

1.1 이상 현상(Anomaly)

2. 함수 종속

**02 함수 종속 FD (Functional Dependency)**
- [ ] 릴레이션내의 모든 투플을 대상으로 한 X 값에 대한 Y값이 항상 하나면 X가 Y를 함수적으로 결정한다

다른 정의

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_23.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_5.png)

1 을 선택하면 항상 RAM이 나옴

근데, RAM을 선택하면 항상 phone#가 같지 않음.

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_32.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_18.png)

- [ ] 함수 종속 관계를 판단할때 유의할 점은, 현재 시점에 릴레이션에 포함된 속성 값만으로 판단하면 안됨
ㅁ. 릴레이션에서 속성값은 계속 변할 수 있기 때문에 속성 자체가 가지고 있는 특성과 의미를 기반으로 판단해야 함 <— ???

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_35.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_19.png)

* 완전 함수 종속 (FFD: Full Functional Dependency)
	* 속성 집합 Y가 속성 집합 X에 함수적으로 종속되어 있지만, 속성 집합 X의 전체가 아닌 일부분에는 종속되어 있지 않음
	* 당첨여부 속성이 {고객아이디, 이벤트 번호} 속성 집합에 완전 함수 종속되어 있음
* 부분 함수 종속 (PFD: Partial Functional Dependency)
	* 속성 집합 Y가 속성 집합 X의 전체가 아닌 일부분에도 함수적으로 종속됨
	* 결정자가 여러개 의 속성들로 구성되어 있음
	* 고객이름!!

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_3.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_13.png)

3. 정규형 (

03 기본 정규형과 정규화 과정

**3.1 정규화의 개념과 종류**

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_8.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_15.png)

3.1 제1정규형 (1NF : First Normal Form)
3.2 제2정규형
3.3 제3정규형
3.4 보이스/코드 정규형
3.5 제4정규형 / 제5정규형

4. 참고

* 정규화
	* [https://yaboong.github.io/database/2018/03/09/database-normalization-1/](https://yaboong.github.io/database/2018/03/09/database-normalization-1/)
	* [https://ko.wikipedia.org/wiki/데이터베이스_정규화](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4_%EC%A0%95%EA%B7%9C%ED%99%94)
	* [http://blog.naver.com/PostView.nhn?blogId=force44&logNo=130100972038](http://blog.naver.com/PostView.nhn?blogId=force44&amp;logNo=130100972038)
	* [http://raisonde.tistory.com/entry/데이터베이스-정규화Normalization](http://raisonde.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%A0%95%EA%B7%9C%ED%99%94Normalization)
	* [https://support.microsoft.com/ko-kr/help/283878/description-of-the-database-normalization-basics](https://support.microsoft.com/ko-kr/help/283878/description-of-the-database-normalization-basics)
	* [http://beansberries.tistory.com/entry/데이터-종속성과-정규화](http://beansberries.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A2%85%EC%86%8D%EC%84%B1%EA%B3%BC-%EC%A0%95%EA%B7%9C%ED%99%94)

- - - -

Chap9 - 정규화

3.2 제1정규형 (1NF: First Normal Form)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_28.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_33.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_17.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_34.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_24.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_41.png)

**3.3 제2정규형 (2NF: Second Normal Form)**
- [ ] 제2정규형을 만족하려면, 부분 함수 종속을 제거하고 모든 속성이 기본키에 완전 종속되도록 릴레이션을 분해하는 정규화 과정을 거쳐야 함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_31.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_36.png)

- [ ] 정규화과정에서 릴레이션을 분해할때 주의할점은, 분해된 릴레이션들을 **자연 조인하여** 분해전의 릴레이션으로 다시 복원할 수 있어야 한다

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_2.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_9.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_38.png)

**3.4 제3정규형 (3NF: Third Normal Form)**
-

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_22.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_4.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_14.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_37.png)

**3.5 보이스_코드 정규형 (BCNF: Boyce_Codd Normal Form)**
- [ ] 제3규형까지 모두 만족하더라도 이상 현상이 발생할 수 있음
ㅁ. 후보키를 여러개 가지고 있는 릴레이션에 발생할 수 있음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_25.png)

- [ ] 담당강사번호 속성이 후보키가 아님에도 인터넷강좌 속성을 결정하므로 강좌 신청 릴레이션은 보이스/코드 정규형에 속하지 않음

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_6.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_29.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_12.png)

- [ ] 여러 이상 현상이 발생하는 이유
ㅁ. 후보키가 아니면서 함수 종속 관계에서 다른 속성을 결정하는 담당강사번호 속성이 존재하기 때문이다.
ㅁ. 모든 결정가가 후보키가 될 수 있도록 강좌선청 릴레이션을 두개로 분해야 햐함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_40.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_20.png)

**3.6 제4정규형과 제5정규형**
* 제4정규형 (MVD : MultiValued Dependency): 함수 종속이 아닌 다치 종속을 제거해야 만족함
* 제5정규형 (JD: Join Dependency) : 후보키를 통하지 않는 조인 종속을 제거해야 만족함
- [ ] 모든 릴레이션이 무조건 제5정규형에 속하도록 분해야 하는 건 아님
ㅁ. 분해하면 비효율적이고 바람직하지 않은 경우도 있음
- [ ] 제3정규형이나 보이스/코드 정규형에 속하도록 릴레이션을 분해하여 데이터 중복을 줄이고 이상현상이 발생하는 문제를 해결함

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%EA%B4%80%EA%B3%84%ED%98%95%20DB%20%EC%A0%95%EA%B7%9C%ED%99%94%EB%9E%80%20(Database%20Normalization)/image_10.png)

#tistory #blog #스터디중