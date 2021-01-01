from __future__ import print_function
from datetime import datetime,timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import traceback
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']



class CalendarController:
    def __init__(self):

        creds = None
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
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

    def create(self):
        try:
            d = datetime.now().date()
            tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
            start = tomorrow.isoformat()
            end = (tomorrow + timedelta(hours=1)).isoformat()

            event_result = self.service.events().insert(calendarId='primary',
                body={ 
                    "summary": 'Automating calendar', 
                    "description": 'This is a tutorial example of automating google calendar with python',
                    "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'}, 
                    "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                }
            ).execute()

            print("created event")
            print("id: ", event_result['id'])
            print("summary: ", event_result['summary'])
            print("starts at: ", event_result['start']['dateTime'])
            print("ends at: ", event_result['end']['dateTime'])
        except:
            print(traceback.print_exc())

    def update(self):
        try:
            d = datetime.now().date()
            tomorrow = datetime(d.year, d.month, d.day, 9)+timedelta(days=1)
            start = tomorrow.isoformat()
            end = (tomorrow + timedelta(hours=2)).isoformat()

            event_result = self.service.events().update(
                calendarId='primary',
                eventId='sgrvpuc1um2mv8djda9pgr8qps',
                body={ 
                    "summary": 'Updated Automating calendar',
                    "description": 'This is a tutorial example of automating google calendar with python, updated time.',
                    "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'}, 
                    "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                },
            ).execute()  
        

            print("updated event")
            print("id: ", event_result['id'])
            print("summary: ", event_result['summary'])
            print("starts at: ", event_result['start']['dateTime'])
            print("ends at: ", event_result['end']['dateTime'])
        except:
            print(traceback.print_exc()) 

    def delete(self):
        try:
            self.service.events().delete(
                calendarId='primary',
                eventId='sgrvpuc1um2mv8djda9pgr8qps',
            ).execute()
        except:
            print(traceback.print_exc())
    
        print("Event deleted")




    def list_events(self):
        try:    
            now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
            print('Getting List o 10 events')
            events_result = self.service.events().list(calendarId='primary', timeMin=now,
                                                maxResults=10, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found.')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
        except:
            print(traceback.print_exc())

    def list_calendars(self):
        try:
            print('Getting list of calendars')
            calendars_result = self.service.calendarList().list().execute()

            calendars = calendars_result.get('items', [])

            if not calendars:
                print('No calendars found.')
            for calendar in calendars:
                summary = calendar['summary']
                id = calendar['id']
                primary = "Primary" if calendar.get('primary') else ""
                print("%s\t%s\t%s" % (summary, id, primary))
        except:
            print(traceback.print_exc())


def main():
    MyCalendar = CalendarController()
    MyCalendar.create()
    MyCalendar.delete()
    #MyCalendar.update()
    MyCalendar.list_events()
    MyCalendar.list_calendars()

if __name__ == '__main__':
    main()