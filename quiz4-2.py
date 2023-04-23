def addList(A,B):
    if len(A)!=len(B):
        return None
    C=[]
    for i in range(len(A)):
        C.append(A[i]+B[i])
    return C
    
