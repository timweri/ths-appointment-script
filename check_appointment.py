import requests
import asyncio
from telegram_bot import bot_message, bot_error_message
from datetime import date
from login import log_in

URL = "https://ths.use1.ezyvet.com/external/portal/calendar/getEvents"

TODAY = date.today()
END_DATE = "2023-07-01"

PAYLOAD = {
    "appointmenttypeid": 26,
    "start": TODAY,
    "end": END_DATE,
}

async def check_appointment():
    await log_in()

    with open(".session", "r") as file:
        SESSION_TOKEN = file.read()

    HEADERS = {
        "cookie": SESSION_TOKEN,
        "accept": "application/json",
    }

    await bot_message(f"Checking for spay appointment from {TODAY} (today) to {END_DATE}")

    try:
        res = requests.post(URL, headers=HEADERS, data=PAYLOAD);
        res.raise_for_status()

        appointments = res.json()
        if len(appointments) == 0:
            await bot_message("No appointments available :(")
        else:
            await bot_message(f"@timweri There are {len(appointments)} appointment(s) available: {appointments}!!!!")
    except Exception as err:
        await bot_error_message(str(err))
        raise err

asyncio.run(check_appointment())
