#Program for Demonstarting the concept of default Arguments.
#DefArgsEx4.py
def dispstudinfo1(sno,sname,marks,crs="PYTHON"):
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))
    
def dispstudinfo2(sno,sname,marks,crs="JAVA"):
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))
    
print("="*50)
print("\tSNO\tSNAME\tMARKS\tCRS")
print("="*50)
dispstudinfo1(100,"RS",34.56)
dispstudinfo1(200,"TR",44.55)
dispstudinfo1(300,"DR",14.55)
dispstudinfo1(400,"KV",11.11)
print("="*50)
print("\tSNO\tSNAME\tMARKS\tCRS")
print("="*50)
dispstudinfo2(500,"TMP",10.11)
dispstudinfo2(600,'BDN',30.11)
dispstudinfo2(700,"VK",40.11)
print("="*50)