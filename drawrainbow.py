# Draw Rainbow using Turtle in Python

#*******************Importing package**************
import turtle

#*******************Creating turtle screen object**************
sc = turtle.Screen()

#******************Creating turtle object********************
pen = turtle.Turtle()

#******************Define method to form semicircle**********
def semi_circle(col, rad, val) :
    pen.color(col)                      # set the fill color of semicircle
    pen.circle(rad, -180)                #draw a circle
    pen.up()                             # move the turtle to air
    pen.setpos(val, 0)                   # move the turtle to given position
    pen.down()                           # move the turtle to ground

    pen.right(180)

#******************** Set the colors to drawing******************
col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

#********************Set the screen features*****************
sc.setup(600, 600)

#*******************set the screen color black**************
sc.bgcolor('black')

#******************set the turtle features*****************
pen.right(90)
pen.width(10)
pen.speed(7)

for i in range(7) :
    semi_circle(col[i], 10*(i + 8), -10*(i + 1))

#pen.hideturtle()
turtle.done()
     

