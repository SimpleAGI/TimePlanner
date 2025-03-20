from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# Sample scope for google calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

def sync_with_google_calendar():
    # Authenticate and construct service.
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('calendar', 'v3', credentials=creds)

    # Example: List the next 10 events from the user's calendar
    events_result = service.events().list(calendarId='primary',
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        print(event['summary'], event['start']['dateTime'])
