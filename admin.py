from bank import Bank

class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        
    def loan_status_of_bank(self):
        print("1. Turn off loan feature")
        print("2. Turn on loan feature")
        option = int(input("Enter your option: "))

        if option == 1:
            Bank.isloan = False

        elif option == 2:
            Bank.isloan = True

        else:
            print("You Entered wrong Option!!!")

    def bankrupt(self):
        print("Is the Bank is Bankrupt?")
        print("1. YES")
        print("2. NO")
        option = int(input("Enter your option: "))

        if option == 1:
            Bank.is_bankcrupt = True

        elif option == 2:
            Bank.is_bankcrupt = False

        else:
            print("You Entered wrong Option!!!")