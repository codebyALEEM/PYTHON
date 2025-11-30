#InnerLoopsMulTablesEx.py
n = int(input("Enter Upto which Number you want to generate Tables:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
for i in range(1,n+1):
    print("\tTable Of {}".format(i))
    print("-"*50)
    for j in range(1,11):
        print("\t{} x {} = {}".format(i,j,i*j))
    else:
        print("-"*50)
else:
    print("Program Execution Completed")
    print("*"*50)
    