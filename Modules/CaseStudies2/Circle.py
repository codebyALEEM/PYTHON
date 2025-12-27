#Circle.py
def area():
    r=float(input("Enter Radius to find Area of Circle:"))    
    ar=3.14*r*r
    print("Area of Circle with Radius ({})={}".format(r,ar))
    print("-"*50)
    
def circum():
    r=float(input("Enter Radius to Circumference of Circle:"))
    cir=2*3.14*r
    print("Circumference of circle with Radius ({})={}".format(r,cir))
    print("-"*50)