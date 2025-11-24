#Program for Evaluate (a**m)**n
#ArithmaticEx4.py
a = int(input("Enter Value of a:"))
m= int(input("Enter Value of m:"))
n = int(input("Enter Value of n:"))
eq1 = (a**m)**n
eq2 = (a**(m*n))
print("="*50)
print('Logic:(a**m)**n')
print("Solution1:{}".format(eq1))
print("\nLogic:a**(m*n)")
print("Solution2:{}".format(eq2))
print("="*50)
