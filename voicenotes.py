def payloadFrom(event):
    return event

def readyStateTransition(str):
    newState = 'ready'
    toSpeak = None
    if str == "read" or str == "read read" or str == 'reed':
        toSpeak = "When would you like me to read?"
        newState = "reading"
    elif str == "write" or str == "right" or str == "right right":
        toSpeak = "What would you like to note?"
        newState = "writing"
    else:
        toSpeak = ("say reed or write")
    return newState, toSpeak


def readingStateTransition(str):
    newState = 'reading'
    toSpeak = None
    if str == "just now":
        # summary = summarizeArr(self.notes.lastBunchofNotes())
        toSpeak = "summary just now"
        return "ready", toSpeak

    dateRange = None # std.getDateUnix(str)
    if not dateRange:
        return newState, "Could not recognize that timeframe"

    begin, end = dateRange
    notes = self.notes.findInRange(begin, end)
    if not notes:
        return newState, "Could not find notes in that time"
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


def handle(event, context):
    print("event: ", event)
    payload = payloadFrom(event)
    wholeState = None
    appState = None
    previousState = None
    speech = None
    if payload:
        wholeState = payload.get('state')
        speech = payload.get('speech')
        if wholeState:
            appState = wholeState.get('appState')
            if appState:
                previousState = appState.get('state')
    if not payload: print("missing payload")
    if not wholeState: print("missing wholeState")
    if not appState: print("missing appState")
    if not previousState: print("missing previousState")
    newState = None
    toSpeak = None
    if previousState == 'greeting' or previousState == 'ready':
        print('previously was greeting')
        newState, toSpeak = readyStateTransition(speech)
    elif previousState == 'reading':
        print('previously was reading')
        newState, toSpeak = readingStateTransition(speech)
    elif previousState == 'writing':
        print('previously was writing')
        newState, toSpeak = writingStateTransition(speech)
    else:
        print("OH NOES!", previousState)
    state = {
        "directory":"home/voicenotes",
        "appState":{
            "state":newState
        }
    }


    body = {
        "actionType":"speak",
        "actionDetail": toSpeak,
        # "actionDetail":{
        #     "url_key" :random.choice(catUrls),
        # }
        "state":state
    }

    return body

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
