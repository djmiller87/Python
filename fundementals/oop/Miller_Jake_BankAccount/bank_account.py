class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "Bank of Dojo"
    all_accounts = []
    balance = 0
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= self.balance - amount:
            self.balance -= amount
        else:
            print("Insufficent funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate 
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            print("Balance: $" + str(account.balance))
        return 

account_1 = BankAccount(1.01, 0)

account_2 = BankAccount(1.01, 1324)

account_1.deposit(432).deposit(451).deposit(426).withdraw(692).yield_interest().display_account_info()

account_2.deposit(84).deposit(873).withdraw(275).withdraw(21).withdraw(233).withdraw(42).yield_interest().display_account_info()

BankAccount.all_balances()


