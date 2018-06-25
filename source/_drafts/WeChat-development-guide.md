---
title: WeChat development guide
tags:
---

没有公众号可以通过下面的链接申请一个测试号进行测试。

[https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)

[微信 JS 接口签名校验工具](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=jsapisign)

调用`wx.config`配置，我打开网页遇到了`config:invalid signature`错误，可能的解决办法：

- 获取`ticket`, 注意`type=jsapi`, 我因为测试卡券写死成了`wx_card` https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=ACCESS_TOKEN&type=jsapi 

- JS安全域名不带协议，即：`http://test.domain.com`, 那么JS安全域名为`test.domain.com`