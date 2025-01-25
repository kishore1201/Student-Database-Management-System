from database import *
from deptdetails import *
print ("=========================================================")
print("======================STU_DETAILS========================")
print("If you completed means type 'end' ")
v=college()            
while True:
    m=input("Enter your the department").strip().lower()
    if m=="end":
         break
    elif m=="aids" :
          v.Aids()
    elif m=="cse":
          v.CSE() 
    elif m== "aiml" : 
          v.AIML()
print("======================STU_DETAILS========================")
v.print_aids()
print("======================STU_DETAILS========================")
v.print_cse()
print("======================STU_DETAILS========================")
v.print_aiml()
