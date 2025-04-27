import tkinter as tk

top = tk.Tk()
top.title("Courier Charge Calculator")

def calculate_cost():
    try:
        weight = float(e1.get())
        if rb1_var.get() == 1:
            rate_per_kg = 50  # Standard rate
        else:
            rate_per_kg = 100  # Express rate

        cost = weight * rate_per_kg
        e3.config(state='normal')
        e3.delete(0, tk.END)
        e3.insert(0, f"₹{cost}")
        e3.config(state='disabled')
    except ValueError:
        clear()

def clear():
    e1.delete(0, tk.END)
    rb1_var.set(0)
    e3.config(state='normal')
    e3.delete(0, tk.END)
    e3.config(state='disabled')

def exit_app():
    top.destroy()

# Widgets
l1 = tk.Label(top, text="Package Weight (kg)")
e1 = tk.Entry(top)

l2 = tk.Label(top, text="Delivery Type")
rb1_var = tk.IntVar()
rb1 = tk.Radiobutton(top, text="Standard - ₹50/kg", variable=rb1_var, value=1)
rb2 = tk.Radiobutton(top, text="Express - ₹100/kg", variable=rb1_var, value=2)

l3 = tk.Label(top, text="Total Cost")
e3 = tk.Entry(top, state="disabled")

b1 = tk.Button(top, text="Calculate Cost", command=calculate_cost)
b2 = tk.Button(top, text="Clear", command=clear)
b3 = tk.Button(top, text="Exit", command=exit_app)

# Grid placement
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)

l2.grid(row=1, column=0)
rb1.grid(row=2, column=1)
rb2.grid(row=3, column=1)

l3.grid(row=4, column=0)
e3.grid(row=4, column=1)

b1.grid(row=5, column=0)
b2.grid(row=5, column=1)
b3.grid(row=5, column=2)

top.mainloop()
