from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
import datetime
from playsound import playsound


def determine_current_iteration():
    day_of_iteration = ''
    found_iteration = ''
    func_current_date = datetime.date.today()
    for x in iteration.values():
        dictionary_entry_end = datetime.date(x["endyear"], x["endmonth"], x["endday"])
        dictionary_entry_start = datetime.date(x["startyear"], x["startmonth"], x["startday"])
        if func_current_date <= dictionary_entry_end:
            found_iteration = x["name"]
            true_day_of_iteration = func_current_date - dictionary_entry_start
            if true_day_of_iteration.days < 3:
                day_of_iteration = true_day_of_iteration.days + 1
            elif true_day_of_iteration.days < 9:
                day_of_iteration = true_day_of_iteration.days - 1
            else:
                day_of_iteration = true_day_of_iteration.days - 3
            break
    return found_iteration, day_of_iteration


def thank_team_member(name):
    message_string = ("And now a word from our\nBUSINESS OWNER,\nMr " + name + ".")
    messagebox.showinfo(title="BUSINESS OWNER", message=message_string)


def boss_window():
    popup = Toplevel(root)
    popup.title('THE BOSS')
    popup.geometry('450x450+2500+300')
    label1 = ttk.Label(popup)
    label1.config(text='TEST')
    danbangimg = PhotoImage(file='C://Users/PHIND5/IdeaProjects/Python/The Basics/Basics/Images/Dan Bang.png')
    label1.img = danbangimg
    label1.config(image=label1.img)
    label1.pack()
    b1 = ttk.Button(popup, text='OK', command=popup.destroy)
    b1.pack()
    playsound('applause6.mp3')
    popup.mainloop()


root = Tk()
root.title('Zephyr Stand-up Rota')
root.geometry('300x1200+0+0')
root.configure(background='#425968')

Zephyr = [["Dan Allenby", False], ["Ravi Shankar", False], ["Prahlad Swamy", False],
          ["Mark Gaywood", False], ["Mel Cooper", False], ["Yemi Lalude", False],
          ["Paul Wallis", False], ["Theo Brown", False], ["Herwig Mueller", False],
          ["David Brighton", False], ["Priya Nair", False],
          ["John LeDrew", False], ["Jon Penny", False], ["Corey Buffham", False]]

