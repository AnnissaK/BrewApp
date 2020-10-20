import uuid
import boto3

def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix,str(uuid.uuid4())])

# print(create_bucket_name('first'))

s3 = boto3.client('s3')
def lambda_handler(event,context):
    bucket ='kfc-boneless-banquest'
    Transaction_to_upload ={}
    Transaction_to_upload['try out']='value to try'
    filename = 'first try.json'
    uploadstream = bytes(json.dumps(Transaction_to_upload).encode('UTF-8'))
    
    s3.put_object(Bucket=bucket,Key=filename,Body =uploadstream)