---
title: 通过编程来学习线性代数3-行列式的性质（更新中）
comments: true
thumbnail: /blog/assets/images/linear-algebra/cover.png
tags:
  - 基础知识
  - 线性代数
date: 2018-08-29 17:29:00
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

#### 性质2：互换行列式的两行（列），行列式变号

添加如下方法
```js
// 互换行列式的两行（列）
Det.prototype.swap = function (n0, n1, isRow=true) {
    let newArr = JSON.parse(JSON.stringify(this.array))

    if(isRow) {
        newArr = swap(newArr, n0, n1)
    } else {
        let len = this.length
        for (let i = 0; i < len; i++) {
            newArr[i] = swap(newArr[i], n0, n1)
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

let tdet = det.swap(3, 1, true) // -27
// let tdet = det.swap(3, 1, false) // -27
tdet.calc()
```

#### 性质3：行列式的某一行（列）中所有元素都乘以同一个数`k`，等于用数`k`乘以此行列式

添加方法：
```js
// 某一行（列）乘以一个数
/**
 * 
 * @param {Number} n 行/列，从0开始
 * @param {Number} k 数 
 * @param {Boolean} isRow 默认行
 */
Det.prototype.multiply = function (n, k, isRow = true) {
    let newArr = JSON.parse(JSON.stringify(this.array)) //deep copy
    let len = this.length

    if (isRow) {
        for (let i = 0; i < len; i++) {
            newArr[n][i] *= k
        }
    } else {
        for (let i = 0; i < len; i++) {
            newArr[i][n] *= k
        }
    }

    return new Det(newArr)
}
```

通过计算乘之前和之后的两个结果来看：
```js
let det = new Det([
    [2, 1, -5, 1],
    [1, -3, 0, -6],
    [0, 2, -1, 2],
    [1, 4, -7, 6]
])
det.calc() // 27

det.multiply(1, 5).calc()   // 135
```

也可以通过计算下面两个行列式来验证，第二个行列式的第一列是第一个行列式第一列的两倍，计算结果分别为27和54

```js
let det = new Det([
    [2, 1, -5, 1],
    [1, -3, 0, -6],
    [0, 2, -1, 2],
    [1, 4, -7, 6]
])
det.calc()  // 27

let det2 = new Det([
    [4, 1, -5, 1],
    [2, -3, 0, -6],
    [0, 2, -1, 2],
    [2, 4, -7, 6]
])
det2.calc() // 54
```

#### 性质4：行列式中如果有两行（列）元素成比例，则此行列式为零

可通过计算下面行列式验证：
```js
let det = new Det([
    [2, 1, -5, 1],  //1
    [1, -3, 0, -6],
    [0, 2, -1, 2],
    [4, 2, -10, 2]  //2*k
])
det.calc()  // 0

let det2 = new Det([
    [2, 1, -5, 1],  //1
    [1, -3, 0, -6],
    [0, 2, -1, 2],
    [2, 1, -5, 1]  //1
])
det2.calc()  // 0
```

#### 性质5：若行列式的某一行（列）的元素都是两个数之和，如：

![](./linear3-2.png)
![](./linear3-3.png)

```js
let det = new Det([
    [2 + 3, 1, 2, 1],
    [1 + 4, -3, 5, -6],
    [0 - 5, 2, 2, 2],
    [4 + 1, 2, -4, 4]
])
det.calc()  //80

let det2 = new Det([
    [2, 1, 2, 1],
    [1, -3, 5, -6],
    [0, 2, 2, 2],
    [4, 2, -4, 4]
])
det2.calc() //36

let det3 = new Det([
    [3, 1, 2, 1],
    [4, -3, 5, -6],
    [-5, 2, 2, 2],
    [1, 2, -4, 4]
])
det3.calc() //44
```

#### 性质6：把行列式的某一行（列）的各元素乘以同一个倍数加到另一行（列）对应的元素上去，行列式不变。

![性质6](./linear-3-4.png)


在`Det`类上添加方法
```js
// 性质6：把行列式的某一行（列）的各元素乘以同一个倍数加到另一行（列）对应的元素上去，行列式不变。
/**
    * 
    * @param {Number} n0 行/列
    * @param {Number} n1 行/列
    * @param {Number} k 行列式的 n0(行/列) + n1(行/列)*k
    * @param {Boolean} isRow
    */
Det.prototype.plusLine = function (n0, n1, k, isRow=true) {
    if(n0==n1) {
        throw('不能加到同一行或列')
    }
    let newArr = JSON.parse(JSON.stringify(this.array))
    let len = this.length

    if (isRow) {
        for (let i = 0; i < len; i++) {
            newArr[n0][i] += newArr[n1][i] * k
        }
    } else {
        for (let i = 0; i < len; i++) {
            newArr[i][n0] += newArr[i][n1] * k
        }
    }

    return new Det(newArr)
}
```

验证：
```js
// 性质6
let det = new Det([
    [1, 1, 2, 1],
    [1, -3, 5, 3],
    [0, 2, 2, 2],
    [1, 2, -4, 4]
])
det.calc()  //-112

// 第1列每行对应元素加上第4列每行对应元素乘3
let det1 = det.plusLine(0, 3, 3, false)
det1.calc()  //-112
```


### 代码

- [tomfriwel/linearAlgebraPro](https://github.com/tomfriwel/linearAlgebraPro)

### 参考

- [线性代数-同济大学(第五版)课件 [完整版]](https://wenku.baidu.com/view/e3efed47fe4733687e21aafd?pn=51)