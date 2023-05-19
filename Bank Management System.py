class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def get_account_holder_name(self):
        return self.account_holder_name

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful. Current balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful. Current balance:", self.balance)
        else:
            print("Insufficient funds. Current balance:", self.balance)


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_holder_name, initial_balance):
        account = BankAccount(account_number, account_holder_name, initial_balance)
        self.accounts.append(account)
        print("Account created successfully.")

    def perform_deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def perform_withdrawal(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print("Account Holder Name:", account.get_account_holder_name())
            print("Account Balance:", account.get_balance())
        else:
            print("Account not found.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None


bank = Bank()

while True:
    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        account_number = input("Enter account number: ")
        account_holder_name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.create_account(account_number, account_holder_name, initial_balance)

    elif choice == "2":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        bank.perform_deposit(account_number, amount)

    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        bank.perform_withdrawal(account_number, amount)

    elif choice == "4":
        account_number = input("Enter account number: ")
        bank.check_balance(account_number)

    elif choice == "5":
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
