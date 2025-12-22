#DictComprehensionEx2.py
print("Enter the values separated by the space:")
diclst={int(val):int(val)**2 for val in input().split() if int(val)>0}
print("\tNumber\tSquares")
for v,s in diclst.items():
    print("{}-->{}".format(v,s))
