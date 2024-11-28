import random
class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = None
        self.balance = 0
        self.transaction = []
        self.count = 1

    def create_account(self, name, email, address, account_type, bank):
        usr = User(name, email, address, account_type)
        usr.account_number = bank.generate_account_number()
        bank.accounts[usr.account_number] = usr


    def deposit_money(self, amount):
        self.balance += amount
        transaction = f'Deposit : {amount}'
        self.transaction.append(transaction)
        print("Money Deposited Succesfully .. ")

    def withdraw_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = f"Withdraw : {amount}"
            self.transaction.append(transaction)
            print("Money withdraw successfully !")
        else:
            print("Withdrawal amount exceeded")

    def check_available_balance(self):
        print(self.balance)

    def chek_transaction_history(self):
      
        for user in self.transaction:
            print(user)


    def take_loan_from_bank(self, amount, bank):
        if bank.loan_feature == True:
            if self.count < 3:
                self.count += 1
                bank.loan_balance += amount
                bank.bank_balance -= amount
                transaction = f'Loan from the Bank : {amount}'
                self.transaction.append(transaction)
                print("You Have Loan The Money Succesfully")
            else:
                print("Loan's Time Is Over !!")
        else:
            print("Bank Is BankRupt !! ")


    def transfer_money(self, from_acc_nmb, recv_acc_nmb, amount, bank):
        if recv_acc_nmb in bank.accounts and from_acc_nmb in bank.accounts:
            bank.accounts[from_acc_nmb].balance -= amount
            bank.accounts[recv_acc_nmb].balance += amount
            transaction = f'Money Transaction : {amount}'
            self.transaction.append(transaction)
            print("Money Transferred Successfully .. ")

        else:
            print("Account does not exist ")


class Bank:
    def __init__(self, name, initial_balance) -> None:
        self.name = name
        self.bank_balance = initial_balance
        self.loan_balance = 0
        self.loan_feature = True
        self.accounts = {}
    
    def generate_account_number(self):
        while True:
            account_num = random.randint(50000, 500000)
            if account_num not in self.accounts:
                return account_num



class Admin:
    def __init__(self, bank) -> None:
        self.bank = bank


    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        user.account_number = bank.generate_account_number()
        self.bank.accounts[user.account_number] = user


    def del_account(self, account_number):
        if account_number in self.bank.accounts:
            del self.bank.accounts[account_number]
            print(f'{account_number} Account Deleted Successfully .. ')
        else:
            print("This Account Dose Not Exit .. ")


    def show_all_account_list(self):
        if self.bank.accounts:
            for acc_nmb, user in self.bank.accounts.items():
                print(f'user account_number : {acc_nmb} -> user_name : {user.name} -> user_email : {user.email}')
        else:
            print("No User Exit .. ")


    def check_available_bank_balance(self):
        print(self.bank.bank_balance)


    def chek_total_loan_ammount(self):
        print(self.bank.loan_balance)

    def loan_feature_system(self):
        self.bank.loan_feature = False
        print("Loan Featue System has been OFF successfully .. ")


    
user = User('karim', 'karim@gmail.com', 'Chittagong', 'Buisness')
bank = Bank('Graming Bank', 100000)
admin = Admin(bank)

def user_account():
    print("Choice : ")

    while True:
        print("1. Create Account : ")
        print("2. Deposit Money : ")
        print("3. Withdraw Money : ")
        print("4. Check Available Balance : ")
        print("5. Check Transiction History : ")
        print("6. Take Loan From The Bank : ")
        print("7. Transfer Money : ")
        print("8. Exit !!")

        ch = int(input("Enter Your Choice : "))

        if ch == 1:
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            address = input("Enter Your Address : ")
            typeOfAcco = input("Enter Type Of Account : ")
            user.create_account(name, email, address,  typeOfAcco, bank)
        elif ch == 2:
            amount = int(input("Enter Your Amount Of Money : "))
            user.deposit_money(amount)
        elif ch == 3:
            amount = int(input("Enter Your Amount Of Money : "))
            user.withdraw_money(amount)
        elif ch == 4:
            user.check_available_balance()
        elif ch == 5:
            user.chek_transaction_history()
        elif ch == 6:
            amount = int(input("Enter Your Amount Of Money : "))
            user.take_loan_from_bank(amount, bank)
        elif ch == 7:
            from_acc_nmb = int(input("Enter Your Account nmb : "))
            recv_acc_nmb = int(input("Enter User nmb : "))
            amount = int(input("Enter Your Amount Of Money : "))
            user.transfer_money(from_acc_nmb, recv_acc_nmb, amount, bank)
        elif ch == 8:
            print("Exit !!")
            break
        else:
            print("Invalid !")


def admin_account():

    print("Choice !!")
    while True:
        print("1. Create Account : ")
        print("2. Delete Any User Account : ")
        print("3. See All User Accounts List : ")
        print("4. Chek Total Available Balance Of The Bank : ")
        print("5. Check The Total Loan Amount : ")
        print("6. ON Or OFF The Loan Feature Of The Bank : ")
        print("7. Exit !!")

        ch = int(input("Enter Your Choice : "))

        if ch == 1:
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            address = input("Enter Your Address :")
            typeOfAcco = input("Enter Type Of Account : ")
            admin.create_account(name, email, address, typeOfAcco)
        elif ch == 2:
            del_acc = int(input("Enter User Account nmb : "))
            admin.del_account(del_acc)
        elif ch == 3:
            admin.show_all_account_list()
        elif ch == 4:
            admin.check_available_bank_balance()
        elif ch == 5:
            admin.chek_total_loan_ammount()
        elif ch == 6:
            admin.loan_feature_system()
        elif ch == 7:
            print("Exit !!")
            break
        else:
            print("Invalid !")


while True:
    print("Choice !! ")
    print("1. User ")
    print("2. Admin ")
    print("3. Exit !!")

    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        user_account()
    elif ch == 2:
        admin_account()
    elif ch == 3:
        print("Exit !! ")
        break
    else:
        print("Invalid !")

    


        

            




    