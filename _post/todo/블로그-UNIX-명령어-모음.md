# 블로그 : UNIX 명령어 모음
* ubuntu : [ohf@ubuntu:~$ ]
* centos : [ohf@centos ~]$
* mac : >#

1.Mac
**# image resolution 줄이기**
># sips -Z 1024 *.JPG --out ~_Desktop_scaleddown/

**# kill used port**
kill ` lsof -i -P | grep 1099 | awk '{print $2}’ `

kill ` lsof -t -i :8080 `

**# create usb stick (ubuntu) on mac**
[http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx)

**# tmux windows attach 다시 하는 방법**
># tmux ls
service: 4 windows (created Mon Mar 23 09:49:13 2015) [152x28] (attached)
weboffice: 5 windows (created Mon Mar 23 09:56:28 2015) [152x28] (attached)

># tmux attach -t service

**# clientA.js title만 뽑기**
># grep title clientA.js | sed -e 's_"g' | sed -e 's_title: g'| cat -n > object.txt

**# empty line와 ## comment 제외한 line 보기**
># egrep -v '^#.*' redis-cluster1.conf | egrep -v '^$’

**# whereis**
># mdfind .workflow | grep -i total

**# countdown clock**
># MIN=1 && for i in $(seq $(($MIN*60)) -1 1); do echo -n "$i, "; sleep 1; done; echo -e "\n\nBOOOM! Time to start.”

># MIN=1 && for i in $(seq $(($MIN*60)) -1 1); do printf "\r%02d:%02d:%02d" $((i/3600)) $(( (i/60)%60)) $((i%60)); sleep 1; done

- [ ] [http://www.commandlinefu.com/commands/view/5886/countdown-clock](http://www.commandlinefu.com/commands/view/5886/countdown-clock)

2.Ubuntu
**# convert CR/LF (Windows) -> LF (Unix)**
[ohf@ubuntu:~$ ] sed 's_.$_/' file

**#remove**
[ohf@ubuntu:~$ ] find . -type f | grep class | xargs rm -f
[ohf@ubuntu:~$ ] find . -name *.class -exec rm -f {} \;
[ohf@ubuntu:~$ ] find . -type d -name .svn -exec ls -ld {} \;
[ohf@ubuntu:~$ ] find | grep car | xargs rm -f

[ohf@ubuntu:~$ ] find . -type f -name '**_Conflict**' -exec ls -l {} \;

**# find all empty files**
[ohf@ubuntu:~$ ] find . -type f -empty | xargs ls -l
[ohf@ubuntu:~$ ] find . -type f -empty -delete

**# find all modified files since #30 days ago**
[ohf@ubuntu:~$ ] find . -mtime -30

**# process grep해서 kill 하는 방법**
[ohf@ubuntu:~$ ] sudo jps | grep -i office | cut -d" " -f1 | awk '{ if ($4 != "COMMAND" && $4 != "sh" && $4 != "ps") system("sudo kill "$1) }’

**# http directory에서 directory에 있는 파일 다 다운로드 받기**
wget --no-parent -r [http://dev.thinkfree.com/build/TFO/7.0/TFO-7-0-140422-weboffice/0001.392/release/package/](http://dev.thinkfree.com/build/TFO/7.0/TFO-7-0-140422-weboffice/0001.392/release/package/)

**# largest files 찾기**
find . -type f -printf '%s %p\n'|sort -nr|head

**# largest files 찾기 - human readable format**
find . -type f -size +5M -exec du -h '{}' + | sort -hr | head

**# 사용중인 largest directory 찾기**
du -hsx * | sort -rh | head -10

**# Centos 7**
**# cron daemon 설치 및 실행**
#1.cronie package 설치되어 있는지 확인
sudo yum install cronie

#2. 실행중인지 체크
sudo systemctl status crond.service

#3.restart
sudo systemctl restart crond.service

[https://www.rosehosting.com/blog/automate-system-tasks-using-cron-on-centos-7/](https://www.rosehosting.com/blog/automate-system-tasks-using-cron-on-centos-7/)

**# log 파일 삭제하지 않고 trim하는 방법**

># echo _dev_null > apache-tomcat-7.0.69/logs/catalina.out
># echo “” > apache-tomcat-7.0.69/logs/catalina.out

3.Centos
**#check whether the machine is running under any virtualization**
which virtualization the machine is running

[ohf@centos ~]$ virt-what

4.VIM
**# search multiple words in vim**
/fail\|sshd

#unix #linux