from database import *
class studetails():
    def __init__(self):
            self.name=input("Enter the name : ")
            self.district=input("Enter the distict : ")
            self.phone=int(input("Enter the mobile num : "))
class college(Database):
    def __init__(self):
        self.aids=[]
        self.cse=[]
        self.aiml=[]
    def Aids(self):
        self.dept_="Ai & Ds"
        a=studetails()
        self.insert(a.name, self.dept_, a.district, a.phone)
        self.aids.append([a.name, self.dept_, a.district, a.phone])
    def CSE(self ):
        self.dept_="CSE"
        a=studetails()
        self.insert(a.name, self.dept_, a.district, a.phone)
        self.cse.append([a.name, self.dept_, a.district, a.phone])
    def AIML(self):
        self.dept_="Ai & ML"
        a=studetails()
        self.insert(a.name, self.dept_, a.district, a.phone)
        self.aiml.append([a.name, self.dept_, a.district, a.phone])
    def print_aids(self):
        print("--------AI&DS-----------  these data's are you currently insert in the Sql")
        for name,dept_,district,phone in self.aids:
             print(f"name : {name}")
             print(f"department: {dept_}")
             print(f"district : {district}")
             print(f"mobile number: {phone}")
    def print_cse(self):
        print("--------CSE-----------    these data's are you currently insert in the Sql")
        for name,dept_,district,phone in self.cse:
             print(f"name : {name}")
             print(f"department: {dept_}")
             print(f"district : {district}")
             print(f"mobile number: {phone}")
    def print_aiml(self):
        print("--------AI&ML-----------  these data's are you currently insert in the Sql")
        for name,dept_,district,phone in self.aiml:
             print(f"name : {name}")
             print(f"department: {dept_}")
             print(f"district : {district}")
             print(f"mobile number: {phone}")      
        
