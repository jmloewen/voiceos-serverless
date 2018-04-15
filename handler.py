import json
import requests
from lambaFunctionCall.lambaFunctionCall import invokeLamba

RASASERVER_URL = "http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse"

APP_DICT = {
    "cats": invokeLamba,
    "home": None,
    "image search":  "imageSearch",
    "voicetunnel": "voicetunnel",
    "notes": "notes"

}

def isPostRequest(event):
    return str(event['requestContext']['httpMethod']) == "POST"

def unwrapEvent(event):
    bodyJson = event['body']
    bodyDict = json.loads(bodyJson)
    return bodyDict['payload'], bodyDict['sender']

def postRasaForIntent(payload):
    # r = requests.post(RASASERVER_URL, json={"q": payload})
    # return r.json()
    # mock
    return {'intent': {'name': 'home'}}

def intentNameFrom(rasaJson):
    return rasaJson['intent']['name']

def wrapIntentSpeakAction(rasaJson, sender):
    bodyPayload = {
        "actionType": "speak",
        "actionDetail": intentNameFrom(rasaJson)
    }
    body = {
        "receiver": sender, # always send back to the sender for now...
        "payload": bodyPayload
    }

    return {
        'statusCode':200,
        'headers': {'Content-Type':'application/json'},
        'body': json.dumps(body)
    }

def wrapResponse(payload, receiver):
    return {"payload":payload, "receiver":receiver}



def testCatappResponse(rasaJson,sender):
    parsedResponse = callCatApp()
    print('parsedResponse:',parsedResponse)
    responseBody = wrapResponse(callCatApp(), sender)
    print('responseBody:',responseBody)
    return response    

def endpoint(event, context):
    if not isPostRequest(event):
        return { "statusCode": 422, "body": "Request should be POST"}

    payload, sender = unwrapEvent(event)
    rasaJson = postRasaForIntent(payload['speech'])
    # return testCatappResponse(rasaJson, sender)
    wrapIntent =  wrapIntentSpeakAction(rasaJson, sender)  
    print('wrapIntent:', wrapIntent)
    return wrapIntent

