---
layout: post
title:  "通过编程来学习线性代数2"
# date: '2018-03-21 10:11:47'
comments: true
---


### 全排列及其逆序数

`全排列`:将n个不同的元素排成一列

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
}

```

得到每一项后, 就可以进行计算逆序数了. 一个排列的逆序数决定了是正或负数.
