import json
import requests
from lambdaFunctionCall.lambdaFunctionCall import invokeLambda

#'onVoiceOsEntry'

RASASERVER_URL = "http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse"

#Given intent, returns app name
#This must be modularized at some point.
AppNameFromIntent = {
    "cats": "catApp",
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
    ##Uncomment this to test next Sunday.
    ##r = requests.post(RASASERVER_URL, json={"q": payload})
    ##return r.json()
    ##Uncomment above to test next sunday.

    # mock
    #garbo
    return {'intent': {'name': 'cats'}}
    #return {}

def intentNameFrom(rasaJson):
    return rasaJson['intent']['name']

def wrapAppResult(result, sender):
    body = {
        "receiver": sender, # always send back to the sender for now...
        "payload": result
    }

    return {
        'statusCode':200,
        'headers': {'Content-Type':'application/json'},
        'body': json.dumps(body)
    }

def wrapIntentSpeakAction(spokenPhrase, sender):
    bodyPayload = {
        "actionType": "speak",
        "actionDetail": spokenPhrase
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

def switchBetweenApp():
    print('switchBetweenApp')

def printCopyableJson(event):
    print()
    print(json.dumps(event, indent=2, sort_keys=True))
    print()

#1. get the event data we want in endpointtest.JSON
#2. print it out, like we have below.
#3. take this printed content and put it into endpointtest.JSON, save it.
#4. use this endpoint test.


#Need a swapping mechanism to go between home and catapp.
#Need a function for swapping to an app once we have gotten appname from AppNameFromIntent.
def endpoint(event, context):

    if not isPostRequest(event):
        return { "statusCode": 422, "body": "Request should be POST"}

    payload, sender = unwrapEvent(event)
    rasaJson = postRasaForIntent(payload['speech'])
    intent = intentNameFrom(rasaJson)
    appName = AppNameFromIntent.get(intent)

    if not appName:
        return wrapIntentSpeakAction("you are home", sender)

    appResult = invokeLambda(appName, payload)
    return wrapAppResult(appResult, sender)
