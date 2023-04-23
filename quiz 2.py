def foo(a,b):
    return a+b

def bar(c,d):
    return c*d

print(foo(3,5)+bar(3,4))
print(foo("three","five")+bar(2,"four"))
print(bar(3,foo("one","two")))

import turtle
wn=turtle.Screen()
alice=turtle.Turtle()
bob=turtle.Turtle()

alice.pencolor("red")
bob.pencolor("blue")

alice.setpos(0,0)
bob.setpos(0,0)

for x in range(4):
    alice.forward(100)
    alice.left(90)

bob.left(45)
bob.forward(200)

wn.mainloop()
