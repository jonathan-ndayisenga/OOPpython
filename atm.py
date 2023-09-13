import datetime
class ATM:
    def __init__(self, pin, card_number):
        self.balance = 0
        self.pin = pin
        self.card_number = card_number
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        transaction = f"Deposit on {datetime.datetime.now()}: {amount}"
        self.transactions.append(transaction)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            transaction = f"Withdrawal on {datetime.datetime.now()}: {amount}"
            self.transactions.append(transaction)
        else:
            print("Insufficient funds.")

    def change_pin(self, new_pin):
        self.pin = new_pin

    def print_transactions(self):
        if len(self.transactions) == 0:
            print("No transactions.")
        else:
            for transaction in self.transactions:
                print(transaction) 

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

# Create an instance of ATM with pin 1234 and card_number 1111222233334444
atm = ATM(1234, 1111222233334444) 

atm.deposit(1000) 

print(atm.check_balance()) 

atm.withdraw(200) 

print(atm.check_balance()) 

print(atm.print_transactions()) 

atm.deposit(100000000)

print(atm.check_balance()) 

print(atm.print_transactions()) 
