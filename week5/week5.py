# import random
#
# for i  in range(10):
#     print(random.random())



# import random
# for i in range(10):
#     print(random.randint(25,35))



# import math
#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
#
# c = math.sqrt(a**2 + b**2)
#
# print(c)



# import math
#
# def areaofcircle(r):
#     return math.pi * r**2
# print(areaofcircle(3))


# import turtle
#
# alex = turtle.Turtle()
# screen = turtle.Screen()
#
# for i in range(5):
#     alex.forward(100)
#     alex.right(144)
#
# screen.exitonclick()


# import turtle
#
# def drawstar(t , side):
#     for i in range(5):
#         t.forward(side)
#         t.left(144)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# drawstar(tess, 100)
#
# screen.exitonclick()


# def drawsquare(t, side):
#     for i in range(4):
#         t.forward(side)
#         t.left(90)
#
# import turtle
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.pensize(3)
#
# for i in range(5):
#     drawsquare(tess, 20)
#     tess.penup()
#     tess.forward(40)
#     tess.pendown()
# screen.exitonclick()



import turtle
tess = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("lightgreen")
tess.color("black")
tess.pensize(3)


def drawsquare(t, side):
    for i in range(4):
        t.forward(side)
        t.left(90)

for i in range(20, 120, 20):
    drawsquare(tess, i)
    tess.penup()
    tess.backward(10)
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()


screen.exitonclick()