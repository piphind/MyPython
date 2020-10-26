from tkinter import *
from tkinter import ttk
root = Tk()
button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')
button1.pack()
button2.pack()

style = ttk.Style()
style.theme_use('winnative')
style.theme_use('clam')
style.theme_use('alt')
style.theme_use('default')
style.theme_use('classic')
style.theme_use('vista')
style.theme_use('xpnative')



root.mainloop()
