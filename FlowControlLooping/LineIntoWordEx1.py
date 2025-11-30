#Program for take line of text and split it to words and display words and lenght of words
#LineIntoWordEx1.py
sen = input("Enter Line of Text:")
word = sen.split()
print("-"*50)
print("Given Line:{}".format(sen))
print("-"*50)
print("Given Words={}".format(word))
print("-"*50)
print("\tWords\t\tLength")
print("-"*50)
i=0
while(i<len(word)):
    s = word[i]
    print("\t{}\t\t{}".format(s,len(s)))
    #print("\t{}\t\t{}".format(word[i],len(word[i])))
    i = i + 1
print("-"*50)

