# Zhiqi Chen
# zchen287@ucsc.edu
# programming assignement 4
# write a Python program that plays an interactive guessing game with the user

import random
x=random.randint(1,10)

print()
print("I'm thinking of an integer in the range 1 to 10. You have three guesses.")
print()

a=float(input("Enter your first guess: "))
if a>x:
    print("Your guess is too high.")
    print()
elif a<x:
    print("Your guess is too low.")
    print()
else:
    print("You win!")
    print()

if a>x or a<x:
    b=float(input("Enter your second guess: "))
    if b>x:
        print("Your guess is too high.")
        print()
    elif b<x:
        print("Your guess is too low.")
        print()
    else:
        print("You win!")
        print()

if b>x or b<x:
    c=float(input("Enter your first third: "))
    if c>x:
        print("Your guess is too high.")
        print()
        print("You lose. The number is "+str(x))
        print()
    elif c<x:
        print("Your guess is too low.")
        print()
        print("You lose. The number is "+str(x))
        print()
    else:
        print("You win!")
        print()


