import mysql.connector
import pandas as pd

db = {
"host" : "localhost",
"password" : "",
"port" : 3306,
"user" : "root",
"database" : "login_system",
}
try: 
    conn = mysql.connector.connect(**db)
    pool = conn.cursor(dictionary=True)
    print("DB connected successfully ")
except Exception as err :
    print("Error is : " , err)