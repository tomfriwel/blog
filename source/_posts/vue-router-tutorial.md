---
title: Vue Router 试探
date: 2018-08-17 16:40:28
thumbnail: /blog/2018/08/17/vue-router-tutorial/2.png
tags:
    - Vue
    - Router
---

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

#### 参考

- [Vue2+VueRouter2+webpack 构建项目实战（一）准备工作](https://blog.csdn.net/fungleo/article/details/53171052)