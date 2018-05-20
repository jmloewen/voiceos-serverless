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
        "actionType":"show_image", 
        "actionDetail":"https://i.redditmedia.com/OL_p0HRQr9chiwy3-1L5UCuTUgk5vNJE0NJOt4Jw7oE.jpg?s=98fcfbe17c8950b7c8a9e882aa42862b", 
        ## object
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
