from tabulate import tabulate
import psycopg2
hostname='localhost'
database='demo'
username='postgres'
pwd='root'
port_id=5432
connection= psycopg2.connect(
      host=hostname,
      dbname=database,
      user= username,
      password=pwd,
      port=port_id)
class Database():
      def db_connect_or_not(self):
                  if connection . is_connected():
                        print("connected succesfully")
                  else:
                        print(" ! failed")
      def insert (self,name,dept,district,PHONE_NUM):
            cur=connection.cursor()
            sql="insert into stu(name,dept,district,PHONE_NUM) values (%s,%s,%s,%s)"
            user=(name,dept,district,PHONE_NUM)
            cur.execute(sql,user)
            connection.commit()
            print("The data should be inserted successfully")
            cur.close()
            

      def update (self,name,dept,district,PHONE_NUM,id):
            cur=connection.cursor()
            sql="update stu set name=%s,dept=%s,district=%s,PHONE_NUM=%s  where id=%s" 
            user=(name,dept,district,PHONE_NUM,id)
            cur.execute(sql,user)
            connection.commit()
            print("The data should be updated successfully")
            cur.close()
            
            
      def delete(self,id):
            cur=connection.cursor()
            sql="delete from stu where id=%s" 
            user=(id)
            cur.execute(sql,user)
            connection.commit()
            print("The data should be delete successfully")
            cur.close()
           
      def select (self):
            cur=connection.cursor()
            sql="SELECT  * FROM stu"
            cur.execute(sql)
            result= cur.fetchall()
            print (tabulate(result,headers=["ID","NAME","DEPT","DISTRICT","PHONE_NUM"]))     
            cur.close()
            
