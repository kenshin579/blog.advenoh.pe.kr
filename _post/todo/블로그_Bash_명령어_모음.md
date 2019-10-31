# 블로그 : Bash 명령어 모음
] $ : centos

># : ubuntu

**# memory slot usage**

sudo dmidecode --type memory

**# Turn off monitor without turning off computers**

xset dpms force off

 # No password prompt for sudo

 # 1. Add myself to the sudo group

sudo vi _etc_group

 # 2. Edit _etc_sudoers

sudo vi _etc_sudoers

 # Members of the admin group may gain root privileges

%admin ALL=(ALL) ALL

%sudo ALL=NOPASSWD: ALL <------- Add this

**# Stat on file**

[ohf@ubuntu:~$ ] stat test.c

**# Get filesystem information (ext2, ext3)**

[ohf@ubuntu:~$ ] dumpe2fs _dev_sda1

[ohf@ubuntu:~$ ] tune2fs _dev_sda1

 # Determine _dev_path for different drives (ext. cdrom, hdd)

[ohf@ubuntu:~$ ] sudo lshw -C disk

 # Adding new hard drive and partitioning them (2 methods)

 # 1. GUI (gaprted) - EASIEST METHOD

[ohf@ubuntu:~$ ] sudo apt-get install gparted

 # 2. command line (DONT KNOW HOW TO DO THIS YET)

 # Write Image to USB key

[ohf@ubuntu:~$ ] sudo dd if =_path_to_your_download.img of=_dev_device_you_saw_in_dmesg bs=1024

**# List open processes**

[ohf@ubuntu:~$ ] lsof

**# VMware mount virtual disk**

[ohf@ubuntu:~$ ] sudo vmware-mount Home _mnt_vdk

**# How to change timezone**

[ohf@ubuntu:~$ ] sudo dpkg-reconfigure tzdata

**# Watch changeable data continuously**

[ohf@ubuntu:~$ ] watch -n1 "cat _proc_interrupts"

 # See how long a command takes

