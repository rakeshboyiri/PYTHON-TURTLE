import turtle
i=turtle.Turtle()
i.speed(10)
i.pensize(10)
turtle.bgcolor('black')
i.color('skyblue')
i.begin_fill()
i.circle(500)
i.end_fill()
i.color('white')
i.up()
i.goto(-250,250)
i.down()
i.begin_fill()
i.seth(350)
i.circle(400,100)
i.seth(35)
i.fd(70)
i.seth(180)
i.fd(70)
i.seth(45)
i.fd(70)
i.seth(190)
i.fd(70)
i.seth(120)
i.circle(150,150)
i.seth(190)
i.circle(-300,55)
i.seth(270)
i.circle(250,55)
i.seth(160)
i.circle(-300,30)
i.seth(280)
i.circle(250,55)
i.seth(190)
i.circle(-200,40)
i.seth(290)
i.circle(200,55)
i.seth(215)
i.circle(-200,45)
i.seth(320)
i.circle(200,45)
i.end_fill()


turtle.done()
