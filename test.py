#requests is for handling api requests (direct access to the api in the browser )
#import requests
# GET request: asking the webserver i made for some information
#print(requests.get("http://127.0.0.1:8000/items/1").json())
# use & for multiple requests
#print(requests.get("http://127.0.0.1:8000/items?name=Hammer&price=9.99&count=4&category=tools").json())

import os
from dotenv import load_dotenv
load_dotenv()  # This loads the variables from .env into the environment

print("Current Working Directory:", os.getcwd())
print("DATABASE_PASSWORD:", os.getenv('DATABASE_PASSWORD'))