##########################################################################################################################

##
## CSC 101 Lab week 14
## Program : Inheritance
## Name : Vishista Vuppulapati
## Email : vvd94@umsystem.edu

## Problem : To create and use classes and to Inherit from a previously defined class, also by using Turtle module. 

## Algorithm


import turtle # this is the module

class Point(object): # this was given in the assignment
                     # here a point class is created and a argument is passed in the object.

    def __init__(self, x, y, color): # __init__ it allows the class to initialize the attributes of the class
        self.x = x # here we are assigning the the instance of a class "self" to a varible called x.
        self.y = y # similarly, for y and color.
        self.color = color

    def draw(self): # this is function is defined to draw what we want.
        turtle.penup() # penup() makes sure the pen is picked up and doesnot draw as it moves.
        turtle.goto(self.x, self.y) # goto is used to move the turtle to an absolute position, and here we're passing 2 aruguments
        turtle.pendown() #  pendown puts the turtle's pen down and draws a line when the turtle moves.
        turtle.color(self.color) # this used to change the color of the turtle.
        turtle.setheading(0) # this is used to set the orientation of the turtle to angle. Here we are setting it to 0.
        self.draw_action() 

    def draw_action(self):
        turtle.dot() #  This dot is used to draw a circular dot with a particular size, and with some color.

class Box(Point): # Here we are defining a new sub- class called box and it is also inherited from another class called Point
    def __init__(self, x1, y1, width, height, color): # passing aruguments required for a box.
        super().__init__(x1, y1, color) # this is to inheret the objects of the parent class.
        self.width = width # Assigning argument to a variable width.
        self.height = height # Assigning argument to a variable called height.

    def draw_action(self): # this function is defined for drawing the box.
        for i in range(2):
            turtle.forward(self.width) # this is used to guide the direction of which it has to draw, which will be width of the box.
            turtle.right(90) # this for drawing the box with a particular turn 90.
            turtle.forward(self.height) #this is used to guide the direction of which it has to draw, which will be height of the box.
            turtle.right(90) # this for drawing the box with a particular turn 90.


class BoxFilled(Box): # this function is defined for filling the color inside the box, also this is a sub - class of box.
    def __init__(self, x1, y1, width, height, color, fillcolor): # Again ,__init__ it allows the class to initialize the attributes of the class
        super().__init__(x1, y1, width, height, color) # this is to inheret the objects of the parent class.
        self.fillcolor = fillcolor # Assigning argument to a variable called fillcolor as it wasn't ever defined.

    def draw_action(self):
        turtle.fillcolor(self.fillcolor) # this is used to fill whatsoever color is inputed by the user.
        turtle.begin_fill() # this is used to call just before drawing a shape to be filled.
        Box.draw_action(self)
        turtle.end_fill() # used to Fill the shape drawn after the call begin_fill().


class Circle(Point): # Here we are defining a function called circle which is also a sub - class or say inherited from a class called point(Parent Class)
    def __init__(self, x1, y1, radius, color): # here we are passing all the required arguments for drawing th circle.
        super().__init__(x1, y1, color) #  # this is to inheret the objects of the parent class.
        self.radius = radius # # Assigning argument to a variable called radius.

    def draw_action(self):
        turtle.circle(self.radius) 


class CircleFilled(Circle): # this function is defined for filling the color inside the circle, also this is a sub - class of circle.
    def __init__(self, x1, y1, radius, color, fillcolor): # Again ,__init__ it allows the class to initialize the attributes of the class.
        super().__init__(x1, y1, radius, color) # this is to inheret the objects of the parent class.
        self.fillcolor = fillcolor  #Assigning argument to a variable called fillcolor.

    def draw_action(self):
        turtle.fillcolor(self.fillcolor) # this is used to fill whatsoever color is inputed by the user.
        turtle.begin_fill() # this is used to call just before drawing a shape to be filled.
        Circle.draw_action(self)
        turtle.end_fill() # # used to Fill the shape drawn after the call begin_fill().

if __name__ == '__main__': # this is the main function and it is going to all the class and the inherited classes.
    point = Point(-100, 100, 'blue') # passing values to the class called point. Here x = -100 , y = 100 , color = blue, (x,y) are coordinates.
    point.draw() # this is used for the drawing of the point.
    box = Box(200,210, 150, 140, 'red') # passing values to the class called Box. Here x = 200 , y = 210 ,width = 150 ,
                                        # height = 140, color = red,(x,y) are coordinates.
    box.draw() # this is used for the drawing of the box.
    color_box = BoxFilled(200,210,150,140,'green','blue') # passing values to the class called Box. Here x = 200 , y = 210 ,width = 150 ,
                                        # height = 140, color = green, the color filled is = blue ,(x,y) are coordinates.
    color_box.draw() # this is used for the drawing of the color inside the box.
    circle = Circle(-200,210, 50, 'green') # passing values to the class called circle. Here x = -200 , y = 210 ,radius = 50, color = green, (x,y) are coordinates.
    circle.draw() # this is used for the drawing of the circle.
    color_circle = CircleFilled(-200,210,50,'green','red') # passing values to the class called circlefilled. Here x = -200 , y = 210 ,radius = 50, 
                                                            # color = green, the color filled is = red, (x,y) are coordinates.
    color_circle.draw() # this is used for the drawing of the circle.
    turtle.done()

##########################################################################################################################