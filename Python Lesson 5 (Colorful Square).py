import turtle
t=turtle. Turtle()
t.pensize(6)
turtle.bgcolor("black")
cols=['red','orange','yellow','green','indigo','magenta']
t.penup()
t.backward(150)
t.right(90)
t.forward(150)
t.left(90)
t.pendown()

for m in range(6):
    t.goto(-150,-15)#+n*50)
    t.pendown()
    for n in range(6):
        t.color(cols[n])
        t.begin_fill()
        for i in range(4):
            t.forward(20)
            t.left(90)
        t.penup()
        t.forward(50)
        t.pendown()
        t.end_fill()
    t.penup()
    t.hideturtle()
#print(t.xcor(),t.ycor())
#magenta(zise)
#hexadecimal color picker on google

print(t.xcor(),t.ycor())
turtle.title("Colorful Square")
