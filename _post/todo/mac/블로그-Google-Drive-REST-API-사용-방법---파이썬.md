# 블로그 : Google Drive REST API 사용 방법 - 파이썬
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
- [ ] script로 google drive 에서 파일 오픈하기
- [ ] subfolder으로 처리가 안되는 듯함.
ㅁ. query로 검색해서 처리하는 걸로 이해했음

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Language : Python3
* Source code : github

- [ ] enable the drive api
ㅁ. credentials.json을 다운로드함

google client library를 설치함
># pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

1. Google Drive API 권한을 받아야 함
[https://console.developers.google.com/flows/enableapi?apiid=drive](https://console.developers.google.com/flows/enableapi?apiid=drive)

3. 사용법

oauth2client 모듈 못찾는 경우
># pip3 install --upgrade oauth2client

[https://stackoverflow.com/questions/44011776/how-to-prevent-importerror-no-module-named-oauth2client-client-on-google-app](https://stackoverflow.com/questions/44011776/how-to-prevent-importerror-no-module-named-oauth2client-client-on-google-app)

4. 참고

* Quickstart
	* [https://developers.google.com/drive/api/v3/quickstart/python](https://developers.google.com/drive/api/v3/quickstart/python)
* Upload file example
	* [https://blog.psangwoo.com/coding/2017/07/10/google_drive_api.html](https://blog.psangwoo.com/coding/2017/07/10/google_drive_api.html)

># pip install --upgrade google-api-python-client

2.
[https://developers.google.com/drive/api/v3/quickstart/python](https://developers.google.com/drive/api/v3/quickstart/python)

참고
[https://developers.google.com/drive/api/v3/quickstart/python](https://developers.google.com/drive/api/v3/quickstart/python)
파일 업로드해보기, [https://blog.psangwoo.com/coding/2017/07/10/google_drive_api.html](https://blog.psangwoo.com/coding/2017/07/10/google_drive_api.html)
[https://help.talend.com/reader/Ovc10QFckCdvYbzxTECexA/EoAKa_oFqZFXH0aE0wNbHQ](https://help.talend.com/reader/Ovc10QFckCdvYbzxTECexA/EoAKa_oFqZFXH0aE0wNbHQ)
[https://stackoverflow.com/questions/45442459/how-to-configure-google-drive-python-api](https://stackoverflow.com/questions/45442459/how-to-configure-google-drive-python-api)

[https://tanaikech.github.io/2017/05/02/ocr-using-google-drive-api/](https://tanaikech.github.io/2017/05/02/ocr-using-google-drive-api/)
[https://tanaikech.github.io/2017/05/01/converting-pdf-to-txt/](https://tanaikech.github.io/2017/05/01/converting-pdf-to-txt/)

[https://pancake.coffee/jekyll/google-drive-file-export-python/](https://pancake.coffee/jekyll/google-drive-file-export-python/)
[https://www.quora.com/How-do-I-upload-a-file-to-Google-Drive-using-Python](https://www.quora.com/How-do-I-upload-a-file-to-Google-Drive-using-Python)
[https://brunch.co.kr/@jayden-factory/6](https://brunch.co.kr/@jayden-factory/6)

#tistory #blog #스터디중