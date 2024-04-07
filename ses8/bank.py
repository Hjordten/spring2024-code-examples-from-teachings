"""

Create a Bank, an Account, and a Customer class.

All classes should be in a single file.

The bank class should be able to hold many accounts.

You should be able to add new accounts.

The Account class should have relevant details.

The Customer class Should also have relevant details.


"""

class Bank:
    
    def __init__(self):
        self.accounts = []

    def __str__(self):
        return f'{self.accounts}'

    def __repr__(self):
        return f'{self.__dict__}'

class Account:
    
    def __init__(self, no, bal, cust):
        self.no = no
        self.bal = bal
        self.cust = cust

    def __str__(self):
        return 'Hello'
        
    def __repr__(self):
        return f'{self.__dict__}'

class Customer:

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f'{self.name}'
nordea = Bank()

print(nordea)












