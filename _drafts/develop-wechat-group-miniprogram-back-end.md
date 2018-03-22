---
layout: post
title: 微信小程序群功能开发前端篇
excerpt: >-
    我们在一些微信群中看到过这样的小程序分享卡片：当你点进去后，会看到一个列表，里面有其他群成员的头像和相关信息。比如《王者荣耀群排行》，但是段位信息是腾讯私有的接口，我们只能拿到头像和昵称等基础信息。
comments: true
---

之前介绍过了如何在微信小程序中获取

下面我将实现小程序端的从转发到用户点击卡片后获取信息的这个过程。

{% include image.html outurl="https://upload-images.jianshu.io/upload_images/2158535-341dcae96ac8bf6e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" description="openGId" width=800 %}


```