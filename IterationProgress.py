import datetime
from datetime import timedelta


def get_date_components(indate):
    fwday = indate.strftime("%a")
    fday = indate.strftime("%d")
    fmonth = indate.strftime("%b")
    fyear = indate.strftime("%y")
    return {'fwday': fwday, 'fday': fday, 'fmonth': fmonth, 'fyear': fyear}

iteration_start_date = datetime.datetime(2020, 9, 17)
next_launch_date = datetime.datetime(2020, 10, 25)

todays_date = datetime.datetime.now()
days_remaining = next_launch_date - todays_date

iteration_date_list = [iteration_start_date]
iteration_date_list.append(iteration_start_date + timedelta(days=1))
iteration_date_list.append(iteration_start_date + timedelta(days=4))
iteration_date_list.append(iteration_start_date + timedelta(days=5))
iteration_date_list.append(iteration_start_date + timedelta(days=6))
iteration_date_list.append(iteration_start_date + timedelta(days=7))
iteration_date_list.append(iteration_start_date + timedelta(days=8))
iteration_date_list.append(iteration_start_date + timedelta(days=11))
iteration_date_list.append(iteration_start_date + timedelta(days=12))
iteration_date_list.append(iteration_start_date + timedelta(days=13))

print(" ++ ITERATION PROGRESS ++")

for day in range(10):
    date_component = get_date_components(iteration_date_list[day])
    if day == 0:
        print(" =====================================")
        print(" Iteration Start Date | " + date_component["fwday"] + " " + date_component["fday"] + " " + date_component["fmonth"] + " " + date_component["fyear"])
    elif day == 9:
        print(" -------------------------------------")
        print(" Iteration End Date   | " + date_component["fwday"] + " " + date_component["fday"] + " " + date_component["fmonth"] + " " + date_component["fyear"])
    else:
        print(" -------------------------------------")
        print("                      | " + date_component["fwday"] + " " + date_component["fday"] + " " + date_component["fmonth"] + " " + date_component["fyear"])
print(" =====================================")
print()
print(" Next launch date: 25/26 October in T - " + str(days_remaining.days) + " days and counting")
print()
input(" Done?")
