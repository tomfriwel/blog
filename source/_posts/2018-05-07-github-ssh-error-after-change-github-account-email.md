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
```
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Enter a file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]
Enter passphrase (empty for no passphrase): [Type a passphrase]
Enter same passphrase again: [Type passphrase again]
```
`passphrase`我也是直接回车没填。

然后再使用相关git命令，就解决了。

大吉大利！

🤪🤪🤪🤪

### 更新

改了之后，`Gitlab`又不行了，出现错误：
```
git@gitlab.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

后来把`id_rsa`添加到`Settings > SSH Keys`，才可以用。

复制命令：`$ pbcopy < ~/.ssh/id_rsa.pub`

或者创建一个新的key：
```
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Enter a file in which to save the key (/Users/you/.ssh/id_rsa): gitlab_id_rsa
Enter passphrase (empty for no passphrase): [Type a passphrase]
Enter same passphrase again: [Type passphrase again]
```

然添加：
```
$ ssh-add ~/.ssh/id_rsa
$ ssh-add ~/.ssh/gitlab_id_rsa
```
最后需要建一个配置文件：

```
$ cd ~/.ssh/
$ touch config
```

然后添加：
```
#gitlab account
Host gitlab.com
	HostName gitlab.com
	User git
	IdentityFile ~/.ssh/gitlab_id_rsa

#github account
Host github.com
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa
```

也要将`gitlab_id_rsa.pub`内容复制到`Settings > SSH Keys`


### 参考

- [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [GitLab and SSH keys](https://docs.gitlab.com/ce/ssh/README.html#working-with-non-default-ssh-key-pair-paths)
- [Multiple SSH Keys settings for different github account](https://gist.github.com/jexchan/2351996)
- [Can I have multiple ssh keys in my .ssh folder?](https://superuser.com/questions/287651/can-i-have-multiple-ssh-keys-in-my-ssh-folder)