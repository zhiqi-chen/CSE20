# Zhiqi Chen
# zchen287@ucsc.edu
# programming assignement 1
# Computes the volume and surface area of a sphere whose radius is entered by the user

from math import pi as p

r=float(input("Enter the radius of the sphere: "))
volume=4/3*p*(r**3)
area=4*p*(r**2)

print("The volume is: "+str(volume))
print("The surface area is: "+str(area))
