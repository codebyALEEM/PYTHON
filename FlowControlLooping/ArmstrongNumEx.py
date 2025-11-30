n = input("Enter a Number to check it is a Armstrong or Not:")
print("-"*50)
if (int(n)<=0):
    print("{} is Invalid Input".format(int(n)))
else:
    total=0
    for i in n:
        total = total+(int(i)**len(n))
    else:
        if (int(n)==total):
            print("{} is Armstrong Number:".format(n))
        else:
            print("{} is not a Armstrong Number".format(n))
print("Program Execution Completed")
print("*"*50)
        