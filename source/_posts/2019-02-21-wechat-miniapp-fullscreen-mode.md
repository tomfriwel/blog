---
title: 微信小程序全屏模式（自定义导航栏）
date: 2019-02-21 16:59:53
thumbnail: /blog/2019/02/21/2019-02-21-wechat-miniapp-fullscreen-mode/2.png
tags:
    - 微信小程序
---

要自定义导航栏，首先需要在`app.json`里设置：
```json
{
"window": {
        "navigationStyle": "custom"
    }
}
```

设置之后进入小程序就只剩下右上角的胶囊了。

在设置导航栏样式时需要知道它的高度，在`app.json`的`onLaunch`里获取状态栏高度：

```js
App({
    onLaunch: function(options) {
        wx.getSystemInfo({
            success: (res) => {
                this.globalData.statusBarHeight = res.statusBarHeight
                this.globalData.navBarHeight = 44 + res.statusBarHeight
            }
        })
    },
    globalData: {
        statusBarHeight: 0,
        screenHeight: 0
    }
})
```

`44`是导航栏除去状态栏的高度，单位`px`。

因为导航栏每个页面都会用到，所以我们用组件会方便使用一些，这里创建一个叫`nav`的组件：

首先在组件`js`里设置`statusBarHeight`和一个可以通过外部设置状态栏颜色的`backgroundColor`的属性，默认透明。

***nav.js***:
```js
const app = getApp()
Component({
    options: {
        multipleSlots: true
    },
    properties: {
        backgroundColor:{
            type: String,
            value: 'rgba(0,0,0,0)'
        }
    },
    data: {},
    ready() {
        let {
            statusBarHeight,
            navBarHeight
        } = app.globalData;

        this.setData({
            statusBarHeight,
            navBarHeight
        })
    },
    methods: {
        back() {
            wx.navigateBack({
                delta:1
            })
        }
    }
})

```

`content`里放置内容，返回按钮固定在左边。

***nav.wxml***:
```html
<view class='nav-wrap' style="background-color:{{bgColor}};">
    <view style="height:{{statusBarHeight}}px;"></view>
    <view class='content'>
        <slot name="content"></slot>
        <view class='back' bindtap='back'></view>
    </view>
</view>
```

***nav.wxss***:
```css
.nav-wrap {
    position: fixed;
    top: 0;
    left: 0;
    width: 750rpx;
    z-index: 1;
}

.content {
    position: relative;
    width: 100%;
    height: 44px;
}

.back {
    position: absolute;
    left: 0;
    top: 0;
    width: 88px;
    height: 44px;
    background: pink;
}
```

在页面中使用：
```html
<nav bgColor="black">
    <view slot="content">
        <view class='txt'>Nav title</view>
    </view>
</nav>
<view>page content</view>
```

效果图：

![](./1.png)

这里`txt`里的样式、内容都是可以自定义的，如果想要使用通用样式，可以写在组件里。

比如把导航栏`title`放在组件里，通过外部传值设置：

***nav.js***:
```js
Component({
    // ...
    properties: {
        title:{
            type: String,
            value: ''
        }
    },
    // ...
})
```

***nav.wxml***:
```html
<view class='nav-wrap' style="background-color:{{bgColor}};">
    <view style="height:{{statusBarHeight}}px;"></view>
    <view class='content'>
        <view class="title">{{title}}</view>
        <view class='back' bindtap='back'></view>
    </view>
</view>
```

***nav.wxss***:
```css
/* ... */
.title {
    color: white;
    text-align: center;
    line-height: 44px;
    font-weight: 500;
}
/* ... */
```

调用`<nav bgColor="black" title="hello">`就可以了。

在第一次使用`nav`组件的页面代码中，`page content`是看不见的，因为是直接从状态栏开始显示的，被`nav`挡住了。

这里可以加一个高度为导航栏高度的`view`当做顶部`padding`：

***nav.wxml***
```html
<view class='nav-wrap' style="background-color:{{bgColor}};">
    <view style="height:{{statusBarHeight}}px;"></view>
    <view class='content'>
        <view class="title">{{title}}</view>
        <view class='back' bindtap='back'></view>
    </view>
</view>
<view wx:if="{{hastop}}" class='padding' style="width:100;height:{{navBarHeight}}px;"></view>
```

这里在`properties`里设置了一个`hastop`，用来控制是否有顶部`padding`。

页面中：
```html
<nav bgColor="black" title="Nav title" hastop></nav>
<view>page content</view>
```

这样就可以显示出来了：

![](./2.png)

### 导航栏背景图

还可以做导航栏背景图，添加一个`image`，绝对定位放置在`nav-wrap`底部：

***nav.wxml***
```html
<view class='nav-wrap' style="background-color:{{bgColor}};">
    <image class='bgimg' wx:if="{{bgsrc}}" src='{{bgsrc}}' mode='aspectFill'></image>
    <view style="height:{{statusBarHeight}}px;"></view>
    <view class='content'>
        <view class='title'>{{title}}</view>
        <view class='back' bindtap='back'></view>
    </view>
</view>
<view wx:if="{{hastop}}" class='padding' style="width:100;height:{{navBarHeight}}px;"></view>
```

***nav.wxss***
```css
.bgimg {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
}
```

页面：
```html
<nav bgColor="black" title="Nav title" hastop bgsrc="/images/bg.jpeg"></nav>
<view>page content</view>
```

![](./3.png)

### 全屏背景

将`bgColor`、`hastop`、`bgsrc`都去掉，在页面中放置一个`position: fixed;`，并且铺满全屏的图片。
```html
<nav title="Nav title"></nav>
<image class='pagebg' src='/images/bg.jpeg' mode='aspectFill'></image>
```

![](./4.png)

`back`的内容自定义就行了，我这里只是简单放置了一个色框。


### 注意事项

官方文档中的注意事项：

* 注1：HexColor（十六进制颜色值），如"#ff00ff"
* 注2：关于navigationStyle
    * 客户端 7.0.0 以下版本，navigationStyle 只在 app.json 中生效。
    * 客户端 6.7.2 版本开始，navigationStyle: custom 对 <web-view> 组件无效
    * 开启 custom 后，低版本客户端需要做好兼容。开发者工具基础库版本切到 1.7.0（不代表最低版本，只供调试用）可方便切到旧视觉

[微信官方文档：全局设置](https://developers.weixin.qq.com/miniprogram/dev/framework/config.html)