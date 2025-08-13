from otherfunc import get_connection, checkamount
from datetime import datetime

mydb = get_connection()
mycursor = mydb.cursor()

def withraw():
    try:
        email = input("Enter Your Email: ")
        password = input("Enter Your Password")

        sql = "SELECT `id`,`status_id` FROM `users` WHERE email= %s AND password= %s "
        val = (email, password)
        mycursor.execute(sql,val)
        result = mycursor.fetchone()


        if result:
            id, status = result
            ihaveamount = checkamount(id)
            if status in [4, 1]:
                print(f"you Have {ihaveamount}")
                amount = float(input("How Much Do You need to Withraw :"))
                if amount <= 0:
                    print("pleas more than 0")
                    return

                description = input("enter description")
                conf = input("Please Conform withraw (y/n) :").lower()

                if conf == "y":
                    amountdb = ihaveamount
                    print(amountdb)
                    if amountdb <= amount:
                        print("Noth enough val")
                    else:
                        balance = amountdb - amount
                        current_time = datetime.now()

                        sql1 = "INSERT INTO `transaction` (users_id, amount, type_id, description, balance, time) VALUES (%s, %s, %s, %s, %s, %s)"
                        val1 = (id, amount, 2, description, balance, current_time)
                        mycursor.execute(sql1, val1)
                        mydb.commit()
                        print("Withraw Successfull")

                else:
                    print("cansel")
            else:
                print("Account is not active")
        else:
            print("NO Account Found ")
    except Exception as e:
        print(e)





