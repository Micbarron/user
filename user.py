class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount\
    

    def display_user_balance(self):
        print(self.account_balance)



Michael = User("Mike Barron", "mike@dojo.com")
Caroline = User("Caroline Barron", "Cbarron47@askjeeves.com")
Sven = User("Sven Johnson", "broOfgus@youtube.com")


Michael.make_deposit(600)
Michael.make_deposit(50)
Michael.make_deposit(350)
Michael.make_withdrawal(500)
Michael.display_user_balance()

Caroline.make_deposit(400)
Caroline.make_deposit(300000000000)
# wife wanted to beat Jeff Bezos
Caroline.make_withdrawal(2)
Caroline.make_withdrawal(40)
Caroline.display_user_balance()

Sven.make_deposit(1000)
Sven.make_withdrawal(100)
Sven.make_withdrawal(60)
Sven.make_withdrawal(240)
Sven.display_user_balance()