import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

token = 'ff23259d76db3cf6ef993524fd4a987019dd19f9e94c82ec'
notebook_path = 'notebooks/one.ipynb'
base = 'http://127.0.0.1:8888/'
headers = {'Authorization': 'Token ff23259d76db3cf6ef993524fd4a987019dd19f9e94c82ec'
           , 'Content-type': 'application/json'}

# http://127.0.0.1:8888/?token=fc6628a48210a7fed3884b1f0fe8aa5b3da1c5f3c3218e15

# api_url = 'http://127.0.0.1:8888/notebooks/one.ipynb'


data = {}



# print("Button", runAll)
# # r = requests.post(api_url)

# print(response.url)
# print(response.headers)
# print(type(response))


