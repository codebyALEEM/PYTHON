#Main.py
from TimeMenu import menu
from YearsToMonths import y2m
from YearsToDays import y2d
from MonthsToYears import m2y
from MonthsToDays import m2d
from DaysToYears import d2y
from DaysToMonths import d2m

while(True):
    menu()
    ch=int(input("\t\tEnter Your Choice:"))
    if ch==1:
        y2m()
    elif ch==2:
        y2d()
    elif ch==3:
        m2y()
    elif ch==4:
        m2d()
    elif ch==5:
        d2y()
    elif ch==6:
        d2m()
    elif(ch==7):
        print("\t\tThnx for using this app")
        break
    else:
        print("\t\tInvalid Input!")
            
    