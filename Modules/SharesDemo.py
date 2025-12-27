#SharesDemo.py
import Shares,time,importlib
def dispshares(d):
    print("------------------------------------------------")
    print("\tShareName\tShareValue")
    print("------------------------------------------------")
    for sn,sv in d.items():
        print("\t{}\t{}".format(sn,sv))
    print("------------------------------------------------")
    
#man program
d=Shares.sharesinfo()
dispshares(d)
print("I am goin to Sleep for 10 seconds")
time.sleep(10)
print("I am coming out of Sleep")
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)
print("I am goin to Sleep for 10 seconds")
time.sleep(10)
print("I am coming out of Sleep")
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)
