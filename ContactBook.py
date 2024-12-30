# Python Contact Book - Address Book Program

#*************** Importing Module********************
from tkinter import *
from tkinter import messagebox

#***************Initialize Window*********************
root = Tk()
root.geometry('700x700')
root.config(bg = '#d3f3f5')
root.title('Contact Book')
root.resizable(0, 0)
contactlist = [
    ['Kajal', '8080750242'],
    ['Batieee', '9561297743'],
    ['Pops', '9922882203'],
    ['Mamma', '9604613005'],
    ['Roha', '9284088959']
]

Name = StringVar()
Number = StringVar()

#******************Create Frame******************************
frame = Frame(root)
frame.pack(side = RIGHT)
scroll = Scrollbar(frame, orient = VERTICAL)
select = Listbox(frame, yscrollcommand = scroll.set, font = ('Times new roman', 16),
bg = '#f0fffc', width = 20, height = 20, borderwidth = 3, relief = 'groove')

#****************Function to get select value***************
def Selected() :
    print("Hello", len(select.curselection()))
    if len(select.curselection()) == 0 :
        messagebox.showerror("Error", "Please select the Name.")
    else :
        return int(select.curselection()[0])

#****************Function to add new contact and edit existing conatct***************
def AddContact() :
    if Name.get() != "" and Number.get() != "" :
        contactlist.append([Name.get(), Number.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully add new contact.")
    else :
        messagebox.showerror("Error", "Please fill the information.")

def UpdateDetails() :
    if Name.get() and Number.get() :
        contactlist[Selected()] = [Name.get(), Number.get()]
        print(contactlist)
        EntryReset()
        Select_set()
    elif not(name.get() and Number.get() and not(len(select.curselection()))== 0) :
        messagebox.showerror("Error", "Please fill information.")

    else :
        if len(select.curselection()) == 0 :
            messagebox.showerror("Error", "Please select the name and \n press Load button.")

        else :
            message1 = """ To Load the all information of \n
                           selected row press Load button\n.
                       """
            messagebox.showerror("Error", message1)

#*****************Function to delete and view contact**********************
def Delete_Entry() :
    if len(select.curselection()) != 0 :
        result = messagebox.askyesno('Confirmation', 'You want to Delect contact\n Which you selected')
        if result == True :
            del contactlist[Selected()]
            Select_set()
        else :
            messagebox.showerror("Error", "Please select the contact.")

def VIEW() :
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

#********************Exit the window***************************
def EXIT() :
    root.destroy()

def Select_set() :
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist :
        select.insert(END, name)

Select_set()

#*******************Define buttons, labels and entry widget********************
Label(root, text = 'Name', font=("Times new roman",22,"bold"), bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name, width=30).place(x= 200, y=30)
Label(root, text = 'Contact No.', font=("Times new roman",20,"bold"),bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Number, width=30).place(x= 200, y=80)

Button(root,text=" ADD", font='Helvetica 18 bold',bg='#e8c1c7', command = AddContact, padx=20). place(x= 50, y=140)
Button(root,text="EDIT", font='Helvetica 18 bold',bg='#e8c1c7',command = UpdateDetails, padx=20).place(x= 50, y=200)
Button(root,text="DELETE", font='Helvetica 18 bold',bg='#e8c1c7',command = Delete_Entry, padx=20).place(x= 50, y=260)
Button(root,text="VIEW", font='Helvetica 18 bold',bg='#e8c1c7', command = VIEW).place(x= 50, y=325)
#Button(root,text="RESET", font='Helvetica 18 bold',bg='#e8c1c7', command = EntryReset).place(x= 50, y=390)
Button(root,text="EXIT", font='Helvetica 24 bold',bg='tomato', command = EXIT).place(x= 250, y=470)

root.mainloop()
