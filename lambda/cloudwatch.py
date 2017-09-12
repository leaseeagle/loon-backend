import json
import boto3

from datetime import datetime, timedelta

def lambda_handler(event, context):

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # List metrics through the pagination interface
    #paginator = cloudwatch.get_paginator('list_metrics')
    #
    #for response in paginator.paginate(Dimensions=[{'Name': 'Database'}],
    #                               MetricName='Outstanding Tasks',
    #                               Namespace='dev1/TriggerTask'):
    #    print(response['Metrics'])
    
    # current date
    CurrentEndDateTime = datetime.now()
    # current date - 24 hours
    CurrentStartDateTime = datetime.now() - timedelta(hours = 24)
    
    response = cloudwatch.get_metric_statistics(
        Namespace='dev1/TriggerTask',
        MetricName='Outstanding Tasks',
        Dimensions=[
            {
                'Name': 'Database',
                'Value': 'master'
            },
        ],
       # StartTime=datetime(2017, 9, 11),
       # EndTime=datetime(2017, 9, 12),
       StartTime=CurrentStartDateTime,
       EndTime=CurrentEndDateTime,
        # period = 5 minutes must be a multiple of 60
        Period=300,
        Statistics=[
           'Maximum'
        ],
    #    ExtendedStatistics=[
    #    'string',
   #     ],
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
