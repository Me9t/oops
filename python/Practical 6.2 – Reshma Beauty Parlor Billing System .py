import tkinter as tk

def calculate_total():
    total = 0
    if hair_var.get():
        total += 200
    if manicure_var.get():
        total += 300
    if makeover_var.get():
        total += 400

    if discount_var.get() == 5:
        discount = total * 0.05
    elif discount_var.get() == 10:
        discount = total * 0.10
    else:
        discount = 0

    net_payable = total - discount

    e1.config(state='normal')
    e1.delete(0, tk.END)
    e1.insert(0, f"{total:.2f}")
    e1.config(state='disabled')

    e2.config(state='normal')
    e2.delete(0, tk.END)
    e2.insert(0, f"{discount:.2f}")
    e2.config(state='disabled')

    e3.config(state='normal')
    e3.delete(0, tk.END)
    e3.insert(0, f"{net_payable:.2f}")
    e3.config(state='disabled')

def clear_fields():
    hair_var.set(0)
    manicure_var.set(0)
    makeover_var.set(0)
    discount_var.set(0)
    for entry in [e1, e2, e3]:
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.config(state='disabled')

def exit_program():
    top.destroy()

top = tk.Tk()
top.title("Reshma Beauty Parlor Billing System")

# Services
l1 = tk.Label(top, text="Select Services")
hair_var = tk.IntVar()
manicure_var = tk.IntVar()
makeover_var = tk.IntVar()

ck1 = tk.Checkbutton(top, text="Hair Styling ₹200", variable=hair_var)
ck2 = tk.Checkbutton(top, text="Manicure & Pedicure ₹300", variable=manicure_var)
ck3 = tk.Checkbutton(top, text="Complete Makeover ₹400", variable=makeover_var)

# Discounts
l2 = tk.Label(top, text="Select Discount")
discount_var = tk.IntVar()
rb1 = tk.Radiobutton(top, text="No Discount", variable=discount_var, value=0)
rb2 = tk.Radiobutton(top, text="5% Discount", variable=discount_var, value=5)
rb3 = tk.Radiobutton(top, text="10% Discount
