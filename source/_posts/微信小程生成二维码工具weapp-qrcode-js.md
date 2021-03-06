---
title: 微信小程生成二维码工具weapp-qrcode.js
date: 2018.01.02 21:07
tags:
    - 微信小程序
    - 开源项目
    - 前端
---

# weapp-qrcode
微信小程序生成二维码工具    

> 生成二维码数据的主要代码来自[davidshimjs/qrcodejs](https://github.com/davidshimjs/qrcodejs)，因为它这个里面生成二维码图片的功能在微信小程序里不能使用，我将这个功能改写成可以在微信小程序中使用。

## 截图

![截图1](http://upload-images.jianshu.io/upload_images/2158535-a571aa52e76c5fd4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/300)
![截图2](http://upload-images.jianshu.io/upload_images/2158535-e83a4b25271ab401.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/300)
![gif](http://upload-images.jianshu.io/upload_images/2158535-1aebcd12a2ff1272.gif?imageMogr2/auto-orient/strip%7CimageView2/2/w/300)

## 使用

页面`js`中引入:
```
var QRCode = require('../../utils/weapp-qrcode.js')
```

页面加载好后:
```
var qrcode = new QRCode('canvas', {
    text: "https://github.com/tomfriwel/weapp-qrcode",
    width: 150,
    height: 150,
    colorDark: "#000000",
    colorLight: "#ffffff",
    correctLevel: QRCode.CorrectLevel.H,
});
```
`text`为需要转化为二维码的字符串；

`width`和`height`为绘制出的二维码长宽，这里设置为跟`canvas`同样的长宽；

`colorDark`和`colorLight`为二维码交替的两种颜色；

`correctLevel`没有细看源码，命名上看应该是准确度；

如果需要再次生成二维码，调用`qrcode.makeCode('text you want convert')`。

## 主要流程

![主流程](http://upload-images.jianshu.io/upload_images/2158535-eb145383b2c50518.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/800)

## 源代码

[tomfriwel/weapp-qrcode](https://github.com/tomfriwel/weapp-qrcode)
