#DigitsSumEx1.py
n = int(input("Enter a Number:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    sum=0
    while(n>0):
        res=n%10
        sum=sum+res
        n=n//10
    else:
        print("Digits Sum={}".format(sum))
    
    