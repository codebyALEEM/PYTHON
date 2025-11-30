#Program for Sum of n numbers,sum of square n numbers and sum of cube of n numbers
#NatNumCubesEx.py
n = int(input("Enter number upto which you want the Cube Sum:"))
print("-" * 50)
print("\tNatNums\tSquares\tCubes")
print("-" * 50)
if (n <= 0):
    print("{} is Invalid Input".format(n))
else:
    i = 1
    sum = 0
    sq = 0
    cube = 0
    while (i <= n):
        print("\t{}\t\t{}\t\t{}".format(i, i * i, i ** 3))
        sum = sum + i
        sq = sq + (i * i)
        cube = cube + (i ** 3)
        i = i + 1
    else:
        print("-" * 50)
        print("Sum {}\t\t{}\t\t{}".format(sum, sq, cube))
        print("-" * 50)


