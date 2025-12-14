#Program to find the Factorial of number by using Function
#FactorialFunEx.py
def fact():
    while(True):
        n = int(input("Enter a Number:"))
        if(n<=0):
            print("{} is Invalid Input".format(n))
        else:
            print("-"*50)
            fact=1
            for i in range(1,n+1):
                fact=fact*i
            print("Factorial of {} = {}".format(n,fact))
            print("*"*50)
        chk = input("Do you want check for other number?(yes/no)")
        print("-"*50)
        if(chk.lower()=='no'):
            print("Thx for using this app")
            print("-"*50)
            break
    print("Program Execution Completed")
           
fact()           
            
            
        
        