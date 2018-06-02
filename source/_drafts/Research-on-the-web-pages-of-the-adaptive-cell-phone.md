---
title: Research on the web pages of the adaptive cell phone
tags:
    - Research
---

手机设计一般以`750px`宽度为标准，微信小程序就是以这样的标准来开发的，引入了一个叫`rpx`的相对单位。

#### 关于`rpx`

rpx（responsive pixel）: 可以根据屏幕宽度进行自适应。规定屏幕宽为750rpx。如在 iPhone6 上，屏幕宽度为375px，共有750个物理像素，则750rpx = 375px = 750物理像素，1rpx = 0.5px = 1物理像素。

| 设备        | rpx换算px (屏幕宽度/750)    |  px换算rpx (750/屏幕宽度)  |
| :-:   | :-:   | :-: |
| iPhone5 | 1rpx = 0.42px | 1px = 2.34rpx |
| iPhone6 | 1rpx = 0.5px | 1px = 2rpx |
| iPhone6 Plus | 1rpx = 0.552px | 1px = 1.81rpx |

所以，在开发网页的时候也可以引入这样的概念。

`1rpx = screenWidth / 750`

`1px = 750 / screenWidth`

在`CSS`中的像素单位就可以用类似于`rpx`的单位来代替。