#Program for Prime Number
#PrimeEx1.py
n = int(input('Enter a Number:'))
if(n<=1):
    print("{} is Invalid Input".format(n))
else:
    for i in range(2,n):
        if n%i==0:
            print("{} Not Prime".format(n))
            break
    else:
        print("{} Prime".format(n))