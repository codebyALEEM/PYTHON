#Program to check Days of week
wkn = input("Enter Day:")
match(wkn.upper()):
    case "MONDAY":
        print("{} is a Working Day".format(wkn))
    case "TUESDAY":
        print("{} is a Working Day".format(wkn))
    case "WEDNESDAY":
        print("{} is a Working Day".format(wkn))
    case "THURSDAY":
        print("{} is a Working Day".format(wkn))
    case "FRIDAY":
        print("{} is a Working Day".format(wkn))
    case "SATURDAY":
        print("{} is a Week End Day".format(wkn))
    case "SUNDAY":
        print("{} is a Holiday Day".format(wkn))
    case _:
        print("{} not a week day".format(wkn))
        
