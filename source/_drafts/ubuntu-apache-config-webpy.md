---
title: ubuntu apache config webpy
tags:
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