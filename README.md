# moodle-new-assignment-checker
A python program that automates the task of adding new Moodle assignments to your Google Calendar.

[![N|Solid](https://www.seleniumhq.org/images/big-logo.png)](https://www.seleniumhq.org/) [![N|Solid](http://s2.glbimg.com/SqbNqj3R6YXwQUYaWTPTSXnzVXk=/695x0/s.glbimg.com/po/tt2/f/original/2017/02/07/win10-7.jpg)](https://www.google.com/calendar)

This is a moodle automation script that can automatically add reminders about new assignments on their way a few days ago to your google calendar.
Basically, you'll want to schedule your pc to run this script once every 5 days so that if a new assignment is uploaded, it gets automatically added to your google calendar. This can help a lot if your primary scheduler is google calendar, if not this project might not be for you.

# Initial Configuration
1. Firslty, you would want to set up an entry-way for you google calendar to allow calendar event creation programatically. Make sure you are logged in with the account you use the calendar with. Next, go [here](https://developers.google.com/calendar/quickstart/python) and click on "Enable the google calendar api". Now follow the flow and once it is set up come back her and continue.

2. Secondly, you will want to download a 'driver' for your browser. For example, if your Chrome version is v76, you need to download a [chromedriver](https://chromedriver.chromium.org/) file for the stable version for chrome with that version number.

3. Now pop up your terminal and run the python script:
    >python3 [finder.py](https://github.com/Naman1997/moodle-new-assignment-checker/blob/master/finder.py)

4. On first run, google will ask your credintials, provide the email credentials of the email you gave at the 1st step. This is a one time process and you will not be asked to do it next time onwards.

# Optional Setup
1. You might want to run this in the background(sorta). For that you can uncomment the "headless" option in the script.
2. You might have noticed that you'll need to run this script everytime you want to add an assignment reminder to your calendar. To automate this such that your pc runs the script on its own every few days, you will want to schedule your pc to run this script for you. Here are some tutorials for [Windows, Macs](https://martechwithme.com/schedule-python-scripts-windows-mac/) and [Linux](https://medium.com/@gavinwiener/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e) users.
