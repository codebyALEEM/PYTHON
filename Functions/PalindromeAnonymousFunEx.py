#Program to check given word is Palindrome or not
#PalindromeAnonymousFunEx.py
palin=lambda word:"Palindrome" if word==word[::-1] else "Not Palindrome"

print("="*50)
word=input("Enter a word :")
res=palin(word)
print("{}".format(res))
print("="*50)
print("Program Execution Completed")