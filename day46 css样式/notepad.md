## 概要
	1.css
		层叠样式表
	
	2.css学习思路
		1.如何查找标签
		2.如何调节样式
	
	3.css注释
		HTML注释:<!---->
		CSS注释:/**/
		前端语言的注释在使用的时候通常遵循成双成对出现
		<!--导航条开始-->
		<!--导航条结束-->
		
		/*导航条样式开始*/
		/*导航条样式结束*/
		
		
		web框架也有针对html页面的注释
		该注释浏览器检查也是看不到的
		称之为模板语法的注释
		jinja2模块: {#模板语法注释#}
		
		
	CSS语法结构
		选择器 {属性1:值;属性2:值;属性3:值}
		
	1.基本选择器
		元素/标签选择器   直接写标签名
		类选择器		  点 + 类名
		id选择器		  # + id值
		通用选择器			*
	
	2.组合选择器
		后代选择器			空格
		儿子选择器			>
		毗邻选择器			+
		弟弟选择器			~
	
	3.属性选择器
		标签都可以设置自定义属性
		[]
		[hobby]
		[hobby="jdb"]
		input[hobby='xxx']
	
	4.分组和嵌套
		div,span,p {color:red}
		#id,.cl,span {color:red}
	
	5.伪类选择器
		a:link
		a:hover  鼠标悬浮
		a:active
		a:visited
		input:focus  input框获取焦点(被点击选中)
		
	
	6.伪元素选择器
		p:first-letter
		p:before
		p:after
	
	
	选择器优先级
		1.选择器相同的情况下:就近原则
		2.选择器不同的情况下:
			行内>id选择器>类选择器>标签选择器
	
	
	2.如何调节样式

		两个快递盒之间的距离(标签与标签之间的距离) 称之为 外边距(margin)
		纸盒的厚度(边框)    称之为边框(border)
		内部的物品到盒子的距离(内部文本与边框的距离)  称之为 内边距(padding)
		物品本身的大小(文本大小)   称之为内容(content)

		浮动的元素 是脱离正常文档流的 也就意味着没有独占一行一说
		也不再占用原来的位置
		
		浮动的元素 会造成父标签塌陷

		clear  清除浮动带来的负面影响(父标签塌陷)

	
	定位：
		所有的标签默认都是静态的 无法直接调节位置
		你需要先将其设置成可定位状态
		1.相对定位
			相对于标签自身原来的位置
		2.绝对定位
			相对于已经定位过的父标签 
			但只给你一个父标签的长宽 让你做定位  
		3.固定定位
			相对于浏览器窗口 固定在某个位置
		
	浏览器会优先展示文本内容
	
	脱离文档流
		脱离文档流
			1.浮动的元素都是脱离文档流的
			2.绝对定位是脱离文档流的
			3.固定定位也是脱离文档流的
		不脱离文档流
			1.相对定位不脱离文档流

	模态框

	opacity   即可以调节颜色透明度也可以调文本透明度
	
	
## 块标签样式属性
行内标签默认无法设置宽高属性
```text
            width: 200px;  宽
            height: 100px; 长
            border: 1px solid black; 边框属性 粗细 线调类型 颜色
```

## 字体属性

color支持rgb和十六进制
```text
            font-family: 微软雅黑;  字体样式
            font-size: 20px;       字体大小
            color: red;            字体颜色
            font-weight: bold;     加粗字体
            text-decoration: underline;  字体上面加横线
            text-decoration: overline;   字体下面加横线
            text-decoration: line-through;   字体中间加横线
```


## 文字属性

字体在块标签中的对齐方式
```text
      font-size: 16px;    一个字体16px
      text-indent: 32px;  两个字体首行缩进 32px
      text-decoration: none;  取消a标签的下划线 
      text-align: center;   居中对齐
      text-align: left;     靠右
      text-align: right;    靠左
      text-align: justify;  靠左
```

## 背景属性

```text
background: black;   颜色填充
background-image: url("ddg.png");  图片填充，不设置宽高就是内容撑开的大小，会自动重复填充

/*不自动填充*/
background-repeat: no-repeat;

从显示器左上角位置点
background-repeat: repeat-x;  # 距离x轴
background-repeat: repeat-y;  # 距离y轴

background-position: center center;  # 图片居中

background-position: 10px 30px;   /* x轴和y轴方向距离 */

background: orange url("ddg.png") no-repeat center center; # 对上面的综合写法
background-attachment: fixed;   把背景图片固定在窗口
```

## 边框属性

```text
# 参考正方形上下左右
          border-top: red solid 2px;  线条颜色 样式 宽度
          border-left: blue dashed 2px;  长方形虚线
          border-right: yellow dotted 2px;  . 虚线 独占一行会被顶出屏幕外面，设置下宽度就能看到
          border-bottom: purple solid 2px;
          border-radius: 50%; 每个边倒多少圆角

```

## 盒子模型

默认情况下，比如画一个200x200的div,在浏览器上显示的不是顶着浏览器写的，而是有空隙，就是盒子模型导致的。

- 两个快递盒之间的距离(标签与标签之间的距离) 称之为 外边距(margin)
- 纸盒的厚度(边框)    称之为边框(border)
- 内部的物品到盒子的距离(内部文本与边框的距离)  称之为 内边距(padding)
- 物品本身的大小(文本大小)   称之为内容(content)


![](box-model.png)

外距离

```text
margin: 0; 外边距,全部方向置为零
margin: 10px 20px 30px 40px;  顺时针方向影响 auto只能左右居中

# 支持4个方向设置
margin-top: 0;
margin-right: 0;
margin-bottom: 0;
margin-left: 0;
padding: 内容到边框的距离
```

内容到标签的距离
```text
border: 3px solid red;
padding-top: 20px;
padding-left: 10px;
padding-bottom: 30px;
padding-right: 50px;
text-align: right;
padding: 10px;  /* padding 同样支持1 2 3 4个参数  效果同margin*/
```


## 浮动

就是块飘在了空中，浮动的元素是脱离正常文档流的也就意味着没有独占一行一说也不再占用原来的位置。
元素浮动之后，父标签会塌陷，要想把父标签撑起来的固定css
```css
.clearfix:after {
    content: '';
    display: block;
    clear: both;  /* 左右两边都不能有浮动的元素*/
}
```

## 溢出

就是说一个便签固定了大小之后文本长度超过了这个框的限制范围。
```css
overflow: hidden;

auto  内容滑块
hidden 直接隐藏超出部分的内容
visible 直接展示
```


## 定位

- 绝对定位：相对于已经定位过的父标签,只给你一个父标签的长宽让你做定位。
- 相对定位：相对于标签自身原来的位置
- 固定定位：回到顶部


# 脱离文档流的情况

```text
脱离文档流
	1.浮动的元素都是脱离文档流的。
	2.绝对定位是脱离文档流的。
	3.固定定位也是脱离文档流的。

不脱离文档流
	1.相对定位不脱离文档流。
```

## 透明度

```text
opacity: 0.5;   调整字体的透明度
```

# display属性

```text
display: inline-block; /*既有行内标签的属性，又有块级标签的属性*/

inline 行级标签
block  块级标签
```
	