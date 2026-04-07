from database1 import conn, pool
import pandas as pd

def login():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        query = """SELECT * FROM users
                   WHERE username=%s AND password=%s"""

        pool.execute(query,(username,password))

        result = pool.fetchone()

        if result:
            print("Login Successful")
        else:
            print("Invalid Username or Password")

    except Exception as err:
        print("Error is:", err)
