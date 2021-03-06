---
layout: post
title:  '第一次使用Carthage记录'
date: '2018-05-07 14:30:41'
comments: true
tags:
    - iOS
---

### 准备

`$ brew update`

> update [--merge] [--force]: 使用git从GitHub获取最新版本的Homebrew和所有formula，并执行任何必要的迁移。

`$ brew install carthage`

> install formula: 安装 formula

很慢，后来用科学上网后快很多。

`$ carthage version`

> 装好后查看版本

### 添加库

在你的项目根目录下创建一个名为`Cartfile`的文件，并添加要用的第三方库，比如使用`Alamofire`:

***project/Cartfile:***
```
github "Alamofire/Alamofire" ~> 4.7
```

`$ carthage update`

> 获取（fetch）并构建（build）您列出的每个框架。

执行命令后，***Carthage*** 会拉取库文件进行编译，会在 ***project/Carthage/Build*** 目录下生成不同平台的`Alamofire.framework`文件。

***Carthage*** 不像 ***Cocoapods*** 会自动帮你做好连接配置，需要手动添加，因为一个一个将`*.framework`文件添加到 ***Build Phases>Link Binary With Libaries*** 里很麻烦，

![Link Binary With Libaries](/blog/assets/images/use-carthage-for-the-first-time/0.png)

所以这里推荐把相应库目录添加到 ***Build Settings>Framework Search Paths*** 里，比如我使用的是*iOS*版，那么添加一个：

```
$(PROJECT_DIR)/Carthage/Build/iOS
```

![Framework Search Paths](/blog/assets/images/use-carthage-for-the-first-time/1.png)

![(PROJECT_DIR)/Carthage/Build/iOS](/blog/assets/images/use-carthage-for-the-first-time/2.png)

上面设置是看别人博客进行配置的，但是一运行，就会报错：

```
dyld: Library not loaded: @rpath/Alamofire.framework/Alamofire
  Referenced from: /var/containers/Bundle/Application/xxx/SwiftDemo.app/SwiftDemo
  Reason: image not found
```

后来查找了这个错误，发现添加库到 ***Framework Search Paths*** 里只是让`import`的时候不报错，但要保证运行的时候不报上面那个错还需要一步。

将 `Alamofire.framework` 添加到 ***General>Embedded binaries***

![Embedded binaries](/blog/assets/images/use-carthage-for-the-first-time/3.png)

最后就可以用官方例子试用一下了：

```swift
Alamofire.request("https://httpbin.org/get").responseJSON { response in
    print("Request: \(String(describing: response.request))")   // original url request
    print("Response: \(String(describing: response.response))") // http url response
    print("Result: \(response.result)")                         // response serialization result

    if let json = response.result.value {
        print("JSON: \(json)") // serialized json response
    }

    if let data = response.data, let utf8Text = String(data: data, encoding: .utf8) {
        print("Data: \(utf8Text)") // original server data as UTF8 string
    }
}
```

### References

- [Carthage/Carthage](https://github.com/Carthage/Carthage)
- [走向Carthage](https://www.jianshu.com/p/3921289cd3c5)
- [Homebrew](https://docs.brew.sh/Manpage)
- [dyld: Library not loaded: @rpath/Alamofire.framework/Alamofire on my iPhone(iOS8) while debuging #101](https://github.com/Alamofire/Alamofire/issues/101)
- [iOS app with framework crashed on device, dyld: Library not loaded, Xcode 6 Beta](https://stackoverflow.com/a/24345546/6279975)