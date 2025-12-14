#Program for Demonstarting the concept of default Arguments.
#DefArgsEx3.py
def dispstudinfo(sno,sname,marks,crs="PYTHON",crt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,crt))
    
    
print("="*50)
print("\tSNO\tSNAME\tMARKS\tCRS\tCRT")
print("="*50)
dispstudinfo(100,"RS",34.56)
dispstudinfo(200,"TR",44.55)
dispstudinfo(300,"DR",14.55)
dispstudinfo(400,"KV",11.11)
dispstudinfo(500,"TMP",10.11,crt="USA")
dispstudinfo(600,'BDN',30.11,"POLITICS","USA")
dispstudinfo(700,"VK",40.11)
print("="*50)
    
    