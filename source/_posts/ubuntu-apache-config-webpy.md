---
title: Python网络框架web.py配置
tags:
  - Ubuntu
  - Apache
  - Python
  - webpy
thumbnail: /blog/2018/08/14/ubuntu-apache-config-webpy/ubuntu-apache-config-webpy-0.png
date: 2018-08-14 17:09:51
---

我服务器系统是Ubuntu，用的是Apache，Apache我已经配置过了，所以不知道如何配置的可以自行搜索相关资料。

我是根据[Webpy + Apache with mod_wsgi on Ubuntu](http://webpy.org/cookbook/mod_wsgi-apache-ubuntu)来安装的。

下面主要看一下我的Apache配置：

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
    </Directory>

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

`line 8` 可以直接访问的静态文件目录, 并且设置`line 19~22`

然后用下面的代码进行初次试探：

```python
import web
# from handle import Handle

web.config.debug = True

class Handle:
    def GET(self):
        return 'Hello tom.'

urls = (
    '/test', 'Handle',
)

application = web.application(urls, globals()).wsgifunc()
```

主要的就是`line 10~12`，相当于路由映射的东西，将`/test`的请求交给`Handle`类来处理。一般情况下是将处理类`Handle`单独建一个`.py`文件，让后通过`line 2`引入。

输入`网址/test`进行访问，比如`test.example.com/test`，不出错就会看到`Handle`类的输出了。

有的时候改动之后可能需要重启一下Apache: `$ service apache2 restart`。

有的时候报错需要到报错日志里查看。`/var/log/apache2/test.example.com.error.log`，从这点来看，不如`PHP`的一些框架（`CodeIgniter`, `Laravel`）那么人性化。
