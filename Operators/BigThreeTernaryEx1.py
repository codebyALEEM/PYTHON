#Program for accepting Three values and find Biggest among them and check for equality
#BigThreeTernaryEx1.py
a =int(input("Enter Value of a:"))
b =int(input("Enter Value of b:"))
c =int(input("Enter Value of c:"))
bv = a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "All values are Equal"
print("big({},{},{})={}".format(a,b,c,bv))