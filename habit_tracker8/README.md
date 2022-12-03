# Habit-Tracker-App

## Introduction:
The Python code is written in python 3.10 in PyCharm and is divided into 10 sections, which allow for a visual structure using a continuous line of minus signs and a preceding comment. The number in the comment refers to the corresponding main menu item:

![01](pictures/01.jpg)

## Overview of the sections:
1) Frameworks, Database and Main Menu
2) Exit program part 1 (#7 exit program)
3) Define a new habit (#1 define a new habit)
4) List existing habits (#2 list existing habits)
5) Check off existing habits (#3 check off an existing habit)
6) Delete an existing habit (#4 delete an existing habit)
7) Add five predefined habits to the database (#5 insert five predefined habits)
8) Help (#6 help)
9) Specific habit (#8 create specific habit)
10) Exit program part 2 (#7 exit program)

### Menu structure of the main menu:

    MAIN MENU "habit tracker":
    Press [1] to define a new habit.
    Press [2] to list existing habits.
    Press [3] to check-off an existing habit.
    Press [4] to delete an existing habit or all habits.
    Press [5] to add five predefined habits to the database.
    Press [6] for help.
    Press [7] to exit the program.

## Sections 1: Frameworks, Database and Main Menu

Here the necessary frameworks are imported, a connection to the database is established and the main menu is defined.

### Frameworks:
- datetime (to capture the current time and date)
- sqlite3 (database where the habits are stored)
- pandas (tool for outputting data from the database)
- tabulate (tool for output in table-like form)

### Database (sqlite3)
In the database, a habit is stored in table form in each row. The table has the following columns:

- habit (name of habit)
- period_day (number of days)
- start_date (start date of the habit)
- enddate (end date of the habit)
- period (periodicity daily/weekly)
- counter (number of ticks)
- checked_off (status of habit)
- finished (time of completion)

### main menu
Definition and listing of the main menu. Further information is contained in the document on the conception phase.

![02](pictures/02.jpg)

## Section 2: Exiting the program Part 1

In this section, the command "command_1" necessary for controlling the main menu is introduced and defined with the value 0. As long as this is not changed to 7 by the user (which causes the program to terminate), the program runs in a while loop. The assignment of the numbers 1 to 6 enable navigation in the main menu. Incorrect entries are intercepted by a try and execute block. The assignment is made using an input command

![03](pictures/03.jpg)

## Section 3: Define New Habit

If you press 1 from the main menu and confirm with Enter, you get to the area where you define and save a new habit. A connection to the database is established. In order to avoid double entries, the user is first shown a list of the habits that have already been saved. The following information must then be entered by the user and confirmed with Enter:
- name of the habit
- Periodicity (1=daily; 2=weekly)
- Number of periods
- Storage request (1=Yes; 2=No)

If the user wishes to save the following data is generated and stored in the database together with the previous data:
- Start date (start_date=habit creation date)
- End date (according to periodicity and number of periods)
- Number of ticks (counter=0)
- Status of the habit (checked_off= habit creation date)
- time of completion (finished=XXX)

Incorrect entries are also intercepted here by two try and exept blocks

![04](pictures/04.jpg)

## Section 4: List Existing Habits

From the main menu, pressing 2 and confirming with Enter takes you to the menu where you can list existing habits (analytics module). First, a submenu is defined in the code, which is displayed to the user.

### Menu structure of the submenu:
    MENU "existing habits":"
    Please press [1] to show the whole table.
    Please press [2] to show every successfully completed habit.
    Please press [3] to show every broken habit.
    Please press [4] to show every ongoing habit (which is not broken or completed).
    Please press [5] to show every daily habit.
    Please press [6] to show every weekly habit.
    Please press [7] to show most checked off habit.
    Please press [8] to show the longest habit.
    Please press [9] to go back to MAIN MENU.

In this section, the "select" command required to control the submenu is introduced and defined with the value 0. As long as this is not changed to 9 by the user (which causes the exit of the submenu and takes you to the main menu), the program runs in a while loop. The assignment of the numbers 1 to 9 enables navigation in the submenu. Incorrect entries are intercepted by a try and execute block. The assignment is made using an input command.

![05](pictures/05.jpg)

The user has various options by navigating in the submenu to display different target data from the database. For example the entire database or all successfully completed habits. Incorrect entries are intercepted by try and exept blocks. As in the entire program, the user is informed by explanatory texts about the following inputs or displayed content.

## Section 5: Check off existing habits

From the main menu, pressing 2 and confirming with Enter takes you to the area where you can check off existing habits. The user selects a habit to tick by typing in the name of the habit. Previously, a list of all existing habits was displayed to facilitate this process. After connecting to the database, the program then detects the presence of the habit and modifies the database depending on various parameters, which have been explained in more detail in the document on the design phase. The relation of the current day to the dates stored in the database is necessary for the check, which formulas generate dates from last week via the current date to next week. The dates generated in this way are then converted from the "date" format to the "str" ​​format in order to be able to compare them with the information from the database.

![06](pictures/06.jpg)

Depending on whether the user moves within the time parameters set by himself or not, the columns “checked_off”, “counter” and/or finished are updated in the database. The user is informed via explanatory texts whether he/she has e.g. completed a habit, already ticked it off within the current period, ticked it off successfully or broken it.

![07](pictures/07.jpg)

## Section 6: Delete Existing Habits

If you press 2 from the main menu and confirm with Enter, you get to a submenu where you can delete existing habits. You can either delete a habit, delete all habits or navigate back to the main menu through the submenu. If you only want to delete a habit, the user must type in the name of the habit and then confirm the deletion. If the user wants to delete all habits, he must select submenu item 2 and is then asked to restart the program in order to avoid program errors.

## Section 7: Adding predefined habits to the database

Under main menu item 5 you can add five predefined habits to the database. To do this, select menu item 1 in a submenu

![08](pictures/08.jpg)

## Section 8: Help

If the user needs help, he/she can have a detailed output of the program contents displayed under main menu item 6. A submenu displays the various help topics.

![09](pictures/09.jpg)

## Section 9: Specific Habits

In order to generate specific habits, an area that is difficult or inaccessible for the user was created for test purposes. If you type in the number "8765" in the main menu, you get to an area similar to the area "Define a new habit (main menu item 2: define a new habit)". The difference is that you can choose the start date freely, in contrast to main menu item 2, where the start date always corresponds to the current date. This has the advantage that you can move the start date of a weekly habit back a week for testing purposes, for example, to test the functionality of the program. However, it is expressly not desired to make this program section accessible to the user, since unexpected errors can occur when checking off habits, e.g. if the start date is before the current day for daily habits.

## Section 10: Exiting the Program Part 2

In the last section of the code, the behavior of the program is defined when the number 9 is typed in in the main menu and confirmed with Enter. The connection to the database is terminated and the user is given a goodbye message.

![10](pictures/10.jpg)

## Database behavior:

In the database (framework: sqlite3), data records are generated, updated or deleted by prompts, depending on which main menu item you are in.

![11](pictures/11.jpg)
