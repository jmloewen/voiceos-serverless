import json

#Continuous commands within catapp.
#Need to be able to swap out with Home.
def handle(event, context):
    state = {
        "directory":"home/catApp",
        "appState":{
            "status":"OK"
        }
    }

    body = {
        "actionType":"speak",
        "actionDetail":"meow",
        "state":state
    }

    return body

#start the cat app.
def onstart(event, context):
    state = {
        "directory":"home/catApp",
        "appState":{
            "status":"OK"
        }
    }

    body = {
        "actionType":"speak",
        "actionDetail":"meowth thats right",
        "state":state
    }

    return body
