---
title: "도커라이즈 파이썬 어플리케이션 (Dockernize Python Application)"
description: "도커라이즈 파이썬 어플리케이션 (Dockernize Python Application)"
date: 2022-06-05
update: 2022-06-05
tags:
  - python
  - docker
  - dockernize
  - 도커
  - 파이썬
  - 도커라이즈
---

## 1.Dockernize Python Application

파이썬 어플리케이션을 도커 이미지로 생성하는 방법에 대해서 알아보자. 도 커 라이 저하는 과정은 개발언어와 상관없이 비슷한 과정을 통해서 도커 이미지를 만든다. 아래는 `Hello World`를 화면에 출력하는 파이썬 코드이다. 이 코드로 도커 이미지를 만들어보자.

```python
#!/usr/bin/env python3

print('Hello World')
```



### 1.1 Dockerfile 생성하기

도커는 `Dockerfile` 파일을 읽어 작성된 명령어를 실행하여 이미지를 만들 수 있다.

```dockerfile
FROM python:3.8-slim-buster
WORKDIR /root
ADD main.py .
CMD ["python3, main.py"]

```

- `FROM` : 베이스 이미지로 사용할 도커 이미지를 지정
- `WORKDIR` : 컨테이너 작업 디렉토리 지정
- `ADD` : 이미지 생성시 파일 추가
- CMD : 컨테이너 시작할 때 실행할 명령어 지정

파이썬 베이스 이미는 아래 3가지를 사용할 수 있다. 각각의 차이점은 다음과 같다.

- `python:3.9-buster`  대부분의 필요한 패키지가 설치된 버전
- `python:3.9-slim-buster` : 표준 라이브러리를 제외하고 전부 제외된 버전
- `python:3.9-alpine` : BusyBox Linux + apk 패키지 관리자가 포함된 버전

`alpine` 베이스 이미지는 `lightweight`한 버전으로 여러 개발 언어로도 제공하여 많이 사용하는 베이스 이미지이다. 간단한 파이썬의 경우에는 `alpine` 이미지를 사용해도 무방하지만, application에서 사용하는 libray에 따라서 alpine에서는 기존 적으로 `linux wheel`을 지원하지 않아 별도 빌드가 필요할 수 있다고 한다. 이런 빌드 과정을 거치지 않고 바로 도커나이즈하려면 `buster`나 `slim-buster`를 베이스 이미지로 선택하기를 추천한다.

#### 참고

- https://nayoungs.tistory.com/m/entry/Docker-Python-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%A5%BC-%EC%8B%A4%ED%96%89%ED%95%98%EB%8A%94-Docker-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%B9%8C%EB%93%9C%ED%95%98%EA%B8%B0
- https://pythonspeed.com/articles/alpine-docker-python/
- https://jx2lee.github.io/cloud-base-image-with-python/



#### Docker 이미지 빌드하기

개인 맥북이 `M1` 버전이라 `platform` 옵션을 추가하여 빌드한다.

```makefile
REGISTRY 	:= kenshin579
APP    		:= advenoh
TAG         := python-hello
IMAGE       := $(REGISTRY)/$(APP):$(TAG)
PLATFORM	:= linux/x86-64

.PHONY: docker-build
docker-build:
	@docker build --platform $(PLATFORM) -t $(IMAGE) -f Dockerfile .

.PHONY: docker-push
docker-push: docker-build
	@docker push $(IMAGE)
```

매번 빌드하기 쉽게 `Makefile`을 위와 같이 작성하고 `make`을 하거나 버로 도커 허브에 이미지를 업로드라고 싶은 경오 `docker-push` 옵션으로 실행한다.
```bash
$ make docker-build
$ make docker-push
```

### 1.2 Docker Image 실행하기

`docker run`으로 Hello World를 찍어보자.

```bash
$ docker run --platform linux/x86-64 kenshin579/advenoh:python-hello
Hello World
```

## 2. Flask Web Application

컨솔 창에서 출력하는 버전외에 웹 어플레이션도 도커나이즈해보자. 서버 구동후 8080 포트로 접속하면 "Flask inside Docker!!"를 출력하는 파이쎤 코드이다.

```python
#!/usr/bin/env python3

from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

```



#### Dockerfile 작성하기

```dockerfile
FROM python:3.8-slim-buster
COPY ../../../src/content/python /app
WORKDIR /app
RUN pip3 install -r requirements.txt

CMD ["python3, app/app.py"]
```



빌드한 도커 이미지를 로컬환경에서 실행하고 8080 포트로 접속하면 잘 실행되는 것을 확인할 수 있다.

```bash
$ make docker-push

$ docker run --rm --platform linux/x86-64 -p 8080:8080 kenshin579/advenoh:python-web-hello
* Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8080
 * Running on http://172.17.0.2:8080 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 878-906-556
```


#### 웹 화면

![](image-20220625175829408.png)

## 3. 참고

- https://runnable.com/docker/python/dockerize-your-python-application
- https://luis-sena.medium.com/creating-the-perfect-python-dockerfile-51bdec41f1c8
- https://blog.logrocket.com/build-deploy-flask-app-using-docker/
