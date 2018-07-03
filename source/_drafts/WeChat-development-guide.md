---
title: 微信开发指南
tags:
---

#### 目标

做一个有品质的微信开发教程。

没有公众号可以通过下面的链接申请一个测试号进行测试。

[微信公众平台接口测试帐号](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)

[微信 JS 接口签名校验工具](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=jsapisign)

调用`wx.config`配置，我打开网页遇到了`config:invalid signature`错误，可能的解决办法：

- 获取`ticket`, 注意`type=jsapi`, 我因为测试卡券写死成了`wx_card` https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=ACCESS_TOKEN&type=jsapi 

- JS安全域名不带协议，即：`http://test.domain.com`, 那么JS安全域名为`test.domain.com`


[微信卡券JSAPI签名校验工具](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=cardsign)

[微信公众平台接口调试工具](https://mp.weixin.qq.com/debug/)


[PHP开发微信公众号（二）消息接受与推送](https://www.cnblogs.com/myIvan/p/7228888.html)


#### card

[顾客回流其实不难，这家店每天40%营业额来自微信会员卡买单](https://mp.weixin.qq.com/s?__biz=MjM5NDQ5Njk3OA==&mid=412978040&idx=1&sn=308a18ef3970b5c62964b508455fb477#rd)

#### error

[老铁们，小程序wx.addcard报fail no permission何故？](http://html51.com/info-1360-1/)
目前只有认证小程序才能使用卡券接口，可参考指引进行认证。

小程序`wx.openCard`里的`code`是解密后的


#### web

- [51程序](http://html51.com)