import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_random_password():
    def on_generate():
        try:
            length = int(entry.get())
            if length <= 0:
                raise ValueError
            password = generate_password(length)
            messagebox.showinfo("Random Password", f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    root = tk.Tk()
    root.title("Random Password Generator")

    entry = tk.Entry(root)
    entry.pack()
    tk.Label(root,text="enter length of password",fg="red").pack()
    generate_button = tk.Button(root, text="Generate", command=on_generate)
    generate_button.pack()

    root.mainloop()

generate_random_password()
