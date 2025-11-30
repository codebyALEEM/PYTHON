while(True):
    while(True):
        eno = int(input("Enter Employ No:"))
        if(eno>0):
            break
        print("{} is an Invalid Input.Try Again!".format(eno))
    ename=input("Enter Employ Name:")
    while(True):
        esal = int(input("Enter Salary:"))
        if(esal>0):
            break
        print("{} is an Invalid Input.Try Again!".format(esal))
    if (esal>=10000):
        da=(20/100)*esal
        ta=(15/100)*esal
        hra=(16/100)*esal
        ma=(2/100)*esal
        lic=(2/100)*esal
        gpf=(2/100)*esal
        intr=(da+ta+hra+ma)
        dtion=(lic+gpf)
        netsal=(esal+da+ta+hra+ma)-(dtion)
        print("="*50)
        print("\tPay Slip Of An Employee")
        print("="*50)
        print("Employee Number:{}".format(eno))
        print("Employee Name:{}".format(ename))
        print("Employee Basic Salary:{}".format(esal))
        print("-"*50)
        print("Dearness Allowance (DA): {}".format(da))
        print("Travel Allowance (TA): {}".format(ta))
        print("House Rent Allowance (HRA): {}".format(hra))
        print("Medical Allowance (MA): {}".format(ma))
        print("Total Incre:{}".format(intr))
        print("-"*50)
        print("Life Insurance Corporation Premium (LIC): {}".format(lic))
        print("General Provident Fund Contribution (GPF): {}".format(gpf))
        print("Total Deduction:{}".format(dtion))
        print("*"*50)
        print("Total Salary of {} is {}".format(ename,((esal+intr)-dtion)))
        print("*"*50)
    else:
        da=(50/100)*esal
        ta=(8/100)*esal
        hra=(7/100)*esal
        ma=(2/100)*esal
        lic=(1/100)*esal
        gpf=(1/100)*esal
        intr=(da+ta+hra+ma)
        dtion=(lic+gpf)
        netsal=(esal+da+ta+hra+ma)-(dtion)
        print("="*50)
        print("\tPay Slip Of An Employee")
        print("="*50)
        print("Employee Number:{}".format(eno))
        print("Employee Name:{}".format(ename))
        print("Employee Basic Salary:{}".format(esal))
        print("-"*50)
        print("Dearness Allowance (DA): {}".format(da))
        print("Travel Allowance (TA): {}".format(ta))
        print("House Rent Allowance (HRA): {}".format(hra))
        print("Medical Allowance (MA): {}".format(ma))
        print("Total Incre:{}".format(intr))
        print("-"*50)
        print("Life Insurance Corporation Premium (LIC): {}".format(lic))
        print("General Provident Fund Contribution (GPF): {}".format(gpf))
        print("Total Deduction:{}".format(dtion))
        print("*"*50)
        print("Total Salary of {} is {}".format(ename,((esal+intr)-dtion)))
        print("*"*50)    
    print("Program Execution Completed")
    print("-"*50)
    ch=input("Do u want to Enter Another Employee Data(yes/no):")
    if(ch.lower()=='no'): 
        print("Thx for using Program")
        break
    

            