---
layout: post
title:  '更改Gihub公开邮箱后发生的ssh错误'
date: '2018-05-07 11:42:05'
comments: true
---

最近改了Github的Public email，然后在电脑上使用git拉取Github的库的时候，发生各种离奇的错误。

一开始查了一下，没找到什么办法，也没去管，就没用`git clone ...`，就直接在Github上通过zip下载。

今天打算使用Carthage，然后用`carthage update`安装库的时候，又看到ssh相关的报错，就开始重视。因为Carthage里面也用到类似于`git Github仓库地址`的相关命令。

猜测是ssh key出错，可以到`$ cd ~/.ssh`查看，发现`id_rsa.pub`文件最后是老的邮箱，怀疑就是这个问题。

想到最近改过Github的公开邮箱（就是Github个人主页那个邮箱），就联系到了一起。

根据[Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)的方法，重新设置了ssh key，填信息部分除了邮箱那里，其他都是默认的。

然后再使用相关git命令，就解决了。

大吉大利！

🤪🤪🤪🤪

### 参考

- [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)