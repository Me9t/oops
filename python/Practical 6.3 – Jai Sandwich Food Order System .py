import tkinter as tk

def calculate_bill():
    total = 0
    if pizza_var.get():
        total += 200
    if sandwich_var.get():
        total += 100
    if burger_var.get():
        total += 120

    # Apply discount
    if discount_var.get() == 1:
        total -= total * 0.05  # 5% Discount
    elif discount_var.get() == 2:
        total -= total * 0.10  # 10% Discount

    # Add Take Away charge
    if takeaway_var.get():
        total += 10

    total_label.config(text=f"Final Bill: ₹{total:.2f}")

def clear_fields():
    pizza_var.set(0)
    sandwich_var.set(0)
    burger_var.set(0)
    discount_var.set(0)
    takeaway_var.set(0)
    total_label.config(text="Final Bill: ₹0.00")

def exit_app():
    top.destroy()

top = tk.Tk()
top.title("Jai Sandwich Food Order System")

# Variables
pizza_var = tk.IntVar()
sandwich_var = tk.IntVar()
burger_var = tk.IntVar()
discount_var = tk.IntVar()
takeaway_var = tk.IntVar()

# Food Checkboxes
tk.Checkbutton(top, text="Pizza ₹200", variable=pizza_var).pack()
tk.Checkbutton(top, text="Grilled Sandwich ₹100", variable=sandwich_var).pack()
tk.Checkbutton(top, text="Burger ₹120", variable=burger_var).pack()

# Discount Radiobuttons
tk.Radiobutton(top, text="5% Discount", variable=discount_var, value=1)._
