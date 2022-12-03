import sqlite3
import pandas as pd
from tabulate import tabulate


connection = sqlite3.connect("habits.db")
cursor = connection.cursor()


def list_habits():
    """routine to list habits dependent on user input under MAIN MENU item [2]"""

    def menu2():
        """submenu structure from menu "existing habits" """
        print("     MENU \"existing habits\":")
        print("     Please press [1] to show the whole table.")
        print("     Please press [2] to show every successfully completed habit.")
        print("     Please press [3] to show every broken habit.")
        print("     Please press [4] to show every ongoing habit (which is not broken or completed).")
        print("     Please press [5] to show every daily habit.")
        print("     Please press [6] to show every weekly habit.")
        print("     Please press [7] to show most checked off habit.")
        print("     Please press [8] to show the longest habit.")
        print("     Please press [9] to show an overview.")
        print("     Please press [10] to go back to MAIN MENU.")

    def select_1():
        """show the whole table"""
        df_habits = pd.read_sql_query('select * from habits', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see a table of all created habits above.")
        input("Please press [Enter] to go back to MENU \"existing habits\".\n")

    def select_2():
        """show every completed habit"""
        df_habits = pd.read_sql_query('select * from habits WHERE checked_off = "completed habit"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see a table of all completed habits above.")
        input("Please press [Enter] to go back to MENU \"existing habits\".\n")

    def select_3():
        """show every broken habit"""
        df_habits = pd.read_sql_query('select * from habits WHERE checked_off = "broken habit"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see a table of all broken habits above.")
        input("Please press [Enter] to go back to MENU \"existing habits\".\n")

    def select_4():
        """show every ongoing habit"""
        df_habits = pd.read_sql_query('select * from habits WHERE finished = "XXX"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see a table of all ongoing habits above.")
        input("Please press [Enter] to go back to MENU \"existing habits\".\n")

    def select_5():
        """show every daily habit"""
        df_habits = pd.read_sql_query('select * from habits WHERE period = "daily"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see a table of all created daily habits above.")
        input("Please press [Enter] to go back to MENU \"existing habits\".\n")

    def select_6():
        """show every weekly habit"""
        df_habits = pd.read_sql_query('select * from habits WHERE period = "weekly"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see a table of all created weekly habits above.")
        input("Please press [Enter] to go back to MENU \"existing habits\".\n")

    def select_7():
        """show most checked off habit"""
        df_habits = pd.read_sql_query('SELECT habit, period_day, start_date, end_date, period, counter, checked_off, '
                                      'finished FROM habits WHERE counter = (SELECT MAX(counter) FROM habits)',
                                      connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see the habit, wich was checked of most often (highest counter value) above.")
        input("Press [Enter] to go back to MENU \"existing habits\".\n")

    def select_8():
        """show the longest habit"""
        df_habits = pd.read_sql_query('SELECT habit, period_day, start_date, end_date, period, counter, checked_off, '
                                      'finished FROM habits WHERE period_day = (SELECT MAX(period_day) FROM habits)',
                                      connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see the habit with the most days (maximum period_day) to run above.")
        input("Please press [Enter] to go back to MENU \"existing habits\".\n")

    def select_9():
        """show an overview"""
        print("You can see a table of all created habits below:")
        df_habits = pd.read_sql_query('select * from habits', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("")
        print("You can see a table of all completed habits below:")
        df_habits = pd.read_sql_query('select * from habits WHERE checked_off = "completed habit"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("")
        print("You can see a table of all broken habits below:")
        df_habits = pd.read_sql_query('select * from habits WHERE checked_off = "broken habit"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("")
        print("You can see a table of all ongoing habits below:")
        df_habits = pd.read_sql_query('select * from habits WHERE finished = "XXX"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("")
        print("You can see a table of all created daily habits below:")
        df_habits = pd.read_sql_query('select * from habits WHERE period = "daily"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("")
        print("You can see a table of all created weekly habits below:")
        df_habits = pd.read_sql_query('select * from habits WHERE period = "weekly"', connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("")
        print("You can see the habit, wich was checked of most often below:")
        df_habits = pd.read_sql_query('SELECT habit, period_day, start_date, end_date, period, counter, checked_off, '
                                      'finished FROM habits WHERE counter = (SELECT MAX(counter) FROM habits)',
                                      connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see the habit, wich was checked of most often (highest counter value) above.")
        print("")
        print("You can see the habit with the maximum days to run below:")
        df_habits = pd.read_sql_query('SELECT habit, period_day, start_date, end_date, period, counter, checked_off, '
                                      'finished FROM habits WHERE period_day = (SELECT MAX(period_day) FROM habits)',
                                      connection)
        print(tabulate(df_habits, headers='keys', tablefmt='psql'))
        print("You can see the habit with the most days to run above.")
        input("Please press [Enter] to go back to MENU \"existing habits\".\n")

    select = 0
    while select != 10:
        menu2()
        try:
            select = int(
                input("     Please chose an option by pressing [1] - [10] and confirm afterwards with [Enter].\n"))
            if select == 1:
                select_1()
            elif select == 2:
                select_2()
            elif select == 3:
                select_3()
            elif select == 4:
                select_4()
            elif select == 5:
                select_5()
            elif select == 6:
                select_6()
            elif select == 7:
                select_7()
            elif select == 8:
                select_8()
            elif select == 9:
                select_9()
        except ValueError:
            print("     Invalid input")
            input("     Press [Enter] to go back to MENU \"existing habits\".\n")
