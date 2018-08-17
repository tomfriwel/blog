---
title: Vue Router 试探
date: 2018-08-17 16:40:28
thumbnail: /blog/2018/08/17/vue-router-tutorial/2.png
tags:
    - Vue
    - Router
---

在这篇[记一次VUE开发环境搭建](/blog/2017/12/11/setup-vue-development-environment-first-time/)文章中我记录了一些`Vue`开发环境搭建的东西，最近接触了一些关于`Router`的内容，在这里做一个记录和分享。

#### 相关设置

稍微理了一下结构，如图

![](./1.png)

首先我们在`main.js`里初始化`Vue`：
```js
import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'

new Vue({
    router,
    el: '#app',
    render: h => h(App)
})
```

在`App.vue`里设置`router-view`以便使用`Router`
```html
<template>
<div id="app" v-cloak>
    <router-view class="view" keep-alive transition transition-mode="out-in"></router-view>
</div>
</template>

<script>
export default {
  components: {}
}
</script>
<style>
[v-cloak] {
    display: none;
}
</style>

```

`line 3` 设置`router-view`

`line 2`里的`v-cloak`配合`line 13~15`保证不会在加载的时候出现带有双`{}`的符号。

设置`router`, `routes.js`:
```js
import Vue from 'vue'
import Router from 'vue-router'
import home from './pages/home.vue'
import test from './pages/test.vue'

Vue.use(Router)

export default new Router({
    routes:[
        {
            path:'/',
            component:home
        },
        {
            path:'/test',
            component:test
        }
    ]
})
```

这里将页面映射到相应的`path`上，比如`/test`就对应了`test.vue`。

#### 使用

比如我们点击后跳转到另一个页面，就可以像下面这样使用：
```js
<template>
<div>
    <div @click="view">{{msg}}</div>
</div>
</template>

<script>
export default {
    data() {
        return {
            msg: "Hello tom."
        };
    },
    methods:{
        view() {
            this.$router.push({
                path: "/test",
                query: {
                    name:'tom'
                }
            })
        }
    }
}
</script>

<style lang="scss">
</style>
```

`query`是传参数用的，可以在下一个页面通过`this.$route.query.name`获取。

可以通过`this.$router.back(-1)`手动返回。

这里就是我初次试探`Router`的内容，这些对应基本的页面来说已经够用了。

#### 参考

- [Vue2+VueRouter2+webpack 构建项目实战（一）准备工作](https://blog.csdn.net/fungleo/article/details/53171052)