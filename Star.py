# Zhiqi Chen
# zchen287@ucsc.edu
# programming assignement 3
# Write a Python program that uses the turtle module to draw an n pointed star

n=int(input("Enter an odd integer greater than or equal to 3: "))
        
import turtle
wn=turtle.Screen()
wn.bgcolor("white")
wn.title(str(n)+"-pointed star")

turtle=turtle.Turtle()
turtle.hideturtle()
turtle.pencolor("blue")
turtle.pensize(2)
turtle.speed(0)

if n%2==1:
    turtle.fillcolor("lime")
    turtle.begin_fill()
    turtle.penup
    turtle.setpos(-150,0)
    turtle.goto(150,0)
    turtle.pendown

    for x in range(n):
        turtle.right(180-(180/n))
        turtle.forward(300)
        turtle.dot(10,"red")

    turtle.end_fill()

if n%2==0:
    print("Wrong input")

wn.mainloop()


