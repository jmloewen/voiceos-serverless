<!--
title: VoiceOS
description: Bouncer makes POST Request to Voice OS deployed on Serverless Lambda, Lambda makes call to rasa and return rasa output to Bouncer
layout: Doc
-->
#James endpoint
https://7egeo7rfc5.execute-api.us-east-1.amazonaws.com/dev/ping

#Jon endpoint
https://zydkkkbc6k.execute-api.us-east-1.amazonaws.com/dev/ping


# Installation

npm install serverless
pip install -r requirements.txt


Set up an AWS IAM serverless-admin with Admin privileges

aws configure

Use your key and secret credentials; Find your proper region in aws console (default us-east-1); Last section set to json


# Installation of python packages on lambda
[serverless packaging](https://serverless.com/blog/serverless-python-packaging/)

`> npm install --save-dev serverless-python-requirements`

# Activate python virtualenv
`> virtualenv -p python3 env`
`> source env/bin/activate`


# Turn on RASA server
Ask James to turn on the server - it is expensive to run full time


# Deploy
Serverless deploy
`> serverless deploy function --function onVoiceOsEntry`
Once you deploy you will get endpoint

##Debug
`> serverless logs -f onVoiceOsEntry -t`

Locally:`serverless invoke local -f onVoiceOsEntry -p endpointTest.json`
