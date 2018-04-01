import json

def handle(event, context):
    response = {
        "statusCode": 200,
        "body": "test"
    }
    return response

def onstart(event, context):
    return ''
