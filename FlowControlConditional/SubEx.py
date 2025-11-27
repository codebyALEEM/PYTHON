#Program for Subject info 
#SubEx.py
sub = {'PYTHON':"for Data Science Application","JAVA":"for Web Application","C++":"for Telecommunication Application","C":"for OS development"}
n = input("Enter Sunject Name:").upper()
print("{} is {}".format(n,sub.get(n)) if(sub.get(n)!=None) else "No Idea")