import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random
from datetime import datetime

class SpaceAgendaPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Space-Themed Agenda Planner")
        self.root.geometry("800x600")
        self.root.config(bg="black")

        # Data structures
        self.tasks = []
        self.categories = ["Work", "Personal", "Fitness"]
        self.stars = 0

        # Start with splash screen
        self.show_splash_screen()

    def show_splash_screen(self):
        # Splash screen with starry background and rocket animation
        self.splash_canvas = tk.Canvas(self.root, width=800, height=600, bg="black", highlightthickness=0)
        self.splash_canvas.pack(fill="both", expand=True)

        # Add stars to the background
        for _ in range(50):  # White stars
            x, y = random.randint(0, 800), random.randint(0, 600)
            self.splash_canvas.create_oval(x, y, x + 2, y + 2, fill="white", outline="")
        for _ in range(30):  # Yellow stars
            x, y = random.randint(0, 800), random.randint(0, 600)
            self.splash_canvas.create_oval(x, y, x + 3, y + 3, fill="yellow", outline="")
        for _ in range(20):  # Galaxies (larger, faint stars)
            x, y = random.randint(0, 800), random.randint(0, 600)
            self.splash_canvas.create_oval(x, y, x + 8, y + 8, fill="lightblue", outline="")

        # Add text with aesthetic font
        self.splash_canvas.create_text(400, 100, text="Initializing Universe...", font=("Arial", 20, "italic"), fill="white")
        
        # Load spaceship image
        spaceship_img = Image.open("rocket.png").convert("RGBA").resize((100, 100))
        # Ensure transparency by removing white background
        datas = spaceship_img.getdata()
        new_data = []
        for item in datas:
            if item[:3] == (255, 255, 255):  # Make white transparent
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        spaceship_img.putdata(new_data)
        self.spaceship_image = ImageTk.PhotoImage(spaceship_img)
        self.rocket = self.splash_canvas.create_image(400, 500, image=self.spaceship_image)
        self.thrust_particles = []

        # Animate rocket flying up
        self.rocket_speed = 5  # Initial speed
        self.animate_rocket()

    def animate_rocket(self):
        # Move the spaceship image and add thrust particles
        self.splash_canvas.move(self.rocket, 0, -self.rocket_speed)
        self.rocket_speed += 0.3  # Accelerate the rocket

        # Create dynamic thrust particles
        x1, y1 = self.splash_canvas.coords(self.rocket)
        thrust_particle = self.splash_canvas.create_oval(
            x1 + random.randint(-5, 5), y1 + random.randint(10, 20),
            x1 + random.randint(-2, 2), y1 + random.randint(20, 30),
            fill="orange", outline=""
        )
        self.thrust_particles.append(thrust_particle)

        # Fade and delete old particles
        for particle in self.thrust_particles[:]:
            x1, y1, x2, y2 = self.splash_canvas.coords(particle)
            self.splash_canvas.move(particle, 0, 3)  # Move particle down
            self.splash_canvas.itemconfig(particle, fill="yellow")  # Change color over time
            if y2 > 600:  # Remove particles off-screen
                self.splash_canvas.delete(particle)
                self.thrust_particles.remove(particle)

        # Check if rocket is off-screen
        coords = self.splash_canvas.coords(self.rocket)
        if coords[1] > 0:  # Rocket still visible
            self.root.after(50, self.animate_rocket)
        else:
            # Transition to the main planner page
            self.splash_canvas.destroy()
            self.create_main_screen()

    def create_main_screen(self):
        # Main Screen UI
        self.clear_screen()

        # Create starry background
        canvas = tk.Canvas(self.root, width=800, height=600, bg="black", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Add stars
        for _ in range(50):  # White stars
            x, y = random.randint(0, 800), random.randint(0, 600)
            canvas.create_oval(x, y, x + 2, y + 2, fill="white", outline="white")
        for _ in range(30):  # Yellow stars
            x, y = random.randint(0, 800), random.randint(0, 600)
            canvas.create_oval(x, y, x + 3, y + 3, fill="yellow", outline="")
        for _ in range(20):  # Galaxies (larger, faint stars)
            x, y = random.randint(0, 800), random.randint(0, 600)
            canvas.create_oval(x, y, x + 8, y + 8, fill="lightblue", outline="")

        # Title and star count
        canvas.create_text(400, 50, text="Space-Themed Agenda Planner", font=("Arial", 28, "bold"), fill="white")
        canvas.create_text(400, 100, text=f"Stars Earned: {self.stars}", font=("Arial", 18), fill="yellow")

        # Store planet images to prevent garbage collection
        self.planet_images = [
            ImageTk.PhotoImage(Image.open("mercury.png").resize((100, 100))),
            ImageTk.PhotoImage(Image.open("neptune.png").resize((125, 125))),
            ImageTk.PhotoImage(Image.open("saturn.png").resize((200, 100)))
        ]

        # Define X-coordinates for planets
        button_x_coords = [125, 325, 525]

        # Loop to create buttons and labels for planets
        for i, x in enumerate(button_x_coords):
            # Create a button for each planet
            planet_button = tk.Button(canvas, image=self.planet_images[i], command=lambda category=self.categories[i]: self.handle_planet_click(category), bg="black", borderwidth=0, highlightthickness=0)
            # Place button on the canvas
            canvas.create_window(x + 75, 300, window=planet_button, anchor="center")

            # Add category label below the button
            canvas.create_text(x + 75, 370, text=self.categories[i], fill="white", font=("Arial", 14, "bold"))

        # Add buttons aligned at the bottom
        buttons = [
            ("Add Task", self.add_task_screen, "#32CD32"),
            ("View Tasks", self.view_tasks_screen, "#1E90FF"),
            ("Customization Shop", self.customization_screen, "#FFD700"),
        ]
        for i, (text, command, color) in enumerate(buttons):
            tk.Button(self.root, text=text, command=command, bg=color, fg="black", font=("Arial", 14, "bold"), width=15, height=2).place(x=button_x_coords[i], y=500)

    def add_task_screen(self):
        # Screen for adding a new task
        self.clear_screen()

        tk.Label(self.root, text="Add New Task", font=("Tahoma", 20, "bold"), bg="black", fg="white").pack(pady=20)

        tk.Label(self.root, text="Task Name:", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        entry_name = tk.Entry(self.root, font=("Arial", 14))
        entry_name.pack(pady=5)

        tk.Label(self.root, text="Due Date (MM-DD-YYYY):", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        entry_due_date = tk.Entry(self.root, font=("Arial", 14))
        entry_due_date.pack(pady=5)

        tk.Label(self.root, text="Category:", bg="black", fg="white", font=("Arial", 14)).pack(pady=5)
        combo_category = ttk.Combobox(self.root, values=self.categories, font=("Arial", 14))
        combo_category.pack(pady=5)

        # Add Calendar
        calendar_frame = tk.Frame(self.root, bg="#2a2a2e", bd=5, relief="ridge")
        calendar_frame.pack(pady=10)
        calendar = Calendar(calendar_frame, selectmode="day", year=2024, month=11, day=16,
                            background="#2a2a2e", foreground="white", selectbackground="#6c63ff",
                            borderwidth=1, headersbackground="#444444", headersforeground="white")
        calendar.pack(pady=(10, 20))

        def save_task():
            name = entry_name.get()
            due_date = entry_due_date.get()
            category = combo_category.get()

            if not name or not due_date or not category:
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                due_date_obj = datetime.strptime(due_date, "%m-%d-%Y")
            except ValueError:
                messagebox.showerror("Error", "Invalid date format! Use MM-DD-YYYY.")
                return

            self.tasks.append({"name": name, "due_date": due_date_obj, "category": category})
            self.create_main_screen()

        tk.Button(self.root, text="Save Task", command=save_task, bg="#32CD32", fg="black", font=("Arial", 14, "bold"), width=12).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_screen, bg="#A9A9A9", fg="black", font=("Arial", 14, "bold"), width=12).pack(pady=10)

    def view_tasks_screen(self):
        # Screen for viewing tasks
        self.clear_screen()

        tk.Label(self.root, text="Tasks", font=("Arial", 20, "bold"), bg="black", fg="white").pack(pady=20)

        if not self.tasks:
            tk.Label(self.root, text="No tasks available!", font=("Arial", 16), bg="black", fg="white").pack(pady=20)
        else:
            # Sort tasks by due date
            # Sort tasks by due date
            self.tasks = sorted(self.tasks, key=lambda task: task['due_date'])

            # Display tasks
            for task in self.tasks:
                frame = tk.Frame(self.root, bg="black")
                frame.pack(pady=5)

                tk.Label(
                    frame,
                    text=f"Due Date: {task['due_date'].strftime('%m-%d-%Y')}\nTask Name: {task['name']}\nCategory: {task['category']}",
                    font=("Arial", 14),
                    bg="black",
                    fg="white"
                ).pack(side=tk.LEFT, padx=10)

                tk.Button(frame, text="Complete", command=lambda t=task: self.complete_task(t), bg="#FF4500", fg="white", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)

        tk.Button(self.root, text="Back", command=self.create_main_screen, bg="#A9A9A9", fg="black", font=("Arial", 14, "bold"), width=12).pack(pady=20)

    def complete_task(self, task):
        self.tasks.remove(task)
        self.stars += 10  # Award stars for task completion
        messagebox.showinfo("Task Completed", f"Task '{task['name']}' completed! You earned 10 stars.")
        self.view_tasks_screen()

    def customization_screen(self):
        # Customization shop
        self.clear_screen()

        tk.Label(self.root, text="Customization Shop", font=("Arial", 20, "bold"), bg="black", fg="white").pack(pady=20)
        tk.Label(self.root, text=f"Stars: {self.stars}", font=("Arial", 16), bg="black", fg="yellow").pack(pady=10)

        tk.Label(self.root, text="(Future feature: Buy items with stars)", font=("Arial", 14), bg="black", fg="white").pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_screen, bg="#A9A9A9", fg="black", font=("Arial", 14, "bold"), width=12).pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SpaceAgendaPlanner(root)
    root.mainloop()
