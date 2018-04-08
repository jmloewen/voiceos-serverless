import json

def handle(event, context):
    body = {
        "actionType":"speak",
        "actionDetail":"meow"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

#start the cat app.
def onstart(event, context):

    body = {
        "actionType":"speak",
        "actionDetail":"meowth thats right"
    }

#Response body must be in JSON format, or it will not work with serverless.
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
