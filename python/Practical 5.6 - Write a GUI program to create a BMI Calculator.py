# Practical 5.6
# Title: Practical 5.6 - Write a GUI program to create a BMI Calculator.py

import tkinter as tk

top = tk.Tk()
top.title("BMI Calculator")

# Labels
l1 = tk.Label(top, text="Weight (kg):")
l2 = tk.Label(top, text="Height (cm):")
l3 = tk.Label(top, text="BMI:")

# Entry fields
e1 = tk.Entry(top, width=15)
e2 = tk.Entry(top, width=15)
e3 = tk.Entry(top, width=15, state="disabled")

# Grid placement
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l3.grid(row=2, column=0)
e3.grid(row=2, column=1)

# Functions
def exits():
    top.destroy()

def clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.config(state="normal")
    e3.delete(0, tk.END)
    e3.config(state="disabled")

def calculate():
    try:
        weight = float(e1.get())
        height_cm = float(e2.get())
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        e3.config(state="normal")
        e3.delete(0, tk.END)
        e3.insert(0, round(bmi, 2))
        e3.config(state="disabled")
    except:
        clear()

# Buttons
b1 = tk.Button(top, text="Calculate", command=calculate)
b2 = tk.Button(top, text="Clear", command=clear)
b3 = tk.Button(top, text="Exit", command=exits)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=4, columnspan=2)

top.mainloop()
