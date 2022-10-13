class Account:

    def __init__(self):
        self._transactions = [] # the "_" prefix means treat this as private
        
    def deposit(self, amount):
        self._transactions.append(amount)