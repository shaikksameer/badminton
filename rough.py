import mysql.connector
from datetime import *


# Connect to the database
conn = mysql.connector.connect(
   host="localhost",
   user="root",
   password="sameer",
   database="badminton",
   port=3308
)
cur = conn.cursor()

name=input("Who do you want to delete?")
cur.execute("select count(*) from rough_name where name like '%{}%' ".format(name))
result=cur.fetchall()
numberOfRec=(result[0])[0]
print(numberOfRec)

if numberOfRec>=2:
   print("There are more than 2 records with same name!!")
   cur.execute("select name from rough_name where name like '%{}%'".format(name))
   result=cur.fetchall()
   num=1
   nameList=[]
   for rows in result:
      name_del=rows[0]
      print("{}. {}".format(num, name_del))
      nameList.append(name_del.lower())
      num+=1
   
   while True:
       indexSelection=input("\nWhich one do you want to delete? \n>>").lower()     
       if indexSelection in nameList:
           cur.execute("delete from rough_name where name= '{}'".format(indexSelection))
           print("\nDone deleting the record!!")
           break
       else:
           print("This name is present in the database!!")
else:
   cur.execute("delete from rough_name where name= '{}'".format(name))
   print("Deleted the record!!")
   
   

    
conn.commit()
cur.close()
conn.close()