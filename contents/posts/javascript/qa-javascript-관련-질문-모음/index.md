---
title: "Q&A JavaScript 관련 질문 모음"
description: "Q&A JavaScript 관련 질문 모음"
date: 2018-03-23
update: 2018-03-23
tags:
  - Q&A
  - faq
  - javascript
  - defaultProps
  - es6
---

개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.

## Q&A 전체 목록

### <span style="color:orange">[답변완료]</span>

### <span style="color:brown">1. `This is a ${msg}` 이건 뭔가?

ES6체 추가된 새로운 문자열 표기법으로 템플릿 리터럴(Template Literal)이라고 합니다.
템플릿 리터럴은 \ 문자 사용없이 문자열에서 줄바꿈도 허용하고 간단하게 \${…} 문자열 인터폴레이션 표현식을 통해서 변수의 값 바로 치환되어 쉽게 사용할 수 있습니다.

![](/media/javascript/QA-JavaScript-관련-질문-모음/image_3.png)

참고

- [https://poiemaweb.com/es6-template-literals](https://poiemaweb.com/es6-template-literals)
- [https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Template_literals](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Template_literals)

### <span style="color:brown">2. var와 const, let의 차이점은?

const와 let의 키워드는 ES6에 도입된 키워드입니다.

- var \* scope가 함수 단위로 동작한다
  ![](/media/javascript/QA-JavaScript-관련-질문-모음/image_5.png)

- const
    - scope가 블록 단위이다
    - 값이 바뀌지 않는 때 사용한다
      ![](/media/javascript/QA-JavaScript-관련-질문-모음/image_4.png)

- let
    - scope가 블록 단위이다
    - 값이 변경될 때 사용한다

참고

- [https://velopert.com/3626](https://velopert.com/3626)

### <span style="color:brown">3. 람다식으로 표현된 () => ({})의 의미는 뭔가?

ES6에서 람다식 문법이 추가되었습니다. () => ({}) 표현식은 function() { return { } }와 동일합니다.

![](/media/javascript/QA-JavaScript-관련-질문-모음/image_7.png)

참고

- [http://hacks.mozilla.or.kr/2015/09/es6-in-depth-arrow-functions/](http://hacks.mozilla.or.kr/2015/09/es6-in-depth-arrow-functions/)

### <span style="color:brown">4. …은 뭔가?

![](/media/javascript/QA-JavaScript-관련-질문-모음/7387AE5C-6B59-4AD8-8546-AA42E65E9734.png)

ES6에 추가된 문법으로 Spread나 Rest Parameter로 사용할 수 있습니다.

- Spread operator
    - iterable가능한 배열, 객체, 스트링에 대해서 단일 요소들로 확장해준다
    - ex.
      ![](/media/javascript/QA-JavaScript-관련-질문-모음/image_6.png)
      ![](/media/javascript/QA-JavaScript-관련-질문-모음/image_1.png)

- Rest Parameter
    - 모든 요소를 배열로 만들어준다
    - Rest Parameter는 맨 마지막 인자여야 한다
      ![](/media/javascript/QA-JavaScript-관련-질문-모음/image_2.png)

참고

- [https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/rest_parameters](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [https://scotch.io/bar-talk/javascripts-three-dots-spread-vs-rest-operators543](https://scotch.io/bar-talk/javascripts-three-dots-spread-vs-rest-operators543)
- [https://jaeyeophan.github.io/2017/04/18/ES6-4-Spread-Rest-parameter/](https://jaeyeophan.github.io/2017/04/18/ES6-4-Spread-Rest-parameter/)

---

### <span style="color:orange">[미 답변 질문]</span>

#### - defaultProps은 언제 사용되나?

