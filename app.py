#!/usr/bin/env python3
"""MyLoc Module
"""
import requests
import calendar
from datetime import datetime
import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

url = "http://ip-api.com/json/165.58.129.199"
combined_calendar_data = []
scopes = ['https://www.googleapi.com/auth/calendar.readonly']
def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.utcnow().isoformat() + '2'
    events = service.events().list(calendarId='primary', timeMin=now,
            singleEvents=True, orderBy='startTime').execute()
    all_events.append(events)
    print(all_events)


def get_api_location(api: str) -> str:
    """Gets the location of a given api
    """
    location = requests.get(api).json()
    print(location['country'])

def get_calendar(year:int) -> str:
    """Gets the calendar
    """
    calendar.setfirstweekday(calendar.SUNDAY)
    car = calendar.calendar(year)
    print(car)

def get_api(api: str) -> str:
    """Query api
    """


if __name__ == "__main__":
    get_api_location(url)
    get_calendar(year=2022)
#    main()
