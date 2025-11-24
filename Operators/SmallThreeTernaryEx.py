a = int(input("Enter Value of a:"))
b = int(input("Enter Value of b:"))
c = int(input("Enter Value of c:"))
#Logic
sv = a if a<=b and a<c else b if b<a and b<=c else c if c<=a and c<b else "All are Equal"
print("Small({},{},{})={}".format(a,b,c,sv))
