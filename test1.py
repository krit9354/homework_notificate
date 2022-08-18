def login(usn, pw):
    if usn == "hello" and pw == "world":
        print("login success")
    else:
        print("username or password incorrect.try again")
        username = input("username : ")
        password = input("password : ")
        login(username,password)

username = input("username : ")
password = input("password : ")

login(username,password)
