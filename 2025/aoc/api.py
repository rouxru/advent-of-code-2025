from typing import Any
import requests
from dotenv import load_dotenv
import os


def get_data(url: str) -> list[Any]:
    load_dotenv()
    aoc_session = os.getenv("AOC_SESSION")
    cookies = {"session": aoc_session}
    response = requests.get(url, cookies=cookies)

    data = response.text.strip().splitlines()
    return data
