---
title: 记一次VUE开发环境搭建
tags:
  - Vue
date: 2017-12-11 04:47:00
---


![vue logo](http://upload-images.jianshu.io/upload_images/2158535-c9700943d83aa88f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

今天想了解一下vue开发相关的东西，就动手搭建了一些开发环境。
下面是我安装和配置的相关过程。（Mac系统）

### 下载安装[nodejs 6.11.4 (包含 npm 3.10.10)](https://nodejs.org/en/download/)
![Download installer](http://upload-images.jianshu.io/upload_images/2158535-33fb128c8fd8a308.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)

安装完成后，命令行升级一下npm
```
$ npm install npm@latest -g
$ npm -v
5.5.1
```
权限设置
```
$ npm config get prefix
/usr/local
$ sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
```

`npm config get prefix`是用来找到`npm`的目录
`sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}`给当前用户读写`npm`相关目录的权限。

### 安装webpack和vue-cli
```
$ npm install webpack -g
$ npm install vue-cli -g

$ npm list -g --depth=0
/usr/local/lib
├── create-react-native-app@1.0.0
├── es-checker@1.4.1
├── npm@5.5.1
├── vue-cli@2.9.1
└── webpack@3.8.1
```

### 创建工程
```
$ cd your_workspace_folder
$ vue init webpack projectname
```
比如我的工程名为`vueStart`，输入的地方没有什么需求直接回车就行了。

```
$ vue init webpack-simple vueStart

? Project name vuestart
? Project description A Vue.js project
? Author tomfriwel <xxx@xx.com>
? Use sass? No

   vue-cli · Generated "vueStart".

   To get started:
   
     cd vueStart
     npm install
     npm run dev.
```
这里注意的是，如果用`vue init webpack-simple projectname`，之后`npm run dev`是运不起来的。所以这里用的`webpack`而不是`webpack-simple`

这里的`vue init webpack`和`npm install webpack`不一样
 `vue init webpack`是安装`webpack`模板（也可以是以下列出的一些模板`webpack-simple/browserify...`）
具体信息可以查看[vuejs-templates](https://github.com/vuejs-templates)/**[webpack](https://github.com/vuejs-templates/webpack)**

一些可用的模板
* [webpack](https://github.com/vuejs-templates/webpack) - A full-featured Webpack + vue-loader setup with hot reload, linting, testing & css extraction.
* [webpack-simple](https://github.com/vuejs-templates/webpack-simple) - A simple Webpack + vue-loader setup for quick prototyping.
* [browserify](https://github.com/vuejs-templates/browserify) - A full-featured Browserify + vueify setup with hot-reload, linting & unit testing.
* [browserify-simple](https://github.com/vuejs-templates/browserify-simple) - A simple Browserify + vueify setup for quick prototyping.
* [pwa](https://github.com/vuejs-templates/pwa) - PWA template for vue-cli based on the webpack template
* [simple](https://github.com/vuejs-templates/simple) - The simplest possible Vue setup in a single HTML file


### 配置工程
进入创建的工程目录
```
$ cd vueStart/
$ npm install
```
`npm install`后就会安装一些乱七八糟的东西。

安装 vue 路由模块`vue-router`和网络请求模块`vue-resource`，这两个如果用不到也可以不用装。
```
$ npm install vue-router vue-resource --save
+ vue-resource@1.3.4
+ vue-router@3.0.1
added 17 packages in 6.541s
```
`--save`的作用
![](http://upload-images.jianshu.io/upload_images/2158535-0b9922d19ae9946b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 运行和构建

```
$ npm run dev
```
没什么问题的话，打开页面是这样的

![Welcome](http://upload-images.jianshu.io/upload_images/2158535-d9e3f3be952834d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)

对`.vue`更改后，页面也会自动更新，挺方便的。

### 开始编写
`src`文件夹目录
```
src
├── App.vue
├── assets
│   └── logo.png
├── components
│   └── HelloWorld.vue
└── main.js
```
这里`App.vue`引用了一个叫`HelloWorld`的组件。我们对`HelloWorld`组件进行更改。
```
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'First modify.'
    }
  }
}
</script>
```
保存后
![First modify.](http://upload-images.jianshu.io/upload_images/2158535-6f9b41a973a68c26.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)

### 发布
执行
```
$ npm run build
```
完成后会生成一个`dist`文件夹
```
dist
├── index.html
└── static
    ├── css
    │   └── app.86d25fd679f2d9f5bee9162ae7804b46.css
    └── js
        ├── app.bcbf2665a80fe0bdc316.js
        ├── app.bcbf2665a80fe0bdc316.js.map
        ├── manifest.f9cc8df0a9bc12617260.js
        ├── manifest.f9cc8df0a9bc12617260.js.map
        ├── vendor.5edf78e409459ac3ccd1.js
        └── vendor.5edf78e409459ac3ccd1.js.map
```
如果是想本地运行而不是放到服务器上，需要对`config/index.js`进行一个小更改。将`build`中的`assetsPublicPath`改为`./`，不然会找不到资源，最后再次`npm run build`，就可以直接浏览器打开`dist`文件夹下的`index.html`了。

![ERR](http://upload-images.jianshu.io/upload_images/2158535-7188024e99a62f4b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)

```
...

module.exports = {
  build: {
    env: require('./prod.env'),
    index: path.resolve(__dirname, '../dist/index.html'),
    assetsRoot: path.resolve(__dirname, '../dist'),
    assetsSubDirectory: 'static',
    assetsPublicPath: './',
    productionSourceMap: true,

...
```



### Tips
`npm run build`和`npm run dev`其实是运行的`package.json`里`scripts`的对应的脚本。例如我的
```
  ...

 "scripts": {
    "dev": "node build/dev-server.js",
    "start": "npm run dev",
    "build": "node build/build.js"
  },

  ...
```
可以自己测试一个
```
  ...

 "scripts": {
    "dev": "node build/dev-server.js",
    "start": "npm run dev",
    "build": "node build/build.js",
    "test": "echo 123"
  },

  ...
```
然后运行`npm run test`看看结果。


### 相关参考
[Installing Node.js and updating npm](https://docs.npmjs.com/getting-started/installing-node)
[Fixing npm permissions](https://docs.npmjs.com/getting-started/fixing-npm-permissions)
[Vue2.0 新手完全填坑攻略——从环境搭建到发布](http://www.jianshu.com/p/5ba253651c3b)
[What is the --save option for npm install?](https://stackoverflow.com/a/35849725/6279975)
[Vue 爬坑之路（一）—— 使用 vue-cli 搭建项目](http://www.cnblogs.com/wisewrong/p/6255817.html)
[基于vue-cli快速构建](http://blog.csdn.net/lollipop94/article/details/78295315)
[npm scripts 使用指南](http://www.ruanyifeng.com/blog/2016/10/npm_scripts.html)
[vuejs](https://github.com/vuejs)/**[vue-cli](https://github.com/vuejs/vue-cli)**