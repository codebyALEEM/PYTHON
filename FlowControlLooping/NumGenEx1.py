#Program for generating 1 to n number where n is +ve
#NumGenEx1.py
n = int(input("Enter How Many Numbers u want to generate:"))
if (n<=0):
    print("{} is invalid input".format(n))
else:
    i=1
    while(i<=n):
        print("\t{}".format(i))
        i = i+1
print("Program execution completed")