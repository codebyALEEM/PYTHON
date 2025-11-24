#Program for biggest among two
#BigTernaryEx1.py
a = int(input("Enter Value of a:"))
b = int(input("Enter Value of b:"))
print("="*50)
c = a if a>b else b #This condition fails when both are equal
print("From {} , {}  Biggest Values is {}".format(a,b,c))