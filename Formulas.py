# Zhiqi Chen
# zchen287@ucsc.edu
# programming assignement 2
# 4 functions that compute volume and surface are of certain 3-dimensional geometric figures

from math import pi as p

print("Enter three numbers:")
x=float(input("x = "))
y=float(input("y = "))
z=float(input("z = "))
print()

def sphere_volume(r):
    sphere_volume=4/3*p*(r**3)
    print("The volume of the sphere with radius "+str(r)+" is: "+str(sphere_volume))

def sphere_area(r):
    sphere_area=4*p*(r**2)
    print("The surface area of the sphere with radius "+str(r)+" is: "+str(sphere_area))

def cylinder_volume(r,h):
    cylinder_volume=p*(r**2)*h
    print("The volume of the cylinder with radius "+str(r)+" and height "+str(h)+" is: "+str(cylinder_volume))

def cylinder_area(r,h):
    cylinder_area=2*p*(r**2)+2*p*r*h
    print("The surface area of the cylinder with radius "+str(r)+" and height "+str(h)+" is: "+str(cylinder_area))

sphere_volume(x)
sphere_area(x)
print()

sphere_volume(y)
sphere_area(y)
print()

sphere_volume(z)
sphere_area(z)
print()

cylinder_volume(x,y)
cylinder_area(x,y)
print()

cylinder_volume(y,z)
cylinder_area(y,z)
print()

cylinder_volume(z,x)
cylinder_area(z,x)
    
