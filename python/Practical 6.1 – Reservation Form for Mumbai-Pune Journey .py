import tkinter as tk

def calculate():
    try:
        age = int(e2.get())
        fare = 500 if ac_var.get() == 1 else 300

        if age < 5 or age > 60:
            fare = fare / 2  # 50% discount for child or senior citizen

        gst = fare * 0.18  # 18% GST
        insurance = 1 if insurance_var.get() else 0
        total = fare + gst + insurance

        e4.config(state='normal')
        e4.delete(0, tk.END)
        e4.insert(0, f"{fare:.2f}")
        e4.config(state='disabled')

        e5.config(state='normal')
        e5.delete(0, tk.END)
        e5.insert(0, f"{gst:.2f}")
        e5.config(state='disabled')

        e6.config(state='normal')
        e6.delete(0, tk.END)
        e6.insert(0, f"{insurance}")
        e6.config(state='disabled')

        e7.config(state='normal')
        e7.delete(0, tk.END)
        e7.insert(0, f"{total:.2f}")
        e7.config(state='disabled')

    except ValueError:
        clear()

def clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    ac_var.set(0)
    insurance_var.set(0)
    for entry in [e4, e5, e6, e7]:
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.config(state='disabled')

def exit_app():
    top.destroy()

top = tk.Tk()
top.title("Mumbai-Pune Reservation Form")

# Labels and Entries
l1 = tk.Label(top, text="Name")
l2 = tk.Label(top, text="Age")
l3 = tk.Label(top, text="Journey Type (AC/Non-AC)")
l4 = tk.Label(top, text="Fare")
l5 = tk.Label(top, text="GST@18%")
l6 = tk.Label(top, text="Insurance")
l7 = tk.Label(top, text="Total Payable")

e1 = tk.Entry(top, width=15)
e2 = tk.Entry(top, width=15)
e4 = tk.Entry(top, width=15, state="disabled")
e5 = tk.Entry(top, width=15, state="disabled")
e6 = tk.Entry(top, width=15, state="disabled")
e7 = tk.Entry(top, width=15, state="disabled")

# Radio buttons for AC/Non-AC
ac_var = tk.IntVar()
rb1 = tk.Radiobutton(top, text="AC", variable=ac_var, value=1)
rb2 = tk.Radiobutton(top, text="Non-AC", variable=ac_var, value=0)

# Checkbox for insurance
insurance_var = tk.IntVar()
ck1 = tk.Checkbutton(top, text="Opt for Insurance at ₹1", variable=insurance_var)

# Buttons
b1 = tk.Button(top, text="Calculate", command=calculate)
b2 = tk.Button(top, text="Clear", command=clear)
b3 = tk.Button(top, text="Exit", command=exit_app)

# Grid placements
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l3.grid(row=2, column=0)
rb1.grid(row=2, column=1)
rb2.grid(row=3, column=1)
ck1.grid(columnspan=2, row=4)
b1.grid(columnspan=2, row=5)
b2.grid(row=6, column=0)
b3.grid(row=6, column=1)
l4.grid(row=7, column=0)
e4.grid(row=7, column=1)
l5.grid(row=8, column=0)
e5.grid(row=8, column=1)
l6.grid(row=9, column=0)
e6.grid(row=9, column=1)
l7.grid(row=10, column=0)
e7.grid(row=10, column=1)

top.mainloop()
