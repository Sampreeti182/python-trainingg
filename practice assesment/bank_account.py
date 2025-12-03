class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_log = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_log.append(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_log.append(f"Withdrew: ${amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return self.balance

    def display_transaction_log(self):
        if not self.transaction_log:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_log:
                print(transaction)


account = BankAccount("Sampreeti", 1000)

account.deposit(500)       # Deposit $500
account.withdraw(200)      # Withdraw $200
account.deposit(300)       # Deposit $300

print(f"Current balance: ${account.check_balance()}")

print("\nTransaction Log:")
account.display_transaction_log()