#Program for Prime numbers upto n number
#PrimeListEx.p
n = int(input("Enter a number:"))
if n<=1:
    print("{} is Invalid Input".format(n))
else:
    lst=list()
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                print("{} is NOT PRIME".format(i))
                break
        else:
            print("{} is PRIME".format(i))   
            lst.append(i)
    print("List of Prime Number up to {}:".format(n))
    print(lst)