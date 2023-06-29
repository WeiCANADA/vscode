# HTTP Verbs

import requests
import json
#url = 'https://icanhazdadjoke.com/'
url = 'https://icanhazdadjoke.com/slack'
response = requests.get(url,
                        headers={"Accept":"application/json"}).json()
#rint(response.text)

# requesting JSON
#print(response)
print(response["attachments"][0]["text"])
#print(type(response.json()))