iteration = {
    "2020 R1.1": {"name": "2020 R1.1", "startyear": 2020, "startmonth": 1, "startday": 9, "endyear": 2020,
                  "endmonth": 1, "endday": 22},
    "2020 R1.2": {"name": "2020 R1.2", "startyear": 2020, "startmonth": 1, "startday": 23, "endyear": 2020,
                  "endmonth": 2, "endday": 5},
    "2020 R2.1": {"name": "2020 R2.1", "startyear": 2020, "startmonth": 2, "startday": 6, "endyear": 2020,
                  "endmonth": 2, "endday": 19},
    "2020 R2.2": {"name": "2020 R2.2", "startyear": 2020, "startmonth": 2, "startday": 20, "endyear": 2020,
                  "endmonth": 3, "endday": 4},
    "2020 R3.1": {"name": "2020 R3.1", "startyear": 2020, "startmonth": 3, "startday": 5, "endyear": 2020,
                  "endmonth": 3, "endday": 18},
    "2020 R3.2": {"name": "2020 R3.2", "startyear": 2020, "startmonth": 3, "startday": 19, "endyear": 2020,
                  "endmonth": 4, "endday": 1},
    "2020 R4.1": {"name": "2020 R4.1", "startyear": 2020, "startmonth": 4, "startday": 2, "endyear": 2020,
                  "endmonth": 4, "endday": 15},
    "2020 R4.2": {"name": "2020 R4.2", "startyear": 2020, "startmonth": 4, "startday": 16, "endyear": 2020,
                  "endmonth": 4, "endday": 29},
    "2020 R5.1": {"name": "2020 R5.1", "startyear": 2020, "startmonth": 4, "startday": 30, "endyear": 2020,
                  "endmonth": 5, "endday": 13},
    "2020 R5.2": {"name": "2020 R5.2", "startyear": 2020, "startmonth": 5, "startday": 14, "endyear": 2020,
                  "endmonth": 5, "endday": 27},
    "2020 R6.1": {"name": "2020 R6.1", "startyear": 2020, "startmonth": 5, "startday": 28, "endyear": 2020,
                  "endmonth": 6, "endday": 10},
    "2020 R6.2": {"name": "2020 R6.2", "startyear": 2020, "startmonth": 6, "startday": 11, "endyear": 2020,
                  "endmonth": 6, "endday": 24},
    "2020 R7.1": {"name": "2020 R7.1", "startyear": 2020, "startmonth": 6, "startday": 25, "endyear": 2020,
                  "endmonth": 7, "endday": 8},
    "2020 R7.2": {"name": "2020 R7.2", "startyear": 2020, "startmonth": 7, "startday": 9, "endyear": 2020,
                  "endmonth": 7, "endday": 22},
    "2020 R8.1": {"name": "2020 R8.1", "startyear": 2020, "startmonth": 7, "startday": 23, "endyear": 2020,
                  "endmonth": 8, "endday": 5},
    "2020 R8.2": {"name": "2020 R8.2", "startyear": 2020, "startmonth": 8, "startday": 6, "endyear": 2020,
                  "endmonth": 8, "endday": 19},
    "2020 R9.1": {"name": "2020 R9.1", "startyear": 2020, "startmonth": 8, "startday": 20, "endyear": 2020,
                  "endmonth": 9, "endday": 2},
    "2020 R9.2": {"name": "2020 R9.2", "startyear": 2020, "startmonth": 9, "startday": 3, "endyear": 2020,
                  "endmonth": 9, "endday": 16},
    "2020 R10.1": {"name": "2020 R10.1", "startyear": 2020, "startmonth": 9, "startday": 17, "endyear": 2020,
                   "endmonth": 9, "endday": 30},
    "2020 R10.2": {"name": "2020 R10.2", "startyear": 2020, "startmonth": 10, "startday": 1, "endyear": 2020,
                   "endmonth": 10, "endday": 14},
    "2020 R11.1": {"name": "2020 R11.1", "startyear": 2020, "startmonth": 10, "startday": 15, "endyear": 2020,
                   "endmonth": 10, "endday": 28},
    "2020 R11.2": {"name": "2020 R11.2", "startyear": 2020, "startmonth": 10, "startday": 29, "endyear": 2020,
                   "endmonth": 11, "endday": 11},
    "2020 R12.1": {"name": "2020 R12.1", "startyear": 2020, "startmonth": 11, "startday": 12, "endyear": 2020,
                   "endmonth": 11, "endday": 25},
    "2020 R12.2": {"name": "2020 R12.2", "startyear": 2020, "startmonth": 11, "startday": 26, "endyear": 2020,
                   "endmonth": 12, "endday": 9},
    "2020 R13.1": {"name": "2020 R13.1", "startyear": 2020, "startmonth": 12, "startday": 10, "endyear": 2020,
                   "endmonth": 12, "endday": 23},
    "2020 R13.2": {"name": "2020 R13.2", "startyear": 2020, "startmonth": 12, "startday": 24, "endyear": 2021,
                   "endmonth": 1, "endday": 6}
}

# Call the function to determine the current iteration and how many days we are into it.
current_iteration, iteration_day = determine_current_iteration()

# Build a displayable Iteration Start Date
iteration_start_date = datetime.datetime((iteration[current_iteration]["startyear"]),
                                         (iteration[current_iteration]["startmonth"]),
                                         (iteration[current_iteration]["startday"]))
display_iteration_start_day_name = (iteration_start_date.strftime("%a"))
display_iteration_start_day = (iteration_start_date.strftime("%d"))
display_iteration_start_month = (iteration_start_date.strftime("%b"))
display_iteration_start_year = (iteration_start_date.strftime("%Y"))
display_iteration_start_date = display_iteration_start_day_name + " " + \
                               display_iteration_start_day + " " + \
                               display_iteration_start_month + " " + \
                               display_iteration_start_year

# Build a displayable Iteration End Date
iteration_end_date = datetime.datetime((iteration[current_iteration]["endyear"]),
                                       (iteration[current_iteration]["endmonth"]),
                                       (iteration[current_iteration]["endday"]))
display_iteration_end_day_name = (iteration_end_date.strftime("%a"))
display_iteration_end_day = (iteration_end_date.strftime("%d"))
display_iteration_end_month = (iteration_end_date.strftime("%b"))
display_iteration_end_year = (iteration_end_date.strftime("%Y"))
display_iteration_end_date = display_iteration_end_day_name + " " + \
                             display_iteration_end_day + " " + \
                             display_iteration_end_month + " " + \
                             display_iteration_end_year

