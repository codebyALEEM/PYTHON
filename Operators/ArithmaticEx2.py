#Program for calculating (a+b)**2
#ArithmeticEx2.py
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
print("="*50)
eq1 = (a+b)**2
print("Logic:(a+b)**2")
print("Sol1:-({}+{})**2={}".format(a,b,eq1))
print("="*50)
eq2 = (a**2)+(2*a*b)+(b**2)
print("Logic:(a+b)**2 = (a**2)+2*a*b+(b**2)")
print("Sol2:-({}+{})**2={}".format(a,b,eq2))
print("="*50)
eq3 = (a*a)+(2*a*b)+(b*b)
print("Logic:(a+b)**2 = (a*a)+2*a*b+(b*b)")
print("Sol3:-({}+{})**2={}".format(a,b,eq3))

