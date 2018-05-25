---
layout: post
title:  "通过编程来学习线性代数2"
date: '2018-05-21 10:11:47'
comments: true
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
function generate(n, A) {
    if(n==1) {
        console.log(A)
    }
    else {
        for(let i=0; i<n-1; i++) {
            generate(n-1, A)
            if(n%2==0) {
                swap(A, i, n-1)
            }
            else {
                swap(A, 0, n-1)
            }
        }
        generate(n-1, A)
    }
}
```

可以在浏览器的控制台中试一下, 如`generate(3, [1, 2, 3])`或者``generate(4, ['a', 'b', 'c', 'd'])``, 字符数字都行, 每一项唯一

这里我们需要用一个数组来保存每一项

```js
let arr = []
function generate(n, A) {
    if(n==1) {
        console.log(A)
        arr.push(A)
    }
    ...
    ...
    ...
}

```

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
