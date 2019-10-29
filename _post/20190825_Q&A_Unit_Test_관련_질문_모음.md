---
title: 'Q&A : Unit Test 관련 질문 모음'
date: 2018-7-29 14:54:31
category: 'python'
---

개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.

### [Q&A 전체 목록](https://advenoh.tistory.com/35)

### <span style="color:orange">[미 답변 질문]</span>

* assertj에서 extracting 메서드의 역할은 뭔가?
  * 결과가 List<Book> 형태인 경우 book 객체의 필드에 있는 값을 체크할 때 유요함. extracting 메서드를 사용하지 않으면 books.get(0).getName()이런 식으로 item을 가져와서 체크를 해야 한다.

![](Q&A%20%20Unit%20Test%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_1.png)

참고

- [https://joel-costigliola.github.io/assertj/assertj-core-features-highlight.html](https://joel-costigliola.github.io/assertj/assertj-core-features-highlight.html)
- [https://mhaligowski.github.io/blog/2014/09/13/new-extracting.html](https://mhaligowski.github.io/blog/2014/09/13/new-extracting.html)

* Repository에 대한 unit test는 어떻게 작성하나?
  * 지금은 그냥 눈으로 확인하지만 MyBatis의 XML을 수정을 하지 않아서 문제가 되었었음.

![](Q&A%20%20Unit%20Test%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_2.png)

* 테스트 메서드 별로 Parameters로 데이터를 실행할 수 없나?
  * JunitParams을 제공함

참고

- [https://blog.parasoft.com/how-to-create-junit-parameterized-tests-faster](https://blog.parasoft.com/how-to-create-junit-parameterized-tests-faster)

* PowerMock.mockStatic(Calendar.class)으로 한번 사용하면 reset이 안됨

참고

- [https://github.com/powermock/powermock/issues/785](https://github.com/powermock/powermock/issues/785)
- [https://stackoverflow.com/questions/11955270/mocking-behaviour-resets-after-each-test-with-powermock](https://stackoverflow.com/questions/11955270/mocking-behaviour-resets-after-each-test-with-powermock)

---

### <span style="color:orange">[답변완료]</span>

#blog #unit test# #q&a #java #advenoh.pe.kr#
