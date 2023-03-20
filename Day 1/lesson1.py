from turtle import*

#we wamnt to draw a house

penup()
goto(-100, -100)
pendown()

#step 1: draw a square
speed(25)
width(7)
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing door

forward(30)
width(4)
color("black")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
#end of door

penup()
goto(100, 100)
pendown()

#drawing roof

width(7)
color("red")

right(150)
forward(200)
left(120)
forward(200)

#end of roof

penup()
goto(15, 20)
pendown()

#drawing window
width(4)
color("black")
left(120)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)

penup()
goto(15, -10)
pendown()

right(90)
forward(60)

penup()
goto(45, 20)
pendown()

right(90)
forward(60)
#end of window

#creating bonus 3rd dimension wall and roof

penup()
goto(100, -100)
pendown()

width(7)
color("brown")
left(135)
forward(200)

penup()
goto(100, 100)
pendown()

forward(200)
right(135)
forward(200)

penup()
goto(0, 273)
pendown()


color("red")

left(135)
forward(200)
right(105)
forward(200)
right(75)
forward(200)
right(45)
forward(200)

#end of 3rd dimensional wall and roof




exitonclick()
