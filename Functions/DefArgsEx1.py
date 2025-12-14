#Program for Demonstarting the concept of default Arguments.
#DefArgsEx1.py
def dispstudinfo(sno,sname,marks,crs='PYTHON'):
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))
    
    
print("="*50)
print("\tSNO\tSNAME\tMARKS\tCRS")
print("="*50)
dispstudinfo(100,"RS",34.56)
dispstudinfo(200,"TR",44.55)
dispstudinfo(300,"DR",14.55)
dispstudinfo(400,"KV",11.11)
print("="*50)


