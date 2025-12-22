#ListComprehensionEx3.py
lst=input("Enter a list of values separated by space:").split()
pslst=[int(val) for val in lst if int(val)>0]
print("List +VE:",pslst)
nglst=[int(val) for val in lst if int(val)<0]
print("List -VE:",nglst)