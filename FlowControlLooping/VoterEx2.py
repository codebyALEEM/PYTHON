#VoterEx2.py
while(True):    
    age = int(input("Enter Age:"))
    if(age>=18) and (age<100):
        break
    else:    
        print("{} Years Invalid Age,Try Again".format(age))
        
print("{} Years Citizen is Eligible to Vote".format(age))