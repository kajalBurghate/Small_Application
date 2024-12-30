# Bank Management System using tkinter
#--------------------------------------------------------------------
#import packages

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
#-----------------------------------------------------------------------
#init method

class BankSystem :
    def __init__(self, master) :
        self.users = {}
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry('400x300')
#-----------------------------------------------------------------------
#Create Account Frame and its Widgets

        self.users = {}
#Create AccountFrame
        self.create_account_frame = Frame(self.master)
        self.create_account_frame.pack()
        self.name_label = Label(self.create_account_frame, text = "Name :")
        self.name_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.name_entry = Entry(self.create_account_frame)
        self.name_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.age_label = Label(self.create_account_frame, text = "Age :")
        self.age_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.age_entry = Entry(self.create_account_frame)
        self.age_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.salary_label = Label(self.create_account_frame, text = "Salary :")
        self.salary_label.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.salary_entry = Entry(self.create_account_frame)
        self.salary_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

        self.pin_label = Label(self.create_account_frame, text = "PIN :")
        self.pin_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.pin_entry = Entry(self.create_account_frame, show= "*")
        self.pin_entry.grid(row = 3, column = 1, padx = 10, pady = 10)

        self.create_account_button = Button(self.create_account_frame, text = "Create Account", command = self.create_account_frame)
        self.create_account_button.grid(row = 4, column = 1, padx = 10, pady = 10)
#---------------------------------------------------------------------
#Login frame and its widgets

        self.login_frame = Frame(self.master, bg = "#FFFFFF")
        self.login_frame.pack(pady = 20)
        self.login_name_label = Label(self.login_frame, text = "Name:", font = ("Arial, 14"), bg = "#FFFFFF")
        self.login_name_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.login_name_entry = Entry(self.login_frame, width = 30, font = ("Arial, 14"))
        self.login_name_entry.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.login_pin_label = Label(self.login_frame, text = "PIN:", font = ("Arial, 14"), bg = "#FFFFFF")
        self.login_pin_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.login_pin_entry = Entry(self.login_frame, show = "*" ,width = 30, font = ("Arial, 14"))
        self.login_pin_entry.grid(row = 1, column = 0, padx = 10, pady = 10)

        #self.login_button = Button(self.login_frame, text = "Login", command = self.login, font = ("Arial", 12), bg = '#4CAF50', fg = '#FFFFFF', activebackground = '#2E8B57', activeforeground = '#FFFFFF', relief = 'raised', borderwidth = 0)
        #self.login_button.grid(row = 2, column = 1, padx = 10, pady = 10)
        #self.master.bind('<Return>', self.login)
#------------------------------------------------------------------------
#User Details Frame

        self.user_details_frame = Frame(self.master)

        #Labels
        label_style = {"fg": "green", "Font": ("Times New Roman", 14)}

        self.name_label2 = Label(self.user_details_frame, text = 'Name:', **label_style)
        self.name_label2.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.age_label2 = Label(self.user_details_frame, text = 'Age:', **label_style)
        self.age_label2.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.salary_label2 = Label(self.user_details_frame, text = 'Salary:', **label_style)
        self.salary_label2.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.current_balance_label2 = Label(self.user_details_frame, text = 'Current Balance:', **label_style)
        self.current_balance_label2.grid(row = 0, column = 1, padx = 10, pady = 10)

        #Buttons

        self.view_tranction_button = Button(self.user_details_frame, text="View Transaction Log", command = self.view_transaction_log, bg="green", fg = "white")
        self.view_transaction_button.grid(row = 4, column = 0, padx = 10, pady = 10)

        self.deposit_button = Button(self.user_details_frame, text="Deposit", command = self.deposit, bg = 'Yellow', fg = "balck")
        self.deposit_button.grid(row = 4, column = 1, padx = 10, pady = 10)

        self.withdraw_button = Button(self.user_betails_frame, text = "Withdraw", command = self.withdraw, bg = "orange", fg = "white")
        self.withdraw_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        self.logout_button = Button(self.user_betails_frame, text = "Logout", command = self.logout, bg = "red", fg = "white")
        self.logout_button.grid(row = 4, column = 3, padx = 10, pady = 10)
#------------------------------------------------------------------------------------------
# User Data Initialization

# Initialize the user data

        self.name = " "
        self.age = " "
        self.salary = " "
        self.pin = " "
        self.current_balance = ""
        self.transaction_log = []
#-------------------------------------------------------------------------------------------------
# Account Creation
        def create_account(self):
            #Get user input
            name = self.name_entry.get()
            age = self.age_entry.get()
            salary = self.salary_entry.get()
            pin = self.pin_entry.get()

            #create a dictory to store user's data
            user_data = {'name': name, 'age': age,'salary': salary, 'pin': pin, 'balance': 0}

            # Add the user's data to the users dictory
            self.users[pin] = user_data

            #Validate input
            if not name or not age or not salary or not pin :
                messagebox.showerror("Error", "All fields are required!!!")
                return

            if not age.isdigit():
                messagebox.showerror("Error", "Age must be a number!!!")
                return

            if not salary.isdigit():
                messagebox.showerror("Error", "Salary must be a number!!!")
                return

            if not pin.isdigit or len(pin) != 4:
                messagebox.showerror("Error", "PIN must be a 4-digit number!!!")
                return

            #save user data

            self.name = name
            self.age = age
            self.salary = salary
            self.pin = pin
            self.current_balance = 0
            self.transaction_log = []

            #Clear input fields
            
            self.name_entry.delete(0, END)
            self.age_entry.delete(0, END)
            self.salary_entry.delete(0, END)
            self.pin_entry.delete(0, END)

            # Show user details

            self.name_label2.config(text = "Name :" +self.name)
            self.age_label2.config(text = "Age :" +self.age)
            self.salary_label2.config(text = "Salary :" +self.salary)
            self.current_balance_label.config(text = "Current Balance :" +str(self.current_balance))

            # Show user details frame

            self.create_account_frame.pack_forget()
            self.login_frame.pack_forget()
            self.user_details_frame.pack()
