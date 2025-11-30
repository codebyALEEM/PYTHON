#Program for Multiplication Table of any +VE Number
#MulTableForEx.py
n = int(input("Enter a number for Multiplication Table:"))
print("-"*50)
if(n<=0):
    print("{} is Invalid Input".format(n))
else:    
    print("Multipication Table of {}".format(n))
    print("-"*50)
    for i in range(1,11):
        print("\t{} x {}= {}".format(n,i,n*i))
    else:
        print("-"*50)
        print("Program Execution Completed")
        print("*"*50)
        