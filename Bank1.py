# Simple Bank Management System Code

class Bank :
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance):
        if account_number in self.accounts:
            return "Account alreday exists...."

        if initial_balance < 0 :
            return "Initial balance must be non negative..."

        self.accounts[account_number] = {

            'account_holder' : account_holder,
            'balance' : initial_balance
        }

        return "Account created successfully..."

    def deposit(self, account_number, amount):
        if account_number not in self.accounts :
            return "Account does not exists..."

        if amount <= 0 :
            return "Amount to deposit must be positive..."

        self.accounts[account_number]['balance'] += amount
        return "Deposited" +str(amount) + "successfully. New balance : " + str(self.accounts[account_number]['balance'])

    def withdraw(self, account_number, amount) :
        if account_number not in self.accounts :
            return "Account does not exists..."
        
        if amount <= 0 :
            return "Amount to withdraw must be positive..."

        if self.accounts[account_number]['balance'] < amount :
            return "Insufficient Balance..."

        self.accounts[account_number]['balance'] -= amount
        return "Withdraw" +str(amount) + "successfully. New balance : " + str(self.accounts[account_number]['balance'])

    def check_balance(self, account_number) :
        if account_number not in self.accounts :
            return "Account does not exists..."

            return "Account Holder : " +self.accounts[account_number]['account_holder'] + "\nBalance : "+ str(self.accounts[account_number]['balance'])


    
bank = Bank()          #Create a bank object

print("\n*************************Bank Management System*************************")
print("\n 1. Create Account")
print("\n 2. Deposit")
print("\n 3. Withdraw")
print("\n 4. Check Balance")
print("\n 5. Exit")

while True :

    choice = input("\n Enter your choice (1 TO 5) :")

    if choice == '1' :
        account_number = input("Enter Account Number :")
        account_holder = input("Enter Account's Holder Name :")
        initial_balance = float(input("Enter Initial Balance :"))
        
        result = bank.create_account(account_number, account_holder, initial_balance)
        print(result)

    elif choice == '2' :
        account_number = input("Enter Account Number :")
        amount = float(input("Enter Amount to be deposited :"))
        
        result = bank.deposit(account_number, amount)
        print(result)

    elif choice == '3' :
        account_number = input("Enter Account Number :")
        amount = float(input("Enter Amount to be withdrawl :"))
        
        result = bank.withdraw(account_number, amount)
        print(result)

    elif choice == '4' :
        account_number = input("Enter Account Number :")
        result = bank.check_balance(account_number)
        print(result)
    
    elif choice == '5' :
        print("Exiting the program.")
        break

    else :
        print("Invalid Choice. please Try Again !!!")


       











    

