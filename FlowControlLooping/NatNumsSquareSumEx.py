n = int(input("Enter number upto which you want the Square sum:"))
print("-" * 50)
print("\tNatNums\tSquares")
print("-" * 50)
if (n <= 0):
    print("{} is Invalid Input".format(n))
else:
    i = 1
    sum = 0
    sq = 0
    while (i <= n):
        print("\t{}\t\t\t{}".format(i, i * i))
        sum = sum + i
        sq = sq + (i * i)
        i = i + 1
    else:
        print("-" * 50)
        print("\t{}\t\t\t{}".format(sum, sq))
        print("-" * 50)


