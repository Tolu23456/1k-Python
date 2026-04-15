class Account:
    def __init__(self, account_name: str):
        self.account_name = account_name
        self.balance = 0
    
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        
        self.balance += amount
        print("Deposit successful\n")
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient Funds\n")
    
    def transfer(self, receiver, amount):
        if amount > self.balance:
            print("Insufficient funds!\n")
        else:
            self.balance -= amount
            receiver.balance += amount
            print("Transfer successful\n")


class Bank:
    def __init__(self):
        self.accounts = []
    
    def create_account(self, account_name):
        if self.find_account(account_name):
            print("User already exists!\n")
            return
    
        new_account = Account(account_name)
        self.accounts.append(new_account)
        print("Account created successfully!\n")
    
    def find_account(self, account_name):
        for acc in self.accounts:
            if acc.account_name == account_name:
                return acc
        return None
    
    def show_all_accounts(self):
        for n in self.accounts:
            print(f"{n.account_name}: {n.balance}")



print("""1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Show Accounts
6. Exit
""")

b1 = Bank()


while True:
    choice = input("Enter choice: ")
    
    match choice:
        case "1":
            user_name = input("Enter account name: ").capitalize()
            b1.create_account(user_name)
        case "2":
            user_name = input("Enter account name: ").capitalize()
            try:
                amount = int(input("Enter amount: "))
                acc = b1.find_account(user_name)
                if acc:
                    acc.deposit(amount)
                else:
                    print("Account not found")
            except ValueError as e:
                print(e)
        case "3":
            try:
                user_name = input("Enter account name: ").capitalize()
                amount = int(input("Amount: "))
                acc = b1.find_account(user_name)
                if acc:
                    acc.withdraw(amount)
                else:
                    print("Account not found")
            except ValueError as e:
                print(e)
        case "4":
            try:
                sender = input("Enter account name: ").capitalize()
                receiver = input("Enter receiver's name: ").capitalize()
                amount = int(input("Amount: "))
                sender_acc = b1.find_account(sender)
                receiver_acc = b1.find_account(receiver)
    
                if not sender_acc or not receiver_acc:
                    print("Account not found")
                else:
                    sender_acc.transfer(receiver_acc, amount)
            except ValueError as e:
                print(e)
        case "5":
            b1.show_all_accounts()
        case "6":
            print("Good bye!")
            break
        case _:
            print("Invalid command")
            