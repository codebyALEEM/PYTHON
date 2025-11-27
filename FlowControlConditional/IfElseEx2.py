#Program for Palindrome by using If Esle
#IfElseEx2.py
word = input("Enter any Word:")
if(word==word[::-1]):
    print("{} is PALINDROME".format(word))
else:
    print("{ is NOT PALINDROME}".format(word))
print("Program Execution Completed")