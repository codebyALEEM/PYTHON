#DaysTOMonths.py
def d2m():
    days=int(input("\t\tEnter Days to find Numbers of Months:"))
    m=days/30.44
    rdays=days%30
    print("\t\t{} Days = {} Months {} Days".format(days,int(m),rdays))
    print("\t\t*****************************************")