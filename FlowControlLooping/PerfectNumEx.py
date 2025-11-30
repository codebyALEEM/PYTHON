n = int(input("Enter a Number:"))
if (n<=0):
    print("{} is Invalid Input".format(n))
else:
    fact=0
    for i in range(1,(n//2)+1):        
        if(n%i==0):
            fact=fact+i
    else:
        print("Sum of Factors:{}".format(fact))
        if n==fact:
            print("-"*50)
            print("Number Entered ({}) = Sum Of Factors ({})".format(n,fact))
            print("{} PERFECT NUMBER".format(n))
            print("-"*50)
        else:
            print("-"*50)
            print("Number Entered ({}) != Sum Of Factors ({})".format(n,fact))
            print("{} NOT PERFECT NUMBER".format(n))
            print("-"*50)     
print("Program Execution is Completed")