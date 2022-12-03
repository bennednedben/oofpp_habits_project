from datetime import timedelta, datetime
import sqlite3
from datetime import date


def create_habits():
    """Creates a new habit under hidden MAIN MENU item [8]."""
    print("Here is a list of your existing habits:")
    connection = sqlite3.connect("habits.db")
    cursor = connection.cursor()
    cursor.execute("SELECT habit FROM habits")
    hb = cursor.fetchall()
    print(hb)
    habit = str(input("Please name your new habit. The input is limited to 20 characters.\n"))
    period = int(input("Please press [1] if you want to set a daily task and [2] if you \n"
                       "want to set a weekly task and confirm afterwards with [Enter].\n"))
    today = date.today()
    one_day_ago = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)
    three_days_ago = today - timedelta(days=3)
    four_days_ago = today - timedelta(days=4)
    five_days_ago = today - timedelta(days=5)
    six_days_ago = today - timedelta(days=6)
    seven_days_ago = today - timedelta(days=7)
    eight_days_ago = today - timedelta(days=7)
    thirteen_days_ago = today - timedelta(days=13)
    fourteen_days_ago = today - timedelta(days=14)
    one_day_later = today + timedelta(days=1)
    two_days_later = today + timedelta(days=2)
    three_days_later = today + timedelta(days=3)
    four_days_later = today + timedelta(days=4)
    five_days_later = today + timedelta(days=5)
    six_days_later = today + timedelta(days=6)
    seven_days_later = today + timedelta(days=7)
    print("some data to copy:")
    print(fourteen_days_ago, "-14")
    print(thirteen_days_ago, "-13")
    print(eight_days_ago, "-8")
    print(seven_days_ago, "-7")
    print(six_days_ago, "-6")
    print(five_days_ago, "-5")
    print(four_days_ago, "-4")
    print(three_days_ago, "-3")
    print(two_days_ago, "-2")
    print(one_day_ago, "-1")
    print(today, "0")
    print(one_day_later, "1")
    print(two_days_later, "2")
    print(three_days_later, "3")
    print(four_days_later, "4")
    print(five_days_later, "5")
    print(six_days_later, "6")
    print(seven_days_later, "7")
    start_date3 = input("Please type a start date (YYYY-MM-DD)\n")
    checked_off3 = input("Please type a check off date (YYYY-MM-DD)\n")
    start_date4 = datetime.strptime(start_date3, '%Y-%m-%d')
    # daily task:
    if period == 1 and 20 >= len(habit) >= 1:
        try:
            period_day = int(input("Please state the number of days for your habit to run and press [Enter]\n"))
            print(f'You has set your habit  \"{habit}\" to {period_day} days.')
            end = start_date4 + timedelta(days=period_day) - timedelta(days=1)
            end2 = str(end)
            print(f'Your habit ends on {end2[0:10]}.')
            counter = 0
            store = int(input("Press [1] to store your new habit or [2] to go back to menu\n"))
            if store == 1 and period_day >= 1:
                try:
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit, 'period_day': period_day, 'start_date': start_date3, 'end': end2[0:10],
                         'period': "daily", 'counter': counter, 'check_off': checked_off3, 'finished': 'XXX'})
                    connection.commit()
                    print("Your new habit has been stored.")
                    print("Please check off your habit today under MAIN MENU item [3].")
                    input("Press [Enter] to go back to MAIN MENU.\n")
                except sqlite3.IntegrityError:
                    print(f'The habit \"{habit}\" already exist.')
                    print("Please try again by using a different name for your new habit under MAIN MENU item [1]")
                    print(f'or delete your existing habit \"{habit}\" under MAIN MENU item [4].')
                    input("Press [Enter] to go back to menu.\n")
            elif store == 1 and period_day <= 0:
                print("Invalid Input. The number of days for your habit to run must be greater than zero day!")
                input("Saving was aborted. Press [Enter] to go back to menu.\n")
            elif store == 2:
                print("")
        except ValueError:
            print("Invalid Input. The decimal number of days for your habit to run must be greater than 0 day!")
            input("Press [Enter] to go back to menu.\n")
            pass
    # weekly task:
    elif period == 2 and 20 >= len(habit) >= 1:
        try:
            period_week = int(input("Please state the number of weeks for your habit to run and press [Enter]\n"))
            print(f'You has set your habit  \"{habit}\" to {period_week} weeks.')
            end = start_date4 + timedelta(weeks=period_week) - timedelta(days=1)
            end2 = str(end)
            counter = 0
            period2 = start_date4 + timedelta(days=6)
            print(f'Your habit ends on {end2[0:10]}.')
            store = int(input("Press [1] to store your new habit or [2] to go back to menu\n"))
            if store == 1 and period_week >= 1:
                try:
                    period_day = int(period_week * 7)
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit, 'period_day': period_day, 'start_date': start_date3, 'end': end2[0:10],
                         'period': "weekly", 'counter': counter, 'check_off': checked_off3, 'finished': 'XXX'})
                    connection.commit()
                    print(f"Your new habit \"{habit}\" has been stored.")
                    print(f"Please check off your habit until {period2} under MAIN MENU item [3].")
                    input("Press [Enter] to go back to menu.\n")
                except sqlite3.IntegrityError:
                    print(f'The habit \"{habit}\" already exist.')
                    print("Please try again by using a different name for your new habit under menu item 1")
                    print(f'or deleting your existing habit \"{habit}\" under MAIN MENU item [4].')
                    input("Press [Enter] to go back to menu.\n")
            elif store == 1 and period_week <= 0:
                print("Invalid Input. The number of weeks for your habit to run must be greater than zero week!")
                input("Saving was aborted. Press [Enter] to go back to menu.\n")
            elif store == 2:
                print("")
        except ValueError:
            print("Invalid Input. The decimal number of weeks for your habit to run must be greater than 0 day!")
            input("Press [Enter] to go back to menu.\n")
    elif period != 1 or period != 2:
        print("Invalid input.")
        input("Please press [Enter] to return to the MAIN MENU and try again.\n")
    else:
        print("Something went wrong. Please note that the habit name is limited from 1 to 20 characters.")
        input("Please press [Enter] to return to the MAIN MENU and try again.\n")
