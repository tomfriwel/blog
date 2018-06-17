---
title: ubuntu apache python mysql setup
tags:
---

#### Version
```
$ cat /etc/issue
> Ubuntu 14.04.2 LTS \n \l
```

#### Setup

[How To Set Up an Apache, MySQL, and Python (LAMP) Server Without Frameworks on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-apache-mysql-and-python-lamp-server-without-frameworks-on-ubuntu-14-04)

```
$ sudo rm /usr/bin/python
$ sudo ln -s /usr/bin/python3 /usr/bin/python
$ sudo a2dismod mpm_event
```
```
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = "en_US:",
	LC_ALL = (unset),
	LC_CTYPE = "UTF-8",
	LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
Module mpm_event already disabled
```

Get rid of this warning:

[How to set locale?](https://askubuntu.com/a/17002)
[Cannot set LC_CTYPE to default locale: No such file or directory](https://askubuntu.com/a/749780)

```
$ sudo apt-get install language-pack-en-base
$ sudo dpkg-reconfigure locales
$ export LC_ALL="en_US.UTF-8"
```

Setup Apache conf:

```
<VirtualHost *:80>
    <Directory /var/www/test>
        Options +ExecCGI
        DirectoryIndex index.py
    </Directory>
    AddHandler cgi-script .py

    ...
```

index.py:
```python
#!/usr/bin/python

print('Content-type:text/html\r\n')
print('hello')

```

```
$ sudo chmod 755 /var/www/test/index.py
$ sudo service apache2 restart
```

