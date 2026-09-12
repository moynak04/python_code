import tkinter as tk

# Create the main window
window = tk.Tk()

# Set window title
window.title("My First Tkinter Program")

# Set window size
window.geometry("400x300")

# Create a label
label = tk.Label(window, text="Hello, Welcome to Tkinter!")
label.pack()

# Run the application
window.mainloop()