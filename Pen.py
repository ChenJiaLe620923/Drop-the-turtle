import matplotlib.pyplot as plt
import math


class Pen():
    def __init__(self, angle=0, x=0, y=0, size=1):
        self.angle = angle
        self.radian = self.angle / 360 * 2 * math.pi
        self.x = x
        self.y = y
        self.size = size
        self.color = 'black'
        self.linestyle = '-'
        self.marker = 'o'

    def draw_line(self, list_x, list_y):
        ax = plt.gca()  
        ax.set_aspect('equal')  
        ax.plot(list_x,
                list_y,
                linewidth=self.size,
                color=self.color,
                linestyle=self.linestyle,
                marker=self.marker)
        return self

    def penup(self):
        self.linestyle = ''
        return self

    def pendown(self):
        self.linestyle = '-'
        return self

    def pu(self):
        self.penup()
        return self

    def pd(self):
        self.pendown()
        return self

    def isdown(self):
        return True if self.linestyle else False

    def pencolor(self, color):
        self.color = color
        return self

    def goto(self, x, y):
        self.draw_line([self.x, x], [self.y, y])
        self.x = x
        self.y = y
        return self

    def jump_to(self, x, y):
        self.pu()
        self.goto(x, y)
        self.pd()
        return self

    def fd(self, length):
        new_x = self.x + math.cos(self.radian) * length  
        new_y = self.y + math.sin(self.radian) * length  
        self.goto(new_x, new_y)
        self.x = new_x
        self.y = new_y
        return self

    def forward(self, length):
        self.fd(length)
        return self

    def backward(self, length):
        self.fd(0 - length)
        return self
    
    def towards(self,n):
        self.angle = n
        self.radian = self.angle / 360 * 2 * math.pi
        return self 
    
    def rt(self, n):
        self.angle += n
        self.radian = self.angle / 360 * 2 * math.pi
        return self

    def lt(self, n):
        self.rt(360 - n)
        return self

    def right(self, n):
        self.rt(n)
        return self

    def left(self, n):
        self.lt(n)
        return self

    def pensize(self, n):
        self.size = n
        return self

    def clear(self):
        plt.cla()
        return self

    def Drawing_regular_polygon(self, n, length): 
        for i in range(n):
            self.fd(length)
            self.right(360 / n)
    def Drawing_regular_polygon_self(self,n,length):
        init_angle = self.angle
        init_radian = init_angle / 360 * 2 * math.pi

        X,Y = [],[]
        for i in range(n+1):
            X.append(length * math.cos(init_radian + i * 2 * math.pi / n))
            Y.append(length * math.sin(init_radian + i * 2 * math.pi / n))

        self.draw_line(X, Y)
        return self
    def square(self,length):
        self.Drawing_regular_polygon_self(4,length)
        return self
    def circle(self,length):
        self.Drawing_regular_polygon_self(360,length)
        return self
    def ls(self,w='F--F--F--',a=60,r={'F':'F+F--F+F'},n=3):
        w = w
        a = a
        r = r
        n = n
        for i in range(n):
            for j in r:
                w = w.replace(j,r[j])
        state_arr = []
        for s in w:
            if s == 'F':
                self.forward(100)
            elif s == '+':
                self.rt(a)
            elif s == '-':
                self.rt(-a)
            elif s == '[':
                state_arr.append([p.x,p.y,p.angle])
            elif s == ']': #s==']'
                x,y,angle = state_arr.pop()
                self.jump_to(x,y).towards(angle)
        print(w)
        return self
        
