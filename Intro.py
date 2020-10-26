from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def callback():
    print("Click")


def showcheckstate():
    print("Click")


root = Tk()

label1 = ttk.Label(root, text = "Hello, Tkinter").pack(padx = 10, pady = 10)

button = ttk.Button(root, text = "Click Me")
button.pack(padx = 10, pady = 10)
# Assign the procedure 'callback', defined above, to the button - Executed when clicked.
button.config(command = callback)
# Disable the button
button.state(['disabled'])
#Check if the button is disabled
print(button.instate(['disabled']))
# Enable the button
button.state(['!disabled'])
#Check if the button is disabled
print(button.instate(['disabled']))

# Create a Checkbox
checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
checkbutton.pack(padx = 10, pady = 10)
# Assign a procedure
checkbutton.config(command = showcheckstate)

# Create a StringVar variable and assign it to the Checkbox
spam = StringVar
checkbutton.config(variable = spam, onvalue = "Spam is ON", offvalue = "Spam is OFF")

breakfast = StringVar

ttk.Radiobutton(root, text= "Option 1", variable = breakfast, value = "OPT1").pack(padx = 10, pady = 10)
ttk.Radiobutton(root, text= "Option 2", variable = breakfast, value = "OPT2").pack(padx = 10, pady = 10)
ttk.Radiobutton(root, text= "Option 2", variable = breakfast, value = "OPT3").pack(padx = 10, pady = 10)

entry = ttk.Entry(root, width = 30).pack()

month = StringVar()

combobox = ttk.Combobox(root, textvariable = month)
combobox.pack(pady = 10)
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr'))

year = StringVar
spinyear = Spinbox(root, from_ = 1990, to = 2020, textvariable = year)
#spinyear = ttk.Spinbox(root, textvariable = year)
spinyear.pack(pady = 10)
#spinyear.config(values = ('1', '2', '3', '4'))

# Progress bar
progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack(pady = 10)

value = DoubleVar
progressbar.config(variable = value)
scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.0, to = 11.0)
scale.pack(pady = 10)

#Text Widget
text = Text(root, width = 40, height = 10)
text.pack()
text.config(wrap = 'word')

treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('', '0', 'item1', text = 'Alpha')
treeview.insert('', '1', 'item2', text = 'Beta')
treeview.insert('', 'end', 'item3', text = 'Charlie')
logo_S = PhotoImage(file = 'C:\\Users\PHIND5\IdeaProjects\Python\TKINTER\Exercise Files\Ex_Files_Python_GUI_Dev_Tkinter\Exercise Files\Ch05\python_logo.gif').subsample(10,10)
logo = PhotoImage(file = 'C:\\Users\PHIND5\IdeaProjects\Python\TKINTER\Exercise Files\Ex_Files_Python_GUI_Dev_Tkinter\Exercise Files\Ch05\python_logo.gif')

treeview.insert('item2', 'end', 'python', text = 'Pyton', image = logo_S)

treeview.config(columns = 'Version')
treeview.column('Version', width = 50, anchor = 'center')
treeview.column('#0', width = 150)
treeview.heading('Version', text = 'Ver')
treeview.set('python', 'Version', '3.4.1')

# Menus
root.option_add('#tearOff', False)
menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
menubar.add_cascade(menu = file, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')

canvas = Canvas(root)
canvas.pack()
canvas.config(width = 640, height = 480)
# Draw a line
line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
canvas.itemconfigure(line, fill = 'green')
print(canvas.coords(line))
canvas.coords(line, 0, 0, 320, 240, 640, 0)
canvas.itemconfigure(line, smooth = True)
canvas.itemconfigure(line, splinesteps = 3)

# Draw a rectangle
rect = canvas.create_rectangle(160, 120,480,360)
# Fill it
canvas.itemconfigure(rect, fill = 'yellow')

# Draw an oval
oval = canvas.create_oval(160, 120, 480, 360)

# Draw an arc - Defaults to a 90 Degree arc
arc = canvas.create_arc(160, 1, 480, 240)
# Configure the arc to start at 0 and 'extent' to 180 - also fill it with green
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')

# Create a polygon (nu,ber of vertices is controlled by the number of coordinate pairs you specify
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')

# Add text to the canvas
text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

# Add an image
image = canvas .create_image(320, 240, image = logo)

# Add a widget (e.g. a button)
button = Button(canvas, text = 'Click Me')
canvas.create_window(320, 60, window = button)

# Tag items on the canvas
canvas.itemconfigure(rect, tag = ('shape'))
canvas.itemconfigure(oval, tag = ('shape', 'round'))

# Use the tags to modify attributes
canvas.itemconfigure('shape', fill = 'grey')
# Display the tags associated with an item
print(canvas.gettags(oval))

messagebox.showinfo(title = 'WARNING', message = 'Don"t press this button again!')

root.mainloop()


