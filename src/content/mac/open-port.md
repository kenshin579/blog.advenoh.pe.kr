---
title: 'List Open Port on Mac'
layout: post
category: 'mac'
author: [Frank Oh]
tags: ["mac", "port", "open", "listen", "nmap"]
image: ../img/cover-mac.jpg
date: '2022-06-05T14:35:21.000Z'
draft: false
---

- 

# lsof

```bash
$ sudo lsof -PiTCP -sTCP:LISTEN
Password:
COMMAND     PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
launchd       1 root   10u  IPv6 0x886ac3be35883d97      0t0  TCP *:49152 (LISTEN)
NWSDaemon   376 root    3u  IPv4 0x886ac3b49c1a489f      0t0  TCP *:21300 (LISTEN)
TaniumCli   589 root   41u  IPv4 0x886ac3b49c19932f      0t0  TCP localhost:17473 (LISTEN)
remotepai   618 root    3u  IPv6 0x886ac3be35883d97      0t0  TCP *:49152 (LISTEN)
ControlCe   629 user   17u  IPv4 0x886ac3b49c1a5dbf      0t0  TCP *:7000 (LISTEN)
ControlCe   629 user   18u  IPv6 0x886ac3be358836b7      0t0  TCP *:7000 (LISTEN)
ControlCe   629 user   19u  IPv4 0x886ac3b49c1a532f      0t0  TCP *:5000 (LISTEN)
ControlCe   629 user   20u  IPv6 0x886ac3be35884477      0t0  TCP *:5000 (LISTEN)
rapportd    641 user    3u  IPv4 0x886ac3b49c1a3e0f      0t0  TCP *:49154 (LISTEN)
rapportd    641 user    4u  IPv6 0x886ac3be35884b57      0t0  TCP *:49154 (LISTEN)
cupsd       838 root    5u  IPv6 0x886ac3be35885237      0t0  TCP localhost:631 (LISTEN)
cupsd       838 root    6u  IPv4 0x886ac3b49c1a337f      0t0  TCP localhost:631 (LISTEN)
Adobe\x20   932 user   12u  IPv4 0x886ac3b49c1a089f      0t0  TCP localhost:15292 (LISTEN)
Adobe\x20   932 user   23u  IPv4 0x886ac3b49c18932f      0t0  TCP localhost:15393 (LISTEN)
Adobe\x20   932 user   30u  IPv4 0x886ac3b49c18684f      0t0  TCP localhost:16494 (LISTEN)
node       1011 user   26u  IPv4 0x886ac3b49c18ddbf      0t0  TCP localhost:49198 (LISTEN)
node       1011 user   27u  IPv4 0x886ac3b49c18e84f      0t0  TCP localhost:49199 (LISTEN)
node       1011 user   30u  IPv4 0x886ac3b49c187e0f      0t0  TCP localhost:45623 (LISTEN)
node       1011 user   31u  IPv4 0x886ac3b49c18889f      0t0  TCP localhost:51289 (LISTEN)
com.docke 14913 user   39u  IPv4 0x886ac3b49dabd32f      0t0  TCP *:50323 (LISTEN)
vpnkit-br 14986 user    8u  IPv4 0x886ac3b49dabd32f      0t0  TCP *:50323 (LISTEN)
```



# nmap

```bash
$ nmap localhost
Starting Nmap 7.92 ( https://nmap.org ) at 2022-06-05 09:15 KST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000049s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 995 closed tcp ports (conn-refused)
PORT      STATE SERVICE
631/tcp   open  ipp
5000/tcp  open  upnp
7000/tcp  open  afs3-fileserver
49152/tcp open  unknown
49154/tcp open  unknown
```



# 참고

- https://www.codegrepper.com/code-examples/shell/mac+check+ports+in+use+terminal
