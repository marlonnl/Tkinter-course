import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get().title() or 'World'}!")


root = tk.Tk()
root.title("Greeter")

user_name = tk.StringVar()


# Input
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Name:")
name_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left", fill="x", expand=True)
name_entry.focus()


# Buttons

buttons_frame = ttk.Frame(root, padding=(20, 10))
buttons_frame.pack(fill="both")

greet_button = ttk.Button(buttons_frame, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)

root.mainloop()
