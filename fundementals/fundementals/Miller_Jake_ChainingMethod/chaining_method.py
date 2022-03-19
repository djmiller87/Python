class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"User: {self.name}, Balance: {self.account_balance}")
        print(f"User: {other_user.name}, Balance: {other_user.account_balance}")
        return self


jake = User("Jake", "jakemiller.bc@gmail.com")
mike = User("Mike", "mike@email.com")
abby = User("Abby", "abby@email.com")

jake.make_deposit(50).make_deposit(65).make_deposit(225).make_withdrawal(135).display_user_balance().transfer_money(abby, 45)

mike.make_deposit(345).make_deposit(45).make_withdrawal(32).make_withdrawal(6).display_user_balance()

abby.make_deposit(320).make_withdrawal(95).make_withdrawal(24).make_withdrawal(80).display_user_balance()


