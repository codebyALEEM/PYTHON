#SetComprehensionEx2.py
print("Enter List of Values separated by space:")
lst=input().split()
print("Given List:",lst)
sqset={int(val)**2 for val in lst}
print("Square Set:",sqset)
print("Type of Sqlst:",type(sqset))
