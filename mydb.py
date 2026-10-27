import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    password= 'root',

)
#prepare a cursor object 
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dcrm_db")
print("ALL DONE!!")