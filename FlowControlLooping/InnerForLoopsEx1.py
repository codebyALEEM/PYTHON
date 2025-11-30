#InnerForLoopEx1.py
for i in range(1,5):
    print("Value for Outer For Loop:{}".format(i))
    print("-"*50)
    for j in range(1,4):
        print("Value for Inner For Loop:{}".format(j))
    else:
        print("I am coming out of Inner For Loop")
        print("-"*50)
else:
    print("I am coming out of Outer For Loop")
    print("Program Execution Completed")
    print("*"*50)
        
        