[[ohf@ubuntu:~$ ] time command

 # Change file timestamp (YYMMDDhhmm)

[ohf@ubuntu:~$ ] touch -c -t 0304050607 file

 # Show process hierarchy

[ohf@ubuntu:~$ ] pstree -p

 # Go to previous directory

[ohf@ubuntu:~$ ] cd -

 # Create cdrom image from directory

[ohf@ubuntu:~$ ] mkiosofs -r dir | gzip > cdrom.iso.gz

 # Make archive of dir in tar.bz2 format

[ohf@ubuntu:~$ ] tar c dir | bzip2 > dir.tar.bz2

 # disk 확인
># cat _proc_scsi/scsi
># sudo fdisk -l
># lsblk -io KNAME,TYPE,SIZE,MODEL

* bash 

 # Use a Different Color for the Root Shell Prompt

 # root account : red color

vi _root_.bashrc

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

 # regular account: green color

vi ~/.bashrc

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

#

#Apt-related aliases

#

alias gimme="sudo apt-get install" #Install new software

alias acs="apt-cache search" #Search available packages

alias purge="apt-get --purge remove" #Removes package and its config files

alias update="sudo apt-get update"

alias debclean="sudo apt-get clean &amp;&amp; sudo apt-get autoremove" #Removes some unneeded files

#

#Misc useful aliases

#

alias ls="ls --color=auto" #Plain ls with color

alias ll="ls -l --color=auto" #Detailed list with color

alias config="dpkg-reconfigure" #Re-run the configuration step for a package

alias cmi="./configure &amp;&amp; make &amp;&amp; sudo make install" #Common steps to install package from source

alias numfiles="echo $(ls -1 | wc -l)" #Count the number of files in current directory

alias free="df -h" #See how much hard drive space is free in easy-to-read format

alias favdir="cd _directory_you_use_a/lot" #Quickly switch to a directory you often need (music, documents, etc)

*

* Find && Grep 

 # Make archive of *.png in dir

[ohf@ubuntu:~$ ] find dir -name "*.png" | xargs -d "\n" tar rf dir.tar; bzip2 dir.tar

 # Search *.c and *.h for "search string" in this dir and below

[ohf@ubuntu:~$ ] find -name "**.[ch]**" | xargs -d "\n" grep -E "search string"

 # run context search on files (w/ filename)

[ohf@ubuntu:~$ ] find . -name "*.[chS]" -exec grep --with-filename -n 'idle' {} \;

*

* dpkg 

 # Querying ..

dpkg-query --list ntp\*

 # List all installed pkg

dpkg -l

 # List of files of the pkg

dpkg -L dpkg

 # Search??

dpkg -S _usr_bin/dpkg

 # Lists the contents of package.deb

dpkg -c package.deb

 # Download the source Debian package for package and extract it

apt-get source [-b] package

 # Download and install the package necessary to build the source

apt-get build-dep package

 # Fix those pkgs that failed

dpkg --configure --pending

*

 # Replace strings 2 with strings 2 in file

[ohf@ubnut:~$ ] sed 's_string1_string2/g' file

 # Convert dos text file to unix

[ohf@ubnut:~$ ] tr -d '\r' < file

 # See what programs have which ports are open

[ohf@ubnut:~$ ] netstat -nape --inet

 # Kill any processes using the sound card

[ohf@ubnut:~$ ] fuser -k _dev_dsp

 # Untar and copy to a folder

[ohf@ubnut:~$ ] tar xzvf test.tar.gz -C _usr_local_src_test

===========================================================================================

C O L L E C T I O N O F H O W T O

===========================================================================================

 # -----------------------------------------------------------------------------------------

 # Install Xen & Guest OS

 # -----------------------------------------------------------------------------------------

 # References

 # - https://help.ubuntu.com/community/Xen

 # 1. Install Xen

[ohf@ubnut:~$ ] sudo apt-get install ubuntu-xen-server

 # #########################################################################################

 # -----------------------------------------------------------------------------------------

 # Networking Configuration Using Command Line

 # -----------------------------------------------------------------------------------------

 # DHCP Setup

vi _etc_network/interfaces

 # The primary network interface - use DHCP to find our address

#auto eth0

#iface eth0 inet dhcp

 # Static IP address

vi _etc_network/interfaces

 # The primary network interface (static)

auto eth0

iface eth0 inet static

address 192.168.3.90

gateway 192.168.3.1

netmask 255.255.255.0

network 192.168.3.0

broadcast 192.168.3.255

 # Setting your ubuntu stytem hostname (_etc_hostname)

sudo _bin_hostname newname

 # Setting DNS server

vi _etc_resolv.conf

nameserver 129.254.15.15

 # #########################################################################################

 # -----------------------------------------------------------------------------------------

 # How to install Ubunut Linux from USB Stick

 # -----------------------------------------------------------------------------------------

1. How to install Ubuntu Linux from USB stick,

http://www.ubuntugeek.com/how-to-install-ubuntu-linux-from-usb-stick.html

 # Prerequisites

A running Ubuntu systems (any versions)

 # #########################################################################################

-----------------------------------------------------------------------------------------

 # About defragmentation on ext3 on linux system

 # -----------------------------------------------------------------------------------------

 # NOTE: for the moment, there aren' tnay developed tools to defragment ext2 or ext3 file

 # system, but there are some linux tools and user scripts to get more defragmentation

 # To see the degree of fragmentation

[ohf@ubuntu:~$ ] LANG=C dumpe2fs _dev_sda1 | eval_dumpe2fs.pl

 # The degree of fragmentation of partition

[ohf@ubuntu:~$ ] ._ext2_frag /dev_sda5 -s

 # The degree of fragmentation of file/directory

[ohf@ubuntu:~$ ] ./fragments -d -x /

[ohf@ubuntu:~$ ] filefrag -v filename

 # Measureing fragmentation of ext3 in linux system

[ohf@ubuntu:~$ ] ./fibmap.pl /usr

 # #########################################################################################

-----------------------------------------------------------------------------------------

 # Howto Access via ssh a Virtualbox Guest machine.

 # -----------------------------------------------------------------------------------------

 # Goal: to make any packet arriving at a given TCP port (i.e. 2222) of the Host machine, to be

 # forwarded to the TCP port 22 of the Guest Machine.

 # References

 # 1. Howto Access via ssh a Virtualbox Guest machine, http://mydebian.blogdns.org/?p=148

[ohf@ubuntu:~$ ] VBoxManage setextradata CentOS "VBoxInternal_Devices_pcnet_0_LUN#0/Config_ssh_HostPort" 2222

[ohf@ubuntu:~$ ] VBoxManage setextradata CentOS "VBoxInternal_Devices_pcnet_0_LUN#0/Config_ssh_GuestPort" 22

[ohf@ubuntu:~$ ] VBoxManage setextradata CentOS "VBoxInternal_Devices_pcnet_0_LUN#0/Config_ssh_Protocol" TCP

[ohf@ubuntu:~$ ] ssh -l root -p 2222 localhost

 # Trouble-shooting

 # To list settings

[ohf@ubuntu:~$ ] VBoxManage getextradata CentOS enumerate

 # To Remove the setting

[ohf@ubuntu:~$ ] VBoxManage setextradata CentOS "VBoxInternal_Devices_pcnet_0_LUN#0/Config_ssh_GuestPort"

 # #########################################################################################

-----------------------------------------------------------------------------------------

 # Installing and Configuring NTP on linux

 # -----------------------------------------------------------------------------------------

[ohf@ubuntu:~$ ] sudo apt-get install ntp

 # Make sure the timezone is set to correctly

[ohf@ubuntu:~$ ] sudo dpkg-reconfigure tzdata

 # Modify the server

 # add server ntp.ubuntulinux.org

[ohf@ubuntu:~$ ] sudo vi _etc_ntp.conf

 # Add the run-level startup

[ohf@ubuntu:~$ ] sudo update-rc.d ntpdate defaults 90

 # Manually setting time

[ohf@ubuntu:~$ ] rdate -s time.bora.net

[ohf@ubuntu:~$ ] sudo ntpdate ntp.ubuntulinux.org

 # Setting hardware clock to updated time...

[ohf@ubuntu:~$ ] sudo hwclock --systohc

 # Trouble-shooting

 # Testing whether
[ohf@ubuntu:~$ ] ntpq -p

#Ubuntu #centos