# Q&A : ReactJS 관련 질문 모음
ReactJS

개인적으로 모르는 부분 적어두고 알게 되는 부분에 대해서 간단하게 정리해둔 자료입니다.
미 답변중에 알고 계신 부분 있으면 코멘트 달아주세요. 감사합니다.

[Q&A 전체 목록](https://advenoh.tistory.com/35)

[미 답변 질문]

-

- - - -

[답변완료]

1. axios.then 부분에서 계속 error catch block으로 실행되는 이슈
this.setState가 undefined이여서 그러했음

![](Q&A%20%20ReactJS%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_1.png)

ㅁ. 해결책 :

![](Q&A%20%20ReactJS%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_2.png)

참고
* [https://github.com/goatslacker/alt/issues/283](https://github.com/goatslacker/alt/issues/283)

2. 서버에서는 성공/오류에 대해서 응답에 message을 담아서 client에 전송하는데, axios에서 응답 값을 어떻게 출력할 수 있나?

![](Q&A%20%20ReactJS%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_3.png)

ㅁ. 해결책 : 메시지는 error.request.response에 있지만, string값이기 때문에 dot 접근자로 접근하려면 JSON.parse를 해서 객체로 인식하도록 변경을 해야 함

![](Q&A%20%20ReactJS%20%EA%B4%80%EB%A0%A8%20%EC%A7%88%EB%AC%B8%20%EB%AA%A8%EC%9D%8C/image_4.png)

#advenoh.pe.kr#