#Program to check word is Vowel word or not
#IfElseEx3Vowel.py
word = input("Enter a word:")
if ('a'in word.lower() or  'e'in word.lower() or 'i'in word.lower() or 'o'in word.lower() or 'u'in word.lower()):
    print("{} is Vowel Word".format(word))
else:
    print("{} is  Not Vowel Word".format(word))
    