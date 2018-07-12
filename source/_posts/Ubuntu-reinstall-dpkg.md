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


```shell
Preparing to unpack .../dpkg_1.17.5ubuntu5.8_amd64.deb ...
/usr/bin/dpkg: symbol lookup error: /usr/bin/dpkg: undefined symbol: setexecfilecon
dpkg: error processing archive /var/cache/apt/archives/dpkg_1.17.5ubuntu5.8_amd64.deb (--unpack):
 subprocess new pre-installation script returned error exit status 127
/usr/bin/dpkg: symbol lookup error: /usr/bin/dpkg: undefined symbol: setexecfilecon
dpkg: error while cleaning up:
 subprocess new post-removal script returned error exit status 127
Errors were encountered while processing:
 /var/cache/apt/archives/dpkg_1.17.5ubuntu5.8_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

[How to resolve “dpkg: error processing /var/cache/apt/archives/python-apport_2.0.1-0ubuntu9_all.deb”?](https://askubuntu.com/a/148389/707430)

#### repair
```
/var/cache/apt/archives
/var/lib/dpkg/info
```

`$ dpkg --configure -a`

```shell
dpkg: error processing package python-pkg-resources (--configure):
 package is in a very bad inconsistent state; you should
 reinstall it before attempting configuration
Errors were encountered while processing:
 python-pkg-resources
```

`$ dpkg -l | grep python`

`$ cd /var/cache/apt/archives/`

[dpkg](https://help.ubuntu.com/lts/serverguide/dpkg.html)
[How to repair apt-get command?](https://askubuntu.com/questions/33949/how-to-repair-apt-get-command)
[Problem installing any new packages in Ubuntu because of python](https://askubuntu.com/questions/534040/problem-installing-any-new-packages-in-ubuntu-because-of-python)
[How to resolve “dpkg: error processing /var/cache/apt/archives/python-apport_2.0.1-0ubuntu9_all.deb”?](https://askubuntu.com/questions/148383/how-to-resolve-dpkg-error-processing-var-cache-apt-archives-python-apport-2-0)

[FIXING THE DREADED “ERRORS WERE ENCOUNTERED WHILE PROCESSING” ERRORS](https://journalxtra.com/linux/fixing-the-dreaded-errors-were-encountered-while-processing-errors/)