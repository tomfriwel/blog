---
title: 通过编程来学习线性代数4-行列式按行(列)展开（更新中）
comments: true
thumbnail: /blog/assets/images/linear-algebra/cover.png
tags:
  - 基础知识
  - 线性代数
date: 2018-09-07 10:07:17
---


***余子式***：将`aij`所在的行和列划去后，剩下的元素组成的行列式，记作`Mij`。(`i, j`为下标)

***代数余子式***：`Aij = Math.pow(-1, i+j) * Mij`

行列式每一项都对应一个余子式和代数余子式，因为`i, j`可以唯一确定一个元素。

求`i`行`j`列的余子式：
```js
/**
  * 余子式
  * 
  * @param {Number} i 行
  * @param {Number} j 列
  */
Det.prototype.complementMinor = function (i, j) {
    let len = this.length
    if (!(i < len && j < len)) {
        throw ('行标或列标超出范围: 0~'+(len-1))
    }
    let detArr = JSON.parse(JSON.stringify(this.array))
    let newArr = []
    for (let k = 0; k < len; k++) {
        if (i != k) {
            let temp = detArr[k]
            temp.splice(j, 1)
            newArr.push(temp)
        }
    }

    return new Det(newArr)
}
```

`line 15~19` 如果`k`等于`i`就跳过（同一行），如果不是，那就移除该行的第`j`个元素，并添加到新数组中。最后生成`Det`对象。

测试：
```js
let det = new Det([
    [1, 1, 2, 1],
    [1, -3, 5, 3],
    [0, 2, 2, 2],
    [1, 2, -4, 4]
])
let c0 = det.complementMinor(0, 0)
// 输出
// [-3, 5, 3]
// [2, 2, 2]
// [2, -4, 4]

let c1 = det.complementMinor(3, 2)
// 输出
// [1, 1, 1]
// [1, -3, 3]
// [0, 2, 2]

```

引理：一个`n`阶行列式，如果其中第`i`行所有元素除`aij`外都为零，那么这行列式等于`aij`与它的代数余子式的乘积，即`D=aijAij`

![](./equation0.png)

测试：
```js
let det1 = new Det([
    [1, 3, 2, 5],
    [5, -3, -1, 3],
    [0, 0, -2, 0],
    [-5, 2, 0, 4]
])
det1.calc() //296
let c2 = det1.complementMinor(2, 2)
let a0 = -2 * Math.pow(-1, 2 + 2) * c2.calc() //-2 * (-148)
console.log(a0) //296
```

### 行列式按行（列）展开法则

**定理** 行列式等于它的任一行（列）的各元素与其对应的代数余子式乘积之和，即：
![](./equation1.png)

在`Det`对象上添加通过`代数余子式`来计算行列式的值的方法`calcViaComplement`:
```js
/**
  * 通过代数余子式来计算行列式的值
  * 
  * @param {Number} i 行
  */
Det.prototype.calcViaComplement = function (i=0) {
    let len = this.length
    if (!(i < len)) {
        throw ('行标或列标超出范围: 0~'+(len-1))
    }
    let sum = 0
    for (let k = 0; k < len; k++) {
        let tempDet = this.complementMinor(i, k)
        sum += tempDet.calc() * Math.pow(-1, k + i) * this.array[i][k]
    }

    return sum
}
```
这里默认以行来计算，默认第0行，可以通过计算不同行来验证：
```js
let det1 = new Det([
    [1, 3, 2, 5],
    [5, -3, -1, 3],
    [0, 0, -2, 0],
    [-5, 2, 0, 4]
])
let res0 = det1.calc()
let res1 = det1.calcViaComplement(0)
let res2 = det1.calcViaComplement(2)

console.log('res0=' + res0) //296
console.log('res1=' + res1) //296
console.log('res2=' + res2) //296
```

**推论** 行列式任一行（列）的元素与另一行（列）的对应元素的代数余子式乘积之和等于零。

![](./equation2.png)

相当于用`j`行替换掉第`i`行，此时有两行的对应列元素都相等，根据`性质4：行列式中如果有两行（列）元素成比例，则此行列式为零`，其结果为零。

### 代码

- [tomfriwel/linearAlgebraPro](https://github.com/tomfriwel/linearAlgebraPro)

### 参考

- [线性代数-同济大学(第五版)课件 [完整版]](https://wenku.baidu.com/view/e3efed47fe4733687e21aafd?pn=51)