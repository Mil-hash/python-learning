stored_username = "Mil-hash"
stored_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("success!")
else:
    print("wrong username or password")