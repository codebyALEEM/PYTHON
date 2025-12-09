#BreakWhileEx1.py
s = "PYTHON"
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i = i+1
else:
    print("I am from else part of While")
    i=0
    while(i<len(s)):
        if(s[i]=="H"):
            break
        else:
            print("\t{}".format(s[i]))
            i=i+1
print("Program Execution Completed")