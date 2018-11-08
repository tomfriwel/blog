---
title: 微信公众号开发之上传图片（附AccessToken获取和处理）
date: 2018-11-08 11:28:33
tags:
    - 微信小程序
    - 前端
---

最近看卡券功能的时候，创建卡券的时候涉及到上传图片的操作，但官方文档里面描述似乎有一点问题，在这里做一个记录。`AccessToken`的获取和处理放后面。

开发语言用的是`PHP 7.0`，使用`CodeIgniter`框架。

[官方文档：上传卡券图片素材](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1451025056)

#### 上传图片

请求地址说明：
```
HTTP请求方式: POST/FROMURL:https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=ACCESS_TOKEN
```

文档里参数是`buffer`和`access_token`，但实际测试下来是不行的，后来网上搜索和查看素材管理相关信息后，发现需要参数为`media`、`access_token`和`type`。

代码如下：

```php
// access_token和type参数
$params = [];

// getAccessToken获取access_token的函数，如何获取查看官方文档
$params['access_token'] = $this->getAccessToken();
$params['type'] = "image";
$url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg";

// 拼接后为 url?access_token=xxx&type=image
$url = $url.'?'.http_build_query($params);

// 相对于网站的图片的绝对路径
$filename = "/path/sample.png";

// 图片在服务器上的真是路径，如果是前端上传的，可以另行获取，这里使用的是网站上的图片作为测试
$real_path = $_SERVER['DOCUMENT_ROOT'].$filename;

// 图片data
$file_data = array("media"=> new \CURLFile($real_path));

// 发送请求
$res = $this->post($url, $file_data, false);
var_dump($res);
```

如果不出错最后返回的信息为：
```
array(1) {
  ["url"]=>
  string(125) "xxxxx"
}
```


post函数：
```php
private function post($url, $data = [], $json_encode=true) {
    $curl = curl_init(); // 启动一个CURL会话
    curl_setopt($curl, CURLOPT_URL, $url); // 要访问的地址
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false); // 对认证证书来源的检查
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false); // 从证书中检查SSL加密算法是否存在
    curl_setopt($curl, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']); // 模拟用户使用的浏览器
    if ($data != null) {
        curl_setopt($curl, CURLOPT_POST, 1); // 发送一个常规的Post请求
        // curl_setopt($curl, CURLOPT_POSTFIELDS, $data); // Post提交的数据包
        if(gettype($data)==="string") {
            curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
        }
        else {
            if ($json_encode) {
                curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data, JSON_UNESCAPED_UNICODE));
            } else {
                curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
            }
        }
    }
    curl_setopt($curl, CURLOPT_TIMEOUT, 300); // 设置超时限制防止死循环
    curl_setopt($curl, CURLOPT_HEADER, 0); // 显示返回的Header区域内容
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1); // 获取的信息以文件流的形式返回
    $res = curl_exec($curl); // 执行操作
    curl_close($curl);

    $data = json_decode($res, true);
    if($data==NULL) {
        return $res;
    }
    else {
        return $data;
    }
}
```

`json_encode`为`false`的话，就不会进行`json_encode`。比如上面上传图片传入的是一个`CURLFile`，如果`json_encode`就会上传失败。


#### `AccessToken`的获取和处理

[官方文档：获取access_token](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140183)

官方文档中建议建立一个刷新机制，不要每次使用`access_token`的时候都去重新获取，详情请仔细阅读官方文档。

请求地址说明：
```
https请求方式: GET
https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
```
参数为`grant_type`、`appid`和`secret`，具体信息可查看官方文档。

代码：
设置`cache`和相关信息：
```php
public function __construct() {
    parent::__construct();
    
    $this->load->driver(
        'cache',
        array('adapter' => 'apc', 'backup' => 'file', 'key_prefix' => 'wechat_')
    );

    // 公众号appid 和 appsecrect
    $this->appid = 'xxx';
    $this->secret = 'xxx';
}
```

获取accessToken：
```php
private function getAccessToken() {
    $appid = $this->appid;
    $secret = $this->secret;

    // 设置cache key，这里是 wechat_[appid]_access_token，保存成功可以到/webpath/application/cache查看
    // 如果想用其他方式保存也可以做相应更改
    $key = $this->appid.'_access_token';

    // 如果cache中没有accessToken或者已过期，重新获取或刷新
    if (!$accessToken = $this->cache->get($key)) {
        $url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={$appid}&secret={$secret}";

        $res = $this->post($url);

        $accessToken = $res['access_token'];

        // 保存accessToken
        $this->cache->save($key, $accessToken, $res['expires_in']);
    }

    return $accessToken;
}
```
