#Program to check the word is palindrome or not by using fuction
#PalindromeFunEx.py
def palin():
    while (True):
        word = input("Enter a Word:")
        if " " in word:
            print("'{}' contains Space. Enter without Space ".format(word))
        else:
            if (word == word[::-1]):
                print("PALINDROME")
            else:
                print("NOT PALINDROME")
        while(True):
            chk = input("Do you want to Try with other word?(yes/no)")
            if(chk.lower()=='yes'):
                break
            elif chk.lower() == 'no':
                print("Tnx for using this app")
                return
            else:
                print("{} is Invalid Input.Try 'yes' or 'no'".format(chk))



palin()
