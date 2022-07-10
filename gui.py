import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ElectiveBayesian import *

# root window
root = tk.Tk()
root.geometry('500x450')
root.resizable(False, False)
root.title('Credit Card Approval')

# Label and form input
label_debt          = Label(root ,text = "Debt").place(x = 40,y = 100) #(row = 0,column = 0)
label_bank          = Label(root ,text = "Bank Customer").place(x = 40,y = 130)
label_employed      = Label(root ,text = "Employed").place(x = 40,y = 160)
label_credit_score  = Label(root ,text = "Credit Score").place(x = 40,y = 200)
label_income        = Label(root ,text = "Income").place(x = 40,y = 230)
label_years         = Label(root ,text = "Years").place(x = 40,y = 260)
label_result        = Label(root ,text = "Result").place(x = 180,y = 320)

# Text Variable for Entry Field
debt_var            = tk.StringVar()
bank_var            = tk.StringVar()
employed_var        = tk.StringVar()
credit_score_var    = tk.StringVar()
income_var          = tk.StringVar()
years_employed_var  = tk.StringVar()


# Entry Field
input_debt          = Entry(root, textvariable = debt_var).place(x = 140,y = 100)
input_bank          = Entry(root, textvariable = bank_var).place(x = 140,y = 130)
input_employed      = Entry(root, textvariable = employed_var).place(x = 140,y = 160)
input_credit_score  = Entry(root, textvariable = credit_score_var).place(x = 140,y = 200)
input_income        = Entry(root, textvariable = income_var).place(x = 140,y = 230)
input_income        = Entry(root, textvariable = years_employed_var).place(x = 140,y = 260)
input_result        = Entry(root).place(x = 220,y = 320)


def isApprove():
    
    #Get input values from entry field
    debt            = int(debt_var.get())
    bank            = int(bank_var.get())
    employed        = int(employed_var.get())
    credit_score    = int(credit_score_var.get())
    income          = int(income_var.get())
    years_employed  = int(years_employed_var.get())
    
    print(str(debt) + " " + str(bank) + " " + str(years_employed) + " " + str(employed) + " " + str(credit_score) + " " + str(income))
    
    # Save get values into input variable
    input = [[debt,bank,years_employed,employed,credit_score,income]]
    
    # predict using naive bayes 
    if(bayesianPrediction(input)):   #bayesianPrediction([test])
        print("Credit Card Approved")
    else:
        print("Credit Card Not Approved")


# button for prediction
ttk.Button(root,text = "Predict", command = isApprove).place(x = 250,y = 290)

root.mainloop()

#okay okay 