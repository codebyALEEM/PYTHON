#Program for biggest among two
#BigEx2.py
a = int(input("Enter Value of a:"))
b = int(input("Enter Value of b:"))
print("="*50)
c = "{} is Biggest".format(a)  if a>b else "{} is Biggest".format(b)  if b>a else "Both are Equal" #This condition fails when both are equal
print("Value of a: {}".format(a))
print("Value of b: {}".format(b))
print("-"*50)
print("{}".format(c))
print("-"*50)