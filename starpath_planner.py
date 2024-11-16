from tkinter import *
from tkcalendar import Calendar

# Create Main Window
root = Tk()
root.geometry("600x600")
root.title("Starpath Planner")

# Load Background Image
backg = PhotoImage(file="spacebackground.png")

# Add Background Label
background_label = Label(root, image=backg)
background_label.place(relwidth=1, relheight=1)

# Create Frame for Widgets (opaque look)
frame1 = Frame(root, bg="#1e1f26", bd=2, relief="ridge")  # Set a background color for opacity effect
frame1.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=400)

# Add Calendar
calendar = Calendar(frame1, selectmode="day", year=2024, month=11, day=16,
                    background="#1e1f26", foreground="white", selectbackground="#6c63ff", borderwidth=0)
calendar.pack(pady=(10, 20))

# Add Label and Entry for Task
task_label = Label(frame1, text="Task:", font=("Helvetica", 14), bg="#1e1f26", fg="white")
task_label.pack(anchor=W, padx=20)

task_entry = Entry(frame1, width=30, font=("Helvetica", 14), bg="#333333", fg="white", insertbackground="white", relief="flat")
task_entry.pack(pady=10)

# Add Buttons (side by side with improved styles)
button_frame = Frame(frame1, bg="#1e1f26")
button_frame.pack(pady=20)

def on_hover(button, bg_color):
    """ Changes button background color on hover """
    def hover_effect(event):
        button['background'] = bg_color
    def leave_effect(event):
        button['background'] = "#6c63ff"
    button.bind("<Enter>", hover_effect)
    button.bind("<Leave>", leave_effect)

add_button = Button(button_frame, text="Add Task", bg="#6c63ff", fg="white", font=("Helvetica", 12), relief="flat", padx=20, pady=5, activebackground="#5555ff")
add_button.pack(side=LEFT, padx=10)
on_hover(add_button, "#5555ff")

view_button = Button(button_frame, text="View Agenda", bg="#6c63ff", fg="white", font=("Helvetica", 12), relief="flat", padx=20, pady=5, activebackground="#5555ff")
view_button.pack(side=LEFT, padx=10)
on_hover(view_button, "#5555ff")

# Run Application
root.mainloop()
