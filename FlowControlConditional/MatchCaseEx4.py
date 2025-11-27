#Program to check Days of week
#MatchCaseEx4.py
wkn = input("Enter Day:")
match(wkn.upper()):
    case "MONDAY" | "TUESDAY" | "WEDNESDAY" | "THURSDAY" | "FRIDAY" :
        print("{} is a Working Day".format(wkn))
    case "SATURDAY":
        print("{} is a Week End Day ".format(wkn))
    case "SUNDAY":
        print("{} is a Holiday".format(wkn))
    case _:
        print("{} is not a day of week".format(wkn))
print("Program Execution Completed")