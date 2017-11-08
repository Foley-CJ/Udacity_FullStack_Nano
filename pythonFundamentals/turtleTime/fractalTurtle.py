"""
Understanding and coding fractal with real design

"""
#
#
# from turtle import Turtle, Screen
#
# window = Screen()
# window.bgcolor('blue')
#
# fractalTurtle = Turtle()
# fractalTurtle.speed(5)
#
# fractalTurtle.right(60)
#
# def triangle(size):
#
#     for x in range(3):
#         fractalTurtle.forward(size)
#         fractalTurtle.right(120)
#
#
#
# depth = 1
# size = 100
#
#
# def fractal(depth,size):
#
#     triangle(size)
#     if depth ==0:
#         return
#     else:
#         fractal(depth-1)
#
#
#
#
#
#
#
#
#
# # import math
# # currSize = 100
# #
# #
# # triangle(100)
# # yPos = math.sqrt(currSize**2-(0.5*100)**2)
# # xPos = 0.5*currSize
# # fractalTurtle.penup()
# # fractalTurtle.setpos(currSize,0)
# # fractalTurtle.pendown()
# # triangle(100)
#
# # import math
# #
# # depth = 10
# #
# # widthDepth = depth
# # heightDepth = widthDepth-1
# #
# # currSize = 200.0/depth
# yPos, xPos = 0,0
#
# for y in range(heightDepth):
#     startPoint = xPos
#     for x in range(widthDepth):
#         triangle(currSize)
#         xPos += currSize
#         fractalTurtle.penup()
#         fractalTurtle.setpos(xPos,yPos)
#         fractalTurtle.pendown()
#
#     widthDepth -= 1
#     yPos += math.sqrt(currSize**2-(0.5*currSize)**2)
#     xPos = startPoint+(currSize*0.5)
#     fractalTurtle.penup()
#     fractalTurtle.setpos(xPos, yPos)
#     fractalTurtle.pendown()
# triangle(currSize)


















import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange','black','purple']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myTurtle.speed(0)
   myWin = turtle.Screen()
   myPoints = [[-400,-220],[0,380],[400,-220]]
   sierpinski(myPoints,7,myTurtle)
   myWin.exitonclick()

main()












# for y in range(10):
#
#     for x in range(3):
#         fractalTurtle.forward(100)
#         fractalTurtle.right(120)
#
#     fractalTurtle.setpos(5*y,5*y)



# def f(length, depth):
#     if depth == 0:
#         fractalTurtle.forward(length)
#     else:
#         f(length / 2, depth - 1)
#         fractalTurtle.right(60)
#
#         f(length / 4, depth - 1)
#         fractalTurtle.right(60)
#
#         f(length / 5, depth - 1)
#         fractalTurtle.left(20)
#
#         f(length / 6, depth - 1)
#         fractalTurtle.right(60)






window.exitonclick()