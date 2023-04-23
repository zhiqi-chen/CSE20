import math
print()
n=int(input("Enter the number of Primes to compute: "))

PrimeList=[2]
def isPrime(m,L):
    for p in L:
        if p>math.sqrt(m):
            return True
        if m%p==0:
            return False

i=3
while True:
    if len(PrimeList)==n:
        break
    if (isPrime(i,PrimeList)):
        PrimeList.append(i)
    i+=1

for x in range(len(PrimeList)):
    if x%10==0:
        print()
        print(PrimeList[x], end=" ")
    else:
        print(PrimeList[x], end=" ")

print()
print()
