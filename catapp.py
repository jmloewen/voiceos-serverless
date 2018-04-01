import json
import datetime
import requests
#from SimpleHTTPServer import SimpleHTTPRequestHandler
#import SocketHandler
RASAURL = "http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse"

def handle(event, context):
    current_time = datetime.datetime.now().time()

    if str(event['requestContext']['httpMethod']) == "GET":
        body = {
            "request type": "" + str(event)
        }
    elif str(event['requestContext']['httpMethod']) == "POST":
        userSaid = event['body'].split("=")[1].replace('+', ' ')
        r = requests.post(RASAURL, json={"q": userSaid})
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


    #body = {
    #    "heres a header!"
    #}
    #else:
    #    body = "request type": "" + str(event['requestContext']['httpMethod'])

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
