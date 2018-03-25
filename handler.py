import json
import datetime
import requests
#from SimpleHTTPServer import SimpleHTTPRequestHandler
#import SocketHandler
RASASERVER_URL = "http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse"

def endpoint(event, context):
    current_time = datetime.datetime.now().time()

    if str(event['requestContext']['httpMethod']) == "GET":
        body = {
            "request type": "" + str(event)
        }
    elif str(event['requestContext']['httpMethod']) == "POST":

        wrappedPayload = json.loads(event['body'])
        print("wrappedPayload: ", wrappedPayload)
        payload = wrappedPayload['payload']
        r = requests.post(RASASERVER_URL, json={"q": payload})
        response = r.json()
        intentString = response['intent']['name']
        responsePayload = {
            "actionType": "speak",
            "actionDetail": intentString
        }
        body = {
            "receiver": wrappedPayload["sender"],
            "payload": responsePayload
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

#class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
#    def do_POST(self):
#        self._set_headers()
#        self.wfile.write("<html><head><title>POST TITLE</title></head><body><h1>POSTING to serverless ep</h1></body></html>")
