import tkinter as tk
from tkinter import ttk

# main window
# creates a tk object -> does not run itself
root = tk.Tk()

# inserindo um label
ttk.Label(root, text="Hello, world!", padding=(30, 10)).pack()

# creating a loop and running the window
root.mainloop()
