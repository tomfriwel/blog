---
layout: post
title: PS图片拼接
date: '2018-04-09 15:25:13'
---

最近看到这样一张图片：

{% include image.html url="/assets/images/ps/stitch0.jpg" description="图片拼接实例" width=800 %}

就很想试一下用`PS`来实现类似的效果。

### 分析

图片结构：

- 三张图片
- 中间处于最下层，另外两张处于上层
- 拼接处带有阴影效果
- 拼接处是不规则形状