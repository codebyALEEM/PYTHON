#Program for Demonstarting the concept of Possitional Arguments.
#PossArgsEx2.py
def dispstudinfo(sno,sname,marks,crs):
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))
    
    
print("="*50)
print("\tSNO\tSNAME\tMARKS\tCRS")
print("="*50)
dispstudinfo(100,"RS",34.56,"PYTHON")
dispstudinfo(200,"TR",44.55,"PYTHON")
dispstudinfo(300,"DR",14.55,"PYTHON")
dispstudinfo(400,"KV",11.11,"PYTHON")
print("="*50)
