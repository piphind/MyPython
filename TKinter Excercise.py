from tkinter import *

root = Tk()


def kg_converter():
    f_grams_out = float(kgs_in.get()) * 1000
    f_pounds_out = float(kgs_in.get()) * 2.20462
    f_ounces_out = float(kgs_in_value.get()) * 35.274
    grams_out.delete('0', END)
    grams_out.insert(END, f_grams_out)
    pounds_out.delete('0', END)
    pounds_out.insert(END, f_pounds_out)
    ounces_out.delete('0', END)
    ounces_out.insert(END, f_ounces_out)


Label(root, text='Kg').grid(row=0, column=0)
kgs_in_value = StringVar()
kgs_in = Entry(root, textvariable=kgs_in_value)
kgs_in.grid(row=0, column=1)
execute_button = Button(root, text='Execute', command=kg_converter)
execute_button.grid(row=0, column=3)

grams_out = Entry(root)
grams_out.grid(row=1, column=0)
pounds_out = Entry(root)
pounds_out.grid(row=1, column=1)
ounces_out = Entry(root)
ounces_out.grid(row=1, column=2)

root.mainloop()