#Program for addition of two numbers by using Normal and Anonymous Function
#AnonymousFunEx1.py
def sumop(a,b): #Normal Function
    c=a+b
    return c

addop=lambda k,v:k+v #Anonymous Function


print("By using Normal Function :")
print("Type of sumo={}".format(type(sumop))) #<class 'function'>
print("Enter Two Values")
res=sumop(int(input()),int(input()))
print("Sum={}".format(res))
print("----------------------------------------------------------")
print("By using AnonymousFunction: ")
print("Type of sumo={}".format(type(addop))) #<class 'function'>
print("Enter Two Values")
res1=addop(int(input()),int(input()))
print("Sum={}".format(res1))
