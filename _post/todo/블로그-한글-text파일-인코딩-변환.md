# 블로그 : 한글 text파일 인코딩 변환
가끔씩 소스를 보다보면 editor(ex. webStorm)에서 한글이 깨져서 나오는 파일들이 종종있다. 맥에서 제공하는 iconv 커멘드를 사용해서 인코딩을 변환해보자.

- [ ] iconv이란? 하나의 인코딩에서 다른 인코딩해주는 명령어 있다.
ㅁ. -f : 입력에 대한 인코딩
ㅁ. -t : 출력에 대한 인코딩
>#

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20%ED%95%9C%EA%B8%80%20text%ED%8C%8C%EC%9D%BC%20%EC%9D%B8%EC%BD%94%EB%94%A9%20%EB%B3%80%ED%99%98/image_1.png)

**- 파일을 읽어드리기**

># iconv -f utf8 < A-9.js
iconv: (stdin):1:3: cannot convert <— 오류 발생

**- 오류가 없는 경우에는**
>#

># iconv -f cp949 < A-9.js
 모듈을 추출합니다.
var net = require('net');
var crypto = require('crypto');

변수를 선언합니다.
var guid = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11';

 TCP 서버를 생성합니다.
net.createServer(function (socket) {
socket.on('data', function (data) {
if (_websocket_.test(data.toString())) {

} else if (_HTTP_.test(data.toString())) {

} else {

}
});
}).listen(52273, function () {
console.log('TCP Server Running at 127.0.0.1:52273');
});

># iconv -f cp949 -t utf8 < A-9.js > A-9a.js

Folder 안에 있는 모든 파일을 스캔해서 utf8로 변경하는 script

**참고**
- [ ] [http://markup.su/highlighter/](http://markup.su/highlighter/)
- [ ] [https://medium.com/@goodfeel/mac](https://medium.com/@goodfeel/mac) 에서-text파일-인코딩-변환-aa21de281eb1

#tistory