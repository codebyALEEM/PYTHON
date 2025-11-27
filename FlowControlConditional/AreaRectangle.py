#Program for Area of Rectangle
#AreaRectangle.py
l = int(input("Enter Length:"))
b = int(input("Enter Breadth:"))
ar = l*b
if (l<=0 or b<=0):
    print("Invalid Input")
else:
    print("Area of Rectanlge with Length({}) and Breadth({}) is {}".format(l,b,ar))
        