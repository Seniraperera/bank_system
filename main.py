from  CreateAccount import createaccount
from DeleteAccount import deleteAccount
from Deposit import  deposit
from Withraw import withraw
from otherfunc import displaymenu,whattodo

def main():
    while True:
        displaymenu()
        whattodo()

        select = input("Enter Number:")

        if select == "1":
            createaccount()
        elif select == "2":
            deposit()
        elif select == "3":
            withraw()
        elif select == "4":
            deleteAccount()
        elif select == "5":
            exit()
        else:
            print("Please select one")


main()