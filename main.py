from user import User
from admin import Admin
from bank import Bank

myBank = Bank("Ma er Doya Bank")

def user_info_input():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    address = input("Enter Your Address: ")
    account_type = input("Enter Your Account Type: ")

    return [name, email, address, account_type, 0] 

while True:
    print(f"===== Welcome To \'{myBank.name}\' =====")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    option = int(input("Enter Your Option: "))

    if option == 1:
        while True:
            print(f"=== Welcome User to our Bank ===")
            print("1. Create an Account")
            print("2. Withdraw Money")
            print("3. Deposite Money")
            print("4. Check Available Balance")
            print("5. Check Transaction History")
            print("6. Take Loan")
            print("7. Transfer Money")
            print("8. Back To Main Page")

            user_option = int(input("Enter Your Option: "))

            if user_option == 1:
                user_info = user_info_input()
                user = User(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4]) 
                myBank.add_user_account(user)

                user.account_num = len(myBank.total_users_account) + 1000

                print("Congrates!!! Your Account has been created!!!")
                print(f"Your Account No. is- {user.account_num}")

            elif user_option == 2:
                if myBank.is_bankcrupt == False:
                    withdraw_amount = int(input("Enter Your Withdraw amount: "))
                    user.withdraw_money(withdraw_amount=withdraw_amount)

                else:
                    print("Bank is Bankrupt!!! Withdraw limit exceeded!")

            elif user_option == 3:
                deposit_amount = int(input("Enter Your Deposit amount: "))
                user.deposit_money(deposit_amount)

            elif user_option == 4:
                user.available_balance()

            elif user_option == 5:
                user.see_transaction_history()

            elif user_option == 6:
                    if user.num_of_taking_loan <= 0:
                        print("You can only take loan 2 times!!!")

                    elif myBank.isloan == True:
                        amount = int(input("Enter Money Amount: "))
                        user.take_loan(amount)

                    else:
                        print("You can't Take loan Now!!!")

            elif user_option == 7:
                sender = int(input("Enter Your account Number: "))
                reciever = int(input("Enter account Number where you want to send money: "))

                check_user = myBank.check_account(sender)
                check_reciver = myBank.check_account(reciever)

                if check_user and check_reciver:
                    amount = int(input("Enter Money Amount: "))
                    if user.balance > 0 and amount <= user.balance:
                        myBank.transfer_money(amount, sender, reciever)            
                        user.balance -= amount 

                    else:
                        if user.balance == 0:
                            print("You don\'t have money!!!")
                        elif amount > user.balance:
                            print("Money amount excceded!!!")
                        else:
                            print("Invalid Amount of money!!!")    

                else:
                    if check_user == False:
                        print("Your Account does not exist!!!")

                    elif check_reciver == False:
                        print("Reciever\'s Account does not exist!!!")

            elif user_option == 8:
                break

            else:
                print("Invalid Option!!!")

    elif option == 2:
        print("To login as a Admin, enter correct user_name and password of admin-")
        admin_name = input("Enter name: ")
        admin_password = input("Enter admin\'s password: ")

        if admin_name == "admin" and admin_password == "123":
            admin = Admin("admin", "123")
            print("Cogrates!!! Now You are Log in as a admin!")
            
            while True:
                print(f"=== Welcome {admin_name} to our Bank ===")
                print("1. Create an Account")
                print("2. Delete an Account")
                print("3. check All Accounts")
                print("4. check total Available Bank Balance") #problem
                print("5. check Total Loan amount")
                print("6. Loan Feature")
                print("7. is The Bank bankrupt?")
                print("8. Back To Main Page")

                admin_option = int(input("Enter Your Option: "))

                if admin_option == 1:
                    user_info = user_info_input()
                    user = User(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4]) 

                    myBank.add_user_account(user)
                    user.account_num = len(myBank.total_users_account) + 1000
                    
                    print("Congrates!!! Account has been created!!!")

                elif admin_option == 2:
                    acc_no = int(input("Enter Account number: "))
                    myBank.delete_account(account_num=acc_no)

                elif admin_option == 3:
                    myBank.see_users_account()

                elif admin_option == 4:
                    myBank.check_balance_of_bank()
                
                elif admin_option == 5:
                    myBank.check_total_loan_amount()

                elif admin_option == 6:
                    admin.loan_status_of_bank()
                    print(myBank.isloan)

                elif admin_option == 7:
                    admin.bankrupt()

                elif admin_option == 8:
                    break

                else:
                    print("You Entered Wrong Option!!!")

        else:
            print("You entered wrong informations!!!")

    elif option == 3:                
        break

    else:
        print("Invalid Option!!! Please select Correct Option!!!")