import requests, os

def lambda_handler(event, context):

    print(requests)
    apiKey = os.environ['newrelic_api_key']
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'X-api-key' : apiKey}
    r = requests.get('https://api.newrelic.com/v2/applications.json', headers=headers)
    return r.json()
