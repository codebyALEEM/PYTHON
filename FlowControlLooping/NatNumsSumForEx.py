#Program for Sum,Square Sum,Cube Sum of first n Nat Nums
#NatNumsSumForEx.py
n = int(input("Enter a Number:"))
sum=0
sq =0
cube=0
print("-"*50)
if (n<=0):
    print("{} is Invalid Input ".format(n))
else: 
    print("Sum,Square Sum,Cube Sum of first n Nat Nums ")
    print("-"*50)       
    for i in range(1,n+1):       
        sum = sum + i
        sq = sq + (i**2)
        cube = cube + (i**3)
        print("\t{}\t\t{}\t\t\t{}".format(i,i*i,i**3))        
    else:  
        print("-"*50)
        print("Sum:{}\t\tsquare:{}\t\tCube:{}".format(sum,sq,cube))
        print("-"*50)
    