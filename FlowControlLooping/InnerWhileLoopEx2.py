#InnerWhileLoopEx2.py
i = 1
while(i<5):
    print("Value for Inner While Loop :{}".format(i))
    print("-"*50)
    j=1
    while(j<4):
        print("Value for Outer Loop:{}".format(j))        
        j = j+1
    else:
        print("I am coming out of Inner While Loop")
        print("-"*50)
        i= i+1
else:
    print("I am coming out of Outer While Loop")
    print("Program Execution Completed")
    print("="*50)