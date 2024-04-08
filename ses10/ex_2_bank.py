class Bank:
    def __init__(self):
        self._accounts = []
        self._customer_accounts = {}  # Initialize dictionary to track customer accounts

    @property
    def accounts(self):
        return self._accounts
     
    def add_account(self, account):
        self._accounts.append(account)
        self._customer_accounts[account.cust] = account  # Update customer accounts dictionary

    def add_accounts(self, accounts):
        self._accounts.extend(accounts)
        for account in accounts:
            self._customer_accounts[account.cust] = account  # Update customer accounts dictionary

    def create_account(self, customer):
        if customer in self._customer_accounts:
            print("Customer already has an account.")
        else:
            account = Account(customer.name + "_account", customer)
            self.add_account(account)
            print("Account created successfully.")
            return account
  

class Account:
    def __init__(self, no, cust):
        self._no = no
        self._cust = cust

    @property
    def no(self):
        return self._no
     
    @property
    def cust(self):
        return self._cust
         

class Customer:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def is_over_18(self):
        return self.age >= 18


"""
# test results

# Define the classes (Bank, Account, and Customer) here

# Create a Bank instance
bank = Bank()

# Create Customer instances
customer1 = Customer("John", 25)
customer2 = Customer("Alice", 17)

# Create accounts for customers
account1 = bank.create_account(customer1)
account2 = bank.create_account(customer2)  # This will not create an account because Alice is under 18

# Display information about accounts
print("Accounts in the bank:")
for account in bank.accounts:
    print(f"Account Number: {account.no}, Customer Name: {account.cust.name}")

# Attempt to create another account for the same customer (John)
account3 = bank.create_account(customer1)  # This will not create another account because John already has one

# Check if the customers are over 18
print(f"{customer1.name} is over 18 years old: {customer1.is_over_18()}")
print(f"{customer2.name} is over 18 years old: {customer2.is_over_18()}")
"""