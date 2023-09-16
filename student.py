from bankaccount import BankAccount
from atm import ATM
class Student: 
    def __init__(self, name, age): 
    
        self.name = name 
        self.age = age 
        self.grades = [] 
        self.bank_account = None 
        

    def add_grade(self, grade): 
        self.grades.append(grade) 

    def average_grade(self): 
        if len(self.grades) == 0: 
            return None 
        return sum(self.grades) / len(self.grades) 
    
     
    def create_bank_account(self, account_number, atm):
        # Create a BankAccount instance and associate it with the student
        self.bank_account = BankAccount(account_number, atm)
    


# Create an instance of Student with name "Alice" and age 18 
student = Student("Alice", 18) 

# Print the name, age, and grades of the student 
print(student.name)  # Alice 
print(student.age)  # 18 
print(student.grades)  # [] 

# Add some grades to the student 
student.add_grade(90) 
student.add_grade(85) 
student.add_grade(95) 

# Print the updated grades and the average grade of the student 
print(student.grades)  # [90, 85, 95] 
print(student.average_grade())  


# # Create a BankAccount instance for the student, passing the ATM instance
student.create_bank_account(12345, ATM)  # Pass the ATM instance, not an integer

# Deposit money into the bank account using the ATM
student.bank_account.make_deposit(1000)

# Print the balance of the bank account
print(f"Balance: {student.bank_account.get_balance()}")

# Withdraw money from the bank account using the ATM
student.bank_account.make_withdrawal(500)

# Print the updated balance of the bank account
print(f"Updated Balance: {student.bank_account.get_balance()}")

# Print the average grade of the student
print(f"Average Grade: {student.average_grade()}")

# Verify PIN using the ATM (from the Student's bank account)
entered_pin = 1234  # Replace with the actual PIN
if student.bank_account.atm.verify_pin(entered_pin):
    print("PIN verified.")
else:
    print("PIN verification failed.")







