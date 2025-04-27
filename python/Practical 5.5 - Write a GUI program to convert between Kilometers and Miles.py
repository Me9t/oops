# Practical 5.5
# Title: Practical 5.5 - Write a GUI program to convert between Kilometers and Miles.py

import tkinter as tk

top = tk.Tk()
top.title("Kilometers to Miles Converter")

# Labels
l1 = tk.Label(top, text="Kilometers:")
l2 = tk.Label(top, text="Miles:")

# Entry fields
e1 = tk.Entry(top, width=15)
e2 = tk.Entry(top, width=15)

# Grid placement
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)

# Functions
def exits():
    top.destroy()

def clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

def convert_km_to_miles():
    try:
        km = float(e1.get())
        miles = km * 0.621371
        e2.delete(0, tk.END)
        e2.insert(0, round(miles, 2))
    except:
        clear()

def convert_miles_to_km():
    try:
        miles = float(e2.get())
        km = miles / 0.621371
        e1.delete(0, tk.END)
        e1.insert(0, round(km, 2))
    except:
        clear()

# Buttons
b1 = tk.Button(top, text="Convert KM to Miles", command=convert_km_to_miles)
b2 = tk.Button(top, text="Convert Miles to KM", command=convert_miles_to_km)
b3 = tk.Button(top, text="Clear", command=clear)
b4 = tk.Button(top, text="Exit", command=exits)

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=3, column=0)
b4.grid(row=3, column=1)

top.mainloop()
