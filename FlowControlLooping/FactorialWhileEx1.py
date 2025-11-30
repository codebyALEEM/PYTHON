#FactorialWhileEx1.py
n = int(input("Enter a Number:"))
print("-"*50)
if (n<=0):
    print("{} is Invalid Input".format(n))
else:
    f=1
    i=1    
    while(i<=n):
        f=f*i
        i=i+1
    print("Factorial of {}={}".format(n,f))
    
        
    