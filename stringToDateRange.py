import dateparser
import moment

# returns ranges for days, weeks, months
def getDate(inputString):
    try:
        return moment.date(inputString).date
    except:
        return None


def getCurrentTime():
    return int(moment.now().date.timestamp())


def getDateUnix(inputString):
    start = getDate(inputString)
    if start is None:
        return None

    try:
        start = int(start.timestamp())
        end = getCurrentTime()
        print(moment.unix(start), moment.unix(end))
        return (start, end)
    except:
        return None

