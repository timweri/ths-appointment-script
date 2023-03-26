import requests
from dotenv import load_dotenv
import os
import re
from telegram_bot import bot_error_message, bot_message, bot_debug
import asyncio

load_dotenv()

URL = "https://ths.use1.ezyvet.com/external/portal/main/verifyLoginAttempts"
PAYLOAD = {
    "login-email": os.getenv("USERNAME"),
    "login-password": os.getenv("PASSWORD")
}
SESSION_REGEX = re.compile("PHPSESSID=*")

async def log_in():
    await bot_debug("Logging into Toronto Humane Society")

    try:
        res = requests.post(URL, data=PAYLOAD)
        res.raise_for_status()

        if "Set-Cookie" not in res.headers:
            raise requests.exceptions.RequestsException("Set-Cookie not found in response headers")

        cookies = res.headers["Set-Cookie"].split(';')
        session_ids = list(filter(SESSION_REGEX.match, cookies))

        if len(session_ids) != 1:
            raise requests.exceptions.RequestsException(f"Unexpected number of session ids: {session_ids}")

        session_id = session_ids[0]

        with open(".session", "w") as file:
            file.write(session_id)

        await bot_debug("Logged into Toronto Humane Society successfully")
    except Exception as err:
        await bot_error_message(str(err))
        raise err
