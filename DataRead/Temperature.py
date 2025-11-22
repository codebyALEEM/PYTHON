#Program to convert Temperature from Celsius to Fehrenhite and Kalvin
tc = float(input("Enter Temperature:"))
f = ((9/5)*tc)+32
k = tc + 273.15
print("="*50)
print("Temperature in Degree Celsius:{}".format(tc))
print("Temperature in Fehrenhite:{}".format(f))
print("Temperature in Kelvin:{}".format(k))
print("="*50)