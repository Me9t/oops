import tkinter as tk
from tkinter import ttk

top = tk.Tk()
top.title("Ice Cream Parlour Order System")

def calculate_total():
    try:
        flavour = selected_flavour.get()
        quantity = int(spin_qty.get())

        if flavour == "Vanilla":
            price = 50
        elif flavour == "Chocolate":
            price = 70
        elif flavour == "Strawberry":
            price = 60
        elif flavour == "Butterscotch":
            price = 65
        elif flavour == "Mango":
            price = 55
        else:
            price = 0

        total = price * quantity
        e3.config(state='normal')
        e3.delete(0, tk.END)
        e3.insert(0, f"₹{total}")
        e3.config(state='disabled')
    except ValueError:
        clear()

def clear():
    selected_flavour.set("Vanilla")
    spin_qty.delete(0, tk.END)
    spin_qty.insert(0, 1)
    e3.config(state='normal')
    e3.delete(0, tk.END)
    e3.config(state='disabled')

def exit_app():
    top.destroy()

# Widgets
l1 = tk.Label(top, text="Select Flavour")
selected_flavour = tk.StringVar()
selected_flavour.set("Vanilla")
flavour_menu = ttk.Combobox(top, textvariable=selected_flavour, 
                           values=["Vanilla", "Chocolate", "Strawberry", "Butterscotch", "Mango"])

l2 = tk.Label(top, text="Quantity")
spin_qty = tk.Spinbox(top, from_=1, to=10)

l3 = tk.Label(top, text="Total Cost")
e3 = tk.Entry(top, state='disabled')

b1 = tk.Button(top, text="Calculate", command=calculate_total)
b2 = tk.Button(top, text="Clear", command=clear)
b3 = tk.Button(top, text="Exit", command=exit_app)

# Grid Layout
l1.grid(row=0, column=0)
flavour_menu.grid(row=0, column=1)

l2.grid(row=1, column=0)
spin_qty.grid(row=1, column=1)

l3.grid(row=2, column=0)
e3.grid(row=2, column=1)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

top.mainloop()
