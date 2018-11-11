<!--
title: VoiceOS
description: Bouncer makes POST Request to Voice OS deployed on Serverless Lambda, Lambda makes call to rasa and return rasa output to Bouncer
layout: Doc
-->
# Endpoints

#### James
https://7egeo7rfc5.execute-api.us-east-1.amazonaws.com/dev/ping

#### Jon
https://zydkkkbc6k.execute-api.us-east-1.amazonaws.com/dev/ping

#### kai (Currently Most Up to Date)
https://hap2a5df4m.execute-api.us-east-1.amazonaws.com/dev/ping


# Installation

`> npm install serverless`

`> pip install -r requirements.txt`


Set up an AWS IAM serverless-admin with Admin privileges

`> aws configure`

Use your key and secret credentials; Find your proper region in aws console (default us-east-1); Last section set to json


# Installation of python packages on lambda
[serverless packaging](https://serverless.com/blog/serverless-python-packaging/)

`npm install --save-dev serverless-python-requirements`

# Activate python virtualenv
`virtualenv -p python3 env`

`source env/bin/activate`


# Turn on RASA server
EC2 server can be configured to turn on and off automatically. It currently turns on every Sunday from 1 to 5

# Testing RASA server
curl 'http://ec2-34-218-219-244.us-west-2.compute.amazonaws.com:5000/parse?q=take+me+home'

### Deploy
`serverless deploy function --function onVoiceOsEntry`
Once you deploy you will get endpoint

### Debug
`serverless logs -f onVoiceOsEntry -t`

### Locally:
[Generate Test File]( https://gist.github.com/jmloewen/84b1ed61598df55ab4a7033ac1edbf43)

`> serverless invoke local -f onVoiceOsEntry -p endpointTest.json`

### End to end testing
Install simple websocket chrome extension, then open up the socket connection to bouncer

`ws://secure-lowlands-10237.herokuapp.com/websocket/`

Once websocket has been opened, enter the following json for request

`{"speech":"show me some cats","endpoint":"https://hap2a5df4m.execute-api.us-east-1.amazonaws.com/dev/ping","state":{"directory":"home"}}`

expect following response

`{"actionType":"speak","actionDetail":"meowth thats right","state":{"directory":"home/catApp","appState":{"status":"OK"}}}`
