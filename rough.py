import mysql.connector
from datetime import *


# Connect to the database
conn = mysql.connector.connect(
   host="localhost",
   user="root",
   password="sameer",
   database="badminton",
   port=3306
)
cur = conn.cursor()

# Menu for updating the database 
print("What do you want to do?")
print("1. Delete a player from the database")
print("2. Add a new player ")
print("3. Alter the time updated")
choiceSelected=int(input(">>\n"))

#1. Delete a player from the database
if choiceSelected==1:      
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

#2. Add a new player 
elif choiceSelected==2:
   print("Please enter the detials below: ")
   name=input("Enter name: ")
   phoneNumber=input("Enter phone number here: ")
   if phoneNumber[0:3]=='+91':
       pass
   else:
       phoneNumber='+91'+phoneNumber
   print("Deatil of the new player ")
   print("Name: {}".format(name))
   print("Phone Number: {}".format(phoneNumber))
   while True:
      print("Do you want to save the record?\n>>")
      confirm=input()
      if confirm=='yes':
         cur.execute("Insert into player value")  
      else:
         print("1. Do you want to ")
         
   
   

    
conn.commit()
cur.close()
conn.close()