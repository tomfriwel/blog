---
title: Ubuntu reinstall dpkg and error related with it
date: 2018-07-12 10:18:26
tags:
    - ubuntu
    - server
    - dpkg
    - error
---

```shell
: Sub-process /usr/bin/dpkg returned an error code (1)
```

Check cpu info to find use i386 or amd64:

`$ cat /proc/cpuinfo`


[How to reinstall dpkg](https://askubuntu.com/questions/878887/how-to-reinstall-dpkg)

[How can I unpack a .deb on Mac OS X without installing it?](https://apple.stackexchange.com/questions/867/how-can-i-unpack-a-deb-on-mac-os-x-without-installing-it)


```shell
dpkg: warning: files list file for package `*****' missing, assuming package has no files currently installed
```

[dpkg: warning: files list file for package `*****' missing, assuming package has no files currently installed解决办法](http://www.cnblogs.com/ahauzyy/archive/2013/05/03/3057409.html)

[dpkg: warning: files list file for package 'x' missing](https://serverfault.com/questions/430682/dpkg-warning-files-list-file-for-package-x-missing)

[How To Run the .sh File Shell Script In Linux / UNIX](https://www.cyberciti.biz/faq/run-execute-sh-shell-script/)

[x11-common contains empty filename](https://unix.stackexchange.com/questions/425355/x11-common-contains-empty-filename)
