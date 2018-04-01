<!--
title: VoiceOS
description: Bouncer makes POST Request to Voice OS deployed on Serverless Lambda, Lambda makes call to rasa and return rasa output to Bouncer
layout: Doc
-->
#james endpoint
https://7egeo7rfc5.execute-api.us-east-1.amazonaws.com/dev/ping


# Installation

npm install serverless

Set up AWS IAM serverless-admin with admin privileges

aws configure
your key and secret, find your proper region in aws console (default us-east-1), last section set to json


# Installation of python packages on lambda
[serverless packaging](https://serverless.com/blog/serverless-python-packaging/)

`> npm install --save-dev serverless-python-requirements`

# Activate python virtualenv
`> virtualenv -p python3 env`
`> source env/bin/activate`


# Turn on RASA server
ask james to turn on the server because it is too expensive to run the server all the time


# Deploy
serverless deploy
`> serverless deploy function --function onVoiceOsEntry`
once you deploy will get endpoint

##Debug
`> serverless logs -f onVoiceOsEntry -t`

locally:`serverless invoke local -f onVoiceOsEntry -p endpointTest.json`
