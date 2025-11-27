print("="*50)
print("\tArithmatic Operators")
print("="*50)
print("\t1.Addition")
print("\t2.Subtraction")
print("\t3.Multiplcation")
print("\t4.Division")
print("\t5.Floor Division")
print("\t6.Modulo Division")
print("\t7.Exponential")
print("\t8.Exit")
print("="*50)
ch = int(input("Enter your Choice:"))
match(ch):
    case 1:
        print("Enter Two values for Addtion:")
        a,b=int(input()),int(input())
        print("sum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two values for Sub:")
        a,b=int(input()),int(input())
        print("Sub({},{})={}".format(a,b,a-b))
    case 3:
        print("Enter Two values for Mul:")
        a,b=int(input()),int(input())
        print("Mul({},{})={}".format(a,b,a*b))
    case 4:
        print("Enter Two values for Div:")
        a,b=int(input()),int(input())
        print("Div({},{})={}".format(a,b,a/b))
    case 5:
        print("Enter Two values for Floor Div:")
        a,b=int(input()),int(input())
        print("FLoor Div({},{})={}".format(a,b,a//b))
    case 6:
        print("Enter Two values for Modulo Div:")
        a,b=int(input()),int(input())
        print("Modulo Div({},{})={}".format(a,b,a%b))
    case 7:
        print("Enter Two values for Exponential:")
        a,b=int(input("Enter Base")),int(input("Enter Power"))
        print("Exponential({},{})={}".format(a,b,a**b))
    case 8:
        print("Thnx for using this App ")
    case _:
        print("Ur Selection of Opeartion is wrong-try again")
print("Program Execution Completed")

        