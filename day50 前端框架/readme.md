# 前端框架

- bootstrap
- https://fa.quickso.cn/examples.html fontwesome图标库
- sweetalert 弹窗效果集
- elementUI

## 1.如何引入框架
每种框架的引入方式都几乎一致。框架依赖jquery所以框架正常工作的前提是正常引入了jquery.

- 把文件下载到本地，直接引用。
- 通过cdn方式引入，适合经常有网的电脑。

框架的目录结构
```bash
# 带有min是压缩之后的内容，没有换行，效果与未压缩的一致。
# 我们只需要保留字体文件、样式、和框架js

js/bootstrap.min.js
fronts/
css/bootstrap.min.css
```

```html
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
    <link rel="stylesheet" href="bootstrap-3.3.7-dist/css/bootstrap.min.css">
    <script src="bootstrap-3.3.7-dist/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="sweetalert/dist/sweetalert.css">
    <script src="sweetalert/dist/sweetalert.min.js"></script>
```

## 2.流式布局容器
布局容器有两种方式，居中和铺满。
class="container" 占中间
class="container-fluid" 占全部

## 3.栅格系统(重要)

框架把一行分成12份，在布局的时候只需要改动class的属性就可以修改样式的显示效果。

```bash
class的作用

row  栅格系统的一行
col-sm-1    电脑显示器的样式
col-sm-n    n 表示栅格的几份
col-lg-offset-3   栅格偏移几份
```