import colorgram
import random
import turtle as t
from turtle import Screen

"""
colors = colorgram.extract("image.png", 30)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    c = (r, g, b)
    color_list.append(c)

print(color_list)
"""
screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 5, screen.window_height() - 1)

color_list = [(200, 167, 110), (237, 241, 246), (144, 74, 52), (169, 152, 45), (58, 92, 119), (224, 203, 131), (136, 162, 180), (131, 34, 26), (51, 117, 89), (199, 94, 72), (143, 25, 30), (18, 97, 74), (69, 47, 40), (173, 146, 153), (150, 177, 152), (131, 70, 74), (56, 43, 46), (237, 174, 163), (184, 88, 94), (38, 58, 71), (28, 82, 89), (182, 204, 178), (242, 156, 160), (93, 144, 124), (20, 66, 57), (36, 65, 96), (108, 125, 154)]
turtle = t.Turtle()
turtle.speed("fastest")
screen.colormode(255)

def drawHirstPainting(turtle, color_list):
    """Method that draws Hirst dot painting"""
    count = 0
    while count < 206:
        color = random.choice(color_list)
        turtle.dot(17, color)
        turtle.penup()
        turtle.forward(80)
        turtle.pendown()
        if count % 12 == 0 and count != 0:
            turtle.penup()
            turtle.sety(turtle.ycor() + 50)
            turtle.setx(0)
            turtle.pendown()
        count += 1


drawHirstPainting(turtle, color_list)

screen.exitonclick()