#FahrenheitToCelcious.py
def FahCel():
    ft=float(input("\tEnter Temp in Fahrenheit to convert to Celcius:"))
    ct=((ft-32)/1.8)
    print("\tCelcius Temprature of {} Degree Fahrenhite is {}".format(ft,ct))    
    print("\t**************************************************")