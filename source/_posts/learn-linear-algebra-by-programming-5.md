---
title: 通过编程来学习线性代数5-克拉默法则
comments: true
thumbnail: /blog/assets/images/linear-algebra/cover.png
tags:
  - 基础知识
  - 线性代数
categories:
  - 数学
date: 2018-11-14 22:31:00
---

下面基本上都是PPT中的内容。

从本篇文章开始，我们用`Node.js`作为运行环境，具体配置和使用方式可到[Node.js官网](https://nodejs.org/en/)查看。[源代码（node-version文件夹）](https://github.com/tomfriwel/linearAlgebraPro)也做了相应的更改。

如果线性方程组的系数行列式不等于零，那么线性方程组有解并且解是唯一的：

![](./e5.png)

解可以表示成：

`x1 = D1/D`, `x2 = D2/D`, `x3 = D3/D`, ... (2)

定理包含三个结论：

* 方程组有解：（解的存在性）
* 解是唯一的：（解的唯一性）
* 解可以由公式（2）给出。

![](./e6.png)


**定理4** 如果线性方程组（1）的系数行列式不等于零，则该线性方程组一定有解，且解是唯一的。

**定理4'** 如果线性方程组无解或有两个不同的解，则它的系数行列式必为零。

![](./e7.png)

常数项全为零的线性方程组称为**齐次线性方程组**，否则称为**非齐次线性方程组**。

齐次线性方程组总是有解的，因为`(0,0,...,0)`就是一个解，称为**零解**。因此齐次线性方程组一定有零解，但不一定有非零解。

#### 齐次线性方程组的相关定理

**定理5** 如果齐次线性方程组的系数行列式 `D!=0`，则其只有零解，没有非零解。

**定理5'** 如果齐次线性方程组有非零解，则其系数行列式比为零。

#### 代码

- [tomfriwel/linearAlgebraPro](https://github.com/tomfriwel/linearAlgebraPro)

#### 参考

- [线性代数-同济大学(第五版)课件 [完整版]](https://wenku.baidu.com/view/e3efed47fe4733687e21aafd?pn=51)