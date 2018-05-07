---
layout: post
title:  '第一次使用Carthage记录'
date: '2018-05-07 14:30:41'
comments: true
---

### Prepare

`$ brew update`

> update [--merge] [--force]: 使用git从GitHub获取最新版本的Homebrew和所有formula，并执行任何必要的迁移。

`$ brew install carthage`

> install formula: 安装 formula

很慢，后来用科学上网后快很多。

`$ carthage version`

> 装好后查看版本

### 添加库

在你的项目根目录下创建一个名为`Cartfile`的文件，比如使用`Alamofire`:

***project/Cartfile:***
```
github "Alamofire/Alamofire" ~> 4.7
```

`$ carthage update`

> 安装

执行命令后，***Carthage*** 会拉取库文件进行编译，会在 ***project/Carthage/Build*** 目录下生成不同平台的`Alamofire.framework`文件。

***Carthage*** 不像 ***Cocoapods*** 会自动帮你做好连接配置，需要手动添加，因为一个一个将`*.framework`文件添加到 ***Build Phases>Link Binary With Libaries*** 里很麻烦，

{% include image.html url="/assets/images/use-carthage-for-the-first-time/0.png" description="Link Binary With Libaries" width=800 %}

所以这里推荐把相应库目录添加到 ***Build Settings>Framework Search Paths*** 里，比如我使用的是*iOS*版，那么添加一个：

```
$(PROJECT_DIR)/Carthage/Build/iOS
```

{% include image.html url="/assets/images/use-carthage-for-the-first-time/1.png" description="Framework Search Paths" width=800 %}

{% include image.html url="/assets/images/use-carthage-for-the-first-time/2.png" description="$(PROJECT_DIR)/Carthage/Build/iOS" width=800 %}

上面设置是看别人博客进行配置的，但是一运行，就会报错：

```
dyld: Library not loaded: @rpath/Alamofire.framework/Alamofire
  Referenced from: /var/containers/Bundle/Application/xxx/SwiftDemo.app/SwiftDemo
  Reason: image not found
```

后来查找了这个错误，发现添加 ***Framework Search Paths*** 只是让写代码的时候不报错，但要运行的时候也不报错还需要一步。

将 `Alamofire.framework` 添加到 ***General>Embedded binaries***

{% include image.html url="/assets/images/use-carthage-for-the-first-time/3.png" description="Embedded binaries" width=800 %}

### References

- [走向Carthage](https://www.jianshu.com/p/3921289cd3c5)
- [Homebrew](https://docs.brew.sh/Manpage)
- [dyld: Library not loaded: @rpath/Alamofire.framework/Alamofire on my iPhone(iOS8) while debuging #101](https://github.com/Alamofire/Alamofire/issues/101)
- [iOS app with framework crashed on device, dyld: Library not loaded, Xcode 6 Beta](https://stackoverflow.com/a/24345546/6279975)