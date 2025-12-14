#Program to find Area and CIrcumference of Circle by using Function
#DefArgsExAreaCircle.py
def circleareacircum(r,pi=3.14):
    area=pi*r**2
    cir = 2*pi*r
    print("Radius = {}".format(r))
    print("Area of Circle = {}".format(area))
    print("Circumference = {}".format(cir))
    
circleareacircum(r=int(input("Enter Radius to find Area and Circumference:")))