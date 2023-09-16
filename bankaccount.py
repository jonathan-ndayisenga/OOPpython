from atm import ATM  # Import the ATM class if it's in a different module

class BankAccount:
    def __init__(self, account_number, atm):
        self.account_number = account_number
        self.atm = atm

    def get_balance(self):
        return self.atm.check_balance()

    def make_deposit(self, amount):
        # Pass the 'amount' argument to the ATM's 'deposit' method
        self.atm.deposit(amount)

    def make_withdrawal(self, amount):
        self.atm.withdraw(amount)

# Usage example outside the class
if __name__ == "__main__":
    # Create an instance of ATM with pin 1234 and card_number 1111222233334444
    atm = ATM(1234, 1111222233334444)

    # Create an instance of BankAccount and associate it with the ATM
    bank_account = BankAccount(12345, atm)

    # Deposit money into the bank account using the ATM
    bank_account.make_deposit(500)

    # Print the updated balance of the bank account
    print(f"Updated Balance: {bank_account.get_balance()}")
