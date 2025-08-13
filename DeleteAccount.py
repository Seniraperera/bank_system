from otherfunc import get_connection, checkamount

mydb = get_connection()
mycursor = mydb.cursor()

def deleteAccount():
    email = input("Enter Your Email: ")
    password = input("Enter Your Password")

    sql = "SELECT `id`,`status_id` FROM `users` WHERE email= %s AND password= %s "
    val = (email, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        id, status = result
        if status in [4, 1]:
            conf = input("Are You sure? (y/n) :").lower()
            if conf == "y":
                sql = "UPDATE users SET status_id = 3 WHERE id =%s"
                val = (id,)
                mycursor.execute(sql,val)
                mydb.commit()
                print("Account Delleted")
        elif status == 3:
            print("Alrady Deleted")
        else:
            print("something error ")

