import tkinter as tk
from tkinter import ttk

def on_click(button_value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(button_value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("420x480")  # Slightly adjusted width to fit buttons

# Entry widget to display input and results
entry = ttk.Entry(root, font=('Arial', 24))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Define button style
style = ttk.Style()
style.configure('TButton', font=('Arial', 16))

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

button_width = 6

for button_value in buttons:
    ttk.Button(
        root,
        text=button_value,
        command=lambda button_value=button_value: on_click(button_value) if button_value != '=' else calculate(),
        style='TButton',
        width=button_width
    ).grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=5, ipady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create Clear button
ttk.Button(root, text='C', command=clear_entry, style='TButton', width=button_width).grid(row=row_val, column=col_val, columnspan=4, padx=5, pady=5, ipadx=5, ipady=5)

# Run the Tkinter event loop
root.mainloop()
