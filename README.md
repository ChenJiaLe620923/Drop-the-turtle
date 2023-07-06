# Code Explanation (English Version)
## This is a library similar to turtle but with better performance!!!
### Function Explanation
#### draw_line
		Draw a line by providing a list of x-coordinates and y-coordinates as input.
#### penup
		Lift the pen, i.e., don't leave any trace when drawing.
#### pendown
		Put the pen down, i.e., leave a trace when drawing.
#### isdown
		Return whether the pen is down or not.
#### pencolor
		Set the color of the pen.
#### goto
		Move from current x, y coordinates to the specified x, y coordinates.
#### jumpto
		Move from current x, y coordinates to the specified x, y coordinates without leaving any trace.
#### forward
		Move forward in the current direction by a given length.
#### backward
		Move backward in the current direction by a given length.
#### towards
		Set the direction to a specified angle.
#### rt
		Rotate the direction clockwise by a specified angle.
#### lt
		Rotate the direction counterclockwise by a specified angle.
#### pensize
		Set the thickness of the pen.
#### clear
		Clear the canvas.
#### Drawing_regular_polygon
		Draw a regular polygon with a specified number of sides and a given side length.
#### Drawing_regular_polygon_self
		Draw a regular polygon with a specified number of sides, a given side length, and use self as the center.
#### ls
		Draw fractals using L-system. Requires input of w (starting symbol), r (rules), a (angle), and n (iteration count).
        
# 代码讲解（中文版）
## 这是一个类似于turtle的库 但是性能更强！！！
### 函数讲解
#### draw_line 
		画线，要求输入x坐标的列表 和y坐标的列表
#### penup 
		不保留画图痕迹
#### pendown
		保留画图痕迹
#### isdown
		返回是否保留画图痕迹
#### pencolor
		设置画笔颜色
#### goto
		从自己的x,y前往到参数x,y
#### jumpto
		从自己的x,y前往到参数x,y,不保留画图痕迹
#### forward
		朝自己的方向前进length
#### backward
		朝自己的方向后退length
#### towards
		将方向设为参数n
#### rt
		将方向增加参数n
#### lt
		将方向减少参数n
#### pensize
		设置画笔粗细
#### clear
		清空画布
#### Drawing_regular_polygon
		绘制正 参数n 边形 边长为 参数length
#### Drawing_regular_polygon_self
		绘制正 参数n 边形 边长为 参数length，中心为self
#### ls
		用L-system 绘制分形 需要输入w（起始）r（规则） a （角度） n（迭代次数）






