---
layout: post
title:  "通过编程来学习线性代数3"
date: '2018-07-29 17:29:00'
comments: true
thumbnail: /blog/assets/images/linear-algebra/cover.png
tag:
    - 基础知识
    - 线性代数
---

#### 行列式类

在讨论行列式的一些性质之前，我先根据之前讲到的内容写一个行列式的类。

```js
// linera algebra determinant class
// filename: det.js

let Det;

(function(){
    Det = function (array) {
        this.array = array
        this.length = array.length
        // 阶乘，元素个数
        this._itemLength = null
    
        // 保存逆序数的数组
        this.inverseNumberArray = null
    
        // 保存每个项的数组
        this._items = null
        this.itemValues = null

        // 是否需要重新计算
        this.reCalc = false
    }
    
    // 阶乘
    Det.prototype.itemLength = function () {
        if (this._itemLength == null) {
            this._itemLength = factorial(this.length)
        }
        return this._itemLength
    }
    
    // 逆序数
    Det.prototype.inverseNumber = function (index) {
        if (this.inverseNumberArray == null) {
            this.inverseNumberArray = new Array(this.itemLength())
        }
        if (this.inverseNumberArray[index] == undefined) {
            let sum = 0
            let item = this.items()[index]
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
            this.inverseNumberArray[index] = sum
        }
        return this.inverseNumberArray[index]
    }
    
    // 获取保存每个项的数组
    Det.prototype.items = function () {
        if (this._items == null) {
            this._items = []
    
            let standardIndex = []
            for (let i = 0; i < this.length; i++) {
                standardIndex.push(i)
            }
            generate(this.length, standardIndex, this._items)
        }
        return this._items
    }
    
    // 获取单个项的值
    Det.prototype.itemValue = function (index) {
        if (this.itemValues == null) {
            this.itemValues = new Array(this.itemLength())
        }
        if(this.itemValues[index]==undefined || this.reCalc) {
            let inverseCount = this.inverseNumber(index)
            let data = this.array
            let item = this.items()[index]
            let value = (inverseCount % 2 ? -1 : 1)
            for (let j = 0, n = this.length; j < n; j++) {
                value *= data[j][item[j]]
            }
            this.itemValues[index] = value
        }
        return this.itemValues[index]
    }
    
    Det.prototype.calc = function () {
        let sum = 0
        for (let i = 0, len = this.itemLength(); i < len; i++) {
            sum += this.itemValue(i)
        }
    
        console.log(this.array)
        console.log(sum)
    
        return sum
    }
})()
```

```js
// filename util.js

/**
 * 列举所有@param A 数组元素的排列
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

/**
 * 计算n的阶乘
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

/**
 * 交互数组中的两个元素
 * 
 * @param {Array} arr
 * @param {Number} i
 * @param {Number} j
 */
function swap(arr, i, j) {
    var temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr
}
```

基本的东西准备好了，下面我们往行列式类`Det`上加一些功能，即行列式的一些性质。

#### 性质1：行列式与它的转置行列式相等

行列式的转置行列式即行变成列，列变成行。

![转置行列式](./linear3-1.png)

在`det.js`添加：
```js
// 获取转置行列式
Det.prototype.getTransposedDet = function () {
    let len = this.length
    let newArr = new Array(len)
    for (let i = 0; i < len; i++) {
        if(!newArr[i]) {
            newArr[i] = new Array(len)
        }
        for (let j = 0; j < len; j++) {
            newArr[i][j] = this.array[j][i]
        }
    }
    return new Det(newArr)
}
```

测试：
```js
let det = new Det([
    [2, 1, -5, 1],
    [1, -3, 0, -6],
    [0, 2, -1, 2],
    [1, 4, -7, 6]
])
det.calc()  // 27

let tdet = det.getTransposedDet()
tdet.calc() // 27
```
这里可以把`tdet.array`打印出来，看是不是真的转置成功。

#### 性质2：