class BankAccount:

    bank_name = "Pigi Bank"

    def __init__(self, owner, account_number, balance = 0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount entered. Number should be positive"

        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount:.2f}")
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if self.balance <= 0:
            return "Withdrawal amount must be positive"

        if amount > self.balance:
            return f"Insufficient funds! Current balance: ${self.balance:.2f}"

        self.balance -= amount
        self.transaction_history.append(f"Deposited: ${amount:.2f}")
        return f"Withdrawal ${amount:.2f}. New balance: ${self.balance:.2f}"

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def get_transactions(self):
        if not self.transaction_history:
            return "No transactions yet"

        history = f"\n--- Transaction history for {self.owner} ---\n"
        for transaction in self.transaction_history:
            history += transaction + "\n"
        history += f"Current Balance: ${self.balance:.2f}"
        return history

    def transfer(self, amount, other_account):
        if amount <= 0:
            return "Transfer cannot be negative"

        if amount > self.balance:
            return f"Insufficient funds! Current balance: ${self.balance:.2f}"

        self.balance -= amount
        self.transaction_history.append(f"Transferred: ${amount:.2f} to {other_account.owner}")

        other_account.balance += amount
        other_account.transaction_history.append(f"Received: ${amount:.2f} from {self.owner}")

        return f"Transferred ${amount:.2f} to {other_account.owner}. New balance: ${self.balance:.2f}"



    def __str__(self):
        return f"{self.bank_name} - Account #{self.account_number} - Owner: {self.owner} - Balance: {self.balance:.2f}"

print("-"*10, " WELCOME TO PIG0 BANK ", "-"*10)

account1 = BankAccount("Max Johnson", "ACC001", 5000)
account2 = BankAccount("Edmund Stone", "ACC002", 7500)

print(account1)
print(account2)
print("")

#deposits
print("--- DEPOSITS ---")
print(account1.deposit(240))
print(account2.deposit(300))
print()
#withdrawals
print("--- WITHDRAWALS ---")
print(account1.withdraw(286))
print(account2.withdraw(670))
print()

try:
    #transfer
    print("--- TRANSFER ---")
    print(account1.transfer(amount=520, other_account=account2))
    print(account1.transfer(amount=170, other_account=account1))
except Exception as error:
    print(error)

# View transaction history
print(f"{account1.account_number}: {account1.transaction_history}")
print()
print(f"{account2.account_number}: {account2.transaction_history}")