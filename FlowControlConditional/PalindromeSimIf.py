#Program to check the given word is palindrome or not
#PalindromeSimIf.py
word = input("Enter any word to check it is a Palindrome:")
if word==word[::-1]:
    print("{} is a PALINDROME".format(word))
if word!=word[::-1]:
    print("{} is NOT PALINDROME".format(word))
print("="*50)