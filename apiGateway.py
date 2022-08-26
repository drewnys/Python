import requests

url = "https://97winmgmwg.execute-api.us-east-2.amazonaws.com/learn-sandbox/events"

data = {
    "items":[ 
        {
            "Detail":"{\"event_group\":\"Work Request\", \"event_action\":\"Update\"}", 
            "DetailType":"Event", 
            "EventBusName": "learn-eventbridge",
            "Source":"Python (localhost)"
        }
   ]
}

response = requests.post(url, json=data)

print("Status Code", response.status_code)
print("Status Code", response.content)