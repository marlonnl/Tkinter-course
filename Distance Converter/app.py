import tkinter as tk
from tkinter import ttk

import tkinter.font as font

root = tk.Tk()
root.title("Distance converter")

font.nametofont("TkDefaultFont").configure(size=16)
default_font = font.nametofont("TkDefaultFont")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variables
meters_value = tk.StringVar()
feet_value = tk.StringVar()


# Functions
def calculate_feet(*args):
    try:
        meters = float(meters_value.get())
        conversion = meters * 3.28084
        feet_value.set(f"{conversion:.3f}")

    # If button is pressed without any value yet
    except ValueError:
        pass


# Frames
mainframe = ttk.Frame(root, padding=(30, 15))
mainframe.grid(row=0, column=0)

# Widgets
meters_label = ttk.Label(mainframe, text="Meters:")
meters_label.grid(row=0, column=0, sticky="W")

meters_input = ttk.Entry(
    mainframe, width=10, textvariable=meters_value, font=(default_font, 15)
)
meters_input.grid(row=0, column=1, sticky="EW")
meters_input.focus()

feet_label = ttk.Label(mainframe, text="Feet:")
feet_label.grid(row=1, column=0, sticky="W")

feet_display = ttk.Label(mainframe, text="feet result", textvariable=feet_value)
feet_display.grid(row=1, column=1, sticky="EW")

calculate_btn = ttk.Button(mainframe, text="Calculate", command=calculate_feet)
calculate_btn.grid(row=2, column=0, columnspan=2, sticky="EW")


# Keybindings
# Enter to calculate
root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

# ESC to exit
root.bind("<Escape>", lambda _: root.destroy())


# winfo_children
for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
