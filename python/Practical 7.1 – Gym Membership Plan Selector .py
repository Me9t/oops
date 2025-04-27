import tkinter as tk

def calculate_total():
    months = 12  # Annual plan
    if plan_var.get() == 1:
        base = 500
    elif plan_var.get() == 2:
        base = 800
    elif plan_var.get() == 3:
        base = 1200
    else:
        base = 0

    total = base * months

    if trainer_var.get():
        total += 1000
    if diet_var.get():
        total += 500

    discount = total * 0.05  # 5% annual discount
    payable = total - discount

    e4.config(state='normal')
    e4.delete(0, tk.END)
    e4.insert(0, f"{total:.2f}")
    e4.config(state='disabled')

    e5.config(state='normal')
    e5.delete(0, tk.END)
    e5.insert(0, f"{discount:.2f}")
    e5.config(state='disabled')

    e6.config(state='normal')
    e6.delete(0, tk.END)
    e6.insert(0, f"{payable:.2f}")
    e6.config(state='disabled')

def clear_fields():
    name_entry.delete(0, tk.END)
    plan_var.set(0)
    trainer_var.set(0)
    diet_var.set(0)
    for entry in [e4, e5, e6]:
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.config(state='disabled')

def exit_app():
    top.destroy()

top = tk.Tk()
top.title("Gym Membership Plan Selector")

# Widgets
l1 = tk.Label(top, text="Name")
name_entry = tk.Entry(top, width=20)

l2 = tk.Label(top, text="Select Gym Plan (Monthly Fees)")
plan_var = tk.IntVar()
rb1 = tk.Radiobutton(top, text="Basic ₹500", variable=plan_var, value=1)
rb2 = tk.Radiobutton(top, text="Standard ₹800", variable=plan_var, value=2)
rb3 = tk.Radiobutton(top, text="Premium ₹1200", variable=plan_var, value=3)

l3 = tk.Label(top, text="Extras")
trainer_var = tk.IntVar()
diet_var = tk.IntVar()
cb1 = tk.Checkbutton(top, text="Personal Trainer ₹1000", variable=trainer_var)
cb2 = tk.Checkbutton(top, text="Diet Plan ₹500", variable=diet_var)

b1 = tk.Button(top, text="Calculate Total", command=calculate_total)
b2 = tk.Button(top, text="Clear", command=clear_fields)
b3 = tk.Button(top, text="Exit", command=exit_app)

l4 = tk.Label(top, text="Total Before Discount")
e4 = tk.Entry(top, width=15, state="disabled")

l5 = tk.Label(top, text="5% Discount")
e5 = tk.Entry(top, width=15, state="disabled")

l6 = tk.Label(top, text="Final Payable Amount")
e6 = tk.Entry(top, width=15, state="disabled")

# Layout
l1.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

l2.grid(row=1, column=0)
rb1.grid(row=2, column=1)
rb2.grid(row=3, column=1)
rb3.grid(row=4, column=1)

l3.grid(row=5, column=0)
cb1.grid(row=6, column=1)
cb2.grid(row=7, column=1)

b1.grid(row=8, column=0)
b2.grid(row=8, column=1)
b3.grid(row=8, column=2)

l4.grid(row=
