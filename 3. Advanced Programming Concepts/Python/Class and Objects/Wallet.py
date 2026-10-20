class Wallet:
    def __init__(self, balance=0):
        self.balance = 0

    def add_money(self,amount):
        if amount > 0:
            self.balance += amount
            print("Money is credited")
        else:
            print("Money cannot be credited")

    def spend_money(self, amount):
        if amount > self.balance:
            print("Money cannot be debited")
        else:
            self.balance -= amount
            print("Money is debited")

my_wallet = Wallet()
my_wallet.add_money(50)
my_wallet.spend_money(20)
print("Total Balance - ",my_wallet.balance)
