/*
program to print youtube logo using Turtle module in Python
*/

import turtle
i=turtle.Turtle()
i.up()
i.goto(-400,200)
i.down()
i.color('red')
i.begin_fill()
i.forward(800)
i.circle(-30,90)
i.forward(500)
i.circle(-30,90)
i.forward(800)
i.circle(-30,90)
i.forward(500)
i.circle(-30,90)
i.end_fill()
i.color('white')
i.up()
i.goto(-70,40)
i.begin_fill()
i.right(90)
i.down()
for j in range(3):
      i.forward(230)
      i.left(360/3)
i.end_fill()      
turtle.done()
