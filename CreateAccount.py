from datetime import datetime
from otherfunc import get_connection

mydb = get_connection()
mycursor = mydb.cursor()

def createaccount():
    fname = input("Enter Your First Name: ")
    lname = input("Enter Your Last Name: ")
    email = input("Enter Your email: ")
    password = input("Enter Your Password: ")
    current_time = datetime.now()

    sql = "SELECT * FROM `users` WHERE email= %s"
    val = (email,)
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    count = result[0] if result else 0

    if count > 0:
        print("An account with this email already exists")
    else:

        sql2 = """
                INSERT INTO users (fname, lname, email, password, created_at, status_id) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
        val2 = (fname, lname, email, password, current_time, 1)
        mycursor.execute(sql2,val2)

        mydb.commit()

        print(" ")
        print(f"Account for {fname} {lname} has been created successfully!")
        print("Thank You, See you again!")
        mycursor.close()
        mydb.close()
        exit()

