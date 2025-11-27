#IfElifElse.py
n = int(input("Enter a Digit:"))
if (n==0):
    print("{} is ZERO".format(n))
elif (n==1):
    print("{} is ONE".format(n))
elif (n==2):
    print("{} is TWO".format(n))
elif (n==3):
    print("{} is THREE".format(n))
elif (n==4):
    print("{} is FOUR".format(n))
elif (n==5):
    print("{} is FIVE".format(n))
elif (n==6):
    print("{} is SIX".format(n))
elif (n==7):
    print("{} is SEVEN".format(n))
elif (n==8):
    print("{} is EIGHT".format(n))
elif (n==9):
    print("{} is NINE".format(n))
elif (n in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("{} is -VE Number".format(n))
elif (n not in [-1,-2,-3,-4,-5,-6,-7,-8,-9] and n not in [1,2,3,4,5,6,7,8,9]):
    print("{} is a Number".format(n))
    
