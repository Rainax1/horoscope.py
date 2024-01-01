"""
Horoscope Fetcher

This script fetches daily horoscope information based on the provided zodiac sign and day.

This script is designed to be imported into the main.py file, serving as a module to provide functionality for fetching and displaying daily horoscope information.


Dependencies:
- requests_cache: Used for caching API requests to improve performance.
- colorama: Used for adding color to console output.

Example:
    fetch_data("Leo", "today")
    fetch_data("Leo", "today", color=True)          # for colored text ( default is False )

"""




from requests_cache import CachedSession
import colorama
from colorama import Fore
import requests

colorama.init(autoreset=True)

CACHE_FILE = "__app_cache__/app_cache"
CACHE_EXPIRY = 86400




def fetch_data(sign: str,day: str = "today", color: bool = False):


    """
        Fetches and prints daily horoscope information.

        Args:
            sign (str): Zodiac sign (e.g., "Leo").
            day (str): Day for which the horoscope is requested ("yesterday", "today", or "tomorrow").
            color (bool): If True, prints the output in colored format and default is False.
    """

    URL =  f"http://sandipbgt.com/theastrologer/api/horoscope/{sign.lower()}/{day.lower()}"

    # Manages and handles errors that may arise during API requests or due to user input, providing meaningful error messages for enhanced user comprehension.

    def handle_errors():
        days = ["yesterday", "today", "tomorrow"]
        if (day.lower() not in days):
            # raise ValueError(f"Invalid Day: '{day}'. You can choose between (Yesterday, Today, or Tomorrow)")
            print(f"Invalid Day: '{day}'.\nYou can choose between (Yesterday, Today, or Tomorrow)")
            print(f"{Fore.RED}Error: {e}")
        else:
            # raise requests.exceptions.RequestException(f"Invalid Zodiac Sign: '{sign}'\nError: {e}")
            print(f"Invalid Zodiac Sign: '{sign}'\n{Fore.RED}Error: {e}")
    
    session = CachedSession(
            cache_name=CACHE_FILE,
            expire_after=CACHE_EXPIRY
            )

    if color:
        try:
            print("Please wait...\n")
            response = session.get(URL).json()
            print(f"- {Fore.RED}Day: {day}")
            print(f" - {Fore.BLUE}Sign: {response['sunsign']}")
            print(f" - {Fore.GREEN}Mood: {response['meta']['mood']}")
            print(f" - Keywords: {response['meta']['keywords']}")
            print(f" - {Fore.MAGENTA}Intensity: {response['meta']['intensity']}\n")

            _ = "(c) Kelli Fox, The Astrologer, http://new.theastrologer.com"
            print(f"{Fore.YELLOW}Horoscope:{Fore.RESET}\n\n{response['horoscope']}".replace(_, ''))
        except(requests.RequestException) as e:
            handle_errors()
    else:

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

