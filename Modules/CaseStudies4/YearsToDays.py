#YearsToDays.py
def y2d():
    y=int(input("\t\tEnter Years to find Number of Days:"))
    days=y*365
    leapyear=(y//4)-(y//100)+(y//100)
    days=days+leapyear
    print("\t\tNumber of Days in ({}) Years ={}".format(y,days))
    print("\t\t*****************************************")
    

        