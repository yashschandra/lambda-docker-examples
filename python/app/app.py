from html2image import Html2Image
import boto3

def upload_file(local_file, s3_file):
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
    hti = Html2Image(output_path='/tmp')
    hti.screenshot(html_str=event['html_str'], save_as='dummy.png')
    upload_file('/tmp/dummy.png', 'posters/test/dummy.png')
    return "it works"
