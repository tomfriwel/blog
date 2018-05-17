---
layout: post
title: 微信小程序群功能开发-后端篇
date: '2018-03-22 18:28:49'
excerpt: >-
    在《微信小程序群功能开发前端篇》中介绍了如何在微信小程序中获取群openGId相关的流程，在这篇文章中我会使用`php`实现之前提到过的相关接口。
comments: true
tag:
    - 微信小程序
    - 后端
---

之前介绍过了如何在微信小程序中获取群openGId相关的流程，在这篇文章中我会使用`php`实现之前提到过的相关接口。解析`encryptedData`和`iv`的代码官方已经给出了`php`、`nodejs`等版本的实现，这篇主要是贴一些相关代码。


![openGId](https://upload-images.jianshu.io/upload_images/2158535-341dcae96ac8bf6e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

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

最后获取`post`传过来的参数，进行调用获取`openGId`：

```php
$code = ... // post 参数
$encryptedData = ... // post 参数
$iv = ... // post  参数

$loginInfo = getInfoWithCode($appid, $appsecret, $code);
$sessionKey = $loginInfo->session_key;
echo getDecodeEncryptedData($sessionKey, $encryptedData, $iv);
```

前端拿到`openGId`后就可以进行绑定相关操作了。

`http_post`函数，是官方某个demo里的，具体是哪里的忘了：

```php
function http_post( $url, $data=null ) {
    $curl = curl_init(); // 启动一个CURL会话
    curl_setopt($curl, CURLOPT_URL, $url); // 要访问的地址
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false); // 对认证证书来源的检查
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false); // 从证书中检查SSL加密算法是否存在
    curl_setopt($curl, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']); // 模拟用户使用的浏览器
    if($data != null){
        curl_setopt($curl, CURLOPT_POST, 1); // 发送一个常规的Post请求
        curl_setopt($curl, CURLOPT_POSTFIELDS, $data); // Post提交的数据包
    }
    curl_setopt($curl, CURLOPT_TIMEOUT, 300); // 设置超时限制防止死循环
    curl_setopt($curl, CURLOPT_HEADER, 0); // 显示返回的Header区域内容
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1); // 获取的信息以文件流的形式返回
    $info = curl_exec($curl); // 执行操作
    curl_close( $curl );
    // var_dump(json_decode($resp, true));
    // echo "<br><br><br><br>";
    return $info;
}
```

其实这些都可以从官方文档里找到，这里只是做一个总结。

因为我用过框架，上面代码是改变过的，没有进行实际测试，但思路就大概是这样的。

如果代码有什么问题可以告知我。

### 参考

- [小程序登录](https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-login.html#wxchecksessionobject)
- [用户数据的签名验证和加解密](https://mp.weixin.qq.com/debug/wxadoc/dev/api/signature.html)

