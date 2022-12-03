import sqlite3
from datetime import date, timedelta, datetime
import pandas as pd
from tabulate import tabulate


def check_off_habits():
    """routine to check off habits under MAIN MENU item [3]"""
    print("")
    connection = sqlite3.connect("habits.db")
    cursor = connection.cursor()
    df_habits = pd.read_sql_query('select * from habits', connection)
    print(tabulate(df_habits, headers='keys', tablefmt='psql'))
    print("You can see a table of all created habits above.")
    check_habit = input("Please typ one of the above names of the habit (correctly) you want to check-off:\n")
    sql = "SELECT * FROM habits WHERE habit LIKE ?"
    cursor.execute(sql, (check_habit,))
    # time variables from six days ago over today to seven days later:
    today = date.today()
    one_day_ago = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)
    three_days_ago = today - timedelta(days=3)
    four_days_ago = today - timedelta(days=4)
    five_days_ago = today - timedelta(days=5)
    six_days_ago = today - timedelta(days=6)
    one_day_later = today + timedelta(days=1)
    two_days_later = today + timedelta(days=2)
    three_days_later = today + timedelta(days=3)
    four_days_later = today + timedelta(days=4)
    five_days_later = today + timedelta(days=5)
    six_days_later = today + timedelta(days=6)
    seven_days_later = today + timedelta(days=7)
    today2 = str(today)
    one = str(one_day_ago)
    two = str(two_days_ago)
    three = str(three_days_ago)
    four = str(four_days_ago)
    five = str(five_days_ago)
    six = str(six_days_ago)
    one_l = str(one_day_later)
    two_l = str(two_days_later)
    three_l = str(three_days_later)
    four_l = str(four_days_later)
    five_l = str(five_days_later)
    six_l = str(six_days_later)
    seven_l = str(seven_days_later)
    for data in cursor:
        # check off a daily habit:
        checked_off = datetime.strptime(data[6], '%Y-%m-%d') + timedelta(days=7)
        checked_off2 = checked_off.strftime('%Y-%m-%d')
        checked_off3 = datetime.date(checked_off)
        if data[4] == "daily":
            if data[6] == "broken habit":
                print("You already has broken your habit.")
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[6] == "completed habit":
                print("You already has completed your habit.")
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[2] == today2 and data[3] == today2:
                counter2 = int(data[5]) + 1
                today3 = datetime.today()
                print(f'Congratulations: You have successfully completed the habit \"{data[0]}\".')
                cursor.execute('''UPDATE habits SET checked_off = "completed habit" WHERE habit = ?''', (data[0],))
                cursor.execute('''UPDATE habits SET counter = ? WHERE habit = ?''', (counter2, data[0],))
                cursor.execute('''UPDATE habits SET finished = ? WHERE habit = ?''', (today3, data[0],))
                connection.commit()
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[2] == today2 and data[5] == 0:
                counter2 = int(data[5]) + 1
                cursor.execute('''UPDATE habits SET checked_off = ? WHERE habit = ?''', (one_l, data[0],))
                cursor.execute('''UPDATE habits SET counter = ? WHERE habit = ?''', (counter2, data[0],))
                connection.commit()
                print(f'You have successfully checked-off your daily habit \"{data[0]}\".')
                print("Please come back tomorrow.")
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[3] == today2 and data[6] == today2:
                counter2 = int(data[5]) + 1
                today3 = datetime.today()
                print(f'Felicitations: You have successfully completed the habit \"{data[0]}\".')
                cursor.execute('''UPDATE habits SET checked_off = "completed habit" WHERE habit = ?''', (data[0],))
                cursor.execute('''UPDATE habits SET counter = ? WHERE habit = ?''', (counter2, data[0],))
                cursor.execute('''UPDATE habits SET finished = ? WHERE habit = ?''', (today3, data[0],))
                connection.commit()
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[6] == one_l:
                print("You have already checked-off your daily habit today.")
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[6] == today2:
                counter2 = int(data[5]) + 1
                cursor.execute('''UPDATE habits SET checked_off = ? WHERE habit = ?''', (today2, data[0],))
                cursor.execute('''UPDATE habits SET counter = ? WHERE habit = ?''', (counter2, data[0],))
                connection.commit()
                print(f'You have successfully checked-off your daily habit \"{data[0]}\".')
                input("Please press [Enter] to go back to MAIN MENU.\n")
            else:
                today3 = datetime.today()
                print(f'Your habit was set to {data[4]} check-off.')
                print(f'You have forgotten to check off your habit at {data[6]}.')
                print("Sorry, but you have broken your habit")
                cursor.execute('''UPDATE habits SET checked_off = "broken habit" WHERE habit = ?''', (data[0],))
                cursor.execute('''UPDATE habits SET finished = ? WHERE habit = ?''', (today3, data[0],))
                connection.commit()
                input("Please press [Enter] to go back to MAIN MENU.\n")
        # check off a weekly habit:
        elif data[4] == "weekly":
            if data[6] == "broken habit":
                print("You already has broken your habit.")
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[6] == "completed habit":
                print("You already has completed your habit.")
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[6] == one_l or data[6] == two_l or data[6] == three_l \
                    or data[6] == four_l or data[6] == five_l or data[6] == six_l or data[6] == seven_l:
                print("You have already checked-off your habit for this week.")
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[6] == today2 or data[6] == one or data[6] == two or data[6] == three or data[6] == four \
                    or data[6] == five or data[6] == six:
                counter2 = int(data[5]) + 1
                cursor.execute('''UPDATE habits SET checked_off = ? WHERE habit = ?''', (checked_off2, data[0],))
                cursor.execute('''UPDATE habits SET counter = ? WHERE habit = ?''', (counter2, data[0],))
                connection.commit()
                print(f'You have successfully checked-off your habit \"{data[0]}\".')
                print(f"Please check off your habit starting {checked_off2}.")
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif data[3] == today2 or data[3] == one_l or data[3] == two_l or data[3] == three_l \
                    or data[3] == four_l or data[3] == five_l or data[3] == six_l:
                counter2 = int(data[5]) + 1
                today3 = datetime.today()
                print(f'Congratulations: You have successfully completed your habit \"{data[0]}\".')
                cursor.execute('''UPDATE habits SET checked_off = "completed habit" WHERE habit = ?''', (data[0],))
                cursor.execute('''UPDATE habits SET counter = ? WHERE habit = ?''', (counter2, data[0],))
                cursor.execute('''UPDATE habits SET finished = ? WHERE habit = ?''', (today3, data[0],))
                connection.commit()
                input("Please press [Enter] to go back to MAIN MENU.\n")
            elif checked_off3 <= today:
                today3 = datetime.today()
                print(f'Your habit was set to {data[4]} check-off, but your last check-off was before {data[6]}.')
                print(f'Sorry, but you have broken your habit \"{data[0]}\".')
                cursor.execute('''UPDATE habits SET checked_off = "broken habit" WHERE habit = ?''', (data[0],))
                cursor.execute('''UPDATE habits SET finished = ? WHERE habit = ?''', (today3, data[0],))
                connection.commit()
                input("Please press [Enter] to go back to MAIN MENU.\n")
        else:
            print("Unexpected error. Please press [Enter] to go back to MAIN MENU.\n")
