class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute

    # Public method to get the balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

# Creating an instance of BankAccount
account = BankAccount("1234567890", 1000)

# Accessing public attributes
print(f"Account Number: {account.account_number}")

# Accessing private attribute directly will raise an AttributeError
try:
    print(account.__balance)
except AttributeError as e:
    print(e)

# Accessing private attribute using a public method
print(f"Initial Balance: {account.get_balance()}")

# Depositing money
account.deposit(500)
print(f"Balance after deposit: {account.get_balance()}")

# Withdrawing money
account.withdraw(300)
print(f"Balance after withdrawal: {account.get_balance()}")

# Attempting to withdraw more than the balance
account.withdraw(1500)

# Attempting to deposit a negative amount
account.deposit(-200)
