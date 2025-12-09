#ContinueEx1.py
s = "PYTHON"
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for lop")
    for ch in s:
        if(ch=="T"):
            continue
        else:
            print("\t{}".format(ch))
    else:
        print("I am from Else part of Inner for loop")
        print("Program Execution Completed")