#Program to generate from n to 1 where n is +VE
#NumGenEx2.py
n = int(input("Enter How Many numberes u want to generate:"))
if (n<=0):
    print("{} is Invalid Input".format(n))
else:
    i = n
    while(i>0):
        print("\t{}".format(i))
        i = i-1
print("Program Execution Completed")