import os, sys
lib_path = os.path.abspath(os.path.join('libs'))
sys.path.append(lib_path)

import requests

def lambda_handler(event, context):

    apiKey = os.environ['newrelic_api_key']
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'X-api-key' : apiKey}
    r = requests.get('https://api.newrelic.com/v2/applications.json', headers=headers)
    return r.json()
