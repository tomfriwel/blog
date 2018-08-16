---
layout: post
title:  "通过编程来学习线性代数2-计算行列式的值"
date: '2018-05-30 22:31:00'
comments: true
thumbnail: /blog/assets/images/linear-algebra/cover.png
tag:
    - 基础知识
    - 线性代数
---


### 全排列及其逆序数

为了计算每一项，我们先要了解如何生成每一个相乘的项，了解什么时候是正数什么时候是负数，关于正负问题就需要了解`逆序数`的定义。

`全排列`:
> 将n个不同的元素排成一列

```

1 > 1

2 > 1,2 | 2,1

3 > 1,2,3 | 1,3,2 | 2,1,3 | 2,3,1 | 3,1,2 | 3,2,1

...

```

从`排列组合`的知识中可以知道: `n`个不同的元素, 从中选取一个放到第一位, 有`n`钟选法, 剩下`n-1`个.

继续从这`n-1`各种继续选取, 放到第二位, 有`n-1`钟选法.

以此类推, 直到选完为止.

n个元素所有排列的种数: `n! = n*(n-1)*...*3*2*1`


这里我们用[`Heap's algorithm`](https://en.wikipedia.org/wiki/Heap%27s_algorithm)算法来生成每一项:

```js
// Heap's algorithm

/**
 * 列举所有@param A 数组元素的全排列(排列)
 * 
 * @param {Number} n A长度
 * @param {Array} A 元素
 * @param {Array} result 全部结果
 */
function generate(n, A, result) {
    if (n == 1) {
        result.push(A.slice())
    }
    else {
        for (let i = 0; i < n - 1; i++) {
            generate(n - 1, A, result)
            if (n % 2 == 0) {
                swap(A, i, n - 1)
            }
            else {
                swap(A, 0, n - 1)
            }
        }
        generate(n - 1, A, result)
    }
}
```

可以在浏览器的控制台中试一下, 如`generate(3, [1, 2, 3], arr)`或者``generate(4, ['a', 'b', 'c', 'd'], arr)``, 字符数字都行，`arr`需要事先定义好`let arr = []`


得到每一项后, 就可以进行计算逆序数了. 一个排列的逆序数决定了这一项是正或负数.

`逆序：`
> n个不同的自然数，规定从小到大为标准次序。当某两个元素的先后次序与标准次序不同时，就称这两个元素组成一个`逆序`

`逆序数：`
> 排列中所有逆序的总数称为此排列的`逆序数`

计算逆序数的方法，我是直接从第一个开始，依次跟剩下的进行对比：

```js
function calcInverseNumber(item) {
    let sum = 0
    for (let i = 0, len = item.length; i < len; i++) {
        // 取出第i个数
        let digit = item[i]
        // 用第i个数与第i位之后的数进行对比
        for (let j = i + 1; j < len; j++) {
            if (digit > item[j]) {
                sum++
            }
        }
    }
    return sum
}
```

到这里，生成计算中的每一项和计算每一项的逆序数的方法都有了，接下来就需要一个计算方法。这个计算方法需要传入一个`行列式`，然后通过`generate`生成相乘的每一项，再通过`calcInverseNumber`算出逆序数并相加得出结果。

```js
// 计算行列式的值
/**
 * @param {Array} data 行列式数组
 * 
 */
function calcDeterminantV1(data) {
    let n = data.length
    let standardIndex = []
    for (let i = 0; i < n; i++) {
        standardIndex.push(i)
    }

    let indexArr = []
    generate(n, standardIndex, indexArr)

    let sum = 0
    for (let i = 0, len = factorial(n); i < len; i++) {
        let arr = indexArr[i]
        let inverseCount = calcInverseNumber(arr)

        let item = (inverseCount % 2 ? -1 : 1)
        for (let j = 0; j < n; j++) {
            item *= data[j][arr[j]]
        }
        sum += item
    }

    return sum
}
```

`line 7` 获取行列式的长度
`line 8-11` 生成一个`标准排列`的数组`[0, 1, 2, ..., n-1]`
`line 13-14` 生成`0~n-1`的所有可能的排列，共`n!`个，`indexArr`有`n!`个长度为`n`的数组，这些数组的元素是`0~n-1`组成的一个排列。
`line 16-26` 计算`行列式data`的值，函数`factorial(n)`为计算`n!`的值。
`line 17-24`遍历`indexArr`数组，计算每个排列的值。
`line 19`计算排列`arr`的`逆序数`，`line 21`判断`逆序数inverseCount`的正负（奇数为负，偶数为正）。
`line 22-25` 使`data`中角标`(j, arr[j])`对应的数进行相乘，得到`item`，并追加到总数`sum`中。

函数`factorial(n)`:
```js
/**
 * 
 * @param {Number} n 
 */
function factorial(n) {
    var result = 1
    for (i = 2; i <= n; i++) {
        result *= i
    }
    return result
}
```

现在可以试试用这个方法来计算行列式的值了，比如：

```js
[[1, 0, 0],
[0, 3, 0],
[0, 0, 3]]
// sum = 9

[[1, 2, -4],
[-2, 2, 1],
[-3, 4, -2]]
// sum = -14

[[2, 1, -5, 1],
[1, -3, 0, -6],
[0, 2, -1, 2],
[1, 4, -7, 6]]
// sum = 27
```

目前，计算行列式的值已经告一段落了，下一节将实现一些行列式的延伸。

比如行列式按行（列）展开相关知识。


### 代码

- [tomfriwel/linearAlgebraPro](https://github.com/tomfriwel/linearAlgebraPro)