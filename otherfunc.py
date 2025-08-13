import mysql.connector

def displaymenu():
    print("______________________________________________________________")
    print("----------------------LS Bank System--------------------------")
    print("--------------------------------------------------------------")

def whattodo():
    print(" ")
    print("Press 1 for Create new Accouunt")
    print("Press 2 for Deposit Money")
    print("Press 3 for Withraw Money")
    print("Press 4 Delete Account ")
    print("Press 5 for exit")

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="senira",
        password="Sethmika@2006",
        database="mydatabase"
    )

def checkamount(user_id):
    mydb = get_connection()
    mycursor = mydb.cursor()

    sql = "SELECT balance FROM transaction WHERE users_id = %s ORDER BY id DESC LIMIT 1;"
    val = (user_id,)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    if data:
        oldbalance = int(data[0][0])
        return oldbalance
    else:
        return 0
