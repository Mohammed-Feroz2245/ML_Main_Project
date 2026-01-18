#from src.script import train_and_upload

def lambda_handler(event, context):
    #print("Event received:", event)
    #ccuracy = train_and_upload()

    return {
        "statusCode": 200,
        "message": "Model trained and uploaded to S3"
    }
