#Program to find the sum of product of n natural numbers
#NatNumsProdEx.py
n = int(input("Enter Number to which you want Product:"))
print("-"*50)
print("Product of First {} Natural Numbers".format(n))
print("-"*50)
if (n<=0):
    print("{} is Invalid Input".format(n))
else:
    prod = 1
    i=1
    while(i<=n):
        print("\t{}".format(i))
        prod = prod * i
        i = i + 1
    else:
        print("-"*50)
        print("Product={}".format(prod))
        print("-"*50)
        
        
    