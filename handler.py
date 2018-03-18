import json
import datetime
#from SimpleHTTPServer import SimpleHTTPRequestHandler
#import SocketHandler

def endpoint(event, context):
    current_time = datetime.datetime.now().time()

    if str(event['requestContext']['httpMethod']) == "GET":
        body = {
            "request type": "" + str(event)
        }
    elif str(event['requestContext']['httpMethod']) == "POST":
        body = {
            "User Said": event['body'].split("=")[1].replace('+', ' ')
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
