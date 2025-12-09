#Program for Prime Number
#PrimeEx2.py
n = int(input('Enter a Number:'))
if(n<=1):
    print("{} is Invalid Input".format(n))
else:
    i=2
    while(i<n):
        if (n%i==0):
            print("{} is Not Prime".format(n))
            break            
        else:
            i=i+1
    else:
        print("{} is Prime".format(n))