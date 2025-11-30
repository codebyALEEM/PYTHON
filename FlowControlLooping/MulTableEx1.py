#Program for Multiplication Table of any number
#MulTableEx1.py
n = int(input("Enter a Number for generating Mul Table:"))
print("-"*50)
print("Mul Table for:{}".format(n))
print("-"*50)
if (n<=0):
    print("{} is Invalid Input".format(n))
else:
    p=5
    i=1
    while(i<=10):
        print("{} x {}= {}".format(p,i,p*i))
        i=i+1
print("*"*50)
    