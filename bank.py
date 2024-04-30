class Bank:
    total_loan = 0
    bank_money = 10000
    def __init__(self, name):
        self.name = name
        self.__is_bankrupt = False
        self.total_users_account = []
        self.__loan_status = True # True means he can take loans
    
    @property
    def is_bankcrupt(self):
        return self.__is_bankrupt
    
    @property
    def isloan(self):
        return self.__loan_status

    def add_user_account(self, account):
        self.total_users_account.append(account)

    def check_balance_of_bank(self):
        print(f"Available balance of Bank: {self.bank_money}")

    def see_users_account(self):
        if len(self.total_users_account) != 0:
            for account in self.total_users_account:
                print(f"Name: {account.name} Email: {account.email} Address: {account.address} Account Type: {account.account_type} Account Number: {account.account_num}") 
        
        else:
            print("There are no users!!!")

    def check_account(self, account_num):
        for account in self.total_users_account:
            if account.account_num == account_num:
                return True
            
        return False
    
    def delete_account(self, account_num):
        for account in self.total_users_account:
            if account.account_num == account_num:
                self.total_users_account.remove(account)
                print("Account Has been removed!!!")
                return

        print("Account Not Found!!!")

    def transfer_money(self, amount, sender_acc_no, reciever_acc_no):
        for account in self.total_users_account:
            if account.account_num == reciever_acc_no:
                account.balance += amount
                print("Money Transferred Successfully!!!")
                return

    def check_total_loan_amount(self):
        print(f"Total Loan: {self.total_loan}") 