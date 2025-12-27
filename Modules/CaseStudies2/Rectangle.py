#Rectangle.py
def area():
    l=float(input("Enter Length of Rectangle to find Area:"))
    b=float(input("Enter Length of Rectangle to find Area:"))
    ar=l*b
    print("Area of Rectangle with Length({}) and Breadth({}) = {}".format(l,b,ar))
    print("-"*50)
    
def peri():
    l=float(input("Enter Length of Rectangle to find Area:"))
    b=float(input("Enter Length of Rectangle to find Area:"))
    pr=2*(l+b)
    print("Perimeter of Rectangle with Length({}) and Breadth({}) = {}".format(l,b,pr))
    print("-"*50)
    