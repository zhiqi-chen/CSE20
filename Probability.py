import random
rng=random.Random(237)
print()

m=int(input("Enter the number of dice: "))
while m<1:
    print("The number of dice must be at least 1")
    m=int(input("Please enter the number of dice: "))
print()
    
k=int(input("Enter the number of sides on each die: "))
while k<2:
    print("The number of sides on each die must be at least 2")
    k=int(input("Please enter the number of sides on each die: "))
print()

trials=int(input("Enter the number of trails to perform: "))
while trials<1:
    print("The number of trails must be at least 1")
    trials=int(input("Please enter the number of trails to perform: "))
print()

def throwDice(m,k):
    i=1
    dielist=[]
    for i in range(m):
        die=rng.randrange(1,k+1)
        dielist.append(die)
        i+=1
    return tuple(dielist)

frequency=(m*k+1)*[0];
for i in range(trials):
    t=throwDice(m,k)
    frequency[sum(list(t))]+=1;

relativeFrequency=m*[0]
probability=m*[0]
for i in range(m,len(frequency)):
    relativeFrequency.append(frequency[i]/trials)
    probability.append((frequency[i]/trials)*100)

print()

f1=" {0:<8}{1:<14}{2:<23}{3:<22}"
f2=70*"-"
f3 ="{0:>4}{1:>11.0f}{2:>18.5f}{3:>21.2f}{4:>}"
print(f1.format("Sum","Frequency","Relative Frequency","Experimental Probability"))
print(f2)
for i in range(m,len(frequency)):
    print(f3.format(i,frequency[i],relativeFrequency[i],probability[i]," %"))

print()


