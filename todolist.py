import tkinter as tk
from tkinter import messagebox


class TodoList:
    def __init__(self, entry, listbox):
        self.entry = entry
        self.listbox = listbox
        self.tasks = []

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        try:
            selected_indices = self.listbox.curselection()
            if selected_indices:
                selected_index = selected_indices[0]  # Extract the first index from the tuple
                task = self.listbox.get(selected_index)
                confirmation = messagebox.askyesno(
                    "Confirmation", f"Are you sure you want to delete the task: {task}?"
                )
                if confirmation:
                    self.tasks.pop(selected_index)
                    self.listbox.delete(selected_index)
        except tk.TclError:
            pass


def create_todo_list():
    root = tk.Tk()
    root.title("To-Do List")

    entry = tk.Entry(root)
    entry.pack()

    listbox = tk.Listbox(root)
    listbox.pack()

    todo_list = TodoList(entry, listbox)

    add_button = tk.Button(root, text="Add Task", command=todo_list.add_task)
    add_button.pack()

    delete_button = tk.Button(root, text="Delete Task", command=todo_list.delete_task)
    delete_button.pack()

    root.mainloop()


create_todo_list()
