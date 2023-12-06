import boto3
import json


bedrock_client = boto3.client('bedrock-runtime')

def handler(event, context):

    #print("boto3 Version"+ boto3.__version__)
    userPrompt = event["userPrompt"]
    
    print("User Prompt :"+ str(userPrompt))

    modelId = 'meta.llama2-13b-chat-v1'

    prompt = "You are santa claus chatbot, and you have to answer only questions related to chirstmas. Do not answer negative things. Talk like santa all the time.The question is"

    body = json.dumps(
        {
            'prompt' : prompt + str(userPrompt),
            'max_gen_len' : 512,
            'top_p' : 0.9,
            'temperature': 0.2
        }
    )

    response = bedrock_client.invoke_model(
        body=body,
        modelId = modelId,
        accept= 'application/json',
        contentType = 'application/json'
    )

    res = response.get('body').read().decode('utf-8')
    response_body = json.loads(res)
    print(response_body['generation'].strip())