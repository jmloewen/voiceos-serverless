import json
import random

catUrls = ['https://i.redditmedia.com/yujnbUChhf7GAlSTW1Y6_WYyRcXk5PtpGnaFTkPRNsU.jpg?s=51fc1febf9f465746de28b94b72ab6db',
           'https://i.redditmedia.com/xdQLKd8e0kWmFhI-TgpLA5bQ6jyt8HIYxo6PIwZOraU.jpg?s=02caa37e1e0f35b6ca12099e27633e24',
            'https://i.redditmedia.com/yCrVmZC7v3pnjXHFL3JqCXPTam_zDqG5A3Myrl-WCBA.jpg?s=6a28bf64b866e3a474a8cc53dddf8e8a',
            'https://i.redditmedia.com/Jgo8UMp0dvOA5g1OLl4kT9KFBxJh8JvBEcMecjsP09M.jpg?s=5026492880d633f5bfda5b09557bbae8'
            ]

def handle(event, context):
    state = {
        "directory":"home/catApp",
        "appState":{
            "status":"OK"
        }
    }

    body = {
        "actionType":"show_image",
        "actionDetail": random.choice(catUrls),
        # "actionDetail":{
        #     "url_key" :random.choice(catUrls), 
        # }
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
