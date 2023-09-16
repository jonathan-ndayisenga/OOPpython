from student import Student
from atm import ATM
from bankaccount import BankAccount


if __name__ == "__main__":
    # Create an instance of ATM with pin 1234 and card_number 1111222233334444
    atm = ATM(1234, 1111222233334444)

    # Create an instance of BankAccount and associate it with the ATM
    bank_account = BankAccount(12345, atm)

    # Create an instance of Student
    student = Student("Alice", 18)

    # Create a bank account for the student and associate it with the ATM
    student.create_bank_account(12345, atm)

    # Deposit money into the student's bank account
    student.deposit_to_account(500)

    # Check the balance of the student's bank account
    balance = student.check_account_balance()
    print(f"Account Balance: {balance}")

    # Change the PIN for the student's bank account
    student.change_pin(4321)
