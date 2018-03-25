<!--
title: VoiceOS 
description: Bouncer makes POST Request to Voice OS deployed on Serverless Lambda, Lambda makes call to rasa and return rasa output to Bouncer
layout: Doc
-->


# Installation

npm install serverless

Set up AWS IAM serverless-admin with admin priviliages

aws -configure
your key and secret, find your proper region in aws console, last section set to JSON


# Installation of python packages on lambda
serverless packaging
https://serverless.com/blog/serverless-python-packaging/
npm install --save-dev serverless-python-requirements


# Turn on RASA server 
ask james to turn on the server because it is too expensive to run the server all the time


## Deploy 
serverless deploy
once  you deploy will get endpoint

##POST request 
need to select X-form data type to pase message for RASA input
VERIFIED BY POSTMAN

{Usersaid: "show me some cats"}

