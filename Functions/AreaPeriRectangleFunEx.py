#AreaCircumCirFunEx.py
def arrect():
    while(True):
        l = int(input("Enter Length of Rectangle to find Area and Perimeter:"))        
        b = int(input("Enter Breadth of Rectangle to find Area and Perimeter:"))
        if (l<=0 or b<=0):
            print("Invalid Input")
        else:
            area = l*b
            peri = 2*(l+b)
            print("Area of Rectangle with Length ({}) ,Breadth ({}) = {}".format(l,b,area))
            print("Perimeter of Rectangle with Length ({}) ,Breadth ({}) = {}".format(l,b,peri))
        while(True):
            chk = input("Do want to Calculate Again(yes/no):")
            if (chk.lower()=='yes'):
                break
            elif(chk.lower()=='no'):
                print("Tnx for using this app")
                return
            else:
                print("{} is Invalid Input.Try with yes or no".format(chk))

arrect()
                
            
            