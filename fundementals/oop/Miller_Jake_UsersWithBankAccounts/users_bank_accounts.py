class BankAccount:
    bank_name = "Bank of Dojo"
    all_accounts = []
    balance = 0
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.01, 0)
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self

    def transfer_money(self, other_user,amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        print(f"User: {self.name}, Balance: {self.account.balance}")
        print(f"User: {other_user.name}, Balance: {other_user.account.balance}")
        return self

jake = User("Jake", "jakemiller.bc@gmail.com")
mike = User("Mike", "mike@email.com")
abby = User("Abby", "abby@email.com")

jake.account.deposit(50).deposit(65).deposit(225).withdraw(135)
jake.transfer_money(abby, 45).display_user_balance()

mike.account.deposit(345).deposit(45).withdraw(32).withdraw(6)
mike.display_user_balance()

abby.account.deposit(320).withdraw(95).withdraw(24).withdraw(80)
abby.display_user_balance()