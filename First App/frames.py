import tkinter as tk
from tkinter import ttk

root = tk.Tk()

mainframe = ttk.Frame(root)
mainframe.pack(side="left", fill="both", expand=True)

tk.Label(mainframe, text="Label top", bg="red").pack(
    side="top", expand=True, fill="both"
)
tk.Label(mainframe, text="Label top", bg="red").pack(
    side="top", expand=True, fill="both"
)
tk.Label(root, text="Label left", bg="green").pack(
    side="left", expand=True, fill="both"
)


root.mainloop()
