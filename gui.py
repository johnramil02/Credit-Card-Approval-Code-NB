import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ElectiveBayesian import *

test = [10,0,1,1,2,35]


        

# root window
root = tk.Tk()
root.geometry('500x450')
root.resizable(False, False)
root.title('Credit Card Approval')

# Label and form input
label_debt = Label(root ,text = "Debt").place(x = 40,y = 100) #(row = 0,column = 0)
label_bank = Label(root ,text = "Bank Customer").place(x = 40,y = 130)
label_employed = Label(root ,text = "Employed").place(x = 40,y = 160)
label_credit_score = Label(root ,text = "Credit Score").place(x = 40,y = 200)
label_income = Label(root ,text = "Income").place(x = 40,y = 230)
label_result = Label(root ,text = "Result").place(x = 180,y = 320)

# Text Variable for Entry Field
debt_var = tk.StringVar()
bank_var = tk.StringVar()
employed_var = tk.StringVar()
credit_score_var = tk.StringVar()
income_var = tk.StringVar()


# Entry Field
input_debt = Entry(root, textvariable = debt_var).place(x = 140,y = 100)
input_bank = Entry(root, textvariable = bank_var).place(x = 140,y = 130)
input_employed = Entry(root, textvariable = employed_var).place(x = 140,y = 160)
input_credit_score = Entry(root, textvariable = credit_score_var).place(x = 140,y = 200)
input_income = Entry(root, textvariable = income_var).place(x = 140,y = 230)
input_result = Entry(root).place(x = 220,y = 320)




def prediction():
    
    debt = debt_var.get()
    bank = bank_var.get()
    employed = employed_var.get()
    credit_score = credit_score_var.get()
    income = income_var.get()
  
    input = [[debt,bank,employed,credit_score,income]]
    
    if(bayesianPrediction([test])):
        print("PASOK")
    else:
        print("HINDI PASOK")


# button for prediction
ttk.Button(root,text = "Predict", command = prediction).place(x = 250,y = 270)

root.mainloop()

#okay okay 