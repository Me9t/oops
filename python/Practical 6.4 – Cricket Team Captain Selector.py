import tkinter as tk
from tkinter import ttk

def show_captain():
    captains = {
        "India": "Rohit Sharma",
        "Australia": "Pat Cummins",
        "England": "Ben Stokes",
        "South Africa": "Temba Bavuma",
        "Pakistan": "Babar Azam"
    }
    selected_country = country_var.get()
    e1.config(state='normal')
    e1.delete(0, tk.END)
    e1.insert(0, captains.get(selected_country, "Unknown"))
    e1.config(state='disabled')

def clear_fields():
    country_var.set("")
    e1.config(state='normal')
    e1.delete(0, tk.END)
    e1.config(state='disabled')

def exit_app():
    top.destroy()

top = tk.Tk()
top.title("Cricket Team Captain Selector")

# Label and Combobox
l1 = tk.Label(top, text="Select Country")
country_var = tk.StringVar()
cmb1 = ttk.Combobox(top, textvariable=country_var, values=[
    "India", "Australia", "England", "South Africa", "Pakistan"
])

# Buttons
b1 = tk.Button(top, text="Show Captain", command=show_captain)
b2 = tk.Button(top, text="Clear", command=clear_fields)
b3 = tk.Button(top, text="Exit", command=exit_app)

# Result Label and Entry
l2 = tk.Label(top, text="Captain")
e1 = tk.Entry(top, width=20, state="disabled")

# Layout
l1.grid(row=0, column=0)
cmb1.grid(row=0, column=1)
b1.grid(row=1, column=1)
b2.grid(row=2, column=0)
b3.grid(row=2, column=1)
l2.grid(row=3, column=0)
e1.grid(row=3, column=1)

top.mainloop()
