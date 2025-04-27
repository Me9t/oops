# Practical 5.2
# Title: Practical 5.2 - Write a GUI program to develop a Simple Interest Calculator

import tkinter as tk

top = tk.Tk()
top.title("Simple Interest Calculator")

# Labels
l1 = tk.Label(top, text="Principal Amount")
l2 = tk.Label(top, text="Rate of Interest")
l3 = tk.Label(top, text="Time (Years)")
l4 = tk.Label(top, text="Simple Interest")
l5 = tk.Label(top, text="Total Amount")

# Entry fields
e1 = tk.Entry(top, width=10)
e2 = tk.Entry(top, width=10)
e3 = tk.Entry(top, width=10)
e4 = tk.Entry(top, width=10, state="disabled")
e5 = tk.Entry(top, width=10, state="disabled")

# Placing
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

# Functions
def exits():
    top.destroy()

def clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.config(state="normal")
    e4.delete(0, tk.END)
    e4.config(state="disabled")
    e5.config(state="normal")
    e5.delete(0, tk.END)
    e5.config(state="disabled")

def calculate():
    try:
        p = float(e1.get())
        r = float(e2.get())
        t = float(e3.get())
        si = (p * r * t) / 100
        total = p + si
        e4.config(state="normal")
        e4.delete(0, tk.END)
        e4.insert(0, round(si, 2))
        e4.config(state="disabled")
        e5.config(state="normal")
        e5.delete(0, tk.END)
        e5.insert(0, round(total, 2))
        e5.config(state="disabled")
    except:
        clear()

# Buttons
b1 = tk.Button(top, text="Calculate", command=calculate)
b2 = tk.Button(top, text="Clear", command=clear)
b3 = tk.Button(top, text="Exit", command=exits)

b1.grid(row=5, column=0)
b2.grid(row=5, column=1)
b3.grid(row=6, columnspan=2)

top.mainloop()
