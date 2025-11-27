#Program to find Area of Shapes
print("="*50)
print("\tFigure Areas")
print("="*50)
print("\tR.Rectangle")
print("\tS.Square")
print("\tC.Circle")
print("\tT.Triangle")
print("\tE.Exit")
print("="*50)
ch =input("Enter Your Choice:")
print("="*50)
match (ch.upper()):
    case "R":
        print("Enter value for Length and Breadth:")
        a,b =int(input()),int(input())
        print("Area of Rectangle(Length:{},Breadth:{})={}".format(a,b,a*b))
    case "S":
        print("Enter Side :")
        s= int(input())
        print("Area of Square with Side {} is {}".format(s,(s**2)))
    case "C":
        print("Enter Radius :")
        r = int(input())
        print("Area of circle with Radius {} is {}".format(r,(3.14*r*r)))
    case "T":
        print("Enter Base and Height:")
        b,h = int(input()),int(input())
        print("Area of Triangle with Base:{},Height:{} is {}".format(b,h,(0.5*b*h)))
    case "E":
        print("Thnx for using ")   
    case _:
        print("Invalid Input ")
print("Program Execution Completed")
