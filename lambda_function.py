import json
from datetime import datetime

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': event['input'],
        'time': datetime.utcnow().isoformat(),

    }
