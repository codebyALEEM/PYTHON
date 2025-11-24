#Program for accepting Three values and find Biggest among them and check for equality
#BigThreeTernaryEx2.py
a = int(input("Enter Value of a:"))
b = int(input("Enter Value of b:"))
c = int(input("Enter Value of c:"))
#Logic
bv = a if b<=a>c else b if a<b>=c else c if a<=c>b else "All are Equal"
print("Big({},{},{})={}".format(a,b,c,bv))