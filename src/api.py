from requests_cache import CachedSession
import requests


CACHE_FILE = "__app_cache__/app_cache"
CACHE_EXPIRY = 86400




def fetch_data(sign: str,day: str = "today"):

    URL =  f"http://sandipbgt.com/theastrologer/api/horoscope/{sign.lower()}/{day.lower()}"

    def handle_errors():
        days = ["yesterday", "today", "tomorrow"]
        if (day.lower() not in days):
            # raise ValueError(f"Invalid Day: '{day}'. You can choose between (Yesterday, Today, or Tomorrow)")
            print(f"Invalid Day: '{day}'.\nYou can choose between (Yesterday, Today, or Tomorrow)")
            print(f"Error: {e}")
        else:
            # raise requests.exceptions.RequestException(f"Invalid Zodiac Sign: '{sign}'\nError: {e}")
            print(f"Invalid Zodiac Sign: '{sign}'\nError: {e}")
    
    session = CachedSession(
            cache_name=CACHE_FILE,
            expire_after=CACHE_EXPIRY
            )

    try:
        print("Please wait...\n")
        response = session.get(URL).json()
        print(f" - Day: {day}")
        print(f" - Sign: {response['sunsign']}")
        print(f" - Mood: {response['meta']['mood']}")
        print(f" - Keywords: {response['meta']['keywords']}")
        print(f" - Intensity: {response['meta']['intensity']}\n")

        _ = "(c) Kelli Fox, The Astrologer, http://new.theastrologer.com"
        print(f"Horoscope:\n\n{response['horoscope']}".replace(_, ''))

    except(requests.RequestException) as e:
        handle_errors()

