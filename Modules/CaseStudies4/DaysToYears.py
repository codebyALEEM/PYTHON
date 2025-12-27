#DaysToYears.py
def d2y():
    days=int(input("\t\tEnter Numbers of Days to find Years:"))
    y=(days/365.25)
    rdays=days%365
    print("\t\t{} Days = {} Years {} Days".format(days,int(y),rdays))
    print("\t\t*****************************************")
    