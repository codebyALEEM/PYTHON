#AopDemo.py
from AopMenu import menu
from AopImplementations import *
while(True):
    menu()
    ch=int(input("Enter Ur Choice:"))
    match(ch):
        case 1:sumop()
        case 2:subop()
        case 3:mulop()
        case 4:divop()
        case 5:floordiv()
        case 6:modop()
        case 7:expo()
        case 8:
            print("Thx for using this program ")
            break
        case _:
            print("Ur Selection of Operations is wrong!!")

