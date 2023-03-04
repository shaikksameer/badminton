from datetime import *
import time
date =  datetime.now().strftime("%d_%m_%Y")
import mysql.connector
from prettytable import PrettyTable


# Code to connec to "badminton" database 
conn = mysql.connector.connect(
   host="localhost",
   user="root",
   password="sameer",
   database="badminton",
   port=3308
)
cur = conn.cursor()
#=========================================================================================#



# Funtion for option "1. Add Time"   
def addTime():
    
    #list of all the members id in the table player
    names=[]
    cur.execute("Select * from player")
    rows = cur.fetchall()
    names=[row[1] for row in rows]
    startIndex=101
    id=[]
    for i in names:
        id.append(startIndex)
        startIndex+=1   
    
    
    # menu to take the input from the user/admin
    timePlayed=[]
    while True:
        for i in names:
            ans=float(input("{} : ".format(i)))
            timePlayed.append(ans)
        confirm=input("Do you want to save the change!?\n>>")
        if (confirm=="yes" ):
            break
        else:
            print("Okay lets try again!!")
            
            
     # to put the name and the hours played in the form of dict (key:value) (name:hourplayed)       
    player_time = dict(zip(id, timePlayed))
              #print(type(player_time))
              
              
     #to get all the column name from the table 
    cur.execute("DESCRIBE playtime")
    rows = cur.fetchall()
    column_names = [row[0] for row in rows]
    
    
     # to get the current date and match it with latest column to fill the data in the correct column 
    current_time  =  datetime.now().strftime("%d_%m_%Y")
    latestColIndex=len(column_names)-1
              # print((column_names[latestColIndex]))
              # print(current_time)
              
              
     # code to check the the details are placed in the latest column created in the database
    if column_names[latestColIndex] == current_time:
        for key, value in player_time.items():
            # print(column_names[latestColIndex])
            # print(value)
            # print(key,"\n")
            cur.execute("update  playtime set `{}`={} where player_id ={}".format(column_names[latestColIndex],value,key))
            conn.commit()  
        print("Successfully  inserted into the database!!")
    else :
        alter_col_name = datetime.now().strftime("%d_%m_%Y")
        cur.execute("Alter table playtime add column {} decimal(4,2)".format(alter_col_name))
        conn.commit()
        print("Table Error: Today's date column was not found, made the coulmn avaiable now restart the application to update the time ")
 




# Funtion for option "2. See all the player details" 
def allPlayer():
    print("Here are all the players:  ")
    time.sleep(1)
    cur.execute("select * from player")    
    results = cur.fetchall()
    table = PrettyTable()    
    table.field_names = [desc[0] for desc in cur.description]
    for row in results:
        table.add_row(row)
    print(table)   
    conn.commit()    
    print("\nThank you for waiting !!") 
    
    
    
    

# Funtion for option "3. Update the records" 
def deletePlayer():
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
               conn.commit()
               print("\nDone deleting the record!!")
               break
           else:
               print("This name is not present in the database!!")
    else:
       cur.execute("delete from rough_name where name= '{}'".format(name))
       conn.commit()
       print("Deleted the record!!")
 

    





print("/--------------------------------------------------------------/")
print("|              **WELCOME TO THE BADMINTON GROUP**              |")
print("|                                             date:{}  |".format(date))
print("/--------------------------------------------------------------/")


print("What do you want to do today ??")
print("1. Add Time")
print("2. See all the player details")
print("3. Update the records")
print("4. Exit")
menuInput=int(input(">>"))





if (menuInput==1):
    print("\nAdd time here:")
    addTime()
elif (menuInput==2):
    allPlayer()   
elif (menuInput==3):
    print("So you want to update the records")

elif (menuInput==4):
    print("Bye Bye!!")
else:
    print("Wrong input")
    
    
    
    

