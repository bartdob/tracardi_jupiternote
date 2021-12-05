import json
import requests
import datetime
import uuid
from pprint import pprint
import socket

import websocket

token = '240d1a6cca260512929e5a876a8a62fe0f34cc5c3560bb92'
notebook_path = 'one.ipynb'
base = 'http://127.0.0.1:8888'
headers = {'Authorization': 'Token {}'.format(token),
           'Content-type': 'application/json'}


url = base + '/api/kernels'
response = requests.post(url, headers=headers)
kernel = json.loads(response.text)

print('kernel: ', kernel['id'])

# Load the notebook and get the code of each cell
url = base + '/api/contents/' + notebook_path
print("url: " + url)
response = requests.get(url, headers=headers)
file = json.loads(response.text)
print("file: ", file)
code = [c["source"] for c in file["content"]["cells"] if len(c["source"]) > 0]

print(code)

# Execution request/reply is done on websockets channels
ws = websocket.WebSocket()

ws.connect("ws://127.0.0.1:8888/api/kernels/" + kernel['id'] + "/channels",
           header=headers)
print(ws)


def send_execute_request(code):
    msg_type = 'execute_request';
    content = {'code': code, 'silent': False}
    hdr = {'msg_id': uuid.uuid1().hex,
           'username': 'test',
           'session': uuid.uuid1().hex,
           'data': datetime.datetime.now().isoformat(),
           'msg_type': msg_type,
           'version': '5.0'}
    msg = {'header': hdr, 'parent_header': hdr,
           'metadata': {},
           'content': content}
    return msg


for c in code:
    ws.send(json.dumps(send_execute_request(c)))


# We ignore all the other messages, we just get the code execution output
# (this needs to be improved for production to take into account errors, large cell output, images, etc.)
for i in range(0, len(code)):
    msg_type = '';
    while msg_type != "stream":
        rsp = json.loads(ws.recv())
        msg_type = rsp["msg_type"]
    print(rsp["content"]["text"])

ws.close()
