from datetime import date
import sqlite3
from define_habits import define_habit
from list_habits import list_habits
from check_off_habits import check_off_habits
from delete_habits import delete_habits
from insert_habits import insert_habits
from help_habits import help_habits
from create_habits import create_habits

connection = sqlite3.connect("habits.db")
cursor = connection.cursor()


def create_table():
    """create table habits if not exists"""
    sql_habits = """
    CREATE TABLE IF NOT EXISTS habits (
    habit VARCHAR(20) UNIQUE, 
    period_day VARCHAR(6), 
    start_date DATE,
    end_date DATE,
    period VARCHAR(6),
    counter INTEGER,
    checked_off,
    finished DATE
    );"""

    cursor.execute(sql_habits)


def menu():
    """main menu that leads through the app"""

    print("MAIN MENU \"habit tracker\":")
    print("Press [1] to define a new habit.")
    print("Press [2] to list existing habits.")
    print("Press [3] to check-off an existing habit.")
    print("Press [4] to delete an existing habit or all habits.")
    print("Press [5] to add five predefined habits to the database.")
    print("Press [6] for help.")
    print("Press [7] to exit the program.")


# 7 exit program--------------------------------------------------------------------------------------------------------

command_1 = 0
while command_1 != 7:
    menu()
    create_table()
    try:
        command_1 = int(
            input("Please chose an option by pressing number [1] - [7] and confirm afterwards with [Enter].\n"))
    except ValueError:
        print("invalid input")
        command_1 = 0
        input("Press [Enter] to go back to menu.\n")
# 1 define a new habit -------------------------------------------------------------------------------------------------
    if command_1 == 1:
        define_habit()
# 2 list existing habits------------------------------------------------------------------------------------------------
    elif command_1 == 2:
        list_habits()
# 3 check-off an existing habit-----------------------------------------------------------------------------------------
    elif command_1 == 3:
        check_off_habits()
# 4 delete an existing habit--------------------------------------------------------------------------------------------
    elif command_1 == 4:
        delete_habits()
# 5 insert five predefined habits---------------------------------------------------------------------------------------
    elif command_1 == 5:
        insert_habits()
# 6 help----------------------------------------------------------------------------------------------------------------
    elif command_1 == 6:
        help_habits()
# 8 create specific habit--------------------------------------------------------------------------------------------
    elif command_1 == 8:
        create_habits()
# 7 exit the program----------------------------------------------------------------------------------------------------
print("Thank you for using the habit tracker app!")
cursor.close()
connection.close()
today4 = date.today()
print(f'Benjamin G. Borrmann, {today4}')
