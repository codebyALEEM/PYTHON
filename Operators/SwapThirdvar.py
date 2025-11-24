#Program for Swapping two values with Third variable
#SwapThirdvar.py
a = int(input("Enter Value of a:"))
b = int(input("Enter Value of b:"))
print('='*50)
print("Original Value of a:{}".format(a))
print("Original Value of b:{}".format(b))
print('='*50)
t = a
a = b
b = t
print("Swapped Value of a:{}".format(a))
print("Swapped Value of b:{}".format(b))
print("="*50)