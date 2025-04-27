import tkinter as tk
from tkinter import ttk

def calculate_bill():
    try:
        seat_type = seat_var.get()
        num_tickets = int(ticket_entry.get())

        prices = {
            "Regular": 200,
            "Premium": 300,
            "VIP": 500
        }

        base_price = prices.get(seat_type, 0) * num_tickets

        # Apply student discount if selected
        if student_var.get():
            discount = base_price * 0.10
        else:
            discount = 0

        final_amount = base_price - discount

        bill_entry.config(state='normal')
        bill_entry.delete(0, tk.END)
        bill_entry.insert(0, f"₹{final_amount:.2f}")
        bill_entry.config(state='disabled')

    except ValueError:
        clear_fields()

def clear_fields():
    movie_var.set("")
    seat_var.set("")
    ticket_entry.delete(0, tk.END)
    student_var.set(0)
    bill_entry.config(state='normal')
    bill_entry.delete(0, tk.END)
    bill_entry.config(state='disabled')

def exit_program():
    top.destroy()

top = tk.Tk()
top.title("Movie Ticket Booking System")

# Variables
movie_var = tk.StringVar()
seat_var = tk.StringVar()
student_var = tk.IntVar()

# Movie selection
movie_label = tk.Label(top, text="Select Movie")
movie_combo = ttk.Combobox(top, textvariable=movie_var, values=[
    "Karate Kid: Legends", "Superman Legacy", "Thunderbolts"
], state="readonly")

# Seat selection
seat_label = tk.Label(top, text="Select Seat Type")
rb_regular = tk.Radiobutton(top, text="Regular ₹200", variable=seat_var, value="Regular")
rb_premium = tk.Radiobutton(top, text="Premium ₹300", variable=seat_var, value="Premium")
rb_vip = tk.Radiobutton(top, text="VIP ₹500", variable=seat_var, value="VIP")

# Ticket Entry
ticket_label = tk.Label(top, text="No. of Tickets")
ticket_entry = tk.Entry(top, width=10)

# Student Discount
student_check = tk.Checkbutton(top, text="Student Discount (10%)", variable=student_var)

# Final Bill
bill_label = tk.Label(top, text="Final Bill")
bill_entry = tk.Entry(top, width=20, state="disabled")

# Buttons
calculate_button = tk.Button(top, text="Calculate Bill", command=calculate_bill)
clear_button = tk.Button(top, text="Clear", command=clear_fields)
exit_button = tk.Button(top, text="Exit", command=exit_program)

# Layout
movie_label.grid(row=0, column=0)
movie
