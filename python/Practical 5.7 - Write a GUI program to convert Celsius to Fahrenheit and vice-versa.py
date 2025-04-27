# Practical 5.7
# Title: Practical 5.7 - Write a GUI program to convert Celsius to Fahrenheit and vice-versa.py

import tkinter as tk

top = tk.Tk()
top.title("Temperature Converter")

# Labels
l1 = tk.Label(top, text="Celsius:")
l2 = tk.Label(top, text="Fahrenheit:")

# Entry fields
e1 = tk.Entry(top, width=15)
e2 = tk.Entry(top, width=15)

# Grid placement
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)

# Functions
def exits():
    top.destroy()

def clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

def convert_to_fahrenheit():
    try:
        c = float(e1.get())
        f = (9/5) * c + 32
        e2.delete(0, tk.END)
        e2.insert(0, round(f, 2))
    except:
        clear()

def convert_to_celsius():
    try:
        f = float(e2.get())
        c = (f - 32) * 5/9
        e1.delete(0, tk.END)
        e1.insert(0, round(c, 2))
    except:
        clear()

# Buttons
b1 = tk.Button(top, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
b2 = tk.Button(top, text="Convert to Celsius", command=convert_to_celsius)
b3 = tk.Button(top, text="Clear", command=clear)
b4 = tk.Button(top, text="Exit", command=exits)

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=3, column=0)
b4.grid(row=3, column=1)

top.mainloop()
