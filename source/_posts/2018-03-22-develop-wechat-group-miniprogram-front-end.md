---
layout: post
title: 微信小程序群功能开发-前端篇
date: '2018-03-22 16:28:49'
excerpt: >-
    我们在一些微信群中看到过这样的小程序分享卡片：当你点进去后，会看到一个列表，里面有其他群成员的头像和相关信息。比如《王者荣耀群排行》，但是段位信息是腾讯私有的接口，我们只能拿到头像和昵称等基础信息。
comments: true
tag:
    - 微信小程序
---

我们在一些微信群中看到过这样的小程序分享卡片：当你点进去后，会看到一个列表，里面有其他群成员的头像和相关信息。比如《王者荣耀群排行》，但是段位信息是腾讯私有的接口，我们只能拿到头像和昵称等基础信息。

下面我将实现小程序端的从转发到用户点击卡片后获取信息的这个过程。

![openGId](https://upload-images.jianshu.io/upload_images/2158535-341dcae96ac8bf6e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 开启

首先我们要调用[`wx.showShareMenu`](https://mp.weixin.qq.com/debug/wxagame/dev/document/share/wx.showShareMenu.html?t=2018321)进行设置，来开启是否使用带`shareTicket`的转发，这个`shareTicket`是开发群功能的关键:

```js
wx.showShareMenu({
    withShareTicket: true,
})
```

我一般将其放在页面`onShow`中。

### 触发转发事件

如果要自定义转发按钮而不是有默认右上角的转发按钮，需要在页面中放置一个`open-type="share"`的[`button`](https://mp.weixin.qq.com/debug/wxadoc/dev/component/button.html)组件:

```html
<button open-type="share">share</button>
```

接下来在页面中设置分享函数[`onShareAppMessage`](https://mp.weixin.qq.com/debug/wxagame/dev/document/share/GroupMsgInfo.md?t=2018321):

```js
onShareAppMessage: function (res) {
    if (res.from === 'button') {
        // 来自页面内转发按钮
        console.log(res.target)
    }
    return {
        title: '自定义转发标题',
        path: '/pages/test/test?id=123',
        success: function (res) {
            // 转发成功
            console.log(res)
            // 只有转发到群聊中打开才可以获取到 shareTickets 返回值，单聊没有 shareTickets
            if (res.shareTickets && res.shareTickets.length>0) {
                app.getShareInfo(res.shareTickets[0])
            }
        },
        fail: function (res) {
            // 转发失败
            console.log(res)
        }
    }
}
```

现在就可以进行转发了，在群聊中将会看到此次分享的小程序消息卡片。每个`shareTicket`对应每个群并且单聊不会有该值。这里只选择一个转发，所以直接取第一个。至于`app.getShareInfo`是用来获取群id(`openGId`)的函数，我们放到后面介绍。

### 群成员点消息卡片

当群成员点消息卡片进入小程序后，在`app.js`的`onShow`/`onLaunch`的`options`中可以获取到`shareTicket`，`shareTicket`每次都是不一样的，比分你分享的时候获取到的跟这里获取到的不是同一个，但是会对应同一个`openGId`。

***app.js***:

```js
// 在onShow中获取转发信息shareTicket
onShow: function (options) {
    console.log(options)
    let scene = options.scene

    // 场景值是1044，带 shareTicket 的小程序消息卡片
    if(scene == 1044) {
        let shareTicket = options.shareTicket
        // 这里的id根据自己的具体需求进行操作，也可以设置其他的
        let id = options.query.id
        this.getShareInfo(shareTicket)
    }
},

// 获取加密信息encryptedData, iv
getShareInfo: function (shareTicket) {
    const z = this
    wx.getShareInfo({
        shareTicket: shareTicket,
        success: function (res) {
            console.log(res)
            let {encryptedData, iv} = res

            if(encryptedData && iv) {
                z.getDecodeEncryptedData(encryptedData, iv)
            }
        },
        fail: function (res) {
            console.log(res)
        }
    })
},

// 获取解密后的信息
getDecodeEncryptedData: function (encryptedData, iv) {
    // 发送到后台解析
    wx.login({
        success: function(res) {
            let code = res.code

            // 下面只是演示代码
            // post({
            //     url:'https://www.example.com/controller/getDecodeEncryptedData'
            //     data:{
            //         code,
            //         encryptedData,
            //         iv,
            //     }
            // })
        }
    })
},
```

首先，我们通过[`wx.getShareInfo`](https://mp.weixin.qq.com/debug/wxadoc/dev/api/share.html#wxgetshareinfoobject)获取`encryptedData`和`iv`，然后将其传给后台进行解析。

在`getDecodeEncryptedData`中，当后台解析成功后，就会返回一个`openGId`。

此时就可以将群`openGId`与用户`openid`进行绑定了，这个绑定信息也是要保存到后台的。如果后台没有保存过头像昵称信息，此时也可以将用户头像和昵称一起保存到后台。

类似于下面这样的一个接口:
```js
// 下面只是演示代码
post({
    url:'https://www.example.com/controller/bindGroupAndUser'
    data:{
        code,
        openGId
    }
})
```

其中的`code`调用[`wx.login`](https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-login.html#wxloginobject)获得，后台根据这个`code`能获取到`openid`。然后进行绑定。

然后根据自己的需求，可能还要一个保存用户基础信息和拉取群成员信息列表的接口。

基本思路就是这样，我将在另一篇文章中描述后端的相关处理。

### 参考

- [小程序开发文档-转发](https://mp.weixin.qq.com/debug/wxadoc/dev/api/share.html)
- [小程序登录](https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-login.html#wxchecksessionobject)
- [用户数据的签名验证和加解密](https://mp.weixin.qq.com/debug/wxadoc/dev/api/signature.html)