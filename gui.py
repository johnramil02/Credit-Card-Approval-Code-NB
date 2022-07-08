import tkinter as tk
from tkinter import *
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('500x450')
root.resizable(False, False)
root.title('Credit Card Approval')

#Label and form input
a = Label(root ,text = "Debt").place(x = 40,y = 100) #(row = 0,column = 0)
b = Label(root ,text = "Bank Customer").place(x = 40,y = 130)
c = Label(root ,text = "Employed").place(x = 40,y = 160)
d = Label(root ,text = "Credit Score").place(x = 40,y = 200)
e = Label(root ,text = "Income").place(x = 40,y = 230)
f = Label(root ,text = "Result").place(x = 180,y = 320)

submit_button = Button(root,text = "Predict").place(x = 250,y = 270)

a1 = Entry(root).place(x = 140,y = 100)
b1 = Entry(root).place(x = 140,y = 130)
c1 = Entry(root).place(x = 140,y = 160)
d1 = Entry(root).place(x = 140,y = 200)
e1 = Entry(root).place(x = 140,y = 230)
f1 = Entry(root).place(x = 220,y = 320)

root.mainloop()