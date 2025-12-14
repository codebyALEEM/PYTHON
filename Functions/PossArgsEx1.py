#Program for Demonstarting the concept of Possitional Arguments.
#PossArgsEx1.py
def dispstudinfo(sno,sname,marks):
    print("\t{}\t{}\t{}".format(sno,sname,marks))
    
    
print("="*50)
print("\tSNO\tSNAME\tMARKS")
print("="*50)
dispstudinfo(100,"RS",34.56)
dispstudinfo(200,"TR",44.55)
dispstudinfo(300,"DR",14.55)
dispstudinfo(400,"KV",11.11)
print("="*50)
