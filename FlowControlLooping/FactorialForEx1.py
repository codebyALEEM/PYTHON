#FactorialForEx1.py
n = int(input("Enter a Number:"))
print("-"*50)
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    f=1
    for i in range(1,n+1):
        f = f*i
    print("Factorial of {} = {}".format(n,f))
    print("-"*50)