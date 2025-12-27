#KelvinToFahrenheit.py
def KelFah():
    kt=float(input("\tEnter Temp in Kalvin to convert into Fahrenheit:"))
    ft=(kt-273.15)*((9/5)+32)
    print("\tFahrenheit Temprature of {} Degree Kelvin is {}".format(kt,ft))
    print("\t**************************************************")
