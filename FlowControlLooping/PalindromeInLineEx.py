#PalindromeInLineEx.py
txt = input("Enter a Line of Text:")
print("-"*50)
ew = txt.split()
for i in ew:
    if i==i[::-1]:
        print("'{}' -  PALINDROME".format(i))
        print("- - "*25)
    else:
        print("'{}' - NOT PALINDROME".format(i))
        print("- - "*25)
else:
    print("Program Execution Completed")