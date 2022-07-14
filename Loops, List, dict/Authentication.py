user_id='geitpl@123'
password=12345

id_var=input("Enter the user ID : ")

if id_var==user_id:
    pin=int(input("Enter the password : "))
    if pin==password:
        print("login successful")
    else:
        print("Invalid password, Try again")
else:
    print("Invalid userID, try again")