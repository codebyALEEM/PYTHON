#Program for Simple Interest and Total Amount to Pay
p =float(input("Enter Principle Amount:"))
t =float(input("Time Period:"))
r =float(input("Rate of interest:"))
si = (p+t+r)/100
ta = p + si
print("="*50)
print("Simple Interest:{}".format(si))
print("Total Amount to Pay:{}".format(ta))
print("="*50)