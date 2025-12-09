#BreakWhileEx2.py
count=1
while count<=5:
    print("Loop iteration:",count)
    if count==4:
        print("Break at count:",count)
        break
    count=count+1
print("Exited while loop")