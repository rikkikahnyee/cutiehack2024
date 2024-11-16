import pygame
import sys
from tkinter import *


# Initialize Pygame
pygame.init()


# Set up the Pygame screen (this will be the window where the astronaut moves)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Astronaut Animation")


# Load astronaut image (replace with your astronaut image path)
astronaut_image = pygame.image.load("/Users/vidhitapde/Downloads/astro.png")
astronaut_rect = astronaut_image.get_rect()


# Set initial position for astronaut
astronaut_rect.x = 0
astronaut_rect.y = screen_height // 2 - astronaut_image.get_height() // 2


# Function to animate the astronaut across the screen
def start_animation():
   running = True
   clock = pygame.time.Clock()


   while running:
       screen.fill((0, 0, 0))  # Fill the screen with black
      
       # Move astronaut across the screen
       astronaut_rect.x += 5
       if astronaut_rect.x > screen_width:
           astronaut_rect.x = 0  # Reset position to start again


       # Draw astronaut
       screen.blit(astronaut_image, astronaut_rect)


       pygame.display.update()  # Update the screen


       # Event handling (like closing the window)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False


       clock.tick(30)  # Frame rate control (30 FPS)


# Set up tkinter UI (separate from the pygame window)
root = Tk()
root.title("Welcome to StarPath")
root.geometry("800x600")
root.config(bg="#1f4277")


# Create a frame for the widgets
frame1 = Frame(root, bg="#1f4277", bd=2)
frame1.place(relx=0.5, rely=0.5, anchor=CENTER, width=800, height=300)


# Create the label inside the frame
lbl = Label(frame1, text="WELCOME TO STARPATH", font=("Comic Sans MS", 45, "bold"),
           fg="white", bg="#1f4277", anchor="center", justify="center")
lbl.grid(sticky="nsew")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)


# Create a canvas for the custom button
canvas = Canvas(root, width=200, height=60, bg="#000000", bd=0, highlightthickness=0)
canvas.pack(pady=(650, 10))


# Create a rectangle for the button on the canvas
canvas.create_rectangle(0, 0, 200, 60, fill="#000000", outline="#000000")


# Add text to the button
canvas.create_text(100, 30, text="LAUNCH", font=("Comic Sans MS", 30), fill="yellow")


# Bind the button click event to a function
def on_button_click(event):
   print("Launch button clicked!")
   start_animation()


canvas.bind("<Button-1>", on_button_click)


# Start Tkinter main loop
root.mainloop()


# Quit Pygame
pygame.quit()
sys.exit()