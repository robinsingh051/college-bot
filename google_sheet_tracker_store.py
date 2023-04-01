from typing import Any, Dict, Optional

from rasa.core.trackers import DialogueStateTracker
from rasa.core.tracker_store import TrackerStore
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheetTrackerStore(TrackerStore):
    def __init__(self, spreadsheet_id: str, sheet_name: str, credentials_file: str):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.credentials_file = credentials_file

        # Load the Google Sheets API credentials
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file,
            scopes=["https://www.googleapis.com/auth/spreadsheets"],
        )

        # Create a Google Sheets API client
        self.client = build("sheets", "v4", credentials=credentials)

        # Find the worksheet by name
        try:
            self.sheet = self.client.spreadsheets().get(
                spreadsheetId=self.spreadsheet_id
            ).execute()
            for sheet in self.sheet.get("sheets", ""):
                properties = sheet.get("properties", {})
                title = properties.get("title", "")
                if title == self.sheet_name:
                    self.worksheet_id = properties.get("sheetId", "")
                    break
        except HttpError as e:
            raise ValueError(f"Unable to find worksheet: {e}")

    def save(self, tracker: DialogueStateTracker) -> None:
        # Extract the conversation from the tracker
        conversation = tracker.as_dialogue().as_dict()

        # Extract the questions and answers from the conversation events
        questions = [event["text"] for event in conversation["events"] if event["event"] == "user"]
        answers = [event["text"] for event in conversation["events"] if event["event"] == "bot"]

        # Write the questions and answers to the Google Spreadsheet
        row = [(questions), "\n".join(answers)]
        values = [row]
        body = {"values": values}
        range_name = f"{self.sheet_name}!A:F"
        result = (
            self.client.spreadsheets()
            .values()
            .append(
                spreadsheetId=self.spreadsheet_id,
                range=range_name,
                valueInputOption="RAW",
                insertDataOption="INSERT_ROWS",
                body=body,
            )
            .execute()
        )
