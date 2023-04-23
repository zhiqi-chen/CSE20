def mult(u,v):
    if len(u)==len(v):
        mult=[]
        for i in range(len(u)):
            mult.append(u[i]*v[i])
        return mult
    if len(u)!=len(v):
        return None

a = [1, 2, 3]
b = [4, 5, 6]
c = ['one', 'two', 'three']
d = [1, 2, 3, 4]
print(mult(a, b))
print(mult(a, c))
print(mult(a, d))
