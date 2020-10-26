from tkinter import *
from tkinter import ttk
import BookStore_be

root = Tk()

# Labels
ttk.Label(root, text='Title').grid(row=0, column=0)
ttk.Label(root, text='Author').grid(row=0, column=2)
ttk.Label(root, text='Year').grid(row=1, column=0)
ttk.Label(root, text='ISBN').grid(row=1, column=2)

# Entry Fields
title_entry = StringVar()
title = ttk.Entry(root, width=20, textvariable=title_entry).grid(row=0, column=1)
author_entry = StringVar()
author = ttk.Entry(root, width=20, textvariable=author_entry).grid(row=0, column=3)
year_entry = StringVar()
year = ttk.Entry(root, width=20, textvariable=year_entry).grid(row=1, column=1)
isbn_entry = StringVar()
isbn = ttk.Entry(root, width=20, textvariable=isbn_entry).grid(row=1, column=3)

# Buttons
view_all_btn = ttk.Button(root, text='View All', width=12).grid(row=2, column=3)
search_entry_btn = ttk.Button(root, text='Search Entry', width=12).grid(row=3, column=3)
add_entry_btn = ttk.Button(root, text='Add Entry', width=12).grid(row=4, column=3)
update_selected_btn = ttk.Button(root, text='Update Selected', width=12).grid(row=5, column=3)
delete_selected_btn = ttk.Button(root, text='Delete Selected', width=12).grid(row=6, column=3)
close_btn = ttk.Button(root, text='Close', width=12).grid(row=7, column=3)

# Text
display_listbox = Listbox(root, width=40, height=10)
display_listbox.grid(row=2, column=0, columnspan=2, rowspan=6)

# Scroll bar for the listbox
sb1 = Scrollbar(root)
sb1.grid(row=2, column=2, rowspan=6)
display_listbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=display_listbox.yview)

root.mainloop()
