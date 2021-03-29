#!/usr/bin/env python

import json
import sys
import random
import requests
import os
from datetime import date
from time import sleep

current_date = date.today().strftime('%B %d')

message = f'Home Office, {current_date}'
webhook_url = os.environ['slack-url']
icon_url = 'https://user-images.githubusercontent.com/17321542/108324827-759d0a00-71d9-11eb-95ec-db98d03cf472.jpeg'
username = 'Aleksandr Khalikov'
channel = os.environ['channel-name']
minutes = 60

slack_data = {
    'text': message
    ,'username': username
    ,"icon_url": icon_url
    ,'channel': channel
}

sleep(random.randint(5, 18) * minutes)

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
