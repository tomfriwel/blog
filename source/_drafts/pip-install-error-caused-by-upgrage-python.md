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