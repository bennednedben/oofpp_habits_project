def help_habits():
    """Offer a help menu under MAIN MENU item [6]."""
    def menu3():
        print("""        Welcome to HELP MENU:
        Please press [1] if you need help for menu item [1] (define a new habit)
        Please press [2] if you need help for menu item [2] (list existing habits)
        Please press [3] if you need help for menu item [3] (check-off an existing habit)
        Please press [4] if you need help for menu item [4] (delete an existing habit)
        Please press [5] if you need help for menu item [5] (add five predefined habits)
        Please press [6] to go back to MAIN MENU""")

    command_2 = 0
    while command_2 != 6:
        menu3()
        try:
            command_2 = int(
                input(
                    "            Please chose an option by pressing number [1] - [7] and confirm with [Enter].\n"))
        except ValueError:
            print("            invalid input")
            input("            Press [Enter] and try again.\n")
        if command_2 == 1:
            print("""            
            Under menu item [1] you can define a habit. First you will be asked to create a habit. 
            It is recommended to name your habit with a bullet point like "drinking", "walking 1000 steps" 
            or better "walking" because the input is limited to 20 characters.
            Next you will be prompted to choose a daily habit or a weekly habit. 
            If you select "weekly" you must check off your habit every week under menu item [3] starting with 
            the current week. If you choose a daily habit, you have to check off your habit
            until the last day of you habit (end_date).
            Finally, you will be asked to enter the number of weeks or days for your habit. For example, 
            if you enter the number 5 here, you will have to confirm this habit for the next 5 days or weeks 
            under menu item [3] if you want fulfill it (complete habit). 
            Once you forget this, your habit is considered to be "broken" (broken habit).
            A daily habit must be checked off for the first time on the same day it is created""")
            input("""            Please press [Enter] to return to the HELP MENU.\n""")

        elif command_2 == 2:
            print("""            
            The following menu structure is given under MAIN MENU item [2]:
            Please press [1] to show the whole table.
            Please press [2] to show every completed habit.
            Please press [3] to show every broken habit.
            Please press [4] to show every ongoing habit (which is not broken or completed).
            Please press [5] to show every daily habit.")
            Please press [6] to show every weekly habit.")
            Please press [7] to show most checked off habit.")
            Please press [8] to show the longest habit.")
            Please press [9] to show an overview.")
            Please press [10] to go back to MAIN MENU.")

            [1]
            A table of available habits is displayed under menu item [1]. 
            The table has the following columns:
            habit, period_day, start_date, end_date, period, counter, checked_off

            habit:          Name of your habit
            period_day:     total number of days of you habit
            start_date:     Day of submission for your habit
            end_date:       End day for your task
            period:         if daily:           please check off your habit under menu item [3] every day
                            if weekly:          please check off your habit under menu item [3] every week
            counter:        counts how many times they you have checked off.
                            the first check off is done automatically when creating the habit.
            checked_off:    Date:               Date of next check off if "period" is daily
                                                Date of next check off period if "period" is weekly
                            if broken habit:    your habit is already broken, because you check off outside 
                                                the period or after the end date
                            if completed habit: your habit is completed.
            finished:       Date and Time of when habit was broken or completed

            [2]
            A list of completed habits is displayed under menu item [2]. 
            The data of each record is enclosed in brackets. Each record has the following data: 
            habit, period_day, start_date, end_date, period, counter, checked_off, finished
            You can see a description of the individual data above.

            [3]
            A list of broken habits is displayed under menu item [3]. 
            The data of each record is enclosed in brackets. Each record has the following data: 
            habit, period_day, start_date, end_date, period, counter, checked_off, finished
            You can see a description of the individual data above.

            [4]
            A list of ongoing habits (which are not broken or completed) is displayed under menu item [4]. 
            The data of each record is enclosed in brackets. Each record has the following data: 
            habit, period_day, start_date, end_date, period, counter, checked_off, finished
            You can see a description of the individual data above.

            [5]
            A list of daily habit is displayed under menu item [5]. 
            The data of each record is enclosed in brackets. Each record has the following data: 
            habit, period_day, start_date, end_date, period, counter, checked_off, finished
            You can see a description of the individual data above.

            [6]
            A list of weekly habits is displayed under menu item [6]. 
            The data of each record is enclosed in brackets. Each record has the following data: 
            habit, period_day, start_date, end_date, period, counter, checked_off, finished
            You can see a description of the individual data above.

            [7]
            The most checked off habit is displayed under menu item 7 (highest counter value).
            The data of the record is enclosed in brackets. The record has the following data: 
            habit, period_day, start_date, end_date, period, counter, checked_off, finished
            You can see a description of the individual data above.

            [8]
            The longest habit is displayed under menu item 8 (maximum "period_day" value).
            The data of the record is enclosed in brackets. The record has the following data: 
            habit, period_day, start_date, end_date, period, counter, checked_off, finished
            You can see a description of the individual data above.

            [9]
            All tables previously described are displayed
            
            [10]
            Press [10] to go back to MAIN MENU
            """)
            input("""            Please press [Enter] to return to the HELP MENU.\n""")

        elif command_2 == 3:
            print("""            Under menu item [3] you have the opportunity to confirm your habit within 
            the period you specify. The first thing you should do is name your habit that you want to check off.
            Please pay attention to the correct spelling. The program will now determine whether you have already 
            completed or broken your habit and are within the period you set under MAIN MENU item [1].
            A summary of the changes made is displayed
            Depending on your input, the following entry is made in the "check-off" 
            column in the list under MAIN MENU item [2]:

            date            = next possible date of "check off" if period=daily
                            = first day of 7 for "check off" if period=weekly
            broken habit    = You checked off your habit outside the given period.
            completed habit = You have checked off every given period of your habit.
            
            Depending on your input, the following entry is made in the "finished" 
            column in the list under MAIN MENU item [2]:
            
            XXX             = your habit is not finished
            datetime        = your habit is finished

            !!! Check off your new daily habit on the same day you created it !!!
            !!! Check off your new weekly habit on the same week you created it !!!

            """)
            input("""            Please press to [Enter] return to the HELP MENU.\n""")

        elif command_2 == 4:
            print("""            the following menu will appear:

            MENU "delete habit(s)"
            Press [1] to delete a single habit and confirm with [Enter] or
            press [2] to delete all habits and confirm with [Enter] or
            press [3] to return to MAIN MENU and confirm with [Enter].
            Please note that this operation cannot be undone!

            [1]
            You will be prompted to name a habit from the list.
            Make sure you type the entry you want to delete from the list exactly.
            Press [1] to delete or [2] to leave your habit without changes.
            The operation cannot be undone!

            [2]
            Attention all data records will be deleted. This step cannot be undone!

            [3]
            Return to MAIN MENU

            """)
            input("""            Please press to [Enter] return to the HELP MENU.\n""")

        elif command_2 == 5:
            print("""                The following data is added to the database:
            +----+---------+--------------+--------------+------------+--------------+-----------+------------------+----------------------------+
            |    | habit   |   period_day | start_date   | end_date   | period       |   counter | checked_off      | finished                   |
            |----+---------+--------------+--------------+------------+--------------+-----------+------------------|----------------------------|
            |    | str     |        1 - ∞ | YYYY-MM-DD   | YYYY-MM-DD | daily/weekly |   1 - ∞   | YYYY-MM-DD       | YYYY-MM-DD HH:MM:SS.SSSSSS |
            |    |         |              |              |            |              |           | broken habit     |                            |
            |    |         |              |              |            |              |           | completed habit  |                            |
            +----+---------+--------------+--------------+------------+--------------+-----------+------------------+----------------------------+
            habit:          Name of your habit
            period_day:     total number of days of you habit
            start_date:     Day of submission for your habit
            end_date:       End day for your task
            period:         if daily:           please check off your habit under menu item [3] every day
                            if weekly:          please check off your habit under menu item [3] every week
            counter:        counts how many times they you have checked off.
                            the first check off is done automatically when creating the habit.
            checked_off=    if Date:            Date of last check off
                            if broken habit:    your habit is already broken, because you check off outside 
                                                the period or after the end date
                            if completed habit: your habit is completed.

            This process cannot be repeated.""")
            input("""
            Please press [ENTER] to return to the MAIN MENU.\n""")
        elif command_2 >= 7 or command_2 <= 0:
            input("""
        Invalid Input. Please press [ENTER] to return to the HELP MENU.\n""")
