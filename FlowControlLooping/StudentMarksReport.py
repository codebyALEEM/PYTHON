while(True):
    while(True):
        sno = int(input("Enter Student Number:"))
        if(sno>0):
            break
        print("{} is Invalid Input.Try Again".format(sno))
    sname = input("Enter Student Name:")
    while(True):
        cm = int(input("Enter C marks:"))
        if(0<cm<=100):
            break
        print("{} is Invalid Marks.Pls Enter Valid Obtained Marks".format(cm))
    while(True):
        cppm=int(input("Enter C++ Marks:"))
        if(0<cppm<=100):
            break
        print("{} is Invalid Marks.Pls Enter Valid Obtained Marks".format(cppm))
    while(True):
        pym = int(input("Enter Python marks:"))
        if(0<pym<=100):
            break
        print("{} is Invalid Marks.Pls Enter Valid Obtained Marks".format(pym))
    totmarks= (cm+cppm+pym)
    perc = (totmarks/300)*100
    if (cm<40) or (cppm<40) or (pym<40):
        grade="FAIL"
    else:
        if(250<=totmarks<300):
            grade="DINTINCTION"
        elif(totmarks>200):
            grade="FIRST"
        elif(totmarks>150):
            grade="SECOND"
        elif(totmarks>120):
            grade="THIRD"
    print("="*50)
    print("Student Marks Report:")
    print("="*50)
    print("\tStudent Number:{}".format(sno))
    print("\tStudent Name:{}".format(sname))
    print("\tStudent C marks:{}".format(cm))
    print("\tStudent C++ marks:{}".format(cppm))
    print("\tStudent Python marks:{}".format(pym))
    print("-"*50)
    print("\tStudent Total Marks:{}".format(totmarks))
    print("\tStudent Percentage:{}".format(perc))
    print("\tStudent Grade:{}".format(grade))
    print("="*50)
    chk = input("Do U want to check Again (yes/no):")
    if chk.lower()=='no':
        print("Tnx for using this app")  
        break
    