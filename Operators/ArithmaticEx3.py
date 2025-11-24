#Program for Evaluate (a**m)/(a**n)
#ArithmaticEx3
a = int(input("Enter Value of a:"))
m= int(input("Enter Value of m:"))
n = int(input("Enter Value of n:"))
eq1 = (a**m)/(a**n)
eq2 = a**(m-n)
print("="*50)
print('\tLogic:(a**m)/(a**n)')
print("\tSol:{}".format(eq1))
print("\n\tLogic:a**(m-n)")
print("\tSol:{}".format(eq2))
print("="*50)

