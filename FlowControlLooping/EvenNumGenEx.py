#Program to generate n number of Even number where n is +VE
#EvenNumGenEx.py
n = int(input("Enter How Many Numbers you want to generate:"))
if (n<=0):
    print("{} is Invalid Input".format(n))
else:
    i = 2
    while(i<=n):
        print("\t{}".format(i))
        i = i+2
print("Program Execution Completed")