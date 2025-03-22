import tkinter as tk
from tkinter import ttk


class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Greet!")

        UserInputFrame(self).pack()


class UserInputFrame(ttk.Frame):
    "Framing tkinter widgets in classes"

    def __init__(self, container):
        super().__init__(container, padding=(15))

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text="Enter your name:")
        label.pack()

        entry = ttk.Entry(self, textvariable=self.user_input)
        entry.focus()
        entry.pack()

        button = ttk.Button(self, text="Greet!", command=self.greet)
        button.pack()

        # Binds
        container.bind("<Return>", self.greet)
        container.bind("<KP_Enter>", self.greet)
        container.bind("<Escape>", lambda _: container.destroy())

    def greet(self, *args):
        print(f"Hello, {self.user_input.get()}!")


root = HelloWorld()
root.mainloop()
