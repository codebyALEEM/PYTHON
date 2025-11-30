i=1
while(i<5):
    print("Values of Outer Loop i {}".format(i))
    print("_"*50)
    for j in range(1,4):
        print("Value of  Inner Loop j {}".format(j))
    else:        
        print("I am coming out of Inner for loop")
        print("-"*50)
        i = i+1
else:
    print("I am coming out of Outer While Loop")
    print("-"*50)
    print("Program Execution Completed")
    print("*"*50)