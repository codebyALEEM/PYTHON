#FactorialWhileEx1.py
n = int(input("Enter a Number:"))
print("-"*50)
if (n<0):
    print("{} is Invalid Input".format(n))
else:
    f=1
    i=n
    while(i>0):
        f = f*i
        i = i-1
    print("Factorial of ({}) = {} ".format(n,f))
        
