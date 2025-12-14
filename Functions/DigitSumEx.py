#Program for Sum of Digit of Given Number
#DigitSumEx.py
def digsum():
    while(True):
        n = input("Enter a Number:")
        if (n.isalpha()==True or " " in n):
            print("{} Invalid Input".format(n))
        else:
            ttl=0
            for i in n:
                ttl=ttl+int(i)
            print("Sum of Digits of {} = {}".format(n,ttl))


        while(True):
            chk = input("Do U want to Add Again (yes/no):")
            if (chk.upper()=='YES'):
                break
            elif(chk.upper()=='NO'):
                print("Thnx for using this app")
                print("Program Execution Completed")
                return
            else:
                print("{} is Invalid Input,Try with YES or NO".format(chk))


digsum()