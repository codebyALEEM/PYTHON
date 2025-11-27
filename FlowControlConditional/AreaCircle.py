#Area of circle 
#AreaCircle.py
r = int(input("Enter Radius:"))
ac = (3.14*r**2)
if (r<=0):
    print("Invalid Input")
else:
    print("Area of circle with Radius {} is {}".format(r,ac))