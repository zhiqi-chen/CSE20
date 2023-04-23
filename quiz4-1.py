n=int(input('Enter an integer: '))
m=int(input('Enter an integer: '))

def printodd():
    for x in range(m):
        if x%2==1 and x!=0:
            print(x, end=" ")

def printeven():
    for x in range(n):
        if x%2==0 and x!=0:
            print(x, end=" ")
            
if n<m:
    printodd()
if m<n:
    printeven()
if n==m:
    pass
    
    
