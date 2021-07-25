---
title: 'ARM 기반 플랫폼(라즈베리파이 4)에서 쿠버네티스 실행할 수 있는 도커 빌드하기 (go app)'
layout : post
category: linux
author: [Frank Oh]
image: ../img/cover-rasberrypi-kubernetes.png
date: '2021-07-24T18:05:23.000Z'
draft: false
tags: ["raspberry", "linux", "docker", "build", "arm", "kubernetes", "image", "raspbian", "go", "golang", "라즈베리파이", "라즈비안", "도커", "이미지", "쿠버네티스", "고랭"]

---



도커 크로스 빌드에 대한 언급이 필요함

Go 프로그램 작성

- 실행

```go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Printf("Hello from %s architecture\n", runtime.GOARCH)
}

```



docker file 생성

도커 빌드 및 push


```dockerfile
FROM golang:alpine AS build
ADD . /buildspace
WORKDIR /buildspace
RUN go build -o helloworld ./...

FROM alpine
WORKDIR /app
COPY --from=build /buildspace/helloworld /app
CMD [ "/app/helloworld" ]

```



```makefile
REGISTRY 	  := kenshin579
APP    		  := rasberrypi
TAG         := go-multi-arch-hello
IMAGE       := $(REGISTRY)/$(APP):$(TAG)

.PHONY: docker-push
docker-push:
	@docker buildx build \
	--platform linux/amd64,linux/arm64,linux/arm/v7,linux/arm/v6 \
	-t $(IMAGE) --push -f Dockerfile .

```



```bash
$ docker login
$ make docker-push
```

도커 실행

- 맥에서 
- 라즈베리파이에서








# 참고

- https://www.starkandwayne.com/blog/building-docker-images-for-kubernetes-on-arm/

- https://collabnix.com/building-arm-based-docker-images-on-docker-desktop-made-possible-using-buildx/

- https://cereme.dev/devops/docker-buildx-for-arm-device/

- https://meetup.toast.com/posts/255

  
