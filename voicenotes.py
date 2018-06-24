def payloadFrom(event):
    bodyJson = event['body']
    bodyDict = json.loads(bodyJson)
    return bodyDict.get('payload', None)

def readyStateTransition(str):
    newState = 'ready'
    toSpeak = None
    if str is "read" or str is "read read" or str is 'reed':
        toSpeak = "When would you like me to read?"
        newState = "reading"
    elif str is "write" or str is "right" or str is "right right":
        toSpeak = "What would you like to note?"
        newState = "writing"
    else:
        toSpeak = ("say reed or write")
    return newState, toSpeak


def readingStateTransition(str):
    newState = 'reading'
    toSpeak = None
    if str is "just now":
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
    payload = payloadFrom(event)
    wholeState = None
    appState = None
    previousState = None
    if payload:
        wholeState = payload.get()
        if wholeState:
            appState = wholeState.get('appState')
            if appState:
                previousState = appState.get('state')

    newState = None
    toSpeak = None
    if previousState is 'greeting' or previousState is 'ready':
        print('previously was greeting')
        newState, toSpeak = handleReadyState(str)
    elif previousState is 'reading':
        print('previously was reading')
        newState, toSpeak = handleReadingState(str)
    elif previousState is 'writing':
        print('previously was writing')
        newState, toSpeak = handleWritingState(str)

    newState = {
        "directory":"home/voicenotes",
        "appState":{
            "state":newState
        }
    }


    body = {
        "actionType":"record_notes",
        "actionDetail": "recording",
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
