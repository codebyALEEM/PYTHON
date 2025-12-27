#TempCalculator.py
from TempMenu import menu
from CelciousToFahrenheit import CalFah
from FahrenheitToCelcious import FahCel
from CelciousToKelvin import CelKel
from KalvinToCelcious import KelCel
from FahrenheitToKelvin import FahKel
from KelvinToFahrenheit import KelFah

while(True):
    menu()
    ch=int(input("\tEnter Your Choice:"))
    match(ch):
        case 1:
            CalFah()
        case 2:
            FahCel()
        case 3:
            CelKel()
        case 4:
            KelCel()
        case 5:
            FahKel()
        case 6:
            KelFah()
        case 7:
            print("\tTnx for using this app")
            break
        case _:
            print("\tInvalid Input!! Try Again ")
        
        