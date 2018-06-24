import json
import requests
from lambdaFunctionCall.lambdaFunctionCall import invokeLambda

#'onVoiceOsEntry'
RASASERVER_URL = "http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse"

#All functions available to VoiceOS.
FUNCTIONS_DICT = {
    "catAppOnStart": "aws-python-simple-http-endpoint-dev-CatAppOnStart",
    "catAppHandle": "aws-python-simple-http-endpoint-dev-CatAppHandle",
    "VoiceNotesOnStart": "aws-python-simple-http-endpoint-dev-VoiceNotesOnStart",
    "VoiceNotesHandle": "aws-python-simple-http-endpoint-dev-VoiceNotesHandle"
}

#Given intent, returns app name
#This must be modularized at some point.
AppNameFromIntent = {
    "cats": "catApp",
    "home": None,
    "image search":  "imageSearch",
    "voicetunnel": "voicetunnel",
    "voice notes": "VoiceNotes"
}

def isPostRequest(event):
    return str(event['requestContext']['httpMethod']) == "POST"

# Unpack the json request body
# return tuple of payload and sender
def unwrapEvent(event):
    bodyJson = event['body']
    # Actual content client sends to endpoint
    bodyDict = json.loads(bodyJson)
    return bodyDict

def postRasaForIntent(payload):
    ##Uncomment this to test next Sunday.
    r = requests.post(RASASERVER_URL, json={"q": payload})
    return r.json()

    # MOCK
    # return {'intent': {'name': 'cats'}}

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

def getState(directory, status):
    state = {
        "directory":directory,
        "appState":{
            "status":status
        }
    }
    return state

def wrapIntentSpeakAction(spokenPhrase, sender):

    state = getState("home", "OK")

    bodyPayload = {
        "actionType": "speak",
        "actionDetail": spokenPhrase,
        "state":state
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
    return {"payload": payload, "receiver": receiver}

# TODO: implement callCatApp() function
# def testCatappResponse(rasaJson,sender):
#     parsedResponse = callCatApp()
#     print('parsedResponse:',parsedResponse)
#     responseBody = wrapResponse(callCatApp(), sender)
#     print('responseBody:',responseBody)
#     return response

def switchBetweenApp():
    print('switchBetweenApp')

def printCopyableJson(event):
    print('#############printCopyableJson(event)###############')
    print(json.dumps(event, indent=2, sort_keys=True))
    print('#############printCopyableJson(event)###############')

#1. get the event data we want in endpointtest.JSON
#2. print it out, like we have below.
#3. take this printed content and put it into endpointtest.JSON, save it.
#4. use this endpoint test.

# Need a swapping mechanism to go between home and catapp.
# Need a function for swapping to an app once we have gotten appname from AppNameFromIntent.
def endpoint(event, context):
    # printCopyableJson(event)
    if not isPostRequest(event):
        return { "statusCode": 422, "body": "Request should be POST"}

    eventBody = unwrapEvent(event)
    print('eventBody: ', eventBody)
    # request to rasa
    rasaJson = postRasaForIntent(eventBody['payload']['speech'])
    intent = intentNameFrom(rasaJson)

    appName = AppNameFromIntent.get(intent)

    if not appName:
        return wrapIntentSpeakAction("you are home", eventBody['sender'])

    #Check if catapp has been called previously (call start or handle?)
    # Extract app directory:
    directory = eventBody['payload']['state']['directory']

    print("eventBody['payload']['state']['directory']: ", directory)

    # Make functionNickname to run app by key in FUNCTIONS_DICT
    functionNickname = appName
    if appName not in directory:
        functionNickname = functionNickname + "OnStart"
    else:
        functionNickname = functionNickname + "Handle"

    print("fNickname: ", functionNickname)
    #invoke the handle function of that app.
    appResult = invokeLambda(FUNCTIONS_DICT[functionNickname], eventBody['payload'])

    return wrapAppResult(appResult, eventBody['sender'])
