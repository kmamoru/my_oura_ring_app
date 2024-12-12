from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import requests


load_dotenv()


access_token = os.getenv("PERSONAL_ACCESS_TOKEN")

url = "https://api.ouraring.com/v2/usercollection/sleep"

headers = {"Authorization": f"Bearer {access_token}"}

monthly_datetime = {
    "start_date": (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
    "end_date": datetime.now().date().strftime("%Y-%m-%d"),
}
params = {
    "start_date": monthly_datetime["start_date"],
    "end_date": monthly_datetime["end_date"],
}

response = requests.get(url, headers=headers, params=params)


if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
