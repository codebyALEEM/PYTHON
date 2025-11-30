#DigitSumEx3.py
n = (input("Enter a Number:"))
if (int(n) <= 0):
    print("{} is Invalid Input".format(n))
else:
    print("Given Number:{}".format(n))
    sum = 0
    digits = list(n)
    for digit in digits:
        sum = sum + int(digit)
    else:
        print("Sum={}".format(sum))



