# Draw Chess Board using Python

#*************Import package**************
import turtle

#*************Create screen object**********
sc = turtle.Screen()

#*************Create turtle object**********
pen = turtle.Turtle()

#*************method to draw square************
def draw() :
    for i in range(4) :
        pen.forward(30)
        pen.left(90)
    pen.forward(30)

#*************Driver Code***************
if __name__=="__main__":

    sc.setup(600, 600)    #setup scrren

    pen.speed(100)        #set turtle object speed

    for i in range(8) :    #loop for board
        pen.up()            #not ready to draw
        pen.setpos(0, 30 * i)    # set position for every row
        pen.down()                #ready to draw
        for j in range(8) :       # row
            if (i + j) % 2 == 0 :
                col = 'black'

            else :
                col = 'white'

            pen.fillcolor(col)    #fill with given color
            pen.begin_fill()       #start filling with color
            draw()
            pen.end_fill()         #stop filling
    pen.hideturtle()


