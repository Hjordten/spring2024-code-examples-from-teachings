class Bank:

    def __init__(self):
        self.accounts = []

    def __repr__(self):
        return f'{self.accounts}'


class Account:

    def __init__(self, no, balance,  cust):
        self.no = no
        self.balance = balance
        self.cust = cust

    def __repr__(self):
        return f'{self.no} {self.balance} {self.cust}'    
    

class Customer:
      
      def __init__(self, name):
        self.name = name

      def __repr__(self):
        return f'{self.name}'        


nordea = Bank()
nordea.accounts.append("nemkonto")