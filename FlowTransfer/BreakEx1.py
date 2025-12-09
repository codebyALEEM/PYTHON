#program for Demonstrating Break statement
#BreakEx1.py
s = "PYTHON"
for i in s:
    print("\t{}".format(i))
else:
    print("I am from else of for loop")
    for i in s:
        if (i=="H"):
            break
        else:
            print("\t{}".format(i))          
print("Program Execution Completed")        