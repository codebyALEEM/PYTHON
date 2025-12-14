#Program for Simple Interest by using Function
#SimpleIntFunEx1.py
def simint():
    while(True):
        am = float(input("Enter Amount:"))
        time = float(input("Enter Time:"))
        rate = float(input("Enter Rate of Interest:"))
        si = (am * time * rate) / 100
        totamt = (am + si)

        print("-" * 50)
        print("\tSimple Intrest Calculator")
        print("*" * 50)
        print("\tPrincipal Amount:{}".format(am))
        print("\tTime Period:{}".format(time))
        print("\tRate of Interest:{}".format(rate))
        print("\tAmount of Interest:{}".format(si))
        print("-" * 50)
        print("Total Amount to Pay:({}+{})={}". format(am, si, totamt))
        print("*" * 50)
        chk=input("Do you want to calculate Again!(yes/no):")
        if chk.lower()=='no':
            print("Thx for using this app")
            print("-" * 50)
            break
        

simint()