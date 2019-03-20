import  turtle
a= turtle.Turtle()
a.shape("turtle")
t=turtle.Pen()
colors=['red','purple','blue', 'green','orange' ,'yellow']
turtle.bgcolor('black')

def sequ():
    for i in range(4):
        a.color("green")
        a.forward(100)
        a.left(90)
    for i in range(5):
        a.color("blue")
        a.forward(100)
        a.left(72)
sequ()
a.left(65)
a.forward(110)
a.right(127)
a.forward(113)
a.clear()
def circl():
    a.speed(700)
    for i in range(36):
        for i in range(36):
            a.forward(10)
            a.right(10)
            a.color("red", "green")
        a.right(10)
circl()
a.clear()
def hamee():
    a.speed(700)
    for i in range(360):
        a.pencolor(colors[ i % 6 ])
        a.width( i / 100 + 1 )
        a.forward(i)
        a.left(59)
hamee()
a.clear()
def star():
    for i in range(50):
        a.forward(50)
        a.right(144)

star()
a.penup()
a.forward(200)
a.pendown()
star()
a.penup()
a.left(90)
a.forward(200)
a.pendown()
star()


turtle.done()
