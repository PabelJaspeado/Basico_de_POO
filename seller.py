from account import Account

class Seller(Account):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
