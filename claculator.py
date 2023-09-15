import tkinter as tk
from tkinter import messagebox

def handle_button_click(value):
    current_expression = entry.get()
    new_expression = current_expression + str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_expression)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid input or expression")

# Create a new Tkinter window
window = tk.Tk()
window.title("Calculator")

# Create an entry field
entry = tk.Entry(window,bg="red",fg="blue", width=25, font=("Arial", 12))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons
buttons = []
for i, label in enumerate(button_labels):
    row = i // 4 + 1
    col = i % 4
    button = tk.Button(window, text=label, width=5, height=2, font=("Arial", 12),fg="red", command=lambda value=label: handle_button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(button)

# Create clear button
clear_button = tk.Button(window, text="C", width=5, height=2, font=("Arial", 12),fg="red", command=clear_entry)
clear_button.grid(row=5, column=0, padx=5, pady=5)

# Create calculate button
calculate_button = tk.Button(window, text="=", width=5, height=2, font=("Arial", 12),fg="red", command=calculate)
calculate_button.grid(row=5, column=1, padx=5, pady=5)

# Start the Tkinter event loop
window.mainloop()
