---
title: pip install error caused by upgrage python
tags:
---

`Ubuntu 14.04.2 LTS`

```shell
Traceback (most recent call last):
  File "/usr/bin/pip", line 5, in <module>
    from pkg_resources import load_entry_point
  File "/usr/lib/python3/dist-packages/pkg_resources.py", line 2749, in <module>
    working_set = WorkingSet._build_master()
  File "/usr/lib/python3/dist-packages/pkg_resources.py", line 444, in _build_master
    ws.require(__requires__)
  File "/usr/lib/python3/dist-packages/pkg_resources.py", line 725, in require
    needed = self.resolve(parse_requirements(requirements))
  File "/usr/lib/python3/dist-packages/pkg_resources.py", line 628, in resolve
    raise DistributionNotFound(req)
pkg_resources.DistributionNotFound: pip==1.5.4
```

[No module named pkg_resources](https://stackoverflow.com/questions/7446187/no-module-named-pkg-resources)

```shell
$ wget https://bootstrap.pypa.io/ez_setup.py -O - | python
$ cd  /usr/local/lib/python3.4/dist-packages/
$ easy_install pip
```

[“pip install unroll”: “python setup.py egg_info” failed with error code 1](https://stackoverflow.com/questions/35991403/pip-install-unroll-python-setup-py-egg-info-failed-with-error-code-1)

[python升级pip报导入错误解决方案](http://www.cnblogs.com/jtlin/p/6510179.html)

```shell
Collecting web.py
  Using cached https://files.pythonhosted.org/packages/fc/58/21649fc1849b1f688f3d42e25e79615cc573469ea57eaa9e6af70b1e3b87/web.py-0.39.tar.gz
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-x7wg98tn/web.py/setup.py", line 6, in <module>
        from web import __version__
      File "/tmp/pip-install-x7wg98tn/web.py/web/__init__.py", line 14, in <module>
        import utils, db, net, wsgi, http, webapi, httpserver, debugerror
    ImportError: No module named 'utils'
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-install-x7wg98tn/web.py/
```
[python安装easyinstall/pip出错](https://blog.csdn.net/i8088/article/details/78484212)

Install required modules.


Down to python2.7

`$ alias python=python2.7`

`web.py` is not support `python3.4.x`

Downgrade `pip`, [How to downgrade the installed version of 'pip' on windows?](https://stackoverflow.com/questions/24773109/how-to-downgrade-the-installed-version-of-pip-on-windows)


[E: Sub-process /usr/bin/dpkg returned an error code (1) 解决方案](http://www.cnblogs.com/eddy-he/archive/2012/06/20/2555918.html)