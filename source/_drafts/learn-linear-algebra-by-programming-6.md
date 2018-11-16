---
title: 通过编程来学习线性代数6-矩阵
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
        this.rowLength = array[0].length;
        this.columnLength = array.length;
    }

    print() {

    }

    // add operation
    static add(mat0, mat1) {
        if (mat0.rowLength != mat1.rowLength && mat0.columnLength != mat1.columnLength) {
            throw new Error("只有同型矩阵才能进行加法运算");
        }

        let newArray = new Array(mat0.columnLength);
        for (let i = 0; i < mat0.columnLength; i++) {
            if(!newArray[i]) {
                newArray[i] = new Array(mat0.rowLength);
            }
            for (let j = 0; j < mat0.rowLength; j++) {
                newArray[i][j] = mat0.array[i][j] + mat1.array[i][j];
            }
        }

        return new Mat(newArray);
    }

    // subtract operation
    static subtract(mat0, mat1) {
        if (mat0.rowLength != mat1.rowLength && mat0.columnLength != mat1.columnLength) {
            throw new Error("只有同型矩阵才能进行加法运算");
        }

        let newArray = new Array(mat0.columnLength);
        for (let i = 0; i < mat0.columnLength; i++) {
            if(!newArray[i]) {
                newArray[i] = new Array(mat0.rowLength);
            }
            for (let j = 0; j < mat0.rowLength; j++) {
                newArray[i][j] = mat0.array[i][j] - mat1.array[i][j];
            }
        }

        return new Mat(newArray);
    }

    add(mat) {
        return Mat.add(this, mat)
    }

    subtract(mat) {
        return Mat.subtract(this, mat)
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

```js
static multiplyNumber(mat, n) {
    let newArray = new Array(mat.columnLength);
    for (let i = 0; i < mat.columnLength; i++) {
        if(!newArray[i]) {
            newArray[i] = new Array(mat.rowLength);
        }
        for (let j = 0; j < mat.rowLength; j++) {
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