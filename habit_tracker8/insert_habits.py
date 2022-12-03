from datetime import date, timedelta
import sqlite3
from sqlite3 import IntegrityError
import pandas as pd
from tabulate import tabulate


def insert_habits():
    """routine for inserting five predefined habits under MAIN MENU item [5]"""

    def menu3():
        print("     MENU \"Enter five predefined habits\".")
        print("     Please press [1] to insert five predefined habits to the database.")
        print("     Please press [2] to go back to MAIN MENU.")

    select2 = 0
    while select2 != 2:
        menu3()
        try:
            select2 = int(
                input(
                    "     Please chose an option by pressing number [1] - [2] and confirm with [Enter].\n"))
            # add 5 five predefined habits
            if select2 == 1:
                connection = sqlite3.connect("habits.db")
                cursor = connection.cursor()
                # Generation of dates depending on the current date
                today3 = date.today()
                one_day_later = today3 + timedelta(days=1)
                habit_1 = "drink"
                habit_2 = "walk"
                habit_3 = "fishing"
                habit_4 = "drive"
                habit_5 = "dance"
                try:
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit_1, 'period_day': int(1), 'start_date': today3, 'end': today3,
                         'period': "daily", 'counter': int(0), 'check_off': today3, 'finished': 'XXX'})
                    connection.commit()
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit_2, 'period_day': int(2), 'start_date': today3, 'end': one_day_later,
                         'period': "daily", 'counter': int(0), 'check_off': today3, 'finished': 'XXX'})
                    connection.commit()
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit_3, 'period_day': int(21), 'start_date': "2022-10-01", 'end': "2022-10-21",
                         'period': "weekly", 'counter': int(2), 'check_off': "broken habit",
                         'finished': "2022-11-03 01:27:58.540430"})
                    connection.commit()
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit_4, 'period_day': int(30), 'start_date': "2022-10-01", 'end': "2022-10-30",
                         'period': "daily", 'counter': int(30), 'check_off': "completed habit",
                         'finished': "2022-10-30 09:22:03.437935"})
                    connection.commit()
                    cursor.execute(
                        "INSERT INTO habits VALUES (:habit, :period_day, :start_date, :end, :period, :counter, "
                        ":check_off, :finished )",
                        {'habit': habit_5, 'period_day': int(35), 'start_date': "2022-10-01", 'end': "2022-10-28",
                         'period': "weekly", 'counter': int(2), 'check_off': "2022-10-15", 'finished': 'XXX'})
                    connection.commit()
                    print("     Five predefined habits has been added to the database.")
                    input("     Press [Enter] to go back to MENU \"Enter five predefined habits\".\n")
                except IntegrityError:
                    print("     You already inserted the five predefined habits")
                    print("     or one or more habits with the following name are in the data base:")
                    print(f'     \"{habit_1}\", \"{habit_2}\", \"{habit_3}\", \"{habit_4}\" or \"{habit_5}\"')
                    try:
                        show = int(input("     Press [1] to show the database or [2] to go back to MENU"
                                         "     \"Enter five predefined habits\".\n"))
                        if show == 1:
                            connection = sqlite3.connect("habits.db")
                            df_habits = pd.read_sql_query('select * from habits', connection)
                            print(tabulate(df_habits, headers='keys', tablefmt='psql'))
                            print("")
                            print("You can see a table of all created habits above.")
                            input("Please press [Enter] to go back to MENU \"Enter five predefined habits\".\n")
                        elif show == 2:
                            print("")
                        else:
                            print("")
                    except sqlite3.IntegrityError:
                        print("     Invalid input")
                        input("     Press [Enter] to go back to MENU \"Enter five predefined habits\".\n")
                    except ValueError:
                        print("     Invalid input")
                        input("     Press [Enter] to go back to MENU \"Enter five predefined habits\".\n")
        except IntegrityError:
            print("     Invalid input")
            input("     Press [Enter] to go back to MENU \"Enter five predefined habits\".\n")
        except ValueError:
            print("     Invalid input")
            input("     Press [Enter] to go back to MENU \"Enter five predefined habits\".\n")
