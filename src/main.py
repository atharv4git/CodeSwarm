import time, socket, sys
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("800x800")

var = tk.StringVar()
entry = ttk.Entry(textvariable=var)
entry.pack()

textBox = tk.Text()
textBox.pack()


# Define a function to update the text in the Text widget
def update_text(*args):
    text = var.get()  # Get the current value of the StringVar
    textBox.delete("1.0", tk.END)  # Clear the Text widget
    textBox.insert(tk.END, text)  # Insert the new text into the Text widget


# Bind the <<Modified>> event of the StringVar to the update_text function
var.trace_add("write", update_text)

window.mainloop()
