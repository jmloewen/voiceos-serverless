import stringToDateRange

def payloadFrom(event):
    import json
    return json.loads(event['body'])['payload']

def readyStateTransition(str):
    newState = 'ready'
    toSpeak = None
    if str == "read" or str == "read read" or str == 'reed':
        return "reading", "When would you like me to read?"
    elif str == "write" or str == "right" or str == "right right":
        return "writing", "What would you like to note?"
    else:
        return "ready", "say reed or write"


def readingStateTransition(str):
    toSpeak = None
    if str == "just now":
        # summary = summarizeArr(self.notes.lastBunchofNotes())
        toSpeak = "summary just now"
        return "ready", toSpeak

    dateRange = stringToDateRange.getDateUnix(str)
    print("dateRange: ", dateRange)
    if not dateRange:
        return 'reading', "Could not recognize that timeframe. try again."

    begin, end = dateRange
    notes = None # notes.findInRange(begin, end)
    if not notes:
        return 'reading', "Could not find notes in that time. try again."
    # write_message(summarizeArr(list(notes.values() ) ) )
    return 'ready', 'here is a summary of what you said in that time'

def writingStateTransition(str):
    newState = 'writing'
    toSpeak = None
    if "end note" in str or 'endnote' in str:
        return 'ready', 'done'

    success = True # self.saveNote(str)

    if success:
        return newState, ""
    else:
        return newState, "could not write that last bit"


def previousStateFromPayload(payload):
    wholeState = payload.get('state', None)
    if wholeState:
        appState = wholeState.get('appState')
        if appState:
            return appState.get('state')


def stateTransitionFrom(previousState, speech):
    if previousState == 'greeting' or previousState == 'ready':
        return readyStateTransition(speech)
    elif previousState == 'reading':
        return readingStateTransition(speech)
    elif previousState == 'writing':
        return writingStateTransition(speech)
    else:
        print("OH NOES! invalud previous state!", previousState)
        return None, None

def sayOopsAction(previousState, errorDescription):
    return {
        "actionType": "speak",
        "actionDetail": "oops. " + errorDescription,
        "state": {
            "directory": "home/voicenotes",
            "appState": {
                "state": previousState
            }
        }
    }

def handle(event, context):
    payload = payloadFrom(event)
    if not payload:
        return sayOopsAction("greeting", "Could not extract payload")
    previousState = previousStateFromPayload(payload)
    speech = payload.get('speech')
    if not previousState:
        return sayOopsAction("greeting", "Could not determine previous state")
    if not speech:
        return sayOopsAction("greeting", "Could not hear what you just said")

    newState, toSpeak = stateTransitionFrom(previousState, speech)
    state = {
        "directory":"home/voicenotes",
        "appState":{
            "state": newState
        }
    }
    return {
        "actionType":"speak",
        "actionDetail": toSpeak,
        "state":state
    }

#start voice notes app.
def start(event, context):
    state = {
        "directory":"home/voicenotes",
        "appState":{
            "state":"greeting"
        }
    }

    body = {
        "actionType":"speak",
        "actionDetail":"welcome to voice notes",
        "state":state
    }

    return body
