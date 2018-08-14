---
title: ubuntu apache config webpy
tags:
  - Ubuntu
  - Apache
  - Python
  - webpy
thumbnail: /blog/2018/08/14/ubuntu-apache-config-webpy/ubuntu-apache-config-webpy-0.png
date: 2018-08-14 17:09:51
---


```
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName test.example.com
    DocumentRoot /var/web/test.example.com
    WSGIScriptAlias / /var/web/test.example.com/index.py/

    # the Alias directive
    Alias /static /var/web/test.example.com/static

    AddType text/html .py

    RewriteEngine On
    <Directory /var/web/test.example.com>
        Options +ExecCGI
        # AddHandler cgi-script .py
        # DirectoryIndex index.py
    </Directory>
    # Alias /foo/static/ /path/to/static
    # ScriptAlias /foo/ /path/to/code.py

    # because Alias can be used to reference resources outside docroot, you
    # must reference the directory with an absolute path
    <Directory /var/web/test.example.com/static>
        # directives to effect the static directory
        Options FollowSymLinks
    </Directory>

    # log location
    ErrorLog ${APACHE_LOG_DIR}/test.example.com.error.log
    CustomLog ${APACHE_LOG_DIR}/test.example.com.access.log combined
</VirtualHost>
```
`line 5` 大概意思是凡是进入`test.example.com`的都会经过这里，如`test.example.com/test`, 如`test.example.com/page/123`，并且在`index.py`中做相应的`url`管理。

`line 8` 可以直接访问的目录, 并且设置`line 23~26`