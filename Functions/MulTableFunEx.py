#Program for Multiplication table of given number
#MulTableFunEx.py
def table():
    while(True):
        n = int(input("Enter a Number for Multiplication Table:"))
        if (n<=0):
            print("{} is Invalid Input ".format(n))
        else:
            for i in range(1,11):
                print("\t{} x {} = {}".format(n,i,n*i))
            while(True):
                chk=input("Do you want any other number Table(yes/no):")
                if (chk.lower()=='yes'):
                    break
                elif(chk.lower()=='no'):
                    print("Tnx for using this app")
                    return
                else:
                    print("{} is Invalid Input,Try with 'yes' or 'no'.".format(chk))
                    
table()
            
            
            
        