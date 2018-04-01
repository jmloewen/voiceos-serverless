import json

def handle(event, context):
    body = {
        "message": "Hello, the current time is meow."
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

#start the cat app.
def onstart(event, context):
    body = {
        "message": "Hello, the current time is startmeow."
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
