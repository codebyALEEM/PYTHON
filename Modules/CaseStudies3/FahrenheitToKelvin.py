#FahrenheitToKelvin.py
def FahKel():
    ft=float(input("\tEnter Temp in Fahrenheit to convert into Kelvin:"))
    kt=(ft-32)*((5/9)+273.15)
    print("\tKelvin Temprature of {} Degree Fahrenhite is {}".format(ft,kt))
    print("\t**************************************************")
