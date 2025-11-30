#DigitsSumEx2.py
n = input("Enter a Number:")
if(int(n)<0):
    print("{} is Invalid Input".format(n))
else:
    print("Given Number:{}".format(n))
    digits=n.split()
    s = 0
    for digit in digits[0]:
        s = s+int(digit)
    else:
        print("Sum of Digits={}".format(s))
        
