#BreakEx3.py
names = ["Travis","David","Jhon","Rossum","Sunny"]

for name in names:
    print("Checking:",name)
    if name=="Rossum":
        print("Found {}->break!".format(name))
        break
print("Search complete")