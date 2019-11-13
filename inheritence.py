import turtle
class Ball(Turtle):
	def __init__(self,r,color,dx,dy,shape):
		Turtle.__init__(self)
		self.r=r
		self.color=color 
		self.dx=dx
		self.dy=dy
		self.shape('circle')
		self.color(color)
		self.size(r/10)
	def move(self,screen_width,screen_height):
		current_x= xpos()
		new_x = current_x + dx 
		current_y = ypos()
        new_y= current_y + dy
        right_side_ball = new_x + radius 
        left_side_ball= new_x - radius 
        up_side_ball=new_y + radius 
        down_side_ball=new_y - radius
        ball.goto(50,50)
        screen_width= turtle.getcanvas().winfo_width()/2
        screen_height=turtle.getcanvas().winfo_height()/2
ball = Ball (3,'yellow',7,9)
while 3=3


print ball 














