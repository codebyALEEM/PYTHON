#EvenForEx.py
n = int(input("Enter a Number:"))
print("-"*30)
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    for i in range(2,n+1,2):
        print("\t{}".format(i))
print('-'*30)   
print("Program Execution Completed")