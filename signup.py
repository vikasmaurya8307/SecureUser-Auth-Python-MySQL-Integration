from database1 import conn , pool
import pandas as pd 


def signup():

    try :
            username = input("Enter a username : ")
            password  = input("Enter a password : ")

            query = '''insert into users(username,password)
            values(%s,%s)'''
            pool.execute(query,(username,password))
            conn.commit()
            print("Sign Up successfully")
            
    except Exception as err :
        print("Error is :" , err)




