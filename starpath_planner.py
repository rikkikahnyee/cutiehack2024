from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk


# Create Main Window
root = Tk()
root.geometry("600x600")
root.title("Starpath Planner")


# Load Background Image
backg = PhotoImage(file="spacebackground.png")


# Add Background Label
background_label = Label(root, image=backg)
background_label.place(relwidth=1, relheight=1)


# Create Frame for Widgets
frame1 = Frame(root, bg="#000000", bd=2)  # Use a slight border to distinguish frame
frame1.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=400)


# Add Calendar
calendar = Calendar(frame1, selectmode="day", year=2024, month=11, day=16,
                    background="#1e1f26", foreground="white", selectbackground="#6c63ff")
calendar.pack(pady=20)


# Add Label and Entry for Task
task_label = Label(frame1, text="Task:", font=("Helvetica", 14), bg="#000000", fg="white")
task_label.pack()


task_entry = Entry(frame1, width=30, font=("Helvetica", 14))
task_entry.pack(pady=10)


# Add Buttons
add_button = Button(frame1, text="Add Task", bg="#6c63ff", fg="white", font=("Helvetica", 12))
add_button.pack(pady=10)


view_button = Button(frame1, text="View Agenda", bg="#6c63ff", fg="white", font=("Helvetica", 12))
view_button.pack(pady=10)


# Run Application
root.mainloop()