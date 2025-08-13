from otherfunc import get_connection, checkamount
from datetime import datetime

mydb = get_connection()
mycursor = mydb.cursor()

def deposit():
    try:
        email = input("Enter Your Email: ")
        password = input("Enter Your Password")

        sql = "SELECT `id`,`status_id` FROM `users` WHERE email= %s AND password= %s "
        val = (email, password)
        mycursor.execute(sql,val)
        result = mycursor.fetchone()

        if result:
            id, status = result
            if status in [4, 1]:
                amount = float(input("How Much Do You need to Deposit :"))
                if amount <= 0:
                    print("pleas more than 0")
                    return

                description = input("enter description")
                conf = input("Please Conform deposit (y/n) :").lower()

                if conf == "y":
                    amountdb = checkamount(id)
                    balance = amountdb + amount
                    current_time = datetime.now()

                    sql1 = "INSERT INTO `transaction` (users_id, amount, type_id, description, balance, time) VALUES (%s, %s, %s, %s, %s, %s)"
                    val1 = (id, amount, 1, description, balance, current_time)
                    mycursor.execute(sql1, val1)
                    mydb.commit()
                    print("Deposit Successfull")

                else:
                    print("cansel")
            else:
                print("Account is not active")
        else:
            print("NO Account Found ")
    except Exception as e:
        print(e)



