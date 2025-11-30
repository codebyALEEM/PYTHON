n = int(input("Enter upto which number u want to Add:"))
print("-"*50)
print("{} First Natural Numbers Sum".format(n))
print("-"*50)
if (n<=0):
    print("{} is Invalid Input")
else:
    sum=0
    i=1
    while(i<=n):
        print("\t{}".format(i))
        sum=sum+i
        i=i+1
    print("-"*50)
    print("Sum={}".format(sum))
    print("-"*50)
        