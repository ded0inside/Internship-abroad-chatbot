import os.path
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import os.path
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import mimetypes
import os
from email.message import EmailMessage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

class ActionResetSlots(Action):
    def name(self) -> Text:
        return "action_reset_slots"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        evt = AllSlotsReset()
        return [evt]


class ActionSentEmail(Action):
    def name(self) -> Text:
        return "action_sent_email"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ):
        print('Sending email')
        self.subject = tracker.get_slot('subject')
        self.body = tracker.get_slot('body')
        self.verifiy_email()
        self.send_email()


    def verifiy_email(self):
        creds = None
        SCOPES = ["https://mail.google.com/"]
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        try:
            # Call the Gmail API
            service = build("gmail", "v1", credentials=creds)
            results = service.users().labels().list(userId="me").execute()
            labels = results.get("labels", [])

            if not labels:
                print("No labels found.")
                return
            print("Labels:")
            for label in labels:
                print(label["name"])

        except HttpError as error:
            print(f"An error occurred: {error}")

    def send_email(self):
        creds = None
        SCOPES = ["https://mail.google.com/"]
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        try:
            service = build("gmail", "v1", credentials=creds)
            message = EmailMessage()

            message.set_content(self.body)

            # You can change this email
            message["To"] = "harsh.doshi@stud.th-deg.de"
            # If you change the sender email, then you would need to setup new credentials and tokens.
            message["From"] = "helpinternship.dit@gmail.com"
            message["Subject"] = self.subject

            # encoded message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

            create_message = {"raw": encoded_message}
            send_message = (
                service.users()
                .messages()
                .send(userId="me", body=create_message)
                .execute()
            )
            print(f'Message Id: {send_message["id"]}')
        except HttpError as error:
            print(f"An error occurred: {error}")
            send_message = None
        return send_message


class ValidateBasicInformation(FormValidationAction):

    def name(self) -> Text:
        return "validate_basic_information"

    def validate_student_email(self,
                               slot_value: Any,
                               dispatcher:"CollectingDispatcher",
                               tracker: Tracker,
                               domain: "DomainDict") -> Dict[Text, Any]:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if '@stud.th-deg.de' not in slot_value or not re.match(pattern, slot_value):
            dispatcher.utter_message(text="Please enter correct student email!")
            return {"student_email": None}
        else:
            return {"student_email": slot_value}
