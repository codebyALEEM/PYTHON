#WhileInForEx.py
for i in range(1,6):
    print("Value of Outer For Loop {}".format(i))
    print("-"*50)
    j=1
    while(j<4):
        print("Value of Inner While Loop {}".format(j))
        j=j+1
    else:
        print("I am coming out from Inner While loop")
        print("-"*50)
else:
    print("I am coming out from Outer For loop")
    print("-"*50)
    print("Program Execution Completed")
    print("*"*50)