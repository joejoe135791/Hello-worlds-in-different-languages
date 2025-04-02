import tkinter
from tkinter import filedialog, Tk, simpledialog, messagebox, ttk
from tkinter import *
from tkinter.ttk import *

root=Tk()
root.withdraw()
name = simpledialog.askstring("Enter Your Name", "What's your name?")
helloString = f"Hello, {name}!"
messagebox.showinfo(helloString, helloString)