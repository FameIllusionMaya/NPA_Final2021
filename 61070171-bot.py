import urllib.parse
import requests
import json
import time

while True:
    access_token = "NWM3M2FhN2ItMzQxMS00ZTcyLTg4MTgtZDIyMzI5MWI3MGE1MzlhN2E1MjYtNzRi_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f"
    url = "https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3&max=1"
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }

    room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3"
    url = "https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3&max=1"
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    res = requests.get(url, headers=headers)
    result = res.json()
    messages = result["items"][0]["text"]
    print(messages)
    if messages == "61070171":
        print("yes")
        message_send = "Loopback61070171 - Operational status is up no netconf"
        url = 'https://webexapis.com/v1/messages'
        headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
        }
        params = {'roomId': room_id, 'markdown': message_send}
        res = requests.post(url, headers=headers, json=params)
        id_pre = result["items"][0]["id"]
    else:
        time.sleep(1)



