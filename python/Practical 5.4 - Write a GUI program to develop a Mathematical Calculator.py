# Practical 5.4
# Title: Practical 5.4 - Write a GUI program to develop a Mathematical Calculator.py

import tkinter as tk
import math

top = tk.Tk()
top.title("Math Calculator")

# Labels
l1 = tk.Label(top, text="Enter Number:")
l2 = tk.Label(top, text="Square:")
l3 = tk.Label(top, text="Square Root:")
l4 = tk.Label(top, text="Cube:")
l5 = tk.Label(top, text="Cube Root:")
l6 = tk.Label(top, text="Factorial:")

# Entries
e1 = tk.Entry(top, width=15)
e2 = tk.Entry(top, width=15, state="disabled")
e3 = tk.Entry(top, width=15, state="disabled")
e4 = tk.Entry(top, width=15, state="disabled")
e5 = tk.Entry(top, width=15, state="disabled")
e6 = tk.Entry(top, width=15, state="disabled")

# Layout
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l3.grid(row=2, column=0)
e3.grid(row=2, column=1)
l4.grid(row=3, column=0)
e4.grid(row=3, column=1)
l5.grid(row=4, column=0)
e5.grid(row=4, column=1)
l6.grid(row=5, column=0)
e6.grid(row=5, column=1)

# Functions
def exits():
    top.destroy()

def clear():
    e1.delete(0, tk.END)
    for e in [e2, e3, e4, e5, e6]:
        e.config(state="normal")
        e.delete(0, tk.END)
        e.config(state="disabled")

def calculate():
    try:
        n = float(e1.get())
        e2.config(state="normal")
        e2.delete(0, tk.END)
        e2.insert(0, n**2)
        e2.config(state="disabled")

        e3.config(state="normal")
        e3.delete(0, tk.END)
        e3.insert(0, round(math.sqrt(n), 2))
        e3.config(state="disabled")

        e4.config(state="normal")
        e4.delete(0, tk.END)
        e4.insert(0, n**3)
        e4.config(state="disabled")

        e5.config(state="normal")
        e5.delete(0, tk.END)
        e5.insert(0, round(n**(1/3), 2))
        e5.config(state="disabled")

        e6.config(state="normal")
        e6.delete(0, tk.END)
        e6.insert(0, math.factorial(int(n)))
        e6.config(state="disabled")
    except:
        clear()

# Buttons
b1 = tk.Button(top, text="Calculate", command=calculate)
b2 = tk.Button(top, text="Clear", command=clear)
b3 = tk.Button(top, text="Exit", command=exits)

b1.grid(row=6, column=0)
b2.grid(row=6, column=1)
b3.grid(row=7, columnspan=2)

top.mainloop()
