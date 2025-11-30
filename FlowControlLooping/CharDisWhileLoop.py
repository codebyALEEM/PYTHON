#Program to display each and every character from string
#CharDisWhileLoop.py
sen = input("Enter a Line Of Text :")
print("-"*50)
print("Each and Every Letter ")
print("-"*50)
i=0
while(i<len(sen)):
    print("\t{} ".format(sen[i]))
    i=i+1
else:    
    print("-"*50)
    print("Program Execution Completed")
    print("-"*50)