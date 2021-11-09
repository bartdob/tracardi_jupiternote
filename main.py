import requests
import json
import datetime
import uuid
from pprint import pprint

notebook_path = 'notebooks/one.ipynb'
base = 'http://127.0.0.1:8888/'
headers = {'Authorization': 'Token fc6628a48210a7fed3884b1f0fe8aa5b3da1c5f3c3218e15'
           , 'Content-type': 'application/json'}

# http://127.0.0.1:8888/?token=fc6628a48210a7fed3884b1f0fe8aa5b3da1c5f3c3218e15

# api_url = 'http://127.0.0.1:8888/notebooks/one.ipynb'
# token = 'fc6628a48210a7fed3884b1f0fe8aa5b3da1c5f3c3218e15'

data = {}

# r = requests.get(api_url, headers={
#              'Authorization': 'token %s' % token,
#             }
#     )


url = base + notebook_path
response = requests.get(url, headers=headers)
file = json.loads(response.text)

# r = requests.post(api_url)

print(response.url)
print(response.headers)
print(type(response))