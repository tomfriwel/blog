---
layout: post
title: 微信小程序群功能开发前端篇
excerpt: >-
    我们在一些微信群中看到过这样的小程序分享卡片：当你点进去后，会看到一个列表，里面有其他群成员的头像和相关信息。比如《王者荣耀群排行》，但是段位信息是腾讯私有的接口，我们只能拿到头像和昵称等基础信息。
comments: true
---

我们在一些微信群中看到过这样的小程序分享卡片：当你点进去后，会看到一个列表，里面有其他群成员的头像和相关信息。比如《王者荣耀群排行》，但是段位信息是腾讯私有的接口，我们只能拿到头像和昵称等基础信息。

下面我将实现小程序端的从转发到用户点击卡片后获取信息的这个过程。

### 开启

首先我们要调用[`wx.showShareMenu`](https://mp.weixin.qq.com/debug/wxagame/dev/document/share/wx.showShareMenu.html?t=2018321)进行设置，来开启是否使用带`shareTicket`的转发，这个`shareTicket`是开发群功能的关键:

```js
wx.showShareMenu({
    withShareTicket: true,
})
```

我一般将其放在页面`onShow`中。

### 触发转发事件

如果要自定义转发按钮而不是有默认右上角的转发按钮，需要在页面中放置一个`open-type="share"`的`button`组件:

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