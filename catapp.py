import json
import datetime
import requests
#from SimpleHTTPServer import SimpleHTTPRequestHandler
#import SocketHandler
VOICEOSURL = "http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse"

def endpoint(event, context):
    current_time = datetime.datetime.now().time()
#want to be able to:
#post with two routes - post/handle, and post/onstart.
#
    #if str(event['requestContext']['httpMethod']) == "GET":
    #    body = {
    #        "request type": "" + str(event)
    #    }

    if str(event['requestContext']['httpMethod']) == "POST":
        userSaid = event['body'].split("=")[1].replace('+', ' ')
        r = requests.post(VOICEOSURL, json={"q": userSaid})
        response = r.json()
        body = {
            "message": userSaid,
            "intent": response['intent']['name'],
            "confidence": response['intent']['confidence']
        }

    else:
        body={
            "request type": "Neither GET or POST"
        }


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
