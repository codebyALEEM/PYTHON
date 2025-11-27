#program for accepting whether a given number of +ve or negative or Zero
#IfElseEx1.py
n = int(input("Enter a Number:"))
if (n>0):
    print('{} is +VE'.foramt(n))
else:
    if(n<0):
        print("{} is -VE".format(n))
    else:
        print("{} is ZERO".format(n))
print("Program execution Completed")