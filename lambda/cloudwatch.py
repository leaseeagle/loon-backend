import json
import boto3
from datetime import datetime

def lambda_handler(event, context):

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # List metrics through the pagination interface
    #paginator = cloudwatch.get_paginator('list_metrics')
    #
    #for response in paginator.paginate(Dimensions=[{'Name': 'Database'}],
    #                               MetricName='',
    #                               Namespace=''):
    #    print(response['Metrics'])

    response = cloudwatch.get_metric_statistics(
        Namespace='',
        MetricName='',
        Dimensions=[
            {
                'Name': 'Database',
                'Value': ''
            },
        ],
        StartTime=datetime(2017, 9, 10),
        EndTime=datetime(2017, 9, 11),
        Period=120,
        Statistics=[
            'Maximum'
        ],
    #    ExtendedStatistics=[
    #    'string',
   #     ],
        Unit='Count'
    )

    return json.dumps(event)  # Echo back the first key value
    #raise Exception('Something went wrong')

