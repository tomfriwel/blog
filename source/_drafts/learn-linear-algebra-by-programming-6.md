---
title: 通过编程来学习线性代数6-矩阵的运算
comments: true
thumbnail: /blog/assets/images/linear-algebra/cover.png
tags:
  - 基础知识
  - 线性代数
date: 2018-11-16 13:44:17
---

矩阵的基本概念这里就不多介绍了。

#### 矩阵的加法

相加的两个矩阵需要为`同型矩阵（行数和列数相等）`，满足`交换律`、`结合律`。

新建一个`Mat`对象来管理矩阵，并添加`add`和`subtract`两个静态方法来处理加减操作：
```js
// matrix object

class Mat {
    constructor(array) {
        console.log(array);
        this.array = array;
        this.rowLength = array.length;
        this.colLength = array[0].length;
    }

    print() {

    }

    // add operation
    static add(mat0, mat1) {
        if (mat0.rowLength != mat1.rowLength && mat0.colLength != mat1.colLength) {
            throw new Error("只有同型矩阵才能进行加法运算");
        }

        let newArray = new Array(mat0.rowLength);
        for (let i = 0; i < mat0.rowLength; i++) {
            if(!newArray[i]) {
                newArray[i] = new Array(mat0.colLength);
            }
            for (let j = 0; j < mat0.colLength; j++) {
                newArray[i][j] = mat0.array[i][j] + mat1.array[i][j];
            }
        }

        return new Mat(newArray);
    }

    // subtract operation
    static subtract(mat0, mat1) {
        if (mat0.rowLength != mat1.rowLength && mat0.colLength != mat1.colLength) {
            throw new Error("只有同型矩阵才能进行加法运算");
        }

        let newArray = new Array(mat0.rowLength);
        for (let i = 0; i < mat0.rowLength; i++) {
            if(!newArray[i]) {
                newArray[i] = new Array(mat0.colLength);
            }
            for (let j = 0; j < mat0.colLength; j++) {
                newArray[i][j] = mat0.array[i][j] - mat1.array[i][j];
            }
        }

        return new Mat(newArray);
    }

    add(mat) {
        return Mat.add(this, mat);
    }

    subtract(mat) {
        return Mat.subtract(this, mat);
    }
}
```

测试：
```js
let mat0 = new Mat([
    [1, 2, 3],
    [2, 1, 3],
]);
let mat1 = new Mat([
    [0, 1.5, 3],
    [5, 1, 3],
]);
let mat2 = new Mat([
    [0, 1.5, 3],
    [5, 1, 3],
    [1, -5, 7],
]);

Mat.add(mat0, mat1);
mat0.add(mat1);
// 0: (3) [1, 3.5, 6]
// 1: (3) [7, 2, 6]

mat0.add(mat2); //error
```


#### 数与矩阵相乘

数`λ`与矩阵`A`相乘，即矩阵的每一项都乘以数`λ`。

满足`结合律`和`分配律`。

```js
    static multiplyNumber(mat, n) {
        let newArray = new Array(mat.rowLength);
        for (let i = 0; i < mat.rowLength; i++) {
            if(!newArray[i]) {
                newArray[i] = new Array(mat.colLength);
            }
            for (let j = 0; j < mat.colLength; j++) {
                newArray[i][j] = mat.array[i][j] * n;
            }
        }

        return new Mat(newArray);
    }
```

验证：
```js
    let mat0 = new Mat([
        [1, 2, 3],
        [2, 1, 3],
    ]);
    // 数与矩阵相乘
    Mat.multiplyNumber(mat0, 2);
    // 0: (3) [2, 4, 6]
    // 1: (3) [4, 2, 6]
```

矩阵相加与数乘矩阵合起来，统称为`矩阵的线性运算`。

#### 矩阵与矩阵相乘

![定义](./e1.png)

```js
    static multiply(mat0, mat1) {
        if (mat0.colLength != mat1.rowLength) {
            throw new Error(`mat0(${mat0.rowLength}*${mat0.colLength})的列数不等于mat1(${mat1.rowLength}*${mat1.colLength})的行数，无法进行相乘运算`);
        }

        let newRowLength = mat0.rowLength;
        let newColLength = mat1.colLength;
        let len = mat0.colLength;

        let newArray = new Array(newRowLength);
        for (let i = 0; i < newRowLength; i++) {
            if(!newArray[i]) {
                newArray[i] = new Array(newColLength);
            }
            for (let j = 0; j < newColLength; j++) {
                newArray[i][j] = 0;
                for (let k = 0; k < len; k++) {
                    newArray[i][j] += mat0.array[i][k] * mat1.array[k][j];
                }
            }
        }

        return new Mat(newArray);
    }
```

测试：
```js
// ---矩阵相乘
let a = new Mat([
    [1, 0, -1, 2],
    [-1, 1, 3, 0],
    [0, 5, -1, 4],
]);
let b = new Mat([
    [0, 3, 4],
    [1, 2, 1],
    [3, 1, -1],
    [-1, 2, 1],
]);
Mat.multiply(a, b);
// 0: (3) [-5, 6, 7]
// 1: (3) [10, 2, -6]
// 2: (3) [-2, 17, 10]
```

1. 矩阵乘法不一定满足交换律
2. 矩阵`A!=O, B!=0`， 但有`AB=O`，所以不能从`AB=O`得出`A=O`或者`B=O`

矩阵乘法的运算规律：
1. 乘法结合律 `(AB)C = A(BC)`
2. 数乘和乘法的结合律 `λ(AB) = (λA)B`，其中`λ`是数
3. 乘法对加法的分配率 `A(B + C) = AB + AC, (B + C)A = BA + CA`
4. 单位矩阵在矩阵乘法中的作用类似于数1，即：`E_m * A_mxn =  A_mxn * E_n = A`
5. 矩阵的幂 矩阵为方阵

#### 矩阵的转置

定义跟行列式转置差不多，`A`右上角有个`T`，叫做`A`的转置矩阵

给`Mat`类添加转置方法：
```js
//获取转置矩阵
static getTransposedMat(mat) {
    let rlen = mat.rowLength;
    let clen = mat.colLength;
    let newArr = new Array(clen);

    for (let i = 0; i < clen; i++) {
        if (!newArr[i]) {
            newArr[i] = new Array(rlen);
        }
        for (let j = 0; j < rlen; j++) {
            newArr[i][j] = mat.array[j][i];
        }
    }
    return new Mat(newArr)
}

//获取转置矩阵
getTransposedMat () {
    return Mat.getTransposedMat(this);
}
```

测试：
```js
let b = new Mat([
    [0, 3, 4],
    [1, 2, 1],
    [3, 1, -1],
    [-1, 2, 1],
]);
let bt = b.getTransposedMat();
// 0: (4) [0, 1, 3, -1]
// 1: (4) [3, 2, 1, 2]
// 2: (4) [4, 1, -1, 1]
```

**转置矩阵的运算性质1**：`A`的转置矩阵再转置变回`A`
```js
bt.getTransposedMat();
// 0: (3) [0, 3, 4]
// 1: (3) [1, 2, 1]
// 2: (3) [3, 1, -1]
// 3: (3) [-1, 2, 1]
```

**转置矩阵的运算性质2**：`A+B`的转置等于`A`的转置加上`B`的转置

测试：
```js

```