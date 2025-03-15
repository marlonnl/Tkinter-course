import tkinter as tk
from tkinter import ttk

# DPI
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except all:
    pass


def greet():
    print(f"Hello, {user_name.get().title() or 'World'}!")


root = tk.Tk()
root.title("Greeter")

root.columnconfigure(0, weight=1)

# Variables
user_name = tk.StringVar()


# Input
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column=0, sticky="EW")

name_label = ttk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=(0, 10))

name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()


# Buttons
buttons_frame = ttk.Frame(root, padding=(20, 10))
buttons_frame.grid(row=1, column=0, sticky="EW")

# buttons_frame.columnconfigure(0, weight=1)
# buttons_frame.columnconfigure(1, weight=1)
buttons_frame.columnconfigure((0, 1), weight=1)

greet_button = ttk.Button(buttons_frame, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")

quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

root.mainloop()
