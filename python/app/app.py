from html2image import Html2Image
import boto3

def upload_file(local_file, s3_file):
    print('local file ', local_file, ' s3 file ', s3_file)
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, 'bounty-public', s3_file)
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")
    except e:
        print('exception ', e)


def handler(event, context):
    print(event)
    with open('/tmp/dummy.html', 'w+') as dummy_file:
        dummy_file.write(event['html_str'])
    with open('/tmp/dummy.html') as dummy_file:
        content = dummy_file.read()
    return content
