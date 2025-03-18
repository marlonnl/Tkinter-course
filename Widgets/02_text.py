import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Text example")

text = tk.Text(root, height=8)
text.pack()

# inserting
# "LINE.CHR"
text.insert("1.0", "Entering this text on the first line at 0 chr.")

# disabling
# text["state"] = "disable"

# getting data from text
text_data = text.get("1.2", "end")
print(text_data)

root.mainloop()
