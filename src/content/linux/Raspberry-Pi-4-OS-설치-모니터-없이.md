---
title: 'Raspberry Pi 4 OS 설치 (모니터 없이)'
layout : post
category: linux
author: [Frank Oh]
image: ../img/cover-raspberry4.jpg
date: '2021-01-16T18:05:23.000Z'
draft: false
tags: ["raspberry", "linux", "pi", "os", "install", "monitor", 라즈베리파이", "설치", "모니터"]

---


# 1. 들어가며

회사에서 좋은 동료로부터 라즈베리파이4를 선물로 얻게 되어 당분가 나의 개인 Toy로 사용할 수 있을 듯하다. 조금 더 적극적으로 사용하기 위해 개인적으로 운용하고 있는 [명언 서비스](https://quote.advenoh.pe.kr/)를 AWS에서 라즈베리파이로 옮길 계획이다. 

자, 라즈베리파이4에 OS를 설치하는 방법에 대해서 알아보자. 모니터로 연결해서 설치할 수 있도 있지만, 모니터 없이도 간단하게 OS를 설치할 수 있다. 필요한 도구는 다음과 같다

- 라즈베리파이4
- SD card
- SD card 리더기
- 전원 케이블 (5V, 3000mA)
  - 개인적으로 USB-C 케이블를 사용해서 구동하고 있음

# 2.라즈베리파이 OS 설치

## 2.1 SD card에 라즈베리파이 PI OS 설치하기

OS 설치는 아래 순서대로 진행하면 된다. 맥을 사용하고 있어 맥 기준으로 설명한다.

1. Raspberry Pi image 다운로드 및 설치
2. SD card format
3. SD card에 OS 쓰기

먼저 [라즈베리파이 PI 사이트](https://www.raspberrypi.org/software/)에 접속하여 Raspberry Pi Imager를 다운로드한다. 다운로드한 파일 더블클릭 하고 App 파일을 선택하여 Applications 폴더로 옮겨 파일을 복사하면 설치가 완료가 된다. 

![image1](images/Raspberry-Pi-4-OS-설치-모니터-없이/image1.png)

Spotlight로 Raspberry Pi를 검색하여 Application을 구동시킨다. 

![Screenshot of Raspberry Pi Imager](images/Raspberry-Pi-4-OS-설치-모니터-없이/md-82e922d180736055661b2b9df176700c.png)

다음은 SD card를 포멧시키기 위해 SD card 리더기에 SD card를 넣고 컴퓨터에 연결시킨다. 그리고 Raspberry Pi Imager에서 

- Storage > 삽입된 SD card를 선택
- Operation System > Choose OS > Erase를 선택

하여 포멧을 시킨다. 

포멧이 완료되면 아래와 같이 옵션 선택이후 WRITE 버턴을 클릭하면 OS 이미지는 인터넷으로 자동 다운로되고 SD card에 쓰여지게 된다. 쓰기 완료 시점은 SD card의 사양에 따라서 다를 수 있다. 

- Operating System > Raspberry PI OS Full (32-BIT) 선택
- Storage > 삽입된 SD card를 선택

![image4](images/Raspberry-Pi-4-OS-설치-모니터-없이/image4-4020439.png)

## 2.2 로컬 환경에서 라즈베리파이에 접근하기



### 2.2.1 ssh로 접근하기

- Ssh empty 파일 생성
- wifi 설정 파일 생성하기 (wpa_supplicant.conf)

```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
    ssid="wifi-name"
    psk="password"
    scan_ssid=1
}
```

새로 할당 받은 IP 주소 확인하기

OS 쓰기가 완료되면 SD card 리더기에서 분리하여 라브베리파이 보드에서 rpi에 넣고 전원 케이블를 연결하여 구동시킨다. 

### 2.2.2 Remote Desktop으로 접근하기

- vnc viewer
- xrdp

# 3. 기타 설정

## 3.1 암호 변경하기








# 4. 참고

- https://www.raspberrypi.org/software/
- https://roboticsbackend.com/install-ubuntu-on-raspberry-pi-without-monitor/
- https://linuxhint.com/install_raspberry_pi_os_without_external_monitor/
- https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html







