#AreaCircumCirFunEx.py
def arcir():
    while(True):
        r = int(input("Enter Radius of circle to find Area and Circumference:"))
        if (r<=0):
            print("{} is Invalid Input".format(r))
        else:
            area = (3.14*r**2)
            circum = 2*3.14*r
            print("Area of Circle with Radius {} = {}".format(r,area))
            print("Circumference of Circle with Radius {} = {}".format(r,circum))
        while(True):
            chk = input("Do want to Calculate Again(yes/no):")
            if (chk.lower()=='yes'):
                break
            elif(chk.lower()=='no'):
                print("Tnx for using this app")
                return
            else:
                print("{} is Invalid Input.Try with yes or no".format(chk))

arcir()
                
            
            