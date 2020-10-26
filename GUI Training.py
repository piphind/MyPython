from tkinter import *

root = Tk()


def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)


b1 = Button(root, text='Execute', command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(root, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(root, height=5, width=20)
t1.grid(row=1, column=1)

root.mainloop()
