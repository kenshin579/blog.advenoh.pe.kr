---
title: "웹 스크래핑하면서 차단 방지하는 방법"
description: "웹 스크래핑하면서 차단 방지하는 방법"
date: 2018-08-13
update: 2018-08-13
tags:
  - scrapping
  - web
  - python
  - robots.txt
  - Tor
  - 스크래핑
  - 웹
  - 파이썬
---

## 1. 소개
스크래핑하면 사이트에 접속하여 데이터를 추출해야 해서 어떻게 작성하느냐에 따라 서버에 많은 부하를 줄 수도 있게 됩니다. 웹 서버를 담당하는 측에서는 서버에 많은 부하를 줄이기 위해 악의적으로? 접속하는 곳을 차단할 수밖에 없습니다. 이번 포스트에서는 웹 스크래핑을 하면서 사이트로부터 차단되지 않는 여러 방법에 대해서 알아보도록 하죠.

* robots.txt 체크하기
* User Agents 설정하기
* 잠시 sleep해서 부하 줄이기
* IP rotation - Tor

## 2. 웹 스크래핑시 차단 되지 않는 여러 방법
### 2.1 robots.txt 체크하기
robots.txt 파일은 웹 크롤러(검색봇)가 크롤링을 할 수 있고 없고 하는 웹 페이지를 정의한 파일입니다. 많은 웹 사이트(ex. [구글](http://www.google.com/robots.txt), [네이버](http://www.naver.com/robots.txt))에서 robots.txt 파일을 정의해두고 있습니다.

```
# Example
User-agent: *
Allow: /
Disallow: /search.php
```

* User-agent : 대상 크롤러 (*: 모든 검색봇, googlebot: 구글봇 등등)
* Allow : 허용하는 경로
* Disallow : 허용하지 않는 경로

robots.txt 파일이 존재한다면, 접근하지 말아야 하는 경로가 무엇인지 미리 파악하여 웹 스크래핑시 해당 경로는 접근하지 않도록 주의를 해야 합니다.

## 2.2 User Agents 설정하기
아래 사이트는 접속하는 브라우져 속성이 웹 서버에 어떻게 보여지는 지 잘 테스트할 수 있는 사이트입니다.

* [http://www.whatismybrowser.com](http://www.whatismybrowser.com/)

제 컴퓨터에서 크롬 브라우져로 위 사이트에 접속을 해보면, 맥 크롬 68 버전임을 알수 있습니다.

![](image_2.png)

웹 사이트에 접속할때 서버로 보내는 HTTP 헤더를 확인해보면 다양한 정보를 담아서 보냅니다. 특히 User-Agent의 정보는 현재 사용하는 브라우져를 알수 있습니다.

![](image_8.png)

urllib 모듈로 사이트에 접속하면 HTTP 헤더 정보에는 python-urllib로 접속했음을 알수 있고 이 정보로 서버 측 담당자들은 쉽게 해당 접속이 일반 사용자가 아님을 판단할 수 있으므로 차단을 할 확률이 높습니다. 되도록이면 웹 스크래핑할 때는 urllib모듈은 사용하지 말고 requests 모듈을 사용하여 헤더 정보를 수정해 보내는게 좋습니다.

![](image_5.png)

아래는 requests 모듈로 header 정보에 크롬 브라우져의 User-Agent를 만들어서 보내는 방법입니다.

```python
import requests

session = requests.Session()
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
"Accept": "text_html,application_xhtml+xml,application_xml;q=0.9,image_webp,**/**;q=0.8"
}
html = session.get(WIKI_URL, headers=headers).content
bsObj = BeautifulSoup(html, "html.parser”)
```

### 2.3 잠시 sleep해서 부하 줄이기
사용자가 실제 사이트에 접속해서 활동하는 것보다 더 빠르게 여러 페이지에 접속하고 온라인 폼을 채워서 스크래핑 한다면 일단 사용자가 아니라는 인식을 주게 되어 차단될 수 있습니다. 또한, 반복문으로 여러 페이지를 로딩하여 처리하거나 멀티 쓰레드 프로그래밍 방식으로 처리하면 서버에 부하를 많이 줄 수 있게 됩니다. 각 페이지에 접속하고 데이터 요청을 하는 건 최소한으로 하는게 좋습니다. 그러기 위해 sleep 문으로 각 페이지에 접속 할때는 조금의 간격을 두고 접속하면 부하를 줄일 수 있습니다.

```python
//사용자가 접속하는 것처럼 램덤 값 사용

rand_value = randint(1, MAX_SLEEP_TIME)
time.sleep(rand_value)
```

### 2.4 IP rotation - Tor
토르(Tor)란 The Onion Router의 약칭 트래픽 분석이나 IP 주소 추적을 불가능케 하는 암호화 라우터 네트워크입니다. 전송되는 데이터는 토르 네트워크를 라우팅할 때 마다 모든 경로에서 암호화가 되어 중간에 패킷을 얻어 풀려고 시도해도 실제 IP 소스 주소를 알아내기란 쉽지 않습니다. 거의 불가능? 하다고 설명하고 있습니다. (책: 파이썬으로 웹 스크래핑)

토르의 실제 동작 원리는 링크(참고 #4.1)를 참고해주세요. 여기서는 실제 어떻게 토르 네트워크안에서 웹 스크래핑을 할 수 있는지 다룹니다.

토르 설치 및 실행 내용은 맥 기반으로 작성 되었습니다. 다른 OS 설치는 아래 링크(참고 #4.5)를 참조하세요.

#### 2.4.1 Tor 설치
```bash
$ brew install tor
$ tor
```

tor 명령어로 토르는 실행할 수 있지만, 네트워크 트래픽은 아직 토르를 통해서 전송되지 않습니다.

#### 2.4.2 Tor 설정 및 실행
모든 시스템 트래픽이 토르를 통해서 라우팅 되려면 시스템의 네트워크 세팅을 변경해줘야 합니다. 사용하는(ex. Wi-Fi, Ethernet) 네트워크마다 세팅을 했다가 기본 네트워크를 사용하려면 다시 세팅을 원복해야 하는 번거로움 있습니다. 네트워크 세팅을 변경해주는 부분을 쉽게 bash 스크립트로 짤 수 있습니다(kremalicious 웹사이트 참고 #4.2).

아래는 tor.sh 스크립트를 실행한 화면입니다.

```bash
$ tor.sh
```

![](image_1.png)

토르 세팅이 잘 되었는지 확인하려면 아래 사이트에 접속하여 확인할 수 있습니다.

* [https://check.torproject.org/](https://check.torproject.org/)
  | 일반 네트워크로 접속 | 토르 네트워크로 접속 |
  | -------------------- | -------------------- |
  |  ![](C16084A1-73EC-4580-83F0-F5D482F30793.png) | ![](AFB09BBA-2A47-4B2F-A6C3-2D4DCE4EC142.png)|


현재 사용 중인 공개 IP 주소와 Tor IP 주소 또한 명령어로 확인할 수 있습니다. 토르 네트워크 확인을 위해서는 torsocks 패키지를 설치해야 합니다.
```bash
$ brew install torsocks
$ torsocks wget -q0- http://icanhazip.com/; echo
```

![](3CA8367A-1885-43C8-AF38-98D920F3CDD5.png)

#### 2.4.3 토르 네트워크에서 웹 스크래핑하기
파이썬에서 토르 네트워크로 웹 스크래핑을 하려면 SOCKS proxy client 모듈이 필요합니다. pip 명령어로 설치합니다.

```bash
$ pip install pysocks
```

```python
#!/usr/bin/env python3
import sys

import requests

def main():
url = "http://icanhazip.com/"
proxies = {
'http': 'socks5://127.0.0.1:9050',
'https': 'socks5://127.0.0.1:9050'
}

response = requests.get(url, proxies=proxies)
print('tor ip: {}'.format(response.text.strip()))

if __name__ == "__main__":
sys.exit(main())
```

torsocks 명령어로 얻은 IP 주소와 위 파이썬 스크립트로 실행한 주소가 같음을 확인할 수 있습니다.

![](F088A986-3EE3-4F16-BE74-4050809E949A.png)

## 3. 웹 스크래핑 작성시 고려사항
### 3.1 코드 작성시 unit test으로 작성하기
스크립트를 작성할때 매번 웹 사이트에 접근하여 코드를 작성해야 합니다. 매번 사이트에 접속하기 보다는 필요한 HTML 부분을 크룸 브라우저에서 복사하여 파일로 저장하고 해당 파일을 unit test로 작성하면 차단될 가능도 적어집니다.

![](image_12.png)

저장된 HTML를 불러오는 코드 부분입니다. 전체 코드는 github에 업로드된 파일을 참조해주세요.

```python
import unittest
import web_scraping as ws

class WebScrapingTest(unittest.TestCase):
FILE_URL = “main_news.html” chrome에서 복사해서

def test_(self):
ws.parse_and_process(open(self.FILE_URL))

if __name__ == '__main__':
unittest.main()
```

## 4. 참고

이 포스트에서 작성된 파일은 [깃허브](https://github.com/kenshin579/tutorials-python/tree/master/web_scraping)에서 확인할 수 있습니다.

* 관련 책
    * [Python Web Scraping](https://www.amazon.com/Scraping-Python-Community-Experience-Distilled/dp/1782164367)
      ![](image_9.jpeg)
    * [Web Scraping with Python](http://www.hanbit.co.kr/store/books/look.php?p_code=B7159663510)
      ![](image_10.jpeg)
* Robots.txt
    * [http://www.robotstxt.org/robotstxt.html](http://www.robotstxt.org/robotstxt.html)
    * [https://www.twinword.co.kr/blog/basic-technical-seo/](https://www.twinword.co.kr/blog/basic-technical-seo/)
    * [http://www.searchengines.co.kr/mkt-bootcamp/7807](http://www.searchengines.co.kr/mkt-bootcamp/7807)
* 웹 스크래핑 차단 방지
    * [https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)
    * [https://hackernoon.com/web-scraping-tutorial-with-python-tips-and-tricks-db070e70e071](https://hackernoon.com/web-scraping-tutorial-with-python-tips-and-tricks-db070e70e071)

* Tor
    * [https://namu.wiki/w/Tor(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)](https://namu.wiki/w/Tor%28%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4%29)
    * [https://kremalicious.com/simple-tor-setup-on-mac-os-x/](https://kremalicious.com/simple-tor-setup-on-mac-os-x/)
    * [http://act.jinbo.net/wp/4449/](http://act.jinbo.net/wp/4449/)
    * [https://gist.github.com/DusanMadar/8d11026b7ce0bce6a67f7dd87b999f6b](https://gist.github.com/DusanMadar/8d11026b7ce0bce6a67f7dd87b999f6b)
    * Tor 윈도우 설치
        * [https://guide.jinbo.net/digital-security/communication-security/how-to-use-tor](https://guide.jinbo.net/digital-security/communication-security/how-to-use-tor)
