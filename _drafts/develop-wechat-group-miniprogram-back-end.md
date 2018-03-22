---
layout: post
title: 微信小程序群功能开发后端篇
excerpt: >-
    在《微信小程序群功能开发前端篇》中介绍了如何在微信小程序中获取群openGId相关的流程，在这篇文章中我会使用`php`实现之前提到过的相关接口。
comments: true
---

之前介绍过了如何在微信小程序中获取群openGId相关的流程，在这篇文章中我会使用`php`实现之前提到过的相关接口。解析`encryptedData`和`iv`的代码官方已经给出了`php`、`nodejs`等版本的实现，这篇主要是贴一些相关代码。

{% include image.html outurl="https://upload-images.jianshu.io/upload_images/2158535-341dcae96ac8bf6e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" description="openGId" width=800 %}

### 准备

下载官方实例：https://mp.weixin.qq.com/debug/wxadoc/dev/demo/aes-sample.zip

在自己的代码中引入并设置相关常数：
```php
require_once('wxBizDataCrypt.php');

$appid= '...';  //小程序 AppID
$appsecret= '...';  //小程序 AppSecret

```

### 获取登录信息

根据微信小程序中通过`wx.login`得到的`code`获取用户对小程序的唯一标识`openid`和`session_key`，`session_key`时会过期的。

当然，满足一定条件还会的到`unionid`，具体可以查看官方文档。[UnionID机制说明](https://mp.weixin.qq.com/debug/wxadoc/dev/api/uinionID.html)

```php
function getInfoWithCode($appid, $appsecret, $code) {
    $url = "https://api.weixin.qq.com/sns/jscode2session?appid=".$appid."&secret=".$appsecret."&js_code=".$code."&grant_type=authorization_code";
    $reData = http_post($url, array());

    $obj = json_decode($reData);

    return $obj;
}
```

### 解析加密信息

下面函数是根据官方示例改成的：

```php
function getDecodeEncryptedData($sessionKey, $encryptedData, $iv) {
    $pc = new WXBizDataCrypt($appid, $sessionKey);
    $errCode = $pc->decryptData($encryptedData, $iv, $data );

    if ($errCode == 0) {
        return $data;
    } else {
        return $errCode;
    }
}
```

`http_post`函数：

最后获取`post`传过来的参数，进行调用：

```php

```

### 参考

* [小程序登录](https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-login.html#wxchecksessionobject)
* [用户数据的签名验证和加解密](https://mp.weixin.qq.com/debug/wxadoc/dev/api/signature.html)

```