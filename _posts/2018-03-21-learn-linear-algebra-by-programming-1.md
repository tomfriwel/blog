---
layout: post
title:  "通过编程来学习线性代数1-解二元线性方程组"
date: '2018-03-21 10:11:47'
comments: true
---

### 环境

采用的编程方式是网页，会使用`javascript`来实现线性代数中的计算方法。
比如文件***linearAlgebra.html***:
```html
<script>
    // 在控制台打印
    console.log(123*2)
</script>
```

写入上面的代码，保存后用浏览器打开，然后右键打开*审查元素*点击*控制台（Console）*来查看输出。

> 更多网页相关知识网上可以搜得到，掌握基本`javascript`编程知识就行了。

### 解二元线性方程组

`行列式`的概念是由解多元线性方程组而引出的。比如下面这个：


{% include image.html url="/assets/images/linear-algebra/101.jpeg" description="二元线性方程组" %}

在坐标系中就是两根直线，分母为零的情况就是两根直线平行不相交。

##### 1. 绘制坐标系

下面是我用`canvas`绘制的坐标系，一般编程中涉及到坐标系的地方，跟数学里有些不同，y轴方向是向下为正。

{% include image.html url="/assets/images/linear-algebra/103.png" description="canvas坐标系" width=800 %}

{% include image.html url="/assets/images/linear-algebra/106.gif" description="canvas坐标系" width=800 %}

那么来看看如何绘制出坐标系。下面主要是编程方面的东西，可以自己创建一个`.html`文件试一试。

首先，创建`canvas`
```html
<html>
    <body>
        <canvas id="myCanvas"></canvas>
    </body>
</html>
<!-- Javascript 代码放在标签script里 -->
<script type="text/javascript">
    // 保存canvas的长宽
    var W = 800.0, H = 600.0

    // 获取canvas对象
    var canvas = document.getElementById('myCanvas')
    canvas.width = W
    canvas.height = H

    // 获取canvas的画布context，我们所有的绘制都将在context上完成。
    // 这里也可以传3d，那么context就是一个3d的画布
    var ctx = canvas.getContext('2d')
</script>
```

画布创建好后，接下来着手绘制直角坐标系的两根辅助线。

创建一个函数方便之后的重复调用。

```js

// 因为原点是从左上角开始的，为了方便看直线，将原点偏移到指定位置
// 每一个设置坐标的地方都要(x + originX, y + originY)
var originX = W / 2.0, originY = H / 2.0

// 调用函数，传入之前创建好的画布ctx
drawCoordinateSystem(ctx)

function drawCoordinateSystem(ctx) {
    // 设置绘制线的颜色为black
    ctx.strokeStyle = 'black'

    // 线宽度
    ctx.lineWidth = 1

    // 水平线
    ctx.beginPath()
    ctx.moveTo(0, 0 + originY)  // 画布的左边界中点
    ctx.lineTo(W, 0 + originY)    // 画布的右边界中点
    ctx.closePath()
    ctx.stroke()

    // 垂直线
    ctx.beginPath()
    ctx.moveTo(0 + originX, 0)  // 画布的上边界中点
    ctx.lineTo(0 + originX, H)  // 画布的下边界中点
    ctx.closePath()
    ctx.stroke()
}
```

`moveTo`是设置一个起点，`lineTo`是将线从上一个点连接到该点。

`stroke`绘制线条，如果`fill`，那么会将线包围的区域用颜色涂满。途中的黑色三角形方向标就是这样绘制的，设置三个点后调用`fill`。

调用函数后得到下图：
{% include image.html url="/assets/images/linear-algebra/104.png" description="canvas坐标系" width=500 %}

阴影样式需要给`canvas`加上一个`box-shadow`：

`<canvas id="myCanvas" style="box-shadow:1px 1px 10px #666;"></canvas>`

##### 2. 绘制坐标系刻度和方向标

同样，分别创建函数来专门绘制刻度和方向标：

```js
// 刻度长度
var scaleD= 10.0

// 绘制刻度
// 传入context和刻度长度
function drawScale(ctx, d) {
    // horizontal
    for (var x = 0; x < W; x += 50) {
        ctx.beginPath()
        ctx.moveTo(x, 0 + originY)
        ctx.lineTo(x, scaleD + originY)
        ctx.stroke()
        ctx.closePath()
    }

    // vertical
    for (var y = 0; y < H; y += 50) {
        ctx.beginPath()
        ctx.moveTo(0 + originX, y)
        ctx.lineTo(scaleD + originX, y)
        ctx.stroke()
        ctx.closePath()
    }
}

//绘制方向标（三角形），底边长度与底边到顶点长度一样的三角形
function drawDirectionArrow(ctx, d) {
    // horizontal
    ctx.beginPath()
    ctx.moveTo(W - d * 2, originY - d)
    ctx.lineTo(W - d * 2, originY + d)
    ctx.lineTo(W, originY)
    ctx.closePath()
    ctx.fill()

    // vertical
    ctx.beginPath()
    ctx.moveTo(originX - d, H - d * 2)
    ctx.lineTo(originX + d, H - d * 2)
    ctx.lineTo(originX, H)
    ctx.closePath()
    ctx.fill()
}
```

然后在`drawCoordinateSystem`函数里追加调用`drawScale(ctx, scaleD)`和`drawDirectionArrow(ctx, scaleD)`，运行后如图：

{% include image.html url="/assets/images/linear-algebra/105.png" description="canvas坐标系" width=500 %}

如果想要在刻度上绘制数字标记，可以自行搜索相关文档，有一个叫[fillText](http://www.w3school.com.cn/tags/canvas_filltext.asp)的函数。

##### 3. 绘制直线

`a11 * x1 + a12 * x2 = b1` 此方程相当于 `a * x + b * y = c`。

我们可以根据直线方程找到两个点，将两个点通过`moveTo`和`lineTo`连接并绘制出来。

```js
//---绘制直线---
// 传入直线方程的三个常数和直线颜色
/* 
    a * x + b * y = c,

    在 x, y 轴上的点
    x = 0 && b != 0, y = c / b => (0, c / b)
    y = 0 && a != 0, x = c / a => (c / a, 0)

    b != 0, y = c / b => (x, (c - a * x) / b)
    a != 0, x = c / a => ((c - b * y) / a, y)
*/
function drawLine(ctx, a, b, c, color = 'red') {
    // 如果有一个为零，那么直线就是平行于x或y轴的
    if (b != 0 && a != 0) {
        var x1 = c / a, y1 = 0  // x轴上的点
        var x2 = 0, y2 = c / b  // y轴上的点
        var x3 = -originX, y3 = (c - a * x3) / b    //左边界点
        var x4 = originX, y4 = (c - a * x4) / b    //右边界点

        ctx.strokeStyle = color
        ctx.lineWidth = 1

        //  绘制直线
        ctx.beginPath()
        ctx.moveTo(x3 + originX, y3 + originY)
        ctx.lineTo(x4 + originX, y4 + originY)
        ctx.closePath()
        ctx.stroke()
    }
}
```

然后调用该函数绘制：

```
drawLine(ctx, 1, 1, 123, 'red')
drawLine(ctx, 1, 5, 999, 'blue')
```

结果：

{% include image.html url="/assets/images/linear-algebra/107.png" description="canvas坐标系" width=500 %}

##### 4. 求出两直线的交点

说了这么多，现在才开始解方程？😤

大多是基础的绘制工作。数学和编程相结合的地方就是如何根据直线方程绘制直线。

对于方程：

```
╭ a11*x1 + a12*x2 = b1
╰ a21*x1 + a22*x2 = b2
```

当`a11*a22 - a12*a21 != 0`时，方程有唯一解：
```js
x1 = (b1*a22 - a12*b2)/(a11*a22 - a12*a21)

x2 = (a11*b2 - b1*a21)/(a11*a22 - a12*a21)
```

```js
    |a11 a12|
D = |       | = a11*a22 - a12*a21 //分母
    |a21 a22|

     |b1 a12|
D1 = |      | = b1*a22 - a1*b2 //x1分子
     |b2 a22|

     |a11 b1|
D2 = |      | = a11*b2 - b1*a21 //x2分子
     |a21 b2|

x1 = D1/D
x2 = D2/D
```

那么我们就可以根据这个来得出两直线相交的点`(x1, x2)`

下面一个函数是根据两直线的常数计算出交点。第二个函数是在以`(x, y)`为圆心，半径为10，绘制一个圆

```js
/*
    a11 > a1
    a21 > b1
    b1 > c1
    ...
    计算两直线交点
*/
function calculateIntersection(a11, a12, b1, a21, a22, b2) {
    x1 = (b1 * a22 - a12 * b2) / (a11 * a22 - a12 * a21)
    x2 = (a11 * b2 - b1 * a21) / (a11 * a22 - a12 * a21)

    return {
        x: x1,
        y: x2
    }
}

// 绘制交点
function drawIntersection(ctx, x, y) {
    ctx.arc(x+originX, y+originY, 10, 0, 2*Math.PI)
    ctx.fill()
}
```

最后，我们的绘制函数大概是这样的：

```js

drawCoordinateSystem(ctx)
drawLine(ctx, 1, 1, 123, 'red')
drawLine(ctx, 1, 5, 999, 'blue')

var p = calculateIntersection(1, 1, 123, 1, 5, 999)
drawIntersection(ctx, p.x, p.y)
```

结果如图：

{% include image.html url="/assets/images/linear-algebra/108.png" description="canvas坐标系" width=500 %}

### 总结

上面求两直线交点的思路是根据`二阶行列式`来解`二元线性方程组`。可以看到，`行列式`是根据解`多元线性方程组`总结出来的。二阶或三阶行列式我们可以比较轻松的计算出结果，但是随着阶数增加，计算量也会越来越大，`n`的`阶乘`（`n*n(n-1)*...*3*2*1`）

我们来看看求`二阶行列式`和`三阶行列式`的值的计算：

```js
// 计算二阶行列式的值
/*
|a11 a12|
|a21 a22|
*/
function calculate2Det(a11, a12, a21, a22) {
    // 2!
    return a11*a22 - a12*a21
}

// 计算三阶行列式的值
/*
|a11 a12 a13|
|a21 a22 a23|
|a31 a32 a33|
*/
function calculate3Det(a11, a12, a13, a21, a22, a23, a31, a32, a33) {
    // 3!
    return a11*a22*a33 + a12*a23*a31 + a13*a21*a32 - a13*a22*a31 - a12*a21*a33 - a11*a23*a32
}
```

如果是`四阶行列式`，那么我们要写`4!=24`个。所以我们要想办法简化计算，使用一种通用的方式来计算`行列式`的值，而不是一个一个全部写出来计算。

那么编程上如何简化这个计算呢？

下一节将会来解决这个问题。