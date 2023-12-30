import json
import pickle
import requests
from requests_cache import CachedSession


def json_cache(cache_path: str, url: str, update: bool = False):

    if update:
        print("Updating json data")
        json_data = None
    else:
        try:
            with open(cache_path, 'r') as file:
                json_data = json.load(file)
                print("Fetched data from local cache")
                print(f"\n {json_data} ")
        except(FileNotFoundError, json.JSONDecodeError) as e:
            print(f"local cache not found... {e}")
            json_data = None
    
    if not json_data:
        print("fetching json data... (Creating local cache)")

        with open(cache_path, 'w') as file:
            json_data = requests.get(url).json()
            json.dump(json_data, file, indent=4)
    return json_data



def pkl_cache():
    pass



def cached_session_cache():
    pass


json_cache(cache_path="cache.json", url="https://dummyjson.com/comments", update=True)
