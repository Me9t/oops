# Practical 5.1
# Title: Practical 5.1 - Write a GUI program to develop a Simple Calculator

import tkinter as tk

top = tk.Tk()
top.title("Simple Calculator")

# Labels
l1 = tk.Label(top, text="Number 1")
l2 = tk.Label(top, text="Number 2")
l3 = tk.Label(top, text="Result")

# Entry fields
e1 = tk.Entry(top, width=10)
e2 = tk.Entry(top, width=10)
e3 = tk.Entry(top, width=10, state="disabled")

# Grid placement
l1.grid(column=0, row=0)
e1.grid(column=1, row=0)
l2.grid(column=0, row=1)
e2.grid(column=1, row=1)
l3.grid(column=0, row=2)
e3.grid(column=1, row=2)

# Functions
def exits():
    top.destroy()

def clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.configure(state='normal')
    e3.delete(0, tk.END)
    e3.configure(state='disabled')

def add():
    num1 = float(e1.get())
    num2 = float(e2.get())
    result = num1 + num2
    e3.configure(state='normal')
    e3.delete(0, tk.END)
    e3.insert(0, result)
    e3.configure(state='disabled')

def subtract():
    num1 = float(e1.get())
    num2 = float(e2.get())
    result = num1 - num2
    e3.configure(state='normal')
    e3.delete(0, tk.END)
    e3.insert(0, result)
    e3.configure(state='disabled')

def multiply():
    num1 = float(e1.get())
    num2 = float(e2.get())
    result = num1 * num2
    e3.configure(state='normal')
    e3.delete(0, tk.END)
    e3.insert(0, result)
    e3.configure(state='disabled')

def divide():
    num1 = float(e1.get())
    num2 = float(e2.get())
    e3.configure(state='normal')
    e3.delete(0, tk.END)
    if num2 != 0:
        result = num1 / num2
        e3.insert(0, result)
    else:
        e3.insert(0, "Error")
    e3.configure(state='disabled')

# Buttons
b1 = tk.Button(top, text="Add", command=add)
b2 = tk.Button(top, text="Subtract", command=subtract)
b3 = tk.Button(top, text="Multiply", command=multiply)
b4 =
