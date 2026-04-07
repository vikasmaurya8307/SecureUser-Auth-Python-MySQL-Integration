from database1 import conn, pool
import pandas as pd
from signup import signup
from login import login
from show_user import show_all_users


def menu():

    try :

        print("1 Sign Up")
        print("2 Login ")
        print("3 Show all users")

        choice = int(input("Enter choice :"))

        if choice == 1 :
            signup()
        
        elif choice == 2 :
            login()

        elif choice == 3 : 
            show_all_users()
        else:
            print("Invalid user choice")
    except Exception as err :
        print("Error is  : ",err)

menu()