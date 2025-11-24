#PalindromeEx.py
word = input("Enter Word:")
pal ="PALINDROME" if word==word[::-1] else "NOT PALINADROME"
print("{} is {}".format(word,pal))