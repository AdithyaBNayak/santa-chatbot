import time
import boto3


def hello(event, context):
    
    prompt = event['arguments']['prompt']
    
    response = {
        'response': prompt,
        'createdAt': str(time.time()) 
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