# Build a displayable current date
current_date = datetime.datetime.now()
display_today_day_name = (current_date.strftime("%a"))
display_today_day = (current_date.strftime("%d"))
display_today_month = (current_date.strftime("%b"))
display_today_year = (current_date.strftime("%Y"))
display_today = display_today_day_name + " " + \
                display_today_day + " " + \
                display_today_month + " " + \
                display_today_year

# Create the frames for each section
iteration_frame = ttk.LabelFrame(root, height=100, width=50, text='Iteration')
iteration_frame.config(padding=(5, 5))
dev_team_frame = ttk.LabelFrame(root, height=100, width=50, text='Development Team')
dev_team_frame.config(padding=(5, 5))
product_owners_frame = ttk.LabelFrame(root, height=100, width=50, text='Product Owners')
product_owners_frame.config(padding=(5, 5))
business_owners_frame = ttk.LabelFrame(root, height=100, width=50, text='Business Owner')
business_owners_frame.config(padding=(5, 5))
boss_frame = ttk.LabelFrame(root, height=100, width=50, text='The Boss')
boss_frame.config(padding=(5, 5))
product_manager_frame = ttk.LabelFrame(root, height=100, width=50, text='Product Manager')
product_manager_frame.config(padding=(5, 5))

# Create Styles
style = ttk.Style()
style.configure('TLabel', background='#425968', foreground='white')
style.configure('TLabelframe', background='#425968')
style.configure('TLabelframe.Label', background='#425968', foreground='yellow')
style.configure('TCheckbutton', background='#425968', foreground='white')

# Generate and display a random list for the Development Team
i = 1
dev = {}
for y in range(15):
    dev[y] = BooleanVar()
    dev[y].set(False)
while i < 15:
    ind = randint(0, 13)
    if Zephyr[ind][1] is False:
        if i < 10:
            txt = " " + str(i) + ") " + str(Zephyr[ind][0])
        else:
            txt = str(i) + ") " + str(Zephyr[ind][0])
        checkbutton = ttk.Checkbutton(dev_team_frame, text=txt, var=dev[i])
        checkbutton.config(width=20)
        checkbutton.grid(row=i-1, column=0)
        status = StringVar()
        combobox = ttk.Combobox(dev_team_frame, textvariable=status)
        combobox.grid(row=i-1, column=1)
        combobox.config(values=('Holiday', 'N/A'))
        combobox.config(width=10)
        Zephyr[ind][1] = True
        i = i + 1
dev_team_frame.pack()

# Display the list of Product Owners
po1 = BooleanVar()
po1.set(False)
po2 = BooleanVar()
po2.set(False)
checkbutton = ttk.Checkbutton(product_owners_frame, text='15) Caroline Apicella', var=po1)
checkbutton.config(width=20)
checkbutton.grid(row=0, column=0)
checkbutton = ttk.Checkbutton(product_owners_frame, text='16) Tricky Davies', var=po2)
checkbutton.config(style='POs.TCheckbutton')
checkbutton.config(width=20)
checkbutton.grid(row=1, column=0)
status1 = StringVar()
status2 = StringVar()
combobox = ttk.Combobox(product_owners_frame, textvariable=status1)
combobox.grid(row=0, column=1)
combobox.config(values=('Holiday', 'N/A'))
combobox.config(width=10)
combobox = ttk.Combobox(product_owners_frame, textvariable=status2)
combobox.grid(row=1, column=1)
combobox.config(values=('Holiday', 'N/A'))
combobox.config(width=10)
product_owners_frame.pack()

# Display the list of Business Owners
bo1 = BooleanVar()
bo1.set(False)
# Checkbutton = ttk.Checkbutton(BOs, text='17) Mike Manchee', var=bo1,
# command = lambda: thank_team_member('Mike Manchee'))
checkbutton = ttk.Checkbutton(business_owners_frame, text='17) Mike Manchee', var=bo1)

checkbutton.config(width=20)
checkbutton.grid(row=0, column=0)
status = StringVar()
combobox = ttk.Combobox(business_owners_frame, textvariable=status)
combobox.grid(row=0, column=1)
combobox.config(values=('Holiday', 'N/A'))
combobox.config(width=10)
business_owners_frame.pack()

# Display the list of Bosses
boss1 = BooleanVar()
boss1.set(False)
checkbutton = ttk.Checkbutton(boss_frame, text='18) Dan Gittins', var=boss1)
checkbutton.config(width=20)
checkbutton.grid(row=0, column=0)
status = StringVar()
combobox = ttk.Combobox(boss_frame, textvariable=status)
combobox.grid(row=0, column=1)
combobox.config(values=('Holiday', 'N/A'))
combobox.config(width=10)
boss_frame.pack()

