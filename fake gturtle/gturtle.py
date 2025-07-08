import turtle


class gturtle:
    def __init__(self):
        self.t = turtle.Turtle()

    def forward(self, distance):
        self.t.forward(distance)

    def right(self, right):
        self.t.right(right)

    def left(self, left):
        self.t.left(left)

    def color(self, colorb):
        self.t.color(colorb)

    def backward(self, backwarde):
        self.t.backward(backwarde)

    def goto(self, gotodo):
        self.t.goto(gotodo)

    def setx(self, xset):
        self.setx(xset)

    def sety(self, yset):
        self.t.sety(yset)

    def circle(self, circle):
        self.t.circle(circle)

    def gohome(self):
        self.t.home()

    def setheading(self, angle):
        self.t.setheading(angle)

    def shape(self, shape):
        self.t.shape(shape)

    def register_shape(addshape):
        return turtle.register_shape(addshape)

    def bgcolor(bgcolor):
        return turtle.bgcolor(bgcolor)

    def bgpic(bgpic):
        return turtle.bgpic(bgpic)

    def title(title):
        return turtle.title(title)

    def clear():
        return turtle.clear()

    def quit():
        return turtle.bye()

    def exitonclick():
        return turtle.exitonclick()
