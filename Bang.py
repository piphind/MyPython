from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
import datetime

root = Tk()
root.title('THE BOSS')
root.geometry('450x450+100+100')

danbangimg = PhotoImage(file='C://Users/PHIND5/IdeaProjects/Python/The Basics/Basics/Images/Dan Bang.png')

label = ttk.Label(root)
label.config(text = 'TEST')
label.img = danbangimg
label.config(image=label.img)
label.pack()
B1 = ttk.Button(root, text='OK')
B1.pack()

root.mainloop()
