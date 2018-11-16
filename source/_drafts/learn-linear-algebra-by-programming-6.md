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