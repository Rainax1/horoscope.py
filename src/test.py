# this is just a test file.
# import os
# import pickle
import time
# from functools import wraps
# import sys
import json
import requests


# sys.set_int_max_str_digits(999999)

# def exportable_cache(func):
#     func.cache = {}

#     if os.path.exists("exportable_cache.cache"):
#         with open("exportable_cache.cache", "rb") as file:
#             func.cache = pickle.load(file)
#             # print(func.cache)

#     @wraps(func)
#     def wrapper(*args):
#         if args in func.cache.keys():
#             return func.cache[args]
#         else:
#             result = func(*args)
#             func.cache[args] = result
#             return result
#     return wrapper



# @exportable_cache



# def Fibonacci(n):
 
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
 
#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0
 
#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)


# # # def factorial(n):
# # #     result = 1
# # #     for i in range(1,n+1):
# # #         result *= i
# # #     return result


# # init = time.perf_counter()

#  # for n in range(10000,10100):
#  #     f(n)

# print(Fibonacci(90))

# # # final = time.perf_counter()

# # # print(final - init)

# with open("exportable_cache.cache", "wb") as file:
#     pickle.dump(Fibonacci.cache, file)


# def cache(*, update: bool = False, json_cache: str, url: str):
#     if update:
#         json_data = None
#     else:
#         try:
#             with  open(json_cache, 'r') as file:
#                 json_data = json.load(file)
#                 print("Fetched data from local cache")
#         except(FileNotFoundError, json.JSONDecodeError) as e:
#             print(f"No local cache found... {e}")
#             json_data = None
    
#     if not json_data:
#         print("Fetching Json data  (Creating local cache)")
#         with open(json_cache, 'w') as file:
#             json_data = requests.get(url).json()
#             json.dump(file, json_data)
#     return json_data




# url =  "https://dummyjson.com/comments"
# json_cache = "cache.json"

# data: dict = cache(update=False, json_cache=json_cache, url=url)
# print(data)




# #     # Loading
# #     with open(filename, 'r') as file:
# #         json_data: dict = json.load(file)
# #         temp_data: list = json_data["comments"]
# #         temp_data.append(data)
# #         json_data["comments"] = temp_data
# #     # Writing
# #     with open(filename, 'w') as file:
# #         json.dump(data, file, indent=4)
# #         print("Data updated succesfully.")

# def update_json(data: dict, filename: str = "cache.json"):
#     # Loading
#     with open(filename, 'r') as file:
#         json_data: dict = json.load(file)
#         temp_data: list = json_data["comments"]  # Use get() to handle missing key
#         temp_data.append(data)
#         json_data["comments"] = temp_data  # Update the "comments" key

#     # Writing
#     with open(filename, 'w') as file:
#         json.dump(json_data, file, indent=4)
#         print("Data updated successfully.")

# data = {
#     "id": 32,
#     "body": "What an accomplishment!. WOW",
#     "postId": 25,
#     "user": {
#         "id": 37,
#         "username": "daalmondz"
#     }
# }

# update_json(data)

