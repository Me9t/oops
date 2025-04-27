# Practical 5.3
# Title: Practical 5.3 - Write a GUI program to develop a Calorie Counter

import tkinter as tk

top = tk.Tk()
top.title("Calorie Counter")

# Labels
l1 = tk.Label(top, text="Food Item")
l2 = tk.Label(top, text="Calories per serving")
l3 = tk.Label(top, text="Number of servings")
l4 = tk.Label(top, text="Total Calories")

# Entry Fields
e1 = tk.Entry(top, width=10)
e2 = tk.Entry(top, width=10)
e3 = tk.Entry(top, width=10)
e4 = tk.Entry(top, width=10, state="disabled")

# Placing
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l3.grid(row=2, column=0)
e3.grid(row=2, column=1)
l4.grid(row=3, column=0)
e4.grid(row=3, column=1)

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

def calculate():
    try:
        cal_per_serving = float(e2.get())
        servings = float(e3.get())
        total_calories = cal_per_serving * servings
        e4.config(state="normal")
        e4.delete(0, tk.END)
        e4.insert(0, total_calories)
        e4.config(state="disabled")
    except:
        clear()

# Buttons
b1 = tk.Button(top, text="Calculate", command=calculate)
b2 = tk.Button(top, text="Clear", command=clear)
b3 = tk.Button(top, text="Exit", command=exits)

b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=5, columnspan=2)

top.mainloop()
