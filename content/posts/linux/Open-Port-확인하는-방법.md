---
title: 'Remote 서버에서 Open Port 여부 확인하는 방법'
tags: [linux, command, port, open, nc, nmap, telnet]
social_image: /media/cover/cover-linux.png
date: 2022-07-16
---

새로 배포한 API 서버가 외부 서비스와 통신이 필요한 경우

API 서버 개발하고 사내 서버에 배포하고 나면 

API -> 외부 서비스

- 배포 하고 나서 다른 외부 서비스를 호출할 때 통신이 안되는 경우를 자주 접하게 된다. 사내 서버에 이

다른 서비스간에 통신이 안되는 경우 

대부분 ACL 등록이 안되었거나 아니면 DNS 조회가 안되어서 통신이 안되어서 

Remote 서버에 포트가 오픈되었는지 

# Port 오픈 확인

# 80 오픈되었는지 확인

```bash
$ nc -zv google.com 80
```

- -z : 
- -v :  

# Port scanning

- -z option will tell nc to only scan for open ports, without sending any data to them 
- -v option to provide more verbose information.

nc -zv google.com 20-80

# 참고

- https://blog.naver.com/PostView.naver?blogId=wideeyed&logNo=222122485955&parentCategoryNo=&categoryNo=7&viewDate=&isShowPopularPosts=false&from=postView
- https://linuxize.com/post/netcat-nc-command-with-examples/
- https://linuxize.com/post/check-open-ports-linux/
