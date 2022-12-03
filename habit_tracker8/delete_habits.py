import sqlite3
import pandas as pd
from tabulate import tabulate


def delete_habits():
    """routine to delete habits from data base under MAIN MENU item [4]"""
    def menu3():
        """submenu structure from menu "delete habit(s)" """

        print("     MENU \"delete habit(s)\"")
        print("     Press [1] to delete a single habit and confirm with [Enter] or")
        print("     press [2] to delete all habits and confirm with [Enter] or")
        print("     press [3] to return to MAIN MENU and confirm with [Enter].")
        print("     Please note that this operation cannot be undone!")

    delete = 0
    while delete != 3:
        menu3()
        try:
            delete = int(
                input("     Please chose an option by pressing [1] - [3] and confirm afterwards with [Enter].\n"))
            # delete single habit:
            try:
                if delete == 1:
                    print("")
                    print("Here is a list of your habits:")
                    connection = sqlite3.connect("habits.db")
                    df_habits = pd.read_sql_query('select * from habits', connection)
                    print(tabulate(df_habits, headers='keys', tablefmt='psql'))
                    cursor = connection.cursor()
                    cursor.execute("SELECT habit FROM habits")
                    check_habit = input(
                        "Please type the name of the habit you want to delete and confirm with [Enter]:\n")
                    sql = "SELECT * FROM habits WHERE habit LIKE ?"
                    cursor.execute(sql, (check_habit,))
                    for data in cursor:
                        delete_exe = int(
                            input(f'Press [1] to delete or [2] to leave your habit \"{data[0]}\" without changes.\n'))
                        if delete_exe == 1:
                            print(f'You have deleted your habit \"{data[0]}\".')
                            cursor.execute('''DELETE FROM habits WHERE habit = ?''', (check_habit,))
                            connection.commit()
                            input("Please press [Enter] to go back to MENU \"delete habit(s)\".\n")
                        elif delete_exe == 2:
                            print("your habit \"{data[0]}\" was NOT deleted.")
                            input("Please press [Enter] to go back to MAIN \"delete habit(s)\".\n")
                        else:
                            input("Invalid input. Please press [Enter] to enter the MENU \"delete habit(s)\" "
                                  "and try again.\n")
                # delete all habits:
                elif delete == 2:
                    delete_exe = int(
                        input(f'Press [1] to delete or [2] to leave your habits without changes.\n'))
                    if delete_exe == 1:
                        connection = sqlite3.connect("habits.db")
                        connection.execute("DROP TABLE habits")
                        print("All data has been deleted.")
                        input("Please restart the application now to avoid errors!\n")
                    elif delete_exe == 2:
                        print("your habits were NOT deleted.")
                        input("Please press [Enter] to go back to MAIN \"delete habit(s)\".\n")
                    else:
                        input("Invalid input. Please press [Enter] to enter the MENU \"delete habit(s)\" "
                              "and try again.\n")
                elif delete == 3:
                    print("    No data has been deleted.\n")
                else:
                    print("Invalid input.")
                    input("No data has been deleted. Please press [Enter] to go back to MENU \"delete habit(s)\".\n")
            except ValueError:
                print("Invalid input.")
                input("No data has been deleted. Please press [Enter] to go back to MENU \"delete habit(s)\".\n")
        except ValueError:
            print("Invalid input.")
            input("No data has been deleted. Please press [Enter] to go back to MENU \"delete habit(s)\".\n")

