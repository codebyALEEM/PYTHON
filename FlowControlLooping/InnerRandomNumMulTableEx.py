#InnerRandomNumMulTableEx.py
n = int(input("Enter a Nunber:"))
print('-'*50)
if (n<=0):
    print("{} is Invalid Input".format(n))
else:   
    lst=list()     
    for i in range(1,n+1):
        m = int(input("Enter {} Number:".format(i)))
        lst.append(m)
    else:
        print('-'*50)
        print("Given list={}".format(lst))
        print('-'*50)
        for num in lst:
            if (num<=0):                               
                print("{} is Invalid Input".format(num))
                print('-'*50)
            else:
                print("Mul Table of {}".format(num)) 
                print('-'*50)
                for i in range(1,11):                                    
                    print("{} x {} = {}".format(num,i,num*i))
                else:
                    print("-"*50)
print("Program Execution Complted")
print("*"*50)
                
            
            