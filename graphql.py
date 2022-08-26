import requests

url = "https://tqh36odakfgtdalvljoakejl4a.appsync-api.us-east-2.amazonaws.com/graphql"

headers = {'Content-Type':'application/graphql', 'x-api-key':'***'}

body = """
        mutation eventTrigger {
            eventTrigger(source:"Python", event:"eventUpdated"){
                source
                event
            }
        }
    """

response = requests.post(url, headers=headers, json={"query": body})

print("Status Code", response.status_code)
print("Status Code", response.content)