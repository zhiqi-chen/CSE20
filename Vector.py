"""
This module provides functions to perform standard vector operations.  Vectors
are represented as lists of numbers (floats or ints).  Functions that take two 
vector arguments may give arbitrary output if the vectors are not compatible,
i.e. of the same dimension.  
"""
#------------------------------------------------------------------------------
# import standard library modules
#------------------------------------------------------------------------------
import math
import random

#------------------------------------------------------------------------------
# function definitions
#------------------------------------------------------------------------------
def add(u, v):
    """
    Return the vector sum u+v.
    """
    add=[]
    for i in range(len(u)):
        add.append(u[i]+v[i])
    return add

# end add()

def negate(u):
    """
    Return the negative -u of the vector u.
    """
    negate=[]
    for i in range(len(u)):
        negate.append(-u[i])
    return negate

# end negate()   

def sub(u, v):
    """
    Return the vector difference u-v.
    """
    sub=[]
    for i in range(len(u)):
        sub.append(u[i]-v[i])
    return sub

# end sub()

def scalarMult(c, u):
    """
    Return the scalar product cu of the number c by the vector u.
    """  
    scalarMult=[]
    for i in range(len(u)):
        scalarMult.append(c*u[i])
    return scalarMult

# end scalarMult()

def zip(u, v):
    """
    Return the component-wise product of u with v.
    """
    zip1=[]
    for i in range(len(u)):
        zip1.append(u[i]*v[i])
    return zip1

# end zip()

def dot(u, v):
    """
    Return the dot product of u with v.
    """
    zip2=[]
    for i in range(len(u)):
        zip2.append(u[i]*v[i])
    dot=sum(zip2)
    return dot

# end dot()

def length(u):
    """
    Return the (geometric) length of the vector u.
    """
    square=[]
    for i in range(len(u)):
        square.append(u[i]*u[i])
    length=math.sqrt(sum(square))
    return length

# end length()
   
def unit(v):
    """
    Return a unit (geometric length 1) vector in the direction of v.
    """
    t=length(v)
    unit=[]
    for i in range(len(v)):
        unit.append(v[i]/t)
    return unit

# end unit()

def angle(u, v):
   """
   Return the angle (in degrees) between vectors u and v.
   """
   return math.degrees(math.acos(dot(unit(u),unit(v))))
# end angle()

def randVector(n, a, b):
    """
    Return a vector of dimension n whose components are random floats in the range [a, b).
    """
    randVector=[]
    for i in range(n):
        randVector.append(random.uniform(a,b))
    return randVector

# end randomVector()
