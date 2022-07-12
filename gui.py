import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from PIL import ImageTk, Image
from ElectiveBayesian import *

# root window
root = tk.Tk()
root.geometry('500x400')
root.resizable(False, False)
root.title('Credit Card Approval')

photo = PhotoImage(file = "sub-icon.png")
root.iconphoto(False, photo)

# Label and form input
label_title         = Label(root ,text = "Credit Card Approval", font=("Courier", 20), fg="#0000FF").place(x = 90,y = 25) #(row = 0,column = 0)
label_debt          = Label(root ,text = "Debt", font=('Helvetica', 9, 'bold')).place(x = 40,y = 100) 
label_bank          = Label(root ,text = "Already a Bank Customer?", font=('Helvetica', 9, 'bold')).place(x = 40,y = 130)
label_employed      = Label(root ,text = "Employed?", font=('Helvetica', 9, 'bold')).place(x = 40,y = 160)
label_credit_score  = Label(root ,text = "Credit Score", font=('Helvetica', 9, 'bold')).place(x = 40,y = 200)
label_income        = Label(root ,text = "Monthly Income", font=('Helvetica', 9, 'bold')).place(x = 40,y = 230)
label_years         = Label(root ,text = "Years of Employment :", font=('Helvetica', 9, 'bold')).place(x = 40,y = 260)
#label_result        = Label(root ,text = "Result").place(x = 150,y = 350)


# Text Variable for Entry Field

debt_var            = tk.StringVar()
bank_var            = tk.StringVar()
employed_var        = tk.StringVar()
credit_score_var    = tk.StringVar()
income_var          = tk.StringVar()
years_employed_var  = tk.StringVar()


# Entry Field
input_debt          = Entry(root, textvariable = debt_var).place(x = 200,y = 100)
input_credit_score  = Entry(root, textvariable = credit_score_var).place(x = 200,y = 200)
input_income        = Entry(root, textvariable = income_var).place(x = 200,y = 230)
input_income        = Entry(root, textvariable = years_employed_var).place(x = 200,y = 260)

# Radio Button for Employed
employed_radio = StringVar()
employed_radio.set(' ')

employed_radio_1 = Radiobutton(root, text = "Yes", variable = employed_radio,value = 1)
employed_radio_1.place(x = 200,y = 160)

employed_radio_2 = Radiobutton(root, text = "No", variable = employed_radio,value = 0)
employed_radio_2.place(x = 250,y = 160)


# Radio Button for Bank Customer
bank_radio = StringVar()
bank_radio.set(' ')

bank_radio_1 = Radiobutton(root, text = "Yes", variable = bank_radio,value = 1)
bank_radio_1.place(x = 200,y = 130)

bank_radio_2 = Radiobutton(root, text = "No", variable = bank_radio,value = 0)
bank_radio_2.place(x = 250,y = 130)

# check if the string is float or not
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Check if the applicant details is approved or not
def is_approve():
    #Get input values from entry field
    debt            = debt_var.get()
    bank            = bank_radio.get()
    employed        = employed_radio.get()
    credit_score    = credit_score_var.get()
    income          = income_var.get()
    years_employed  = years_employed_var.get()
    
    print(str(debt) + " " + str(bank) + " " + str(employed) + " " + str(years_employed) + " " + str(credit_score) + " " + str(income))
    
    
    # Check if the input is valid
    is_all_numeric = (debt.isnumeric() or isfloat(debt)) and (credit_score.isnumeric() or isfloat(credit_score)) and (income.isnumeric() or isfloat(income)) and (years_employed.isnumeric() or isfloat(years_employed))
    is_empty = debt == "" or bank == ' ' or employed == ' ' or credit_score == "" or income == "" or years_employed == ""
    
    if(is_empty):
        messagebox.showwarning("Error", "Empty field must be filled out")
    else:
        if(is_all_numeric):
            # Save get values into input variable
            input = [[float(debt),float(bank),float(years_employed),float(employed),float(credit_score),float(income)]]
            
            # predict using naive bayes 
            if(bayesianPrediction(input)):  
                print("Credit Card Approved")
                messagebox.showinfo("Approval", "Credit Card Approved")
            else:
                print("Credit Card Not Approved")
                messagebox.showinfo("Approval", "Credit Card Not Approved")
        else:
            messagebox.showwarning("Invalid Input", "Input must be numerical")
        
# style of button
s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 12))

ttk.Button(root,text = "Predict", command = is_approve, style='my.TButton').place(x = 230,y = 300)

root.mainloop()