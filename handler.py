import json
import requests

RASASERVER_URL = "http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse"

def isPostRequest(event):
    return str(event['requestContext']['httpMethod']) == "POST"

def unwrapEvent(event):
    wrappedPayload = json.loads(event['body'])
    return wrappedPayload['payload'], wrappedPayload['sender']

def postRasaForIntent(payload):
    r = requests.post(RASASERVER_URL, json={"q": payload})
    return r.json()

def intentNameFrom(rasaJson):
    return rasaResponse['intent']['name']

def wrapIntentSpeakAction(rasaJson, sender):
    bodyPayload = {
        "actionType": "speak",
        "actionDetail": intentNameFrom(rasaJson)
    }
    body = {
        "receiver": sender, # always send back to the sender for now...
        "payload": bodyPayload
    }
    return { "statusCode": 200, "body": json.dumps(body) }

def endpoint(event, context):
    if !isPostRequest(event):
        return { "statusCode": 422, "body": "Request should be POST"}
    payload, sender = unwrapEvent(event)
    rasaJson = postRasaForIntent(payload)
    return wrapIntentSpeakAction(rasaJson, sender)
