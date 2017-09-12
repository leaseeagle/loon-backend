import json
import boto3

from datetime import datetime, timedelta

def lambda_handler(event, context):

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')
    
    # current date
    CurrentEndDateTime = datetime.now()
    # current date - 24 hours
    CurrentStartDateTime = datetime.now() - timedelta(hours = 24)
    Metric = event['params']['querystring']['metric']
    NameSpace = event['params']['querystring']['namespace']
    Database = event['params']['querystring']['name']
    response = cloudwatch.get_metric_statistics(
        Namespace= NameSpace,
        MetricName= Metric,
        Dimensions=[
            {
                'Name': 'Database',
                'Value': Database
            },
        ],
       StartTime=CurrentStartDateTime,
       EndTime=CurrentEndDateTime,
        # period = 5 minutes must be a multiple of 60
        Period=300,
        Statistics=[
           'Maximum'
        ],
        Unit='Count'
    )

    print(event)
    # return json.dumps(response)  # Echo back the first key value
    # raise Exception('Something went wrong')
    return json.dumps(response, cls=DateTimeEncoder)



class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)
