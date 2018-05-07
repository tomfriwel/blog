---
layout: post
title:  '第一次使用Carthage'
date: '2018-05-07 10:27:15'
comments: true
---

### Prepare

`$ brew update`

> update [--merge] [--force]: Fetch the newest version of Homebrew and all formulae from GitHub using git(1) and perform any necessary migrations.

`$ brew install carthage`

> install formula: Install formula

very slow..., I canceled, then after using vpn it will be much faster.

`$ carthage version`

### Add a libaray

> View carthage version

Create a file named 'Cartfile' in your project root folder.

For example, add Alamorefire:

***project/Cartfile:***
```
github "Alamofire/Alamofire" ~> 4.7
```

`$ carthage update`



### References

- [走向Carthage](https://www.jianshu.com/p/3921289cd3c5)
- [Homebrew](https://docs.brew.sh/Manpage)