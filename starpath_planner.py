import tkinter as tk
from tkinter import ttk


def save_agenda():
    date = date_entry.get()
    task = task_entry.get()
    agenda_list.insert(tk.END, f"{date}: {task}")
    date_entry.delete(0, tk.END)
    task_entry.delete(0, tk.END)


app = tk.Tk()
app.title("Agenda Planner")


tk.Label(app, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
date_entry = tk.Entry(app)
date_entry.grid(row=0, column=1)


tk.Label(app, text="Task:").grid(row=1, column=0)
task_entry = tk.Entry(app)
task_entry.grid(row=1, column=1)


tk.Button(app, text="Add Task", command=save_agenda).grid(row=2, column=0, columnspan=2)


agenda_list = tk.Listbox(app, width=50, height=10)
agenda_list.grid(row=3, column=0, columnspan=2)


app.mainloop()