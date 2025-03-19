import requests
from dotenv import load_dotenv
import os

load_dotenv()

class CalendlyClient:
    def __init__(self):
        self.token = os.getenv("CALENDLY_API_TOKEN")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_booking_link(self):
        response = requests.get("https://api.calendly.com/event_types", headers=self.headers)
        if response.status_code == 200:
            event = response.json()["collection"][0]  # Get first event type
            return event["scheduling_url"]
        return None