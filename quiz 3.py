r=2.55
s=10.082
t=10.037
A=(r<s)
B=(s<t)
C=(t<=r)
print(A and (B or C))
print(not (A or B))
print((not C) or B)

def rotate(A,i,j,k):
    temp=A[i]
    A[i]=A[j]
    A[j]=A[k]
    A[k]=temp

L=['one','two','three','four','five']
print(L)
rotate(L,0,2,4)
print(L)
