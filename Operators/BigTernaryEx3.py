#program for Finding Biggest of Two Numbers and Check for equality
#BigEx2.py
a=int(input("Enter First value:"))
b=int(input("Enter Second value:"))
#Logic for Finding biggest and for equality
bv=a if a>b else b if b>a else "VALUES ARE EQUAL"
print("Big({},{})={}".format(a,b,bv))