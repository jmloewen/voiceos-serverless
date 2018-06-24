import boto3
import json
lambda_client = boto3.client('lambda', region_name="us-east-1",)

# Exported Function:
# Input:
# string: functionName
# dictionary: payload
# Output:
# response dictionary
def invokeLambda(functionName, payload):
    try:
        response = lambda_client.invoke(
            FunctionName=functionName,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload)
        )

        string_response = response["Payload"].read().decode('utf-8')
        parsed_response = json.loads(string_response)
    except Exception as e:
        print("invokeLambda error: ", e)
        parsed_response = {
            "InvokeLambdaError": e
        }
    return parsed_response
