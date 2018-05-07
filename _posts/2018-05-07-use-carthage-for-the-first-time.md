---
layout: post
title:  '第一次使用Carthage记录'
date: '2018-05-07 10:27:15'
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

### References

- [走向Carthage](https://www.jianshu.com/p/3921289cd3c5)
- [Homebrew](https://docs.brew.sh/Manpage)