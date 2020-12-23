import pickle
import sys
import os.path
from os import path 

REQUIRED_ENTRIES = {"name", "u_name", "password", "email"}

accounts = []
if path.exists("accounts.dat"):
    accounts = pickle.load(open("accounts.dat", "rb"))

for account in accounts:
    if not all(val in account for val in REQUIRED_ENTRIES):
        del accounts[accounts.index(account)]
        pickle.dump(accounts, open("accounts.dat", "wb"))

def idle():
    while True:
        next_state = input("What would you like to do next? ")

        if next_state == "add":
            add_account()
        elif next_state == "log":
            log_in()
        elif next_state == "quit":
            sys.exit("\nGood bye! Thanks for using this database!\n")
        elif next_state == "help":
            print ("""\n    add  : add an account
    log  : log in an existing account -> view the information or delete it
    quit : to stop the execution\n""")

def add_account():
    while input("Would you like to add an account? ") == "yes":
        account = {}
        name = input("Name: ")
        u_name = input("User Name: ")
        password = input("Password: ")
        conf_password = input("Confirm Password: ")
        email = input("Email: ")
        account['name'] = name
        account['u_name'] = u_name
        if password == conf_password:
            account['password'] = password
        else: 
            print ("Passwords do not match! Your account will not be added to the database!")
        account['email'] = email

        accounts.append(account)
        pickle.dump(accounts, open("accounts.dat", "wb"))


def log_in():
    if input("Would you like to log in? ") == "yes":
        success = False
        u_name = input("User Name: ")
        password = input("Password: ")
        for account in accounts:
            if u_name == account['u_name'] and password == account['password']:
                print ("Log In successful!")
                print (account)
                success = True
                # assuming that the user has already logged in
                if input("Would you like to delete your account? ") == "yes":
                    name = input("Type your name to delete this account: ")
                    if name == account['name']:
                        print ("Your account was successfully removed!")
                        del accounts[accounts.index(account)]
                        pickle.dump(accounts, open("accounts.dat", "wb"))
                    else:
                        print ("Error! Wrong name!")

        if success == False:
            print ("Error!")


idle()