n=int(input('Enter an integer: '))
m=int(input('Enter an integer: '))
x=1
oddlist=[]
def printodd():
    for x in range(m-1):
        if x%2!=0 and x!=0:
            oddlist.append(x)
        x+=1

evenlist=[]
def printeven():
    for x in range(n-1):
        if x%2==0 and x!=0:
            evenlist.append(x)
        x+=1
            
if n<m:
    printodd()
    print(oddlist)
if m<n:
    printeven()
    print(evenlist)
    

    
      
