---
title: 'Telepresence Terminated Ungracefully 오류 해결방법'
layout: post
category: 'cloud'
author: [Frank Oh]
tags: ["telepresence", "kubernetes", "error", "쿠버네티스"]
image: ../img/cover-kubernetes.png
date: '2021-08-03T13:56:20.000Z'
draft: false
---



```bash
$ telepresence connect
INFO[0000] No config found. Using default
Launching Telepresence Root Daemon
Need root privileges to run: /usr/local/bin/telepresence daemon-foreground /Users/user/Library/Logs/telepresence '/Users/user/Library/Application Support/telepresence' ''
Password:
Telepresence Root Daemon quitting... done
telepresence: error: connection error: desc = "transport: error while dialing: dial unix /tmp/telepresence-connector.socket: connect: connection refused"; this usually means that the process has terminated ungracefully
```



```bash
$ rm /tmp/telepresence-connector.socket
```



# 참고

- https://github.com/telepresenceio/telepresence/issues/1723
