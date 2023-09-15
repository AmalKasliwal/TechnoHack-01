import tkinter as tk
from tkinter import messagebox


class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance}")

    def deposit(self):
        root = tk.Tk()

        def on_deposit():
            try:
                amount = float(entry.get())
                self.balance += amount
                messagebox.showinfo("Deposit",
                                    f"${amount} has been deposited into your account. Current balance: ${self.balance}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")

        deposit_window = tk.Toplevel(root)
        deposit_window.title("Deposit")

        entry = tk.Entry(deposit_window)
        entry.pack()

        deposit_button = tk.Button(deposit_window, text="Deposit", command=on_deposit)
        deposit_button.pack()

    def withdraw(self):
        root = tk.Tk()

        def on_withdraw():
            try:
                amount = float(entry.get())
                if amount <= self.balance:
                    self.balance -= amount
                    messagebox.showinfo("Withdraw",
                                        f"${amount} has been withdrawn from your account. Current balance: ${self.balance}")
                else:
                    messagebox.showerror("Error", "Insufficient funds.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")

        withdraw_window = tk.Toplevel(root)
        withdraw_window.title("Withdraw")

        entry = tk.Entry(withdraw_window)
        entry.pack()

        withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=on_withdraw)
        withdraw_button.pack()


def run_atm():
    atm = ATM()

    root = tk.Tk()
    root.title("ATM Simulator")

    check_balance_button = tk.Button(root, text="Check Balance", command=atm.check_balance)
    check_balance_button.pack()

    deposit_button = tk.Button(root, text="Deposit", command=atm.deposit)
    deposit_button.pack()

    withdraw_button = tk.Button(root, text="Withdraw", command=atm.withdraw)
    withdraw_button.pack()

    root.mainloop()


run_atm()
