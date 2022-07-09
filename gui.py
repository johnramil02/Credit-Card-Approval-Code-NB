import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ElectiveBayesian import *

test = [10,0,1,1,2,35]

def prediction():
    if(bayesianPrediction([test])):
        print("PASOK")
    else:
        print("HINDI PASOK")
        

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

# INPUT FIELD
input_debt = Entry(root).place(x = 140,y = 100)
input_bank = Entry(root).place(x = 140,y = 130)
input_employed = Entry(root).place(x = 140,y = 160)
input_credit_score = Entry(root).place(x = 140,y = 200)
input_income = Entry(root).place(x = 140,y = 230)
input_result = Entry(root).place(x = 220,y = 320)

# button for prediction
ttk.Button(root,text = "Predict", command = prediction).place(x = 250,y = 270)

root.mainloop()

#okay okay 