#Program to check for EVEN and ODD Only Positive numbers
#EvenOddPosOnly.py
n = int(input("Enter a Number:"))
if (n<0):
    print("{} is -VE ,Enter +VE Number".format(n))
else:
    if (n%2==0):
        print("{} is EVEN".format(n))
    else:
        print("{} is ODD".format(n))