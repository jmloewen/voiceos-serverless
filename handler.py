import json
import requests
import boto3

RASASERVER_URL = "http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse"
lambda_client = boto3.client('lambda', region_name="us-east-1",)

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


def callCatApp():

    fake = {
        "actionType":"speak",
        "actionDetail":"meow"
    }

    response = lambda_client.invoke(
        FunctionName="aws-python-simple-http-endpoint-dev-CatAppOnStart",
        InvocationType="RequestResponse",
        Payload=json.dumps(fake)
    )
    string_response = response["Payload"].read().decode('utf-8')
    parsed_response = json.loads(string_response)
    return parsed_response

def testCatappResponse(rasaJson,sender):
    parsedResponse = callCatApp()
    print('parsedResponse:',parsedResponse)
    responseBody = wrapResponse(callCatApp(), sender)
    print('responseBody:',responseBody)
    return response    

def switchBetweenApp():
    print('switchBetweenApp')

def endpoint(event, context):
    if not isPostRequest(event):
        return { "statusCode": 422, "body": "Request should be POST"}

    payload, sender = unwrapEvent(event)
    rasaJson = postRasaForIntent(payload['speech'])
    # return testCatappResponse(rasaJson, sender)
    wrapIntent =  wrapIntentSpeakAction(rasaJson, sender) 
    # switchBetweenApp()

    print('wrapIntent:', wrapIntent)
    return wrapIntent
