import os
import datetime

"""
Datetime Reminder Script
   - Ask user for a date (YYYY-MM-DD).
   - Calculate how many days remain until that date.
   - If it is in the past, print "This date has already passed."
   - Otherwise, save the reminder into "reminders.txt" in format:
        "{date} -> {days_left} days left"
   - Append multiple reminders without overwriting.
"""

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

def dateReminder():
    # validate date format 
    while True:
        user_input = input("Enter a date (yyyy-mm-dd): ").strip()
        try:
            reminder_date = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")


    today = datetime.date.today()
    # check if date is in the past
    if reminder_date < today:
        print("This date has already passed.")
    else:
        days_left = (reminder_date - today).days
        
        reminders_file = os.path.join(BASE_DIR, "files/reminders.txt")
        print(f"Saving reminder to {reminders_file}")
        with open(reminders_file, "w") as file:
            file.write(f"{reminder_date} -> {days_left} days left" + "\n")
        print(f"Reminder saved: {reminder_date} -> {days_left} days left")

# dateReminder()
