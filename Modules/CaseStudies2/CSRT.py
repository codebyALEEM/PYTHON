#CSRT.py
from MenuShapeArea import menu
from Circle import area as ca,circum as cr
from Square import area as sa,peri as ps
from Rectangle import area as ra,peri as prt
from Triangle import area as ta,peri as pt

while(True):
    menu()        
    ch=int(input("Enter your Choice:"))
    if ch==1:
        ca()
    elif ch==2:
        cr()
    elif ch==3:
        sa()
    elif ch==4:
        ps()
    elif ch==5:
        ra()
    elif ch==6:
        prt()
    elif ch==7:
        ta()
    elif ch==8:
        pt()
    elif ch==9:
        print("Thnx for using this app")
        break
    else:
        print("Invalid Input")
        
    