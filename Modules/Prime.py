#Prime.py----File Name and Module Name
def decide(n):
    if n<=0:
        print("{} is Invalid Input".format(n))
    else:
        for i in range(2,n):
            if n%i==0:
                print("Not Prime")
                break
        else:
            print("Prime")