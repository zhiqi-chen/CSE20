print()
print("Enter two numbers, low then high.")

low=int(input("low = "))
high=int(input("high = "))

print()

if low>high:
    while True:
        print("Please enter the smaller followed by the larger number.")
        low=int(input("low = "))
        high=int(input("high = "))
        print()
        if low<=high:
            break

print("Think of a number in the rank "+str(low)+" to "+str(high))
print()

L=list(range(low,high+1))
n=0
def compare(n,L):
    low=0
    high=len(L)-1
    m=(low+high)//2
    if len(L)==1:
        print("Your number is "+str(L[m])+". I found it in "+str(n)+" guesses")
        print()
        return
    if m<0:
        print("Your answers have not been consistent.")
        print()
        return
    print("Is your number Less than, Greater than, or Equal to "+str(L[m])+"?")
    guess=str(input("Type 'L', 'G' or 'E': "))
    print()
    while guess!='L' and guess!='l' and guess!='G' and guess!='g' and guess!='E' and guess!='e':
            guess=str(input("Please type 'L', 'G' or 'E': "))
            print()
            if guess=='L' or guess=='l' or guess=='G' or guess=='g' or guess=='E' or guess=='e':
                break
    if guess=='E' or guess=='e':
        n+=1
        if n==1:
            print("I found your number in 1 guess.")
        else:
            print("I found your number in "+str(n)+" guesses")
    elif guess=='L' or guess=='l':
        del L[m:]
        n+=1       
        compare(n,L)
    elif guess=='G' or guess=='g':
        del L[0:m+1]
        n+=1
        compare(n,L)
        
compare(n,L)
            


        
