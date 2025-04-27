import tkinter as tk

top = tk.Tk()
top.title("Fast Food Order System")

def calculate_bill():
    try:
        pizza_qty = int(e1.get()) if e1.get() else 0
        burger_qty = int(e2.get()) if e2.get() else 0
        fries_qty = int(e3.get()) if e3.get() else 0
        coke_qty = int(e4.get()) if e4.get() else 0

        total = pizza_qty * 200 + burger_qty * 150 + fries_qty * 100 + coke_qty * 50

        if ck1_var.get():
            total += 20  # Take Away charge

        gst = total * 0.05
        final_amount = total + gst

        e5.config(state='normal')
        e5.delete(0, tk.END)
        e5.insert(0, f"₹{total}")
        e5.config(state='disabled')

        e6.config(state='normal')
        e6.delete(0, tk.END)
        e6.insert(0, f"₹{gst}")
        e6.config(state='disabled')

        e7.config(state='normal')
        e7.delete(0, tk.END)
        e7.insert(0, f"₹{final_amount}")
        e7.config(state='disabled')
    except ValueError:
        clear()

def clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    for entry in [e5, e6, e7]:
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.config(state='disabled')

def exit_app():
    top.destroy()

# Widgets
l1 = tk.Label(top, text="Pizza Quantity")
e1 = tk.Entry(top)

l2 = tk.Label(top, text="Burger Quantity")
e2 = tk.Entry(top)

l3 = tk.Label(top, text="Fries Quantity")
e3 = tk.Entry(top)

l4 = tk.Label(top, text="Coke Quantity")
e4 = tk.Entry(top)

ck1_var = tk.IntVar()
ck1 = tk.Checkbutton(top, text="Take Away (₹20)", variable=ck1_var)

b1 = tk.Button(top, text="Calculate Bill", command=calculate_bill)
b2 = tk.Button(top, text="Clear", command=clear)
b3 = tk.Button(top, text="Exit", command=exit_app)

l5 = tk.Label(top, text="Total Before GST")
e5 = tk.Entry(top, state="disabled")

l6 = tk.Label(top, text="GST (5%)")
e6 = tk.Entry(top, state="disabled")

l7 = tk.Label(top, text="Final Amount")
e7 = tk.Entry(top, state="disabled")

# Grid placement
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)

l2.grid(row=1, column=0)
e2.grid(row=1, column=1)

l3.grid(row=2, column=0)
e3.grid(row=2, column=1)

l4.grid(row=3, column=0)
e4.grid(row=3, column=1)

ck1.grid(row=4, columnspan=2, column=0)

b1.grid(row=5, column=0)
b2.grid(row=5, column=1)
b3.grid(row=5, column=2)

l5.grid(row=6, column=0)
e5.grid(row=6, column=1)

l6.grid(row=7, column=0)
e6.grid(row=7, column=1)

l7.grid(row=8, column=0)
e7.grid(row=8, column=1)

top.mainloop()
