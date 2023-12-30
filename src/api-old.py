import requests
import os
import time
import json
from requests_cache import CachedSession
# API = : http://sandipbgt.com/theastrologer/api/horoscope/{sign}/{day}"


CACHE_FILE = "cache/app_cache.json"
CACHE_PATH = "cache/app_cache"
CACHE_EXPIRY = 86400  # 24 hours in seconds



# def json_cache(cache_path: str, url: str, update: bool = False):

#     if update:
#         print("Updating json data")
#         json_data = None
#     else:
#         try:
#             with open(cache_path, 'r') as file:
#                 json_data = json.load(file)
#                 print("Fetched data from local cache")
#                 print(f"\n {json_data} ")
#         except(FileNotFoundError, json.JSONDecodeError) as e:
#             print(f"local cache not found... {e}")
#             json_data = None

#     if not json_data:
#         print("fetching json data... (Creating local cache)")

#         with open(cache_path, 'w') as file:
#             json_data = requests.get(url).json()
#             json.dump(json_data, file, indent=4)
#     return json_data

# def cache_pkl():
#     pass


# def cache(file: str, json: bool = True):
#     if os.path.exists(file):
#         if json:
#             cache_json(file,URL,)
#         else:
#             cache_pkl()


def is_cache_expired(cache_file):
    if os.path.exists(cache_file):
        last_modified_time = os.path.getmtime(cache_file)
        current_time = time.time()
        return current_time - last_modified_time > CACHE_EXPIRY
    return True



def update_cache(cache_file, data):
    with open(cache_file, 'w') as file:
        json.dump(data, file, indent=4)



def fetch_data(sign: str,day: str = "today"):

    URL =  f"http://sandipbgt.com/theastrologer/api/horoscope/{sign.lower()}/{day.lower()}"


    def handle_errors():
        days = ["yesterday", "today", "tomorrow"]
        if (day.lower() not in days):
            raise ValueError(f"Invalid Day: '{day}'. You can choose between (Yesterday, Today, or Tomorrow)")
        else:
            raise requests.exceptions.RequestException(f"Invalid Zodiac Sign: '{sign}'\nError: {e}")
    
    session = CachedSession(
            cache_name=CACHE_PATH,
            expire_after=None
            )

    try:
        print("Please wait...\n")
        response = session.get(URL).json()
        update_cache(CACHE_PATH, response)
    except requests.RequestException as e:
        handle_errors()
    with open(CACHE_PATH, 'r') as file:
        data = json.load(file)

        print(f" - Day: {day}")
        print(f" - Sign: {data['sunsign']}")
        print(f" - Mood: {data['meta']['mood']}")
        print(f" - Keywords: {data['meta']['keywords']}")
        print(f" - Intensity: {data['meta']['intensity']}\n")

        _ = "(c) Kelli Fox, The Astrologer, http://new.theastrologer.com"
        print(f"Horoscope:\n\n{data['horoscope']}".replace(_, ''))


def get_data(sign: str):
    if is_cache_expired(CACHE_PATH):
        fetch_data(sign)

get_data("aries")
