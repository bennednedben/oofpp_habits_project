from datetime import date, timedelta
import sqlite3


def define_habit():
    """Defines a new habit under MAIN MENU item [1]."""

    print("Here is a list of your existing habits:")
    connection = sqlite3.connect("habits.db")
    cursor = connection.cursor()
    cursor.execute("SELECT habit FROM habits")
    hb = cursor.fetchall()
    print(hb)
    today = date.today()
    habit = str(input("Please name your new habit. The input is limited to 20 characters.\n"))
    period = input("Please press [1] if you want to set a daily task and [2] if you \n"
                   "want to set a weekly task and confirm afterwards with [Enter].\n")
    # daily task:
    if period == "1" and 20 >= len(habit) >= 1:
        try:
            period_day = int(input("Please state the number of days for your habit to run and press [Enter]\n"))
            end = today + timedelta(days=period_day) - timedelta(days=1)
            store = int(input("Press [1] to store your new habit or [2] to go back to menu\n"))
            if store == 1 and period_day >= 2:
                try:
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit, 'period_day': str(period_day), 'start_date': today, 'end': end,
                         'period': "daily", 'counter': "0", 'check_off': today, 'finished': 'XXX'})
                    connection.commit()
                    print(f'You has set your habit  \"{habit}\" to {period_day} days.')
                    print(f'Your habit ends on {end}.')
                    print(f'Your new habit \"{habit}\" has been stored.')
                    print("Please check off your habit today under MAIN MENU item [3].")
                    input("Press [Enter] to go back to MAIN MENU.\n")
                except sqlite3.IntegrityError:
                    print(f'The habit \"{habit}\" already exist.')
                    print("Please try again by using a different name for your new habit under MAIN MENU item [1]")
                    print(f'or delete your existing habit \"{habit}\" under MAIN MENU item [4].')
                    input("Press [Enter] to go back to menu.\n")
            elif store == 1 and period_day == 1:
                try:
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit, 'period_day': str(period_day), 'start_date': today, 'end': end,
                         'period': "daily", 'counter': "0", 'check_off': today, 'finished': 'XXX'})
                    connection.commit()
                    print(f'You has set your habit  \"{habit}\" to one day.')
                    print(f'Your habit ends today.')
                    print("Your new habit has \"{habit}\" been stored.")
                    print("Please check off your habit today under MAIN MENU item [3] to finish your habit.")
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
    elif period == "2" and 20 >= len(habit) >= 1:
        try:
            period_week = int(input("Please state the number of weeks for your habit to run and press [Enter]\n"))
            end = today + timedelta(weeks=period_week) - timedelta(days=1)
            period2 = today + timedelta(days=6)
            period_day = int(period_week * 7)
            store = int(input("Press [1] to store your new habit or [2] to go back to menu\n"))
            if store == 1 and period_week >= 2:
                try:
                    print(f'You has set your habit \"{habit}\" to {period_week} weeks.')
                    print(f'Your habit ends on {end}.')
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit, 'period_day': period_day, 'start_date': today, 'end': end,
                         'period': "weekly", 'counter': "0", 'check_off': today, 'finished': 'XXX'})
                    connection.commit()
                    print(f"Your new habit \"{habit}\" has been stored.")
                    print(f"Please check off your habit until {period2} under MAIN MENU item [3].")
                    input("Press [Enter] to go back to MAIN MENU.\n")
                except sqlite3.IntegrityError:
                    print(f'The habit \"{habit}\" already exist.')
                    print("Please try again by using a different name for your new habit under menu item 1")
                    print(f'or deleting your existing habit \"{habit}\" under MAIN MENU item [4].')
                    input("Press [Enter] to go back to menu.\n")
            elif store == 1 and period_week == 1:
                try:
                    print(f'You has set your habit  \"{habit}\" to one week.')
                    print(f'Your habit ends on {end}.')
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit, 'period_day': period_day, 'start_date': today, 'end': end,
                         'period': "weekly", 'counter': "0", 'check_off': today, 'finished': 'XXX'})
                    connection.commit()
                    print(f"Your new habit \"{habit}\" has been stored.")
                    print(f"Please check off your habit today or the next 6 days (until {period2}) "
                          f"under MAIN MENU item [3] to finish your habit.")
                    input("Press [Enter] to go back to MAIN MENU.\n")
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
    else:
        print("Something went wrong. Please note that the habit name is limited to 20 characters.")
        input("Please press [Enter] to return to the MAIN MENU and try again.\n")
