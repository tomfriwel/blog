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

### 例14：解线性方程组
![](Screen Shot 2020-04-22 at 11.13.22.png)

```js
const det = new Det([
  [2, 1, -5, 1],
  [1, -3, 0, -6],
  [0, 2, -1, 2],
  [1, 4, -7, 6],
])

// 计算行列式的值，不为零，有唯一解
const D = det.calc() // 27
```
这里计算出了分母`D`的值。接下来我们给类`Det`新增一个方法`replace`，用于将行列式的一列替换为方程组右边的常熟项。

这样我们就可以计算出分子的值了，进而算出方程组的解。

```js
// 常熟项
const c = [8, 9, -5, 0]

// 替换对应的列，算出分子的值
const det1 = det.replace(0, c, false)
const D1 = det1.calc()  // 81

const det2 = det.replace(1, c, false)
const D2 = det2.calc()  // -108

const det3 = det.replace(2, c, false)
const D3 = det3.calc()  // -27

const det4 = det.replace(3, c, false)
const D4 = det4.calc()  //27

// 得出方程组的解
x1 = D1/D
x2 = D2/D
x3 = D3/D
x4 = D4/D

console.log(x1, x2, x3, x4)
// 3 -4 -1 1
```

为了方便，可以将上面计算方程组的方法写成一个函数，方便使用：
```js
/**
 * 计算方程组的解
 * 
 * @param {Array} array 线性方程组系数行列式
 * @param {Array} carray 常数项
 */
function calcEquations(array, carray) {
  const len = array.length
  const det = new Det(array)
  const D = det.calc()
  if(D === 0) {
    return null
  }
  const results = new Array(len).fill()
  for (let i = 0; i < len; i++) {
    const tempdet = det.replace(i, carray, false)
    results[i] = tempdet.calc() / D
  }
  return results
}

const result = calcEquations([
  [2, 1, -5, 1],
  [1, -3, 0, -6],
  [0, 2, -1, 2],
  [1, 4, -7, 6],
], [8, 9, -5, 0])

console.log(result)
// [ 3, -4, -1, 1 ]
```

### 例15
![](./Screen Shot 2020-04-22 at 14.18.17.png)

系数项行列式是范德蒙德行列式。

```js
const result = calcEquations([
  [1, 1, 1, 1],
  [1, 2, 4, 8],
  [1, 3, 9, 27],
  [1, 4, 16, 64],
], [3, 4, 3, -3])
console.log(result)
// [ 3, -1.5, 2, -0.5 ]
```



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