# Display the list of Product Managers
pm1 = BooleanVar()
pm1.set(False)
checkbutton = ttk.Checkbutton(product_manager_frame, text='19) Phil Hind', var=pm1)
checkbutton.config(width=20)
checkbutton.grid(row=0, column=0)
status = StringVar()
combobox = ttk.Combobox(product_manager_frame, textvariable=status)
combobox.grid(row=0, column=1)
combobox.config(values=('Holiday', 'N/A'))
combobox.config(width=10)
product_manager_frame.pack()

# Display details for the current Iteration
label = ttk.Label(iteration_frame, text=current_iteration)
label.config(width=32)
label.config(justify=LEFT)
label.config(foreground='#2D96CD', font=('Arial', 10, 'bold'))
label.pack()
label = ttk.Label(iteration_frame, text="Start Date:  " + display_iteration_start_date)
label.config(width=38)
label.config(justify=LEFT)
label.pack()
label = ttk.Label(iteration_frame, text="Today:       " + display_today + " - Day " + str(iteration_day))
label.config(width=38)
label.config(justify=LEFT)
label.pack()
label = ttk.Label(iteration_frame, text="End Date:  " + display_iteration_end_date)
label.config(width=38)
label.config(justify=LEFT)
label.pack()
iteration_frame.pack()

# Setup and display the 5 Scrum Values
# Load the 5 Icons
courageimg = PhotoImage(file='C://Users/PHIND5/IdeaProjects/Python/The Basics/Basics/Images/Courage.png')
courageimg_s = courageimg.subsample(5, 5)
focusimg = PhotoImage(file='C://Users/PHIND5/IdeaProjects/Python/The Basics/Basics/Images/Focus.png')
focusimg_s = focusimg.subsample(5, 5)
commitment_img = PhotoImage(file='C://Users/PHIND5/IdeaProjects/Python/The Basics/Basics/Images/Commitment.png')
commitment_img_s = commitment_img.subsample(5, 5)
respect_img = PhotoImage(file='C://Users/PHIND5/IdeaProjects/Python/The Basics/Basics/Images/Respect.png')
respect_img_s = respect_img.subsample(5, 5)
openness_img = PhotoImage(file='C://Users/PHIND5/IdeaProjects/Python/The Basics/Basics/Images/Openness.png')
openness_img_s = openness_img.subsample(5, 5)

# Display the values
label = ttk.Label(root, text='SCRUM VALUES')
label.config(justify=LEFT)
label.config(font=('Ariel', 11, 'bold'))
label.pack()
label = ttk.Label(root, text='Courage')
label.config(justify=LEFT)
label.config(font=('Ariel', 10, 'bold'))
label.pack()
label = ttk.Label(root, text='Scrum Team members have courage to do the right thing and work on tough problems')
label.config(justify=LEFT)
label.config(wraplength=220)
label.config(image=courageimg_s)
label.config(compound='left')
label.pack()
label = ttk.Label(root, text='Focus')
label.config(justify=LEFT)
label.config(font=('Ariel', 10, 'bold'))
label.pack()
label = ttk.Label(root, text='Everyone focuses on the work of the Sprint and the goals of the Scrum Team')
label.config(justify=LEFT)
label.config(wraplength=220)
label.config(image=focusimg_s)
label.config(compound='left')
label.pack()
label = ttk.Label(root, text='Commitment')
label.config(justify=LEFT)
label.config(font=('Ariel', 10, 'bold'))
label.pack()
label = ttk.Label(root, text='People personally commit to achieving the goals of the Scrum Team')
label.config(justify=LEFT)
label.config(wraplength=220)
label.config(image=commitment_img_s)
label.config(compound='left')
label.pack()
label = ttk.Label(root, text='Respect')
label.config(justify=LEFT)
label.config(font=('Ariel', 10, 'bold'))
label.pack()
label = ttk.Label(root, text='Scrum Team members respect each other to be capable, independent people')
label.config(justify=LEFT)
label.config(wraplength=220)
label.config(image=respect_img_s)
label.config(compound='left')
label.pack()
label = ttk.Label(root, text='Openness')
label.config(justify=LEFT)
label.config(font=('Ariel', 10, 'bold'))
label.pack()
label = ttk.Label(root,
                  text='The Scrum Team and its stakeholders agree to be open about all '
                       'the work and the challenges with performing the work')
label.config(justify=LEFT)
label.config(wraplength=220)
label.config(image=openness_img_s)
label.config(compound='left')
label.pack()

root.mainloop()