#-------------------------------------------------------------------------------------

# Login Function

        def login(self, event = None) :
            #Get the user's PIN from the login entry widget
            pin = self.login_pin_entry.get()

            #Check if the user exists in the users dictonary

            if pin in self.users :
                #Set the current user data to the user's dictonary
                self.current_user_data = self.users[pin]

                # Show the suer details frame and update the labels
                self.user_details_frame.pack(pady = 20)
                self.name_label2["text"] = f"Name : {self.current_user_data['name']}"
                self.age_label2["text"] = f"Age : {self.current_user_data['age']}"
                self.salary_label2["text"] = f"Salary : {self.current_user_data['salary']}"
                self.current_balane_label["text"] = f"Name : {self.current_user_data['balance']}"

                # pack forget login frame
                self.login_frame.pack_forget()
            else :
                #Show an error message box if the user does not exist
                messagebox.showerror("Error", "Invalid PIN or UserName")
#--------------------------------------------------------------------------------------------

# Deposit Function

        def deposit(self) :
            # Get user input
            pin = simpledialog.askstring("Deposit", "Enter PIN :")
            amount = simpledialog.askstring("Deposit", "Enter Amount :")

            # Validate input
            if not pin :
                Return

            if not amount or not amount.isdigit() or int(amount) <= 0 :
                messagebos.showerror("Error", "Invalid Input...!!!")
                return

            if pin not in self.users :
                messagebox.showerror("Error", "Invalid PIN...!!!")
                return

            # Add amount to current balance
            self.users[pin]['balance'] += int(amount)

            # Update current balance label
            self.current_balance_label.config(text = "Current Balance :" +str(self.users[pin]['balance']))

            # Add transaction to transaction log
            transaction = "Deposit : +" +amount + " ,New Balance :" +str(self.users[pin]['balance'])
            self.transaction_log.append(transaction)
            self.users[pin]['transactions'] = self.transaction_log
#-------------------------------------------------------------------------------------------------------------------

# Withdrawl Function
        def withdraw(self) :
            # Get user Input
            pin = simpledialog.askstring("Withdraw", "Enter Your PIN :")
            amount = simpledialog.askstring("Withdraw", " Enter Amount :")

            # Validate Input
            if not (pin and amount) :
                return

            if not amount.isdigit() or int(amount) <= 0 :
                messagebox.showerror("Enter", "Invalid Amount...!!!")
                return

            # Check if PIN is valid
            if pin not in self.users :
                messagebox.showerror("Error", "Invalid PIN...!!!")
                return

            # Check if there is enough balance
            current_balance = self.users[pin]['balance']
            if int(amount) > current_balance :
                messagebox.showerror("Error", "Insufficient balance...!!!")
                return

            # Substract amount from current balance
            current_balance -= int(amount)
            self.users[pin]['balance'] = current_balance

            # Update current balance label
            self.current_balance_label.config(text = "Current Balance :" +str(current_balance))

            # Add transaction to transaction log
            transaction = "Withdraw :- " +amount+ " ,New balance :" +str(current_balance)
            self.transaction_log.append(transaction)
            self.users[pin]['transaction'] = self.transaction_log
#-----------------------------------------------------------------------------------
# View Transaction Log method

        def view_transaction_log(self) :
            #create transaction log window
            transaction_log_window = Toplevel(self.master)
            transaction_log_window.title("Transaction Log")

            # Get current user's PIN
            pin = self.login_pin_entry.get()

            # Append transaction to user's transaction log
            if pin in self.users :
                self.users[pin]['transaction'].extend(self.transaction_log)

            # Create transaction log frame
            transaction_log_frame = Frame(transaction_log_window)
            transaction_log_frame.pack(padx = 10, pady = 10)

            # Create transaction log label
            transaction_log_label = Label(transaction_log_frame, text = "Transation Log :")
            transaction_log_label.grid(row = 0, column = 0, padx = 10, pady = 10)

            # Create transaction log listbox
            transaction_log_listbox = Label(transaction_log_frame, text = "Transation Log :")
            transaction_log_listbox.grid(row = 1, column = 0, padx = 10, pady = 10)

            # Fetch and insert all transaction into listbox

            if pin in self.users :
                # Insert transaction into listbox
                for transaction in self.transaction_log :
                    transaction_log_listbox.insert(END, transaction)
# ----------------------------------------------------------------------------------------------
# Logout method

        def logout(self) :
            # Clear user data
            self.name = ""
            self.age = ""
            self.salary = ""
            self.pin = ""
            self.current_balance = 0
            self.transaction_log = []

            #Claer input fields
            self.login_pin_entry.delete(0, END)

            # Show login frame
            self.user_details_frame.pack_forget()
            self.create_account_frame.pack(pady = 20)
            self.login_frame.pack()
#---------------------------------------------------------------------------------------------------
# Starting the Program

def main():
    #create a Tk object
    root = Tk()

    #Create an instance of the BankSystem class
    bank_system = BankSystem(root)

    #starting the mainloop
    root.mainloop()

if __name__ == '__main__':
    main()













