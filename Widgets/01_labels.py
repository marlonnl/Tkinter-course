import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

# Working with tkinter & images
from PIL import Image, ImageTk

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Labels with tkinter")

label = ttk.Label(root, text="Label example", padding=20)
# Adjusting font
# font=(Font name, Font size)
label.config(font=("Courier", 60))
label.pack()


image = Image.open("Widgets/logo.jpg").resize((64, 64))
photo = ImageTk.PhotoImage(image)

imageLabel = ttk.Label(root, image=photo, padding=5)
imageLabel.pack()


root.mainloop()
