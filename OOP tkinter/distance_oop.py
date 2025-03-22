import tkinter as tk
from tkinter import ttk

import tkinter.font as font


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance converter")

        font.nametofont("TkDefaultFont").configure(size=15)
        self.default_font = font.nametofont("TkDefaultFont")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Variables
        self.frames = dict()

        # Frames
        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        for FrameClass in (MetersToFeet, FeetToMeters):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        # Keybindings
        # ESC to exit
        self.bind("<Escape>", lambda _: self.destroy())

        self.show_frame(MetersToFeet)

    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()


class MetersToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        # Variables
        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        self.default_font = font.nametofont("TkDefaultFont")

        # Widgets
        meters_label = ttk.Label(self, text="Meters:")
        meters_label.grid(row=0, column=0, sticky="W")

        meters_input = ttk.Entry(
            self,
            width=10,
            textvariable=self.meters_value,
            font=(self.default_font, 15),
        )
        meters_input.grid(row=0, column=1, sticky="EW")
        meters_input.focus()

        feet_label = ttk.Label(self, text="Feet:")
        feet_label.grid(row=1, column=0, sticky="W")

        feet_display = ttk.Label(self, text="feet result", textvariable=self.feet_value)
        feet_display.grid(row=1, column=1, sticky="EW")

        calculate_btn = ttk.Button(self, text="Calculate", command=self.calculate)
        calculate_btn.grid(row=2, column=0, columnspan=2, sticky="EW")

        switch_page_btn = ttk.Button(
            self,
            text="Switch convertion",
            command=lambda: controller.show_frame(FeetToMeters),
        )
        switch_page_btn.grid(row=3, column=0, columnspan=2, sticky="EW")

        # winfo_children
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def calculate(self, *args):
        try:
            meters = float(self.meters_value.get())
            conversion = meters * 3.28084
            self.feet_value.set(f"{conversion:.3f}")

        # If button is pressed without any value yet
        except ValueError:
            pass


class FeetToMeters(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        # Variables
        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        self.default_font = font.nametofont("TkDefaultFont")

        # Widgets
        feet_label = ttk.Label(self, text="Feet:")
        feet_label.grid(row=0, column=0, sticky="W")

        feet_input = ttk.Entry(
            self,
            width=10,
            textvariable=self.feet_value,
            font=(self.default_font, 15),
        )
        feet_input.grid(row=0, column=1, sticky="EW")
        feet_input.focus()

        meters_label = ttk.Label(self, text="Meters:")
        meters_label.grid(row=1, column=0, sticky="W")

        meters_display = ttk.Label(
            self, text="meters result", textvariable=self.meters_value
        )
        meters_display.grid(row=1, column=1, sticky="EW")

        calculate_btn = ttk.Button(self, text="Calculate", command=self.calculate)
        calculate_btn.grid(row=2, column=0, columnspan=2, sticky="EW")

        switch_page_btn = ttk.Button(
            self,
            text="Switch convertion",
            command=lambda: controller.show_frame(MetersToFeet),
        )
        switch_page_btn.grid(row=3, column=0, columnspan=2, sticky="EW")

        # winfo_children
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            conversion = feet / 3.28084
            self.meters_value.set(f"{conversion:.3f}")

        # If button is pressed without any value yet
        except ValueError:
            pass


root = DistanceConverter()
root.mainloop()
