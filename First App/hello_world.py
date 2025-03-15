import tkinter as tk
from tkinter import ttk


def greet():
    print("Button clicked!")


# main window
# creates a tk object -> does not run itself
root = tk.Tk()

# inserindo um label
ttk.Label(root, text="Hello, world!", padding=(30, 10)).pack()

# button widget
greet_button = ttk.Button(root, text="Greet", command=greet)
# side=top default
greet_button.pack(side="left", fill="x", expand=True)

# closes window
quit_button = ttk.Button(root, text="Quite", command=root.destroy)
quit_button.pack(side="left")

# creating a loop and running the window
root.mainloop()
