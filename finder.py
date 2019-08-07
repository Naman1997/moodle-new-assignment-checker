from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random
import datetime
from datetime import datetime


SCOPES = ['https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/calendar.events']


def bhardo(summary, matter):
    date1 = matter.split()[1]
    date2 = date1.lower()[:-1]
    if(date2 == "jan"):
        month = "01"
    elif(date2 == "feb"):
        month = "02"
    elif(date2 == "mar" or date2 == "march"):
        month = "03"
    elif(date2 == "apr" or date2 == "april"):
        month = "04"
    elif(date2 == "may"):
        month = "05"
    elif(date2 == "jun" or date2 == "june"):
        month = "06"
    elif(date2 == "july" or date2 == "jul"):
        month = "07"
    elif(date2 == "aug" or date2 == "august"):
        month = "08"
    elif(date2 == "sept" or date2 == "sep" or date2 == "september"):
        month = "09"
    elif(date2 == "oct" or date2 == "october" or date2 == "octo"):
        month = "10"
    elif(date2 == "nov" or date2 == "november" or date2 == "novemb"):
        month = "11"
    elif(date2 == "dec" or date2 == "december"):
        month = "12"
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    currentYear = datetime.now().year
    duedate = int(matter.split()[0])
    godate = str(int(duedate)-2)
    duedate = str(int(duedate)-1)

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    """
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    """
    # Refer to the Python quickstart on how to setup the environment:
    # https://developers.google.com/calendar/quickstart/python
    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
    # stored credentials.

    event = {
        'summary': summary,
        'location': 'Moodle',
        'description': 'Complete your asignment',
        'start': {
            'dateTime': str(currentYear)+'-'+str(month)+'-'+godate+'T09:00:00-07:00',
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': str(currentYear)+'-'+str(month)+'-'+str(duedate)+'T09:00:00-07:00',
            'timeZone': 'Asia/Kolkata',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': '#Your_EMAIL'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()


def hasXpath(xpath):
    try:
        self.driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


driver = webdriver.Chrome(
    executable_path='C:\\Users\\Naman\\Desktop\\Automata_Moodle\\chromedriver.exe')

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")
# options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.get('https://moodlecc.vit.ac.in/login/index.php')

# Username
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('#Your_Registration_Number')

# password
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('#Your_Moodle_Password')

# Login
butt = driver.find_element_by_xpath('//*[@id="loginbtn"]')
butt.click()
driver.implicitly_wait(30)

# Dashboard
dash = driver.find_element_by_xpath('//*[@id="label_2_2"]/span')
if(dash.is_displayed() and dash.is_enabled()):
    dash.click()
    time.sleep(2)
else:
    gogo = driver.find_element_by_xpath(
        '//*[@id="header"]/div/div/div/div[1]/div/button')
    gogo.click()
    time.sleep(1)
    dash.click()
    time.sleep(2)

driver.implicitly_wait(30)

# Lising out assignments
ass = driver.find_elements_by_xpath('//*[@class="event-name text-truncate"]')
due = driver.find_elements_by_xpath(
    '//*[@class="span5 text-truncate"]')


ass_names = []
due_dates = []

for i in ass:
    if i.text == '':
        pass
    else:
        ass_names.append(i.text)

for j in due:
    if j.text == '':
        pass
    else:
        due_dates.append(j.text)

# print(ass_names)
# print(due_dates)

for x, y in zip(ass_names, due_dates):
    print("\n")
    summ = str(x)
    mat = str(y)
    bhardo(summ, mat)
    print("Name = ", summ)
    print("Due =", mat)
    print("Event added to your calendar")
