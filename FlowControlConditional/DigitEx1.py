#DigitEx1.py
d= {0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
n = int(input("Enter a  Digit:"))
res = d.get(n)
if (res!=None):
    print("{} is {}".format(n,res))
else:
    print("{} is a Number".format(n))