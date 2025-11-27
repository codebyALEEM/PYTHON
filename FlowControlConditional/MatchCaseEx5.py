#Program to check Days of week
#MatchCaseEx5.py
wkn = input("Enter Day of Week :")
if wkn.upper() in ["MON","TUE",'WED',"THU","FRI","SAT","SUN","MODAY","TUESDAY","WEDNESDAY","FRIDAY","SATURDAY","SUNDAY"]:
    match(wkn[0:3].upper()):
        case "MON" | "TUE" | "WED" | "THU" | "FRI" :
            print("{} is a Working Day".format(wkn))
        case "SAT":
            print("{} is a Week End Day ".format(wkn))
        case "SUN":
            print("{} is a Holiday".format(wkn))
    print("Program Execution Completed")
else:
    print("{} is not a day of week".format(wkn))