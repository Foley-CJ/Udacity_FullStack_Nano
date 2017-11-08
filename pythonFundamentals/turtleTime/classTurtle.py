"""
Playing with turtle.Turtle to understand classes and inheritence.

Drawing a square, a circle or something different
"""


from turtle import Turtle, Screen


class artTurtle(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.window = Screen()
        self.window.bgcolor('blue')


    def draw_shape(self, sides=4, newColor='black', directCall=True):
        self.color(newColor)
        print directCall

        for x in range(sides):
            self.forward(100)
            self.right(360/sides)

        if(directCall):
            print 'draw_shape ended'
            self.window.exitonclick()



    def repeat_shape(self, iterations, directCall=True, **new_args):

        for y in range(iterations):
            self.right(360/iterations)
            self.draw_shape(directCall=False,**new_args)

        if (directCall):
            self.window.exitonclick()



testD = artTurtle()

testD.repeat_shape(20,newColor='orange',sides=3)












