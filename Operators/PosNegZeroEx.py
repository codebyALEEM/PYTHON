#Program to find positive ,negative and zero by using Ternary Operator
#PosNegZeroEx..py
n = int(input("Enter any Number:"))
res = "+VE" if n>0 else "-VE" if n<0 else "ZERO"
print("{} is {}".format(n,res))