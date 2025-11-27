#Program to check Number is POsitive ,Negative and Zero by using If Else
#PosNegZeroIfElse.py
n = int(input("Enter a Number:"))
if n==0:
    print("{} is ZERO".format(n))
else:
    if(n>0):
        print("{} is POSITIVE".format(n))
    else:
        print("{} is NEGATIVE".format(n))