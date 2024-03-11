class Bank:

    def __init__(self, accounts):
        self.accounts = [accounts]

    def add_account(self, account):
        self.accounts.append(account)


arbejdernes_landsbank = Bank()

arbejdernes_landsbank.add_account("test1")
arbejdernes_landsbank.add_account("test2")
arbejdernes_landsbank.add_account("test3")
           