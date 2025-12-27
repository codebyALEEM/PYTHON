#Triangle.py
def area():
    b=float(input("Enter Base to find Area of Triangle:"))
    h=float(input("Enter Base to find Area of Triangle:"))
    ar=(1/2)*(b*h)
    print("Area of Triangle with Base({}) and Height({}) = {}".format(b,h,ar))
    print("-"*50)
    
def peri():
    s1=float(input("Enter First Side to find Perimeter of Triangle:"))
    s2=float(input("Enter Second Side to find Perimeter of Triangle:"))
    s3=float(input("Enter Third Side to find Perimeter of Triangle:"))
    pr=(s1+s2+s3)
    print("Perimeter of Triangle with Sides({},{},{}) = {}".format(s1,s2,s3,pr))
    print("-"*50)
    
    