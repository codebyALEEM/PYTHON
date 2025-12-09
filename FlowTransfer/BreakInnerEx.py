#BreakInnerEx.py
for i in range(1,4):
    print("Outer loop i=",i)
    for j in range(1,4):
        print("\tInner loop j=",j)
        if j==2:
            print("Break inner loop at j=",j)
            break
    print("\tOuter loop continues")
print("Program Execution Completed")