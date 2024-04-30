from bank import Bank
from datetime import datetime

class User:
    def __init__(self, name, email, address, account_type, balance):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = balance
        self.account_num = 0
        self.transaction_history = []
        self.num_of_taking_loan = 2

    def deposit_money(self, deposit_amount):
            if deposit_amount > 0:
                self.balance += deposit_amount
                print("Money deposited successfully!!!")
                self.transaction_history.append([datetime.now(), deposit_amount, "Deposit"])

            else:
                print("Invalid Amount of money!!!")

    def withdraw_money(self, withdraw_amount):
        if withdraw_amount < 0: #negetive
            print("Invalid Amount of money!!!")

        elif withdraw_amount > self.balance:
            print("Withdraw amount exceeded!!!")

        elif self.balance == 0:
            print('You don\'t have money!!! Please deposit some mopney!')

        else:
            print("You withdraw money successfully!!!")
            self.balance -= withdraw_amount 
            self.transaction_history.append([datetime.now(), withdraw_amount, "Withdraw"])

    def available_balance(self):
        print(f"Available Balance in your account: {self.balance}")

    def see_transaction_history(self):
        for transaction in self.transaction_history:
            print(f"Time: {transaction[0]} Money Amount: {transaction[1]} Transaction Type: {transaction[2]}")
    
    def take_loan(self, amount): #problem
        if amount > Bank.bank_money:
            print("You can't take loan!!! amount exceeded!")

        else:
            if self.num_of_taking_loan > 0:
                Bank.bank_money -= amount
                self.balance += amount
                self.num_of_taking_loan -= 1
                Bank.total_loan += amount 
                self.transaction_history.append([datetime.now(), amount, "Loan"])
                print("You take Loan from Successfully!!!")