class BankAccount:

    def __init__(self, name, number, balance, currency):

        self.name = name
        self.number = number
        self.balance = balance
        self.currency = currency

account1 = BankAccount("Fredrik Stoltenberg", 89003, 25000, "NOKR")


print(account1.name)
print(account1.balance)