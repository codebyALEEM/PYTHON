#Program for Swapping two values with two variables
#SwapEx1.py
a = int(input("Enter Value of a:"))
b = int(input("Enter Value of b:"))
print('-'*50)
print("Original Value of a:{}".format(a))
print("Original Value of b:{}".format(b))
print('-'*50)
a,b = b,a #multi line assignment
print("Swaped Value of a:{}".format(a))
print("Swaped Value of b:{}".format(b))