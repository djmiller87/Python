class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"User: {self.name}, Balance: {self.account_balance}")
        print(f"User: {other_user.name}, Balance: {other_user.account_balance}")
        return


jake = User("Jake", "jakemiller.bc@gmail.com")
mike = User("Mike", "mike@email.com")
abby = User("Abby", "abby@email.com")

jake.make_deposit(50)
jake.make_deposit(65)
jake.make_deposit(225)
jake.make_withdrawal(135)
jake.display_user_balance()

mike.make_deposit(345)
mike.make_deposit(45)
mike.make_withdrawal(32)
mike.make_withdrawal(6)
mike.display_user_balance()

abby.make_deposit(320)
abby.make_withdrawal(95)
abby.make_withdrawal(24)
abby.make_withdrawal(80)
abby.display_user_balance()

jake.transfer_money(abby, 45)


