import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    def on_convert():
        try:
            value = float(entry.get())
            result = 0.0

            if selected_option.get() == "Fahrenheit to Celsius":
                result = (value - 32) * 5 / 9
            elif selected_option.get() == "Celsius to Fahrenheit":
                result = (value * 9 / 5) + 32

            messagebox.showinfo("Result", f"Result: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    root = tk.Tk()
    root.title("Temperature Converter")

    selected_option = tk.StringVar()
    selected_option.set("Fahrenheit to Celsius")

    option_menu = tk.OptionMenu(root, selected_option, "Fahrenheit to Celsius", "Celsius to Fahrenheit")
    option_menu.pack()

    entry = tk.Entry(root)
    entry.pack()

    convert_button = tk.Button(root, text="Convert", command=on_convert)
    convert_button.pack()

    root.mainloop()

convert_temperature()
