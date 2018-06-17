import json
import random

def handle(event, context):
    state = {
        "directory":"home/VoiceNotes",
        "appState":{
            "status":"OK"
        }
    }

    actionType = 'Read'
    note = 'I haven taken down the following notes: currently stubbed, should be read from event or context'

    body = {
        "actionType":"speak",
        "actionDetail": note,
        "state":state
    }

    return body

#start the cat app.
def onstart(event, context):
    state = {
        "directory":"home/VoiceNotes",
        "appState":{
            "status":"OK"
        }
    }

    body = {
        "actionType":"speak",
        "actionDetail":"Would you like to take notes or read notes",
        "state":state
    }

    return body
