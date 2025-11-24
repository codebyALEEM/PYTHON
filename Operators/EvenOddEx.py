#Program to check the number is even or odd by using Ternary Operator
n = int(input("Enter Number:"))
res = "Even" if n%2==0 else "Odd"
print("{} is {}".format(n,res))