import tkinter as tk
from tkinter import ttk


class HelloWorld(tk.Tk):
    "Hello World tk window example"

    def __init__(self):
        super().__init__()

        self.title("Hello, world!")
        ttk.Label(self, text="Label widget inside an OOP GUI with tkinter!").pack()


root = HelloWorld()
root.mainloop